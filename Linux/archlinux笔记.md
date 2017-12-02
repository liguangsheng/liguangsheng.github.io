Title: archlinux笔记
Date: 2017-02-09
Modified: 2017-02-09
Category: Linux
Tags: linux, archlinux

Shell: zsh
窗口管理器: i3wm 
终端模拟器: urxvt 
文本编辑器: vim/emacs
文件浏览器: pfmanfm
网页浏览器: firefox
音乐播放器: moc
邮件客户端: mutt
代理服务器: shadowsocks
文档浏览器: zeal

## 安装

## VirtualBox Additions
```
sudo pacman -S virtualbox-guest-utils xf86-video-dummy xf86-video-fbdev xf86-video-vesa
sudo modprobe -a vboxguest vboxsf vboxvideo
sudo systemctl enable vboxservice.service
```

## yaourt
编辑`/etc/pacman.conf`，在末尾添加：
```
[archlinuxcn]
SigLevel = Optional TrustedOnly
Server = http://repo.archlinuxcn.org/$arch
```

## 安装软件包
```
sudo pacman -S curl wget tmux moc rxvt-unicode zsh chromium vim emacs git python python-setuptools python-pip python2 python2-setuptools python2-pip
```

## 字体
```
yaourt -S ttf-ms-fonts
yaourt -S adobe-source-code-pro
yaourt wqy
git clone https://github.com/powerline/fonts.git
```

## xorg
```
sudo pacman -S xorg-server xorg-server-utils xorg-apps xorg-xinit xorg-twm xorg-xclock xterm 
cp /etc/X11/xinit/xinitrc ~/.xinitrc
```

## i3wm
```
sudo pacman -S i3wm i3status
```

常用快捷键
|快捷键(区分大小写)|功能描述|
|---|---|
|Mod E|关闭i3|
|Mod C|重新加载i3|
|Mod R|重新启动i3|
|Mod Q|关闭当前窗口|
|Mod e|进入排列模式|
|Mod w|进入标签模式|
|Mod s|进入层叠模式|
|Mod r|进入窗口尺寸调整模式|
|Mod Enter|打开终端|

## urxvt
```
# 安装
yaourt -S rxvt-unicode rxvt-perls
```
`~/.Xresources`配置见https://github.com/liguangsheng/dotfiles/blob/master/.Xresources

### Cpoy & Patse
urxvt使用PRIMARY来复制和粘贴，不能与系统的clipboard同步。

使用urxvt-perls的selection-to-clipboard可以同步。

也可以使用第三方的程序来同步PRIMARY和系统的clipboard。
```
yaourt -S autocutsel
```
在`~/.xinitrc`中加入
```
autocutsel -fork &
autocutsel -selection PRIMARY -fork &
```

## 中文输入法
```
yaourt -S fcitx fcitx-im fcitx-cloudpinyin fcitx-sogoupinyin fcitx-configtool
```

## zsh
```
yaourt -S zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

## feh
使用feh设置壁纸
```
feh --bg-scale <path-to-wallpaper>
```

## misc
```
pacman -Syu 更新系统
pacman -Rsc 删除包及其以来
```