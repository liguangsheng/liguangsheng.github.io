Title: 搭建git服务器
Date: 2017-06-28
Modified: 2017-06-28
Tags: git, centos

1. 安装git
 ```
 yum install git
 ```

2. 添加用户git并切换到git用户来运行git服务
 ```
 useradd git
 passwd git
 su git
 ```

3. 创建相应的ssh目录
 ```
 mkdir .ssh && chmod 700 .ssh
 touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys
 ```

4. 切换到一个空的目录来存放git仓库
 ```
 mkdir -p /opt/git/project.git
 cd /opt/git
 chown -R git:git project.git
 cd project.git
 git init --bare
 ```

5. 禁用shell登录，将`/etc/passwd`中的
 ```
 git:x:1001:1001:,,,:/home/git:/bin/bash
 ```
 改为
 ```
 git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell
 ```

6. 赋予使用者权限，将授权使用git的ssh公钥收集到`~/.ssh/authorizes_keys`中

7. 使用git
 ```
 git clone git@<server_address>:/opt/git/project.git
 Cloning into 'project'...
 warning: You appear to have cloned an empty repository.
 ```
 ```
 git clone ssh://<user>@<server>:<port><path>
 git clone ssh://root@xxx.xxx.xxx.xxx:28802/opt/git/proje ct.git
 ```
