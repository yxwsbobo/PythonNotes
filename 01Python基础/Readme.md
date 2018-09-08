# Python基础

> 标识符

    可以使用中文等非ascii  
    其余规则为一般常识


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

> 类型
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

> 字符串
* 使用 '' 或 "" 包裹 定义字符串
* 使用 ''' 或 ''' 包裹 定义多行字符串
* 支持转义符 \, 通过加前缀 r/R 禁用转义 R"原样输出\n不会换行"
* 常量字符串可自动连接 "this " "is " "a string" == "this is a string"
