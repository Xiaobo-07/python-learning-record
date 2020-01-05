# 字符串
## 1. 字符串的声明
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

## 2. 字符串运算符
常用字符串运算符，假设`str1 = 'hello', str2 = 'world'`

|符号|描述|例子|
|---|---|---|
|+|拼接两个字符串|str1+str2='helloworld'|
|* | 字符串复制操作|str1*10相当于将str1复制10次|
|in|判断是否是字符串的子串|'h' in str1,结果为True|
|not in|判断是否不是字符串的子串|'he' not in str2,结果为True|

## 3. str,repr和原始字符串
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

## 4. 字符型变量与字符串索引
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

## 5. 字符串内置函数

<table border=0 cellpadding=0 cellspacing=0 width=1034 style='border-collapse:
 collapse;table-layout:fixed;width:775pt'>
 <col class=xl67 width=143 style='mso-width-source:userset;mso-width-alt:4565;
 width:107pt'>
 <col class=xl67 width=891 style='mso-width-source:userset;mso-width-alt:28501;
 width:668pt'>
 <tr height=24 style='height:18.0pt'>
  <td height=24 class=xl66 width=143 style='height:18.0pt;width:107pt'><font
  class="font6">函数</font></td>
  <td class=xl66 width=891 style='width:668pt'><font class="font6">描述</font></td>
 </tr>
 <tr height=23 style='height:17.5pt'>
  <td rowspan=2 height=48 class=xl69 style='height:36.0pt'>capitalize()</td>
  <td class=xl65>功能：首字母大写，返回新的字符串</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl67 style='height:18.5pt'><font class="font6">格式：</font><font
  class="font7">str.capitalize()</font></td>
 </tr>
 <tr height=25 style='mso-height-source:userset;height:18.5pt'>
  <td rowspan=2 height=50 class=xl69 style='height:37.0pt'>title()</td>
  <td class=xl65>功能：将每个单词的首字母大写，返回新的字符串</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl68 style='height:18.5pt'><font class="font6">格式：</font><font
  class="font7">str.title()</font></td>
 </tr>
 <tr height=25 style='mso-height-source:userset;height:18.5pt'>
  <td rowspan=2 height=50 class=xl69 style='height:37.0pt'>istitle()</td>
  <td class=xl65>功能：判断每个单词的首字母是否是大写，返回值为布尔值</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl68 style='height:18.5pt'><font class="font6">格式：</font><font
  class="font7">str.istitle()</font></td>
 </tr>
 <tr height=23 style='height:17.5pt'>
  <td rowspan=2 height=48 class=xl69 style='height:36.0pt'>upper()</td>
  <td class=xl65>功能：将所有字母转成大写,返回新的字符串</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl68 style='height:18.5pt'><font class="font6">格式：</font><font
  class="font7">str.upper()</font></td>
 </tr>
 <tr height=25 style='mso-height-source:userset;height:18.5pt'>
  <td rowspan=2 height=50 class=xl69 style='height:37.0pt'>lower()</td>
  <td class=xl65>功能：将所有字母转成小写，返回新的字符串</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl68 style='height:18.5pt'><font class="font6">格式：</font><font
  class="font7">str.lower()</font></td>
 </tr>
 <tr height=25 style='mso-height-source:userset;height:18.5pt'>
  <td rowspan=2 height=50 class=xl69 style='height:37.0pt'>swapcase()</td>
  <td class=xl65>功能：将字符串中的大小写转换,返回新的字符串</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl68 style='height:18.5pt'><font class="font6">格式：</font><font
  class="font7">str.swapcase()</font></td>
 </tr>
 <tr height=25 style='mso-height-source:userset;height:18.5pt'>
  <td rowspan=2 height=50 class=xl69 style='height:37.0pt'>len()</td>
  <td class=xl65>功能：计算字符串的长度，返回一个整型数值</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl68 style='height:18.5pt'><font class="font6">格式：</font><font
  class="font7">len(str)</font></td>
 </tr>
 <tr height=25 style='mso-height-source:userset;height:18.5pt'>
  <td rowspan=2 height=50 class=xl69 style='height:37.0pt'>count()</td>
  <td class=xl65>功能：统计字符串中某个元素的数量，返回一个整型数值</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl68 style='height:18.5pt'><font class="font6">格式：</font><font
  class="font7">str.count(char)</font></td>
 </tr>
 <tr height=25 style='mso-height-source:userset;height:18.5pt'>
  <td rowspan=2 height=50 class=xl69 style='height:37.0pt'>find()</td>
  <td class=xl65>功能：查找某个字符串在一定范围内第一次出现的位置，并返回索引值，如果没有查找到则返回-1</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl68 style='height:18.5pt'><font class="font6">格式：</font><font
  class="font7">str.find(str s, int beg, int end)(default: beg = 0,end =
  len(str))</font></td>
 </tr>
 <tr height=25 style='mso-height-source:userset;height:18.5pt'>
  <td height=25 class=xl67 style='height:18.5pt'>rfind()</td>
  <td rowspan=2 class=xl70><font class="font6">功能：查找最右侧或者最左侧第一次出现某元素的位置，并返回索引值，没有查到则返回</font><font
  class="font7">-1</font></td>
 </tr>
 <tr height=24 style='height:18.0pt'>
  <td height=24 class=xl67 style='height:18.0pt'>lfind()</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl67 style='height:18.5pt'>index()</td>
  <td class=xl68><font class="font6">功能用法同</font><font class="font7">find()</font><font
  class="font6">，区别在于如果没找到会报异常</font></td>
 </tr>
 <tr height=23 style='height:17.5pt'>
  <td rowspan=2 height=48 class=xl69 style='height:36.0pt'>replace()</td>
  <td class=xl65>功能：替换字符串中指定字符，返回新的字符串</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl68 style='height:18.5pt'><font class="font6">格式：</font><font
  class="font7">str.repalce(old,new,max)(max</font><font class="font6">指定则替换最多不超过</font><font
  class="font7">max</font><font class="font6">次</font><font class="font7">)</font></td>
 </tr>
 <tr height=23 style='height:17.5pt'>
  <td rowspan=2 height=48 class=xl69 style='height:36.0pt'>isalpha()</td>
  <td class=xl65>功能：判断字符串是否全由字母组成</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl68 style='height:18.5pt'><font class="font6">用法：</font><font
  class="font7">str.isalpha()</font></td>
 </tr>
 <tr height=23 style='height:17.5pt'>
  <td rowspan=2 height=48 class=xl69 style='height:36.0pt'>isdigit()</td>
  <td class=xl65>功能：判断字符串是否全由数字组成</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl68 style='height:18.5pt'><font class="font6">用法：</font><font
  class="font7">str.isdigit()</font></td>
 </tr>
 <tr height=23 style='height:17.5pt'>
  <td rowspan=2 height=48 class=xl69 style='height:36.0pt'>join()</td>
  <td class=xl65>功能：将一个列表按某种规则连接成字符串</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl68 style='height:18.5pt'><font class="font6">用法：</font><font
  class="font7">''.join(seq)</font></td>
 </tr>
 <tr height=23 style='height:17.5pt'>
  <td rowspan=2 height=48 class=xl69 style='height:36.0pt'>strip()</td>
  <td class=xl65>功能：去掉指定的字符串，默认为换行</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl68 style='height:18.5pt'><font class="font6">用法：</font><font
  class="font8">str.strip(str)</font></td>
 </tr>
 <tr height=23 style='height:17.5pt'>
  <td rowspan=2 height=48 class=xl69 style='height:36.0pt'>lstrip()</td>
  <td class=xl65>功能：从左侧去除字符串的某个元素</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl68 style='height:18.5pt'><font class="font6">用法：</font><font
  class="font7">str.lstrip(char)</font></td>
 </tr>
 <tr height=23 style='height:17.5pt'>
  <td rowspan=2 height=48 class=xl69 style='height:36.0pt'>split()</td>
  <td class=xl65>功能：按照指定的字符进行切分字符串，默认为空格，返回一个列表</td>
 </tr>
 <tr height=25 style='height:18.5pt'>
  <td height=25 class=xl68 style='height:18.5pt'><font class="font6">用法：</font><font
  class="font7">str.split(char)</font></td>
 </tr>
 <![if supportMisalignedColumns]>
 <tr height=0 style='display:none'>
  <td width=143 style='width:107pt'></td>
  <td width=891 style='width:668pt'></td>
 </tr>
 <![endif]>
</table>