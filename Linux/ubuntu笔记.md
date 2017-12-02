---
Title: ubuntu笔记
Date: 2017-03-17
Modified: 2017-03-17
---

OS: Ubuntu 16.04 xenial
Kernel: x86_64 Linux 4.4.0-xx-generic

## 启动:text mode or GUI
```
# 禁用GUI，启动到text mode
sudo systemctl disable display-manager.service
# 启用GUI
sudo systemctl enable display-manager.service
```

## ssh服务
```
sudo apt install openssh-server # 安装ssh服务
sudo systemctl start sshd.service # 启动ssh服务
sudo systemctl enable sshd.service # 开机自启动
```

## zsh
```
sudo apt install zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

## emacs25
通过ppa安装emacs25
```
# through ppa
sudo add-apt-repository ppa:alexmurray/emacs
sudo apt-get update
sudo apt-get install emacs25
```
通过源代码编译安装emacs
```
# through source code
sudo apt install build-essential checkinstall
sudo apt-get build-dep emacs24

wget http://ftp.gnu.org/gnu/emacs/emacs-25.1.tar.gz
tar xzvf emacs-25.1.tar.gz
cd emacs-25.1
./configure
make
sudo checkinstall

# 删除emacs25
sudo dpkg -r emacs-25
```

