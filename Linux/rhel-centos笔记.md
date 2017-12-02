---
Title: rhel/centos笔记
Date: 2017-07-13
Modified: 2017-07-13
---

**OS: CentOS 6.8 | RHEL 6.5 **
---

# VirtualBox中为系统安装增强功能包
安装增强功能包需要依赖一些工具包，装上就好
```
sudo yum install -y gcc gcc-c++ make kernel kernel-devel
```

# VirtualBox共享文件夹

在设置中，为虚拟机分配一个共享文件夹，勾选固定分配。
在虚拟机中执行以下命令挂载共享文件夹。
```
sudo mkdir /mnt/vmshare # 创建共享文件夹挂载点
sudo mount -t vboxsf vmshare /mnt/vmshare # 挂载
```

# 修改主机名(hostname)
```
vim /etc/sysconfig/network

NETWORKING=yes
NETWORKING_IPV6=no
HOSTNAME=<your hostname> # 修改这里
```

# 安装epel扩展
```
yum intsall epel-release -y
```