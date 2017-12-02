Title: linux配置Shadowsocks
Date: 2017-04-06
Modified: 2017-04-06
Category: Linux
Tags: linux, shadowsocks

## 安装Shadowsocks
```
pip install shadowsocks
```

## 服务端配置
shadowsocks配置文件，shadowsocks.json
```
{
    "server":"0.0.0.0",
    "server_port":1118,
    "local_address":"127.0.0.1",
    "local_port":1080,
    "password":"11181118",
    "timeout":300,
    "method":"aes-256-cfb"
}
```

启动ssserver
```
ssserver -c shadowsocks.json -d start
```

关闭ssserver
```
ssserver -d stop
```
 
## 客户端配置 
shadowsocks配置文件，/etc/shadowsocks/config.json
```
{
    "server":"0.0.0.0",
    "server_port":1118,
    "local_address":"127.0.0.1",
    "local_port":1080,
    "password":"11181118",
    "timeout":300,
    "method":"aes-256-cfb"
}
```
 
启动shadowsocks客户端
```
sslocal -c /etc/shadowsocks/config.json -d start
```
  
 