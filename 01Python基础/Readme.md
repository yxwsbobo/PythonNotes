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
* Python使用相同缩进来标识一个代码块,或称为复合语句
* 空语句使用 pass 表示
```python


if True:
    print("hi")
    print("Julia")
elif True:
    pass
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
只有值有类型
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
* bool 类型的值为 True,False
```python
#除法,得到实数
10/3    #>>> 3.3333

#除法 得到整数
10//3    #>>>3

#乘方
2 ** 10    #>>>1024

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
* 使用函数 list(seq) 得到列表
* 列表中元素的值可以改变
* 列表支持嵌套
* 支持下表访问,支持加法
* 切片后返回新的列表
* 支持部分操作append,pop
```python
    Student = ["Kin",31,"Python"]
    Student += ["Lin",21]
    
    Studen[0:3] = ["Name","Age","Language"]

```

---
> 元组 Tuple
* 使用()定义一组值不可变元素
* 使用函数 tuple(seq) 得到元组
* 可以与List互相转换
* 速度比List快
* 似乎是一个值不可变的List
* 可以同String一样,使用 * 重复
* Tuple 赋值时只有一个元素时需要在元素后跟 , #*好奇怪的设定,大概怕和别的类型混了吧*
```python

   Student = ("Kin",31,"Python")
   Student += ("Lin",21)

   Studen = ("Kin",)

   Studen = Studen *4

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
* 访问不存在的键会发生异常,相应的可以使用成员函数 .get(key,defaultValue) 代替,当键不存在是会返回 defaultValue
* 初始化使用{Key:Value,...}
* 创建空字典使用 {}
* 可以使用 dict() 创建字典 

成员函数列表:
函数名|说明
---|---
.clear()    |   清空
.copy()     |   浅复制
.fromkeys(seq) |   以seq为键创建字典,值为默认值
.get(key,value) |   返回指定键的值,不存在则返回 value
.setdefault(key,value)  | 如果键不存在则创建键并赋值value (*如果存在说明都不做?*)
.items()    |   返回一个List,元素为键值Tuple
.keys()     |   返回键组成的List
.values()   |   返回值组成的List
.update(dict2)  |   使用dict2更新字典 (*是替换还是增加?*)

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

---
> 范围 range
* 使用函数range(StartNum,EndNum,Step)用来自动生成序
* 其中StartNum省略表示从0开始,Step省略表示步进为1,Step可为负
* *似乎只能用来生成数字?*
```python
Numbers = range(5) #--> == range(0,5)

for n in Numbers:
    print(n,end=",")

```