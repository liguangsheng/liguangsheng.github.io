---
Title: MySQL连接次数过多报错
Date: 2016-12-12
Modified: 2017-07-21
---

## MySQL 连接报错
> "Host '10.7.30.133' is blocked because of many connection errors; unblock with 'mysqladmin flush-hosts'"

## 解决方法
### 增加最大错误连接数
```shell
mysql> use mysql;
# 查看最大错误连接数
mysql> show variables like '%max_connect_errors%'
# 修改最大错误连接数
mysql> set global max_connect_errors = 1000;
# 查看修改结果
mysql> show variables like '%max_connect_errors%'
```

### 重置计数器
```shell
mysql> flush hosts;
```
或者
```shell
$ mysqladmin flush-hosts
```