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
参考程序[conv_grade.py](./code/conv_grade.py)

### 3.2 循环语句

循环语句的应用场景：
- 用户登录，当用户输入的账号或者密码不正确时需要重新输入
- 猜数字游戏，当玩家没猜中数字时会让玩家重新猜测，直到猜中数字为止

实际应用中当然还有很多类似的例子。

#### 3.2.1 for循环
语法结构：

```
for 变量 in 集合:
	...
	...
	...
```

我们注意到，如果要执行 for 循环语句就必须有一个参数的集合来指定循环的次数，所以我们就要提到一个Python的内置函数 `range()` 这个函数可以产生一个整数集。关于 `range()` 函数的用法我们可以先打开在cmd命令行操作窗口打开Python环境输入`help(range)`得到以下结果：

```
>>> help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
```

从帮助里我们不难得到`range()`函数的用法：
1. 可以输入可以是一个变量也可以是多个变量
2. 返回一个整型数列
3. 如果输入一个变量则默认从0开始产生一个数列，步长默认为1
4. 产生数列的范围包含开头不包含结束

```python
range(start, stop, step)
'''
start:数列开始的数字
stop:数列结束的数字
step:步长
'''
#用法：
range(0,10,1) #产生0, 1, 2, 3, 4, 5, 6, 7, 8, 9的一个数列
range(1,10,2) #产生1, 3, 5, 7, 9的数列
range(0,10) #生成0-9的数列步长为1同range(0,10,1)
range(10) #默认start = 0, step = 1
```

一个简单的案例：用 for 循环打印三遍Hello, world!
```python
for i in range(2):
	print('Hello, World!')
#这里的i就是变量，range(2)就是集合
```
接下来可以做一个小练习了，我们都玩过这样一个游戏，1个青蛙，1一张嘴，2个眼睛，4条腿。现在我们要用Python来打印1-20数青蛙。
```
练习1：数青蛙游戏
要求：
	1. 输出格式'x只青蛙x张嘴x个眼睛x条腿，扑通扑通跳下水'
	2. 输出1,2,3...,20
	3. 要求使用for循环
	4. 用range()函数产生数列
```
参考程序[count_frogs.py](./code/count_frogs.py)
```
练习2：猜数字游戏
要求：
	1. 从1~10中随机产生一个数字
	2. 玩家可以从键盘输入数字进行猜测
	3. 玩家共有3次机会
	4. 如果玩家输入的数字超出答案范围(1~10)则警告
	5. 每次输入前提示玩家剩余次数
提示：
	产生随机数需要
	'''
	 import random
	 random.randint(1,10)
	'''
```
参考程序[num_guess1.py](./code/num_guess1.py)

最后提两个关键字：
- pass: 在条件语句中如果没有要执行的语句时不能空着需要用`pass`来代替。pass代表的就是空语句
- break: 中断循环，如果循环进行到某个阶段时想跳出循环就可以用`break`来执行

#### 3.2.2 while循环
语法结构：
```
while 条件:
	语句块1
else:
	语句块2
```
说明：当条件成立时会一直执行语句块1，直到条件不成立时执行语句块2

一个简单的例子：打印1~20的累加和
```python
sum01 = 0
n = 1
while n <= 20:
	sum01 += n
	n += 1
print(sum01)
```
下面来做一个练习，还是刚刚玩过的猜数字游戏，只不过现在规则发生了变化：
```
while循环练习之猜数字
要求：
    1. 从1~99中产生随机数字 answer_num
    2. 用户可以从键盘输入猜测的数字 user_guess
    3. 判断用户输入的数字是否猜中
    4. 若用户没有猜中数字则输出提示并不断缩小范围，直到用户猜中数字为止
    5. 记录用户猜中数字用的次数并输出
```
参考程序[num_guess.py](./code/num_guess.py)

#### 3.2.3 嵌套循环
在实际案例中有时一个循环并不能满足我们的要求，这就需要嵌套循环。顾名思义，嵌套循环就是指在循环内部再加一个或多个循环。下面通过一个实例来说明嵌套循环结构：
```python
'''
打印5层三角形输出形式如下：
*
**
***
****
*****
'''

#用for循环
for i in range(1,6):
	for j in range(i):
		print('*', end='')
	print()

#用while循环
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
    print()
    i += 1
```
看明白上面的嵌套循环之后就可以来用一个练习来验证一下我们的成果了：
```
练习：九九乘法表
要求：
	输出以下形式的九九乘法表
	1x1=1
	1x2=2 2x2=4
	...
	1x9=9 ... 9x9=81
```
参考程序[multi_table.py](./code/multi_table.py)

## 四、字符串
### 4.1 字符串的声明
在Python中声明字符串有三种方法：
```python
s1 = 'abc' #单引号
s2 = "abc" #双引号
s3 = '''abc''' #三引号
```
这三种方法声明三种字符串呢？下面就每一种声明方法单独介绍

1. 单引号：一般声明字符串变量时使用，或者使用双引号会产生歧义时使用。例如：

```
在Python中如果声明一个字符串变量，将其赋值为 Boy say:"Good morning"
如果使用双引号进行声明则会出现以下情况：
str1 = "Boy say:"Good morning""
于是这样就产生了歧义，Python解释器会认为"Boy say: "为一个字符串后面的无法识别然后就会报语法错误。
所以这时我们就要用单引号来进行声明：
str1 = 'Boy say:"Good morning"'
```

2. 双引号：一般字符串声明时使用，或者使用单引号会出现歧义时。例如：

```
如果声明一个字符串变量其内容为 Let's go!
使用单引号声明：
str2 = 'Let's go!'
这样也会产生歧义，Python解释器就会报语法错误，为了解决这个错误，我们可以用两种方法：
1. 用双引号
str2 = "Let's go!"
2. 对单引号进行转义
str2 = 'Let\'s go!'
显然用双引号声明更加直观
```

3. 三引号：三引号不同于以上两种，三引号可以保留格式，多用来声明长字符串。如果字符串中出现换行等，三引号定义的字符串也能很好的保留下来：

```
str3 = '''Let's go!'''
str3 = '''Bob say:"Good morning"'''
str3 = '''请爱的xxx:
你好
'''
这样的声明都是合法的
```

### 4.2 字符串运算符
常用字符串运算符，假设`str1 = 'hello', str2 = 'world'`

|符号|描述|例子|
|---|---|---|
|+|拼接两个字符串|str1+str2='helloworld'|
|* | 字符串复制操作|str1*10相当于将str1复制10次|
|in|判断是否是字符串的子串|'h' in str1,结果为True|
|not in|判断是否不是字符串的子串|'he' not in str2,结果为True|

### 4.3 str,repr和原始字符串
当我们定义一个字符串，其中包含转义字符时，系统就会默认输出转义字符，除非我们对转义字符再进行转义。那么有什么更好的方法来解决这个问题么，我们先来看几个例子：
```
>>> print(str('hello\nworld'))
hello
world
>>> print(repr('hello\nworld'))
'hello\nworld'
>>> print(r'hello\nworld')
hello\nworld
```
通过上面的例子我们不难发现，str函数不能将字符串中的转义字符自动转义，在输出时还是会输出转义字符。但是repr函数就可以保留用户原始输入的字符串，即使其中包含了转义字符也会屏蔽掉。

原始字符串用前缀 r 表示，原始字符串不以特殊方式处理反斜杠，即原始字符串中的转义字符不会被翻译，这种功能类似于repr函数。

### 4.4 字符型变量与字符串索引
有过C/C++学习基础的人就会有疑惑，为什么先讲字符串而没有将字符型变量？岂不是本末倒置了。不是这样的，因为在Python中没有针对字符型变量的定义。那么如何定义字符型变量呢。只需要定义一个字节的字符串就行了。

```
//C/C++
char c = 'a';
#python
char = 'a'
```

字符串索引，当我们需要字符串中的某一个子串的时候应该怎么办呢。这时候就要用字符串索引。拿我们的第一个Python程序`hello.py`来说，如何取出文件名`hello`而不要拓展名`.py`呢？

```python
file1 = 'hello.py'
file_name = file1[0:5] #取字符串file1里的第0-4个字符组成的字符串
extention_name = file1[5:8] #取字符串file1里的第5-7个字符组成的字符串
```

通过上面的例子我们简单的了解了字符串索引`[]`的用法了，下面深一步介绍字符串索引。

```python
str0 = 'abcdefg'
#str0[start:stop:step] 从start开始到stop为止以步长为step取字符串str0中的字符构成新的字符串
#start默认为0，stop默认到字符串结尾，step默认为1
str1 = str0[1:4] #结果为 bcd 注意，索引值从0开始，第一个字符对应的是0，而且索引包含开始不包含结尾，类似于range
str2 = str0[::-1] #结果为 gfedcba 当步长为负时表示从后往前数
#start和stop还可以为负数，表示倒数第几个。最后一个为-1
str3 = str0[-4:-1] #结果为 def 不包含-1
```

所以当我们想要逆序一个字符串的时候就可以这样来做:`str1 = str0[::-1]`

### 4.5 字符串内置函数

常用字符串的内置函数表见[string_table.md](./string_table.md)