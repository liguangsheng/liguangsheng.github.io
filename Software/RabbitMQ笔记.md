Title: RabbitMQ笔记
Date: 2017-02-07 14:57
Modified: 2017-07-18 16:51
Tags: rabbitmq

# 安装
```
sudo yum install -y rabbitmq-server
```

# 启动
```
systemctl start rabbitmq-server
```

# rabbitmqctl
```
# 列出所有queue
rabbitmqctl list_queues
```

# Python 示例
```
# rmq_producer.py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

for i in range(0, 10):
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    print('[x] Sent "Hello World!"')

channel.basic_publish(exchange='', routing_key='hello', body=':exit')

connection.close()
```

```
# rmq_consumer.py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print('[x] Received {}'.format(body))

channel.basic_consume(callback, queue='hello', no_ack=True)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
```

```
# rmq_new_task.py
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

for message in ['First Message', 'Second Message', 'Third Message',
        'Fourth Message', 'Fifth Message']:
    channel.basic_publish(exchange='', routing_key='task_queue',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=2
                              ))
    print(' [x] Sent "{}"'.format(message))

connection.close()
```

```
# rmq_worker.py
import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
    print(' [x] Received {}'.format(body))
    time.sleep(len(body))
    print(' [x] Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='task_queue')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
```




