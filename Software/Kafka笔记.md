Title: Kafka笔记
Date: 2016-06-17 21:14
Modified: 2017-07-17 22:24
Tags: kafka

# 安装
访问`http://kafka.apache.org/downloads`下载对应Scala版本的Kafka下载即可

# 启动Kafka

```
# 启动Zookkeeper
bin/zookeeper-server-start.sh config/zookeeper.properties &

# 启动Kafka
bin/kafka-server-start.sh config/server.properties
```

# Kafka
```
# 创建Topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

# 列出Topic
bin/kafka-topics.sh --list --zookeeper localhost:2181
```

# python示例
```
# kafka_producer.py
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

for i in range(0, 10):
    message = ('Message {}'.format(i)).encode()
    print('Produce: {}'.format(message))
    producer.send('test', message)
```

```
# kafka_consumer.py
from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'])

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
```