# 集合
定义：无序的不重复的元素组成的序列

关键字：set

特点：集合内的元素是不重复的

## 集合的声明 `set`
```python
set0 = set() # 声明空集合
set1 = {1,2,3} # 集合的声明可以用{}，只不过{}内的元素不是成对出现而是单独存在的。
```

## 应用
集合常用来去除列表中的重复元素：
```python
list0 = [3,1,4,3,5,5,6,2,0]
set0 = set(list0)
#结果：set0 = {0,1,2,3,4,5,6}
```

## 集合中的运算符
- ` - `取差集
```python
set0 = {1,2,3,4}
set1 = {1,4}
set2 = set0 - set1
# set2 = {2,3}
```

- ` & `取交集
```python
set0 = {1,2,3,4}
set1 = {1,4，5}
set2 = set0 & set1
# set2 = {1,4}
```

- ` | `取并集
```python
set0 = {1,2,3,4}
set1 = {1,4,5,6}
set2 = set0 | set1
# set2 = {1,2,3,4,5,6}
```

- ` ^ `对称差集，取两个集合中不同的元素
```python
set0 = {1,2,3,4}
set1 = {1,4,5,6}
set2 = set0 ^ set1
# set2 = {2,3,5,6}
```

## 集合的内置函数
- `add()`集合添加元素
```python
set0 = set()
set0.add(1)
# set0 = {1}
```

- `update()`以列表或其他内容更新集合
```python
set0 = {1,2,3}
list0 = {4,5,6}
set0.update(list0)
# set0 = {1,2,3,4,5,6}
```
- `remove()`删除集合中的指定元素，元素不存在则报错
```python
set0 = {1,2,3,4}
set0.remove(3)
# set0 = {1,2,4}
```

- `pop()`删除集合中的元素并返回其值
```python
set0 = {1,2,3,4}
result = set0.pop()
# result = 1 set0 = {2,3,4}
```

- `clear()`清除集合中的所有元素
```python
set0 = {1,2,3,4}
set0.clear()
# set0 = {}
```

- `discard()`与`remove()`类似，但元素不存在时不会报错

- `difference()`取差集
```python
set0 = {1,2,3,4}
set1 = {1,4}
set2 = set0.difference(set1)
# set2 = {2,3}
```

- `intersection()`取交集
```python
set0 = {1,2,3,4}
set1 = {1,4}
set2 = set0.intersection(set1)
# set2 = {1,4}
```

- `union()`取并集
```python
set0 = {1,2,3,4}
set1 = {1,4,5,6}
set2 = set0.union(set1)
# set2 = {1,2,3,4,5,6}
```