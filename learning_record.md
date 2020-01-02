# Python学习笔记

<div style="text-align: right"> Author: Xiaobo </div>

## 一、基础准备

### 1.1 Python环境配置
进行Python开发之前需要安装Python或者核实已经安装了它。

#### 1.1.1 Python安装
- 首先下载Python\
    官网下载：https://www.python.org/getit/ \
	如果想一次性解决问题也可以下载Anaconda
	下载地址：https://www.anaconda.com/distribution/ \
	或者也可以从清华源下载：https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
- 安装Python\
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

#### 1.1.3 Python with Visul Studio Code
比较了很多Python编辑器，诸如pycharm，sublime等，最终选择了VS Code. VSCode是一个非常轻量化的编辑器，支持插件扩展，如果调教好了的话将会是一个十分趁手的开发环境。

关于VS Code开发Python的配置网上很多就不列举了。

## 二、基础知识
### 2.1.1 Hello World
Hello World是所有编程者学习的第一个程序，在Python中也不例外。所以我们将开始学习如何用Python打印Hello World.

首先新建一个文件命名为 hello.py 然后在文件中写入一下内容：
```python
print('Hello, World!')
```
然后 Ctrl + s 保存，再在前面一节中所讲的cmd命令行窗口中用以下运行我们的第一个Python程序：
```html
C:\Users\Xiaobo>cd D:\User_Files\python\study

C:\Users\Xiaobo>d:

D:\User_Files\python\study>python hello.py
Hello, World!
```
如果运行过程中没有报任何的错误，那么恭喜你，你的第一个Python程序就完成了。

### 2.1.2 变量
变量通俗的理解就是内存开辟出来的用以存储数据的“容器”

Python的变量是弱类型的，简单来说当你定义一个变量之后，你对变量赋什么类型的值这个变量就是什么类型的。和C或者Java等强类型的变量不同，强类型的变量一旦声明之后就必须赋给同类型的数据，否则就会报错。这个问题在Python中就不存在，因为他的变量是弱类型的，即变量的类型会发生改变。

举一个简单的例子，在java中我们可以这样声明变量：
```java
int count = 0;
String str = 'hello'
count = 1;
str = 'world';//这样是可行的赋值操作，类型相同
/*
下面这种赋值操作是不可行的
count = 'hello';
str = 1;
整型的变量只能赋予整型值，字符串类型的变量只能赋予字符串
*/
```
而在Python中：
```python
name = 'xiaoming' #此时name是字符串类型
age = 12 #此时age是整型
#下面的赋值操作在Python中是合法的
name = 567 #由于567是整型值，所以name由字符串类型变为整型变量
age = '12岁' #age也同样变为字符串类型
```

