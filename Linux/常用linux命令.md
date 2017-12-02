---
Title: 常用linux命令
Date: 2017-07-21
Modified: 2017-11-20
---

## ssh
```
# ssh登陆
# ssh user@host -p port
ssh lgs@localhost -p 9922
```

## scp
```
# 上传文件
# scp -P port /path/to/local user@host:/path/to/remote
scp -P 9922 d:\tmp\test.py lgs@localhost:/tmp/test.py

# 上传文件夹
# scp -r -P port /path/to/local user@host:/path/to/remote
scp -r -P 9922 d:\tmp\test\ lgs@localhost:/tmp/test/

# 下载文件
scp -P 9922 lgs@localhost:/tmp/test.py d:\tmp\test.py 

# 下载文件夹
scp -r -P 9922 lgs@localhost:/tmp/test/ d:\tmp\test\
```

## 进程
```
Ctrl-z # 挂起当前进程到后台
bg # 查看后台进程
bg [id] # 后台运行进程
fg [id] # 将进程切到前台运行
```

## 查找文件
```
find <path> -name "*xxx*"
```

## 统计行数
```
find . -name "*.py"|xargs cat|wc -l
```

## OpenSSH
openssh 要求密码，提示`passphrase length hidden intenationlly`
```
ssh-copy-id localhost
```

## SSH断开后，使进程仍在后台运行

**nohup**

run a command immune to hangups, with output to a non-tty
```
nohup ping www.baidu.com > /dev/null &
aaa
```

**setsid**

Run a program in a new session.
```
setsid ping baidu.com > /dev/null
```
**将&也放入()中执行命令**

```
(ping baidu.com > /dev/null &)
```
**disown**

dosown 使作业能够忽略HUP信号

disown: usage: disown [-h] [-ar] [jobspec ...]

**screen**