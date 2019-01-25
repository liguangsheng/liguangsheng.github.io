---
Title: Nginx笔记
Date: 2017-07-08
Modified: 2017-11-18
---

# CentOS上编译安装Nginx

首先下载nginx的源代码，这里选择的是当前最前的稳定版1.12.2。
```shell
wget http://nginx.org/download/nginx-1.12.2.tar.gz
tar xzvf nginx-1.12.2.tar.gz
```

(可选)接着下载想要额外添加的模块的源代码
```
# rtmp 直播支持
git clone https://github.com/arut/nginx-rtmp-module

# mp4 流媒体支持
wget http://h264.code-shop.com/download/nginx_mod_h264_streaming-2.2.7.tar.gz
tar xzvf nginx_mod_h264_streaming-2.2.7.tar.gz
```
mp4模块还需要修改一下源代码，注释掉`nginx_mod_h264_streaming-2.2.7/src/ngx_http_streaming_module.c`这个文件中的第158到161行
```c
157   /* TODO: Win32 */
158   //if (r->zero_in_uri)
159   //{
160   //  return NGX_DECLINED;
161   //}
```

安装编译必要的依赖包，不同的系统包名不同。
```
# ubuntu
sudo apt-get install openssl libssl-dev libpcre3 libpcre3-dev zlib1g-dev

# centos
sudo yum -y install pcre-devel openssl openssl-devel
```

开始编译和安装
```shell
cd nginx-1.12.2 # 进入nginx源码目录
./configure --prefix=/usr/local/nginx --with-pcre \
    --add-module=../nginx-rtmp-module \
    --add-module=../nginx_mod_h264_streaming-2.2.7

修改objs/Makefile，去掉其中的-Werror

make
make install
```

# 常用命令
```
# 启动
/usr/local/nginx/sbin/nginx

# 停止
/usr/local/nginx/sbin/nginx -s stop

# 重新加载配置
/usr/local/nginx/sbin/nginx -s reload
```

