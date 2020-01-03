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

首先新建一个文件命名为 hello.py 然后在文件中写入以下内容：
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

数据的格式化输出，适用于一个print()输出多组数据和提示符
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

### 2.4 运算符

#### 2.4.1 算数运算符
顾名思义，算术运算符就是用来进行算数运算的符号，下面列出了常用的算术运算符：

| 符号 | 描述 |
|-------|-------|
| + | 加法运算，字符串变量也可使用表示连接两个字符串
| - | 减法运算符 |
| * | 乘法运算符 |
| / | 除法运算符 |
| % | 求余数，a % b 表示a除以b的余数 |
| // | 整除运算，a // b 表示a除以b 得到的整数部分 |
| ** | 幂运算，a ** b 表示a的b次方 |

#### 2.4.2 关系运算符
假设 `a = 10, b = 20` 则：

|符号|描述|实例|
|---|---|---|
|==|等于，比较两个对象是否相等|a == b，结果为False|
|!=|不等于，比较两个对象是否不等|a != b，结果为True|
|>|大于，返回是否大于|a > b，结果为False|
|<|小于，返回是否小于|a < b，结果为True|
|>=|大于等于|a >= b，结果为False|
|<=|小于等于|a <= b，结果为True|

关系运算符的结果只有两种True和False

#### 2.4.3 赋值运算符
假设有变量`a, b, c` 则

|符号|描述|实例|
|---|---|---|
|=|简单赋值运算符|c = a + b 将 a + b 的结果赋值给 c|
|+=|加法赋值运算符|c += a 等价于 c = c + a|
|-=|减法赋值运算符|c -= a 等价于 c = c - a|
|*=|乘法赋值运算符|c *= a 等价于 c = c * a|
|/=|除法赋值运算符|c /= a 等价于 c = c / a|
|%=|取余赋值运算符|c %= a 等价于 c = c % a|
|**=|幂赋值运算符|c **= a 等价于 c = c ** a|
|//=|整除赋值运算符|c //= a 等价于 c = c // a|

#### 2.4.4 逻辑运算符
假设`a = True, b = False`

|运算符|表达式|描述|实例|
|---|---|---|---|
|and|x and y|x与y，两者同为True时为True，一个为False则为False|a and b，结果为False|
|or|x or y|x或y，两者有一个为True则为True|a or b，结果为True|
|not|not(x)|取反，x为True则为False，x为False则为True|not(a),结果为False|

#### 2.4.5 位运算符

|运算符|描述|
|---|---|
|&|按位相与|
|\||按位相或|
|~|按位取反|
|^|按位异或|
|<<|左移运算，将二进制数向左移若干位，高位舍弃低位补0|
|>>|右移运算，将二进制数向右移若干位，低位舍弃高位补0|

#### 2.4.6 三目运算符

```python
result = a if x == y else b
'''
以上表达式就是三目运算，该表达式的意思是
如果 x == y 这个表达式成立，n那么就将a赋值给result否则将b赋值给result
这里的 x == y 只是一个例子，可以是任何关系运算表达式，当然a, b也可以是数值也可以是表达式如果 a, b 为表达式则应该写做：
result = (a + b) if x == y else (a - b)
'''
```

## 三、条件与循环

### 3.1 if条件语句
我们在使用邮箱的时候总是先登陆邮箱，在登陆的时候就要输入你的邮箱地址和密码。那么如何判断你的密码输入的是否正确呢，这时候就需要一个判断，或者说用一个条件语句进行判断你输入的密码是否正确，或者检查你的用户名是否注册了。

在Python中`if else` 就是进行这种工作的语句。相信很多有基础的人对这个语句并不陌生，同样的，我们通过对比的方式来看Python的`if`语句与其他语言有何不同

举一个简单的例子，有两个数`a = 10, b = 20`判断两者的大小并输出，然后计算`|a - b|`

```c
//C语言
#include <stdio.h>

int main()
{
	int a = 10;
	int b = 20;
	int ans = 0;
	if(a > b)
	{
		printf("%d > %d\n",a,b);
		ans = a - b;
		printf("|%d - %d| = %d",a,b,ans);
	}
	else
	{
		printf("%d < %d\n",a,b);
		ans = b - a;
		printf("|%d - %d| = %d",a,b,ans);
	}
	return 0;
}
```
```python
#python
a = 10
b = 20
if a > b:
	print('{} > {}'.format(a,b))
	print('|{}-{} = {}|'.format(a,b,a-b))
else:
	print('{} < {}'.format(a,b))
	print('|{} - {} = {}'.format(a,b,b-a))
```
通过比较上面两组代码我们可以很清楚地看到Python与C语言的不同。在Python中十分重视缩进，不同于其他有些语言的花括号将代码块括起来，Python是利用缩进来区分代码块的。而且`if`语句的使用也有其特点，写完`if`之后敲一个空格然后写条件表达式最后以冒号开始执行判断后的操作。注意要想执行判断结果为True后的操作必须将代码进行缩进，否则后面的代码就会是与`if`同级的代码，不会受到`if`的影响。

同其他语言一样Python的条件语句也是可以嵌套的，如果多个条件也可以用`if elif else`来执行判断
```python
'''
多条件的判断
if 条件1:
	xxx
elif 条件2:
	xxx
elif 条件3:
	xxx
else:
	xxx
'''
```

接下来可以用一个简单的练习来巩固`if`语句的学习：
```
if语句练习之成绩转换
要求：
	1. 输入一个百分制成绩，然后将成绩输出为等级
	2. 各等级对应的成绩段如下:
		优+     >=90
		优-     >=80, <90
		良      >=70, <80
		及格    >=60, <70
		不及格  <60
```
参考程序[conv_grade.py](code\conv_grade.py)