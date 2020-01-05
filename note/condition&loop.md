条件与循环

## 1. if条件语句
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
参考程序[conv_grade.py](../code/conv_grade.py)

## 2. 循环语句

循环语句的应用场景：
- 用户登录，当用户输入的账号或者密码不正确时需要重新输入
- 猜数字游戏，当玩家没猜中数字时会让玩家重新猜测，直到猜中数字为止

实际应用中当然还有很多类似的例子。

### 2.1 for循环
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
参考程序[count_frogs.py](../code/count_frogs.py)
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
参考程序[num_guess1.py](../code/num_guess1.py)

最后提两个关键字：
- pass: 在条件语句中如果没有要执行的语句时不能空着需要用`pass`来代替。pass代表的就是空语句
- break: 中断循环，如果循环进行到某个阶段时想跳出循环就可以用`break`来执行

### 2.2 while循环
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
参考程序[num_guess.py](../code/num_guess.py)

### 2.3 嵌套循环
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
参考程序[multi_table.py](../code/multi_table.py)