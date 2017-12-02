Title: VirtualBox克隆虚拟机后重新初始化网卡
Date: 2017-01-22 15:21
Modified: 2017-06-15 17:45
Tags: virtualbox

VirtualBox重新初始化虚拟机后，新虚拟机会重新生成两张不一样的网卡。

系统会扫描新生成的网卡，添加到`/etc/udev/rules.d/70-persistent-net.rules`中。删除多余的网卡，只剩下两条，将名称改为`eth0`和`eth1`，将`ATTR{address}`修改为对应的MAC地址。
```
cat /etc/udev/rules.d/70-persistent-net.rules

# PCI device 0x8086:0x100e (e1000)
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="08:00:27:20:2b:d6", ATTR{type}=="1", KERNEL=="eth*", NAME="eth0"

# PCI device 0x8086:0x100e (e1000)
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="08:00:27:bc:43:e8", ATTR{type}=="1", KERNEL=="eth*", NAME="eth1"
```

在`/etc/sysconfig/network-scripts`下删除多余的ifcfg-eth*，并建立ifcfg-eth0和ifcfg-eth1。
```
cat ifcfg-eth0 
DEVICE=eth0
BOOTPROTO=dhcp
IPV6INIT=yes
NM_CONTROLLED=no
ONBOOT=yes
TYPE=Ethernet
USERCTL=no
PEERDNS=yes
```

```
cat ifcfg-eth1 
DEVICE=eth1
BOOTPROTO=dhcp
IPV6INIT=yes
NM_CONTROLLED=no
ONBOOT=yes
TYPE=Ethernet
USERCTL=no
PEERDNS=yes
```

重启。