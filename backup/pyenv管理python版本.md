---
Title: pyenv管理Python版本
Date: 2017-03-19
Modified: 2017-11-11
---

## 安装
```shell
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```
添加以下语句到.bashrc并重新source。
```
export PATH="/home/<user>/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

运行一下`pyenv update`。

## 依赖
编译Python时需要一些依赖。
Ubuntu/Debian:
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
```

Fedora/CentOS/RHEL:
FIXME: you may need to install xz to build some CPython version
```
yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel
```
Mac OS X:
```
brew install readline xz
```

**注意**: libssl-dev is required when compiling Python, installing libssl-dev will actually install zlib1g-dev, which leads to uninstall and re-install Python versions (installed before installing libssl-dev). On Redhat and derivatives the package is named openssl-devel.

## pyenv命令
```
# 列出所有可用的命令
pyenv commands

# 更新pyenv
pyenv update

# 查看当前所有的python版本
pyenv versions 

# 查看当前激活的python版本
pyenv version

# 安装指定版本的python
pyenv install -v [version] 

# 卸载指定版本的python
pyenv uninstall -v [version]

# 为所有已安装的可执行文件创建 shims，因此，每当你增删了 Python 版本或带有可执行文件的包（如 pip）以后，都应该执行一次本命令
pyenv rehash

# 指定全局python版本
pyenv global [version]

# 指定本地面向应用程序的python版本
pyenv local [version]
```

## pyenv与virtualenv配合
```
# 新建一个virtualenv
pyenv virtualenv [version] [venv_name]

# 激活一个virtualenv
pyenv activate [venv_name]

# 退出virtualenv环境
pyenv deactivate

# 删除一个virtualenv环境
pyenv uninstall [venv_name]
```

通过pyenv建立的虚拟环境都在`~/.pyenv/versions`下，不会出现在应用目录里面


## 遇到的问题
### pyenv安装新版本时，默认的源速度比较慢
选择国内的镜像站（比如mirrors.sohu.com），手动下载python包，放到`~/.pyenv/cache`目录下，再安装时会用cache下的包安装。
```
version=2.7.13 && wget http://mirrors.sohu.com/python/$version/Python-$version.tar.xz -P ~/.pyenv/cache && pyenv install -v $version
```