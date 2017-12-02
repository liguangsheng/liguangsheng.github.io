---
Title: git笔记
Date: 2017-07-03
Modified: 2017-07-03
---

```
# 克隆仓库
git clone <url> <localpath>

# 查看分支
git branch

# 查看所有分支
git branch -a

# 切换分支
git checkout <branch_name>

# 创建并切换分支
git checkout -b <branch_name>

# 添加文件到暂存区
git add <filename>

# 添加所有文件到暂存区
git add --all

# 提交修改
git commit -m "<comment>"
```

# 暂存
stash 操作是栈式的操作。
```
# 将当前修改暂存起来
git stash

# 列出当前stash栈
git stash list

# 查看stash详情
git stash show

# 丢弃stash
git stash drop

# 将先前的暂存的状态恢复出来
git stash pop | apply

# 清空暂存的状态
git stash clear
```

# 修改commit

```
# 合并commit
git rebase -i
```