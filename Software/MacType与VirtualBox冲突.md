Title: MacType与VirtualBox冲突
Date: 2017-01-12 15:45
Modified: 2017-06-15 17:52
Tags: mactype, virtualbox

MacType渲染字体会与VirtualBox冲突导致虚拟机不能启动。

## 解决方法

在MacType的配置文件中加入以下节点

```
[ExcludeSub] 
javaw.exe 
vbox-img.exe
VBoxBalloonCtrl.exe
VBoxDTrace.exe
VBoxExtPackHelperApp.exe
VBoxHeadless.exe
VBoxManage.exe
VBoxNetDHCP.exe
VBoxNetNAT.exe
VBoxSDL.exe
VBoxSVC.exe
VBoxTestOGL.exe
VBoxWebSrv.exe
VirtualBox.exe
```