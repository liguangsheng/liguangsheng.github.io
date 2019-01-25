---
Title: jupyter笔记
Date: 2016-12-03
Modified: 2016-12-03
---

```
# 安装jupyter
pip install jupyter
# 建立server文件夹
mkdir jupyter-server
cd jypyter-server
# 运行jypyter-notebook
jupyter notebook
```

## 配置

在`~/.jupyter/custom`下新建`custom.css`。notebook会自动加载这个css文件，来改变页面样式。

## 快捷键

|快捷键|描述|
|------|----|
|Tab|代码补全或者缩进|
|Ctrl-Enter|运行当前cell|
|Shift-Enter|运行当前cell，选择下一个cell|
|Alt-Enter|运行当前cell，下面插入一个cell|
|Ctrl-]|缩进|
|Shift-Tab|帮助信息|