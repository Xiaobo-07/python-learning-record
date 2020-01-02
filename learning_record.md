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
### 2.1 Hello World
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

### 2.2 变量
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
接下来介绍Python变量命名的规则。与其他语言有相似的地方也有不同之处。Python的变量命名也只能是字符、数字、下划线的组合，而且不能以数字开头。

不同之处在于Python的字符可以是汉字等，但是其他语言必须是26个英文字母及其大小写。虽说Python可以用汉字来给变量命名但是并不推荐这么做，谁知道什么时候会报错呢。
```java
int username
int userNaem1
int user_name1
int _username1
//以上这些变量名（标识符）在java中都是可行的
/*
这些命名方式都会报错：1username,用户名……
*/
```
```python
'''
在Python中下面的变量名都是合法的：
username, user_name, username1, username_1, 用户名, 用户名1
但是不能以数字开头，下面的命名是非法的：
1username, 1用户名
'''
```

### 2.3 输入、输出
#### 2.3.1 输出（ print ）
类似于C语言的`printf()`、C++的`cout<<`、java的`System.out.Println()`，Python也有其内置的输出函数即`print()`。是不是很接近于我们人类的语言了，就是一个print（打印）就能清楚地表达输出关系。

下面来介绍`print()`的用法：
```python
#case 1: 直接在print()中写入要输出的内容
print('hello,world!')
print(567)
#case 2: 通过变量名输出
message = 'hellow,world!'
num = 567
print(message)
print(num)
#case 3: 多输出
print(message,num)
#case 4: 多输出更改sep和end,sep为数据之间的间隔默认为空格, end为结尾默认为换行'\n'
print(message,num,sep = '',end = '\t')
```

数据的格式化输出，使用与一个print()输出多组数据和提示符
```python
#方法一: %xxx的格式化输出，其中%xxx是占位符，需要写明变量类型
name = '小明'
age = 12
money = 10.00
print('我的名字是%s,今年%d岁了,每周有%.2f元零花钱。' % (name,age,money))
#方法二: format的格式化输出，{}为占位符，不用写明变量类型
print('我的名字是{},今年{}岁了,每周有{}元零花钱。'.format(name,age,money))
```
总结常见的格式控制符
|  符号 | 描述  |
| ------------ | ------------ |
| %s  | 格式化字符串  |
| %d  | 格式化整数（整型）  |
| %f  | 格式化浮点数字，可指定小数点后数字  |
| %.1f  | 格式化浮点型数字，精确到小数点后1位  |

#### 2.3.2 输入（input）
和输出一样，Python也有内置的输入函数`input()`，以C语言为比较，说明Python的`input()`函数的特点与用法

在C语言中，如果输出输入提示语，并且输入一个数据时要进行如下操作：
```c
int a;//声明变量
char b;
float c;
printf("请输入：");//输出提示信息
scanf("%d",&a);//输入整型数据，%d指定整型
scanf("%c",&b);
scanf("%f",&c);
```
但是在Python中，我们可以通过一个`input()`函数来解决C语言中一系列复杂的操作。就如同输入一个整型数据来说，在C语言中需要先声明变量名，（然后输出提示语），再从输入键盘读取数据。但在Python中我们可以这样操作：、
```python
a = int(input('请输入整型数据'))
```
在这里值得一提的是，Python的`input()`输入的都是字符串类型的数据，如果要得到整型的数据就要进行强制类型转换`int()`。还有其他类型的强制类型转换：浮点型`float()`, 字符串类型`str()`。