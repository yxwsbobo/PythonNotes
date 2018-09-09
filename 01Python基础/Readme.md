# Python基础

> 标识符

    可以使用中文等非ascii  
    其余规则为一般常识

---
> 注释
```python
# 单行注释

"""
多行注释
与多行字符串写法相同
是规则还是使用字符串假装注释了?
"""

'''
同上
'''

```

---
> 代码块
```python
#Python使用相同缩进来标识一个代码块,或称为符合语句

if True:
    print("hi")
    print("Julia")
else:
    print("hi")
    print("Kite")

print("how are you")

# >>> hi Julia how are you
```

---
> 赋值
* 可同时对多个变量进行赋值,变量与值数量必须一致
```python
    Name,Age = "Kin",32
    Name,Age = "Lin","ok"

    # Name,Age = "Kin",32,1  #Error
    # Name,Age = "Kin"  #Error

```

# 类型

```python
"""
Python中变量没有类型
只有值友类型
基本类型,有整数,实数,字符串等
"""

var = 1;
print(var, " type :", type(var))
var = 1.99;
print(var, " type :", type(var))
var = "hello"
print(var, " type :", type(var))

```

---
> 数字 *支持 int,float,bool,complex*
* 使用除法运算符 / 得到实数
* 使用除法运算符 // 得到整数
* 使用乘方运算符 ** 计算乘方
* 混合运算时会把整数提升为实数计算
```python
#除法,得到实数
10/3

#除法 得到整数
10//3

#乘方
2 ** 10

#其他与常识相同

```

---
> 字符串 String
* 使用 '' 或 "" 包裹 定义字符串
* 使用 ''' 或 ''' 包裹 定义多行字符串
* 支持转义符 \\, 通过加前缀 r/R 禁用转义 R"原样输出\n不会换行" (*除\\" ?*)
* 常量字符串可自动连接 "this " "is " "a string" == "this is a string"
* 使用 * 重复字符串
* 引索字符允许使用负数 

```python
Say = "Hello World" + (" I love you" * 3)
Path = R"C:\Windows\System"

ch = Path[-1] #>> ch == m
```
* 获取子字符串
```python
>>> word = 'ilovepython'
>>> word[1:5]
'love'
>>> word[:]
'ilovepython'
>>> word[5:]
'python'
>>> word[-10:-6]
'love'
```

---
> 列表 List
* 使用[]定义一组元素,类型可以不相同
* 支持下表访问,支持加法
* 切片后返回新的列表
* 支持部分操作append,pop
```python
    Student = ["Kin",31,"Python"]
    Student += ["Lin",21]
```

---
> 元组 Tuple
* 使用()定义一组值不可变元素
* 可以与List互相转换
* 速度比List快
* 似乎是一个值不可变的List
```python

   Student = ("Kin",31,"Python")
   Student += ("Lin",21)

```

---
> 集合 Sets
* 使用大括号或 set() 定义一组无序不重复元素的集合
* 支持 交,并,补,差
* 定义空集合使用 set(),{}定义一个空字典
```python
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a
{'a', 'b', 'c', 'd', 'r'}
>>> a - b     # a和b的差集
{'b', 'd', 'r'}
>>> a | b     # a和b的并集
{'l', 'm', 'a', 'b', 'c', 'd', 'z', 'r'}
>>> a & b     # a和b的交集
{'a', 'c'}
>>> a ^ b     # a和b中不同时存在的元素
{'l', 'm', 'b', 'd', 'z', 'r'}
```

---
> 字典 Dictionaries
* 键值对的集合
* 键 无序不重复
* 初始化使用{Key:Value,...}
* 创建空字典使用 {}
* 可以使用 dict() 创建字典 
```python
>>> dic = {}  # 创建空字典
>>> tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}
>>> tel
{'Tom': 1320, 'Jack': 1557, 'Rose': 1886}
>>> tel['Jack']   # 主要的操作：通过key查询
1557
>>> del tel['Rose']  # 删除一个键值对
>>> tel['Mary'] = 4127  # 添加一个键值对
>>> tel
{'Tom': 1320, 'Jack': 1557, 'Mary': 4127}
>>> list(tel.keys())  # 返回所有key组成的list
['Tom', 'Jack', 'Mary']
>>> sorted(tel.keys()) # 按key排序
['Jack', 'Mary', 'Tom']
>>> 'Tom' in tel       # 成员测试
True
>>> 'Mary' not in tel  # 成员测试
False

>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'jack': 4098, 'sape': 4139, 'guido': 4127}

>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

>>> dict(sape=4139, guido=4127, jack=4098)
{'jack': 4098, 'sape': 4139, 'guido': 4127}

```
