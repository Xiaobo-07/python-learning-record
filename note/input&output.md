# 输入、输出
## 输出（ print ）
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

## 输入（input）
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