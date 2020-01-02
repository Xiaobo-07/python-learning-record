# Python学习笔记
<div style="text-align: right"> Author: Xiaobo </div>
## 一、基础准备
### 1.1 Python环境配置
进行Python开发之前需要安装Python或者核实已经安装了它。
#### 1.1.1 Python安装
- 首先下载Python
	官网下载：https://www.python.org/getit/
	如果想一次性解决问题也可以下载Anaconda
	下载地址：https://www.anaconda.com/distribution/
	或者也可以从清华源下载：https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
-  安装Python
	可自行从网上查找安装教程

#### 1.1.2 运行Python
Windows环境下 win+r 打开运行，输入cmd点击确定，进入命令行程序窗口。
输入 python 回车看到如下内容说明Python安装成功，并且你已经进入到Python环境之中
```html
C:\Users\Xiaobo>python
Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
接下来可以在Python中尝试着写出第一个程序hello world
```html
>>> print('hello, world')
hello, world
>>>
```
如果你想退出Python环境可以在命令行写下 exit()

#### 1.1.3 Python with Visul Studio Code
比较了很多Python编辑器，诸如pycharm，sublime等，最终选择了VS Code. VSCode是一个非常轻量化的编辑器，支持插件扩展，如果调教好了的话将会是一个十分趁手的开发环境。
关于VS Code开发Python的配置网上很多就不列举了。
