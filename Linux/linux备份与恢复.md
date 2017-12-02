---
Title: linux备份与恢复
Date: 2017-03-20
Modified: 2017-03-20
---

## tar

```
# 备份系统
cd /
tar cvpzf backup.tgz --exclude=/proc --exclude=/lost+found --exclude=/backup.tgz --exclude=/mnt --exclude=/sys /  

# 恢复系统
tar xvpfz backup.tgz -C /
# 创建备份时跳过的文件夹
mkdir proc
mkdir mnt
mkdir sys
mkdir lost+found
```

## dd
```
# 在livecd中操作
# 备份系统
dd if=/dev/sdax of=~/archlinux.backup
，在livecd中
dd if=archlinux.backup of=/dev/sdax
```