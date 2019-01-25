---
Title: ZeroMQ笔记
Date: 2017-07-17
Modified: 2017-07-18
---

# 安装
安装ZeroMQ
```
# 下载源代码并解压
wget https://github.com/zeromq/libzmq/releases/download/v4.2.1/zeromq-4.2.1.tar.gz
tar xzvf zeromq-4.2.1.tar.gz

# 编译安装
cd zeromq-4.2.1
./configure
make
sudo make install
sudo ldconfig
```
安装pyzmq
```
pip install pyzmq
```

# 简介
## Request-reply pattern 请求-回复模型
这种模型主要用于从客户端向一个或多个服务实例发送请求，然后等待紧接着对于每个请求的回复
里面又具体分了ZMQ_REQ ZMQ_REP ZMQ_DEALER ZMQ_ROUTER
REQ 发送完消息后，必须接收一个回应消息后，才能发送新的消息。
REP当接收消息时，都会返回一个消息。
![](leanote://file/getImage?fileId=596c6975ab644114ba0014f1)
![](leanote://file/getImage?fileId=596c6975ab644114ba0014f2)

## Publish-subscribe pattern 发布-订阅模式
这种模式主要用于1对多的数据发布（一个发布者，多个订阅者）
里面又具体分了ZMQ_PUB ZMQ_SUB
PUB发送消息给所有的SUB。如果此时SUB没有启动，下次启动时会漏掉该消息。
![](leanote://file/getImage?fileId=596c6975ab644114ba0014f0)

## Pipeline pattern 管道模式
这种模式主要用于发布数据到由管道排列的节点上面，数据总是沿着管道流动。每个管道阶段连接了至少一个节点
里面又具体分了ZMQ_PUSH ZMQ_PULL
一个1对N队列的实现，PUSH将数据放入队列，PULL从队列中取出数据。数据会负载均衡的发送给每一个PULL。
![](leanote://file/getImage?fileId=596c6d7dab644114ba00156b)
 
## Exclusive pair pattern 独立对模式
peer to peer 模式。主要用于进程内部线程间通信
里面又具体分了ZMQ_PAIR
线程间1-to-1队列的实现，采用了lock free实现，所以速度很快。

# 示例
##　Request - Reply
```
# zmq_rep.py
import zmq
import time

context = zmq.Context()
socket  = context.socket(zmq.REP)
socket.bind('tcp://*:5555')

while True:
    message = socket.recv()
    print('Received request: ', message)
    if message == b':exit':
        break
    time.sleep(1)
    socket.send_string('World')
```

```
# zmq_req.py
import zmq

context = zmq.Context()

socket  = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

for request in range(1, 10):
    print('Sending request: ', request)
    socket.send_string('Hello')
    message = socket.recv()
    print('Received reply: ', message)

socket.send_string(':exit')
```

## Publish - Subscribe
```
# zmq_pub.py
 import zmq
import time

context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind('tcp://127.0.0.1:5557')



for i in range(0, 10):
    print('Sending A {}'.format(i))
    publisher.send_string('A {}'.format(i))
    print('Sending B {}'.format(i))
    publisher.send_string('B {}'.format(i))
    time.sleep(1)

publisher.send_string('A :exit')
publisher.send_string('B :exit')
```

```
# zmq_sub.py
 import zmq

context = zmq.Context()
subscribe = context.socket(zmq.SUB)
subscribe.connect('tcp://127.0.0.1:5557')

subscribe.setsockopt(zmq.SUBSCRIBE, b'A')

while True:
    message = subscribe.recv_string()
    print('Reveived: ', message)
    topic, data = message.split()
    if data == ':exit':
        break
```

## Pipeline
```
# zmq_ventilator.py
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)

socket.bind('tcp://*:5557')

for i in range(0, 10):
    print('Push message:', i)
    socket.send_string('Message {}'.format(i))
```

```
# zmq_worker.py
import zmq

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.connect('tcp://127.0.0.1:5557')

sender = context.socket(zmq.PUSH)
sender.connect('tcp://127.0.0.1:5558')

while True:
    message = receiver.recv()
    print(message)
    sender.send(message)
```

```
# zmq_sink.py
import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind('tcp://*:5558')

while True:
    data = socket.recv()
    print(data)
```