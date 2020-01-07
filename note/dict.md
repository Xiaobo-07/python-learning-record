# 字典
首先了解映射，所谓映射就是通过名称（而不是索引值）来访问其各个值的数据结构。在Python中，字典是唯一的内置映射类型，其中的值不是按顺序排列，而是存储在关键字（key）下。关键字可以是数字、字符串或元组。

字典的用途，旨在能够通过找到特定的关键字（key）来获悉其值（value）。

## 字典的定义与声明
字典的声明有两种方法，直接通过`{}`进行定义，`{}`内填入字典的内容，要注意的是字典的内容都是关键字和值成对出现的。或者可以使用`dict()`函数将其他格式的内容转换成字典。
```python
#声明空字典
dict0 = {} #较常用的声明方式
dict1 = dict()
#声明字典
dict2 = {'ID':'1234567','name':'xiaoming'}#字典声明为{key1:value1,key2:value2}的形式，关键字与值用冒号隔开
dict3 = dict([('name','Xiaoming')])#相当于dict4 = {'name':'Xiaoming'}
```

## 字典的常用操作
- 添加与修改元素
```python
#格式：dict[key] = value(如果没有同名的key时会增加，有同名的key时则会修改value)
dict0 = {}
dict0['brand'] = 'HUAWEI'#dict0 = {'brand':'HUAWEI'}
dict0['brand'] = 'MI' #dict0 = {'brand':'MI'}
```

- 查询元素
```python
#格式：dict[key]
dict0 = {'brand':'HUAWEI','type':'mate 30 pro(5G)'}
value = dict0['brand']#value = 'HUAWEI'
```

## 字典常用内置函数
- `clear()`删除所有的字典项

- `copy()`复制字典，返回一个与原字典项相同的字典

- `fromkeys()`通过关键字新建一个新字典，值默认为None
```python
dict0 = dict.fromkeys(['name','age'])
#结果：dict0 = {'name':None, 'age':None}
```

- `get()`获取字典中某关键字对应的值。若字典中没有该关键字则返回None
```python
dict0 = {'name':'小明', 'age':12}
value = dict0.get('name')
#value = '小明'
```

- `items()`返回一个包含所有字典项的列表，其中每个元素都是(key,value)的形式。
```python
dict0 = {'name':'小明', 'age':12}
result = dict0.items()
#结果：result = dict_items([('name', '小明'), ('age', 12)])
```

- `values()`取出字典中所有值保存在列表中
```python
dict0 = {'name':'小明', 'age':12}
result = dict0.values()
#结果：result = dict_values(['小明', 12])
```

- `keys()`取出字典中所有关键字保存在列表中
```python
dict0 = {'name':'小明', 'age':12}
result = dict0.values()
#结果：result = dict_keys(['name', 'age'])
```

- `pop()`通过关键字删除字典中的键—值对,返回键—值对的值
```python
dict0 = {'name':'小明', 'age':12}
result = dict0.pop('name')
#结果：result = '小明' dict0 = {'age':12}
```

- `update()`使用一个字典中的项来更新另一个字典
```python
dict0 = {'name':'小明', 'age':12}
dict1 = {'adress':'CHINA'}
dict0.update(dict1)
#结果：dict0 = {'name':'小明', 'age':12, 'adress':'CHINA'}
```