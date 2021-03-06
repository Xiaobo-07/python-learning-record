# 变量
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