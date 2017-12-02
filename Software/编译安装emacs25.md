Title: 编译安装emacs25
Date: 2017-05-05 17:37
Modified: 2017-06-15 17:45
Tags: centos, emacs

# 下载源码并解压
```
wget http://mirrors.ustc.edu.cn/gnu/emacs/emacs-25.2.tar.gz
tar xzvf emacs-25.2.tar.gz
cd emacs-25.2
```

# 安装编译依赖
```
yum install -y gcc gtk2 gtk2-devel libXpm libXpm-devel libtiff libtiff-devel libjpeg-turbo  libjpeg-turbo-devel giflib giflib-devel
```

# 编译
```
./configure --prefix=/usr/local/emacs-25
make
make install
```
make时出现了`aclocal-1.5.1 missing`的错误，执行`autoreconf -f -i`后再make。

`make install`时出现`makeinfo command not found`，执行`yum install texinfo`。
