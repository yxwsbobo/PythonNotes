# 内置函数
> input
* 标准输入?

```python
var = input("Some tips")

```
> int,float等
* 可以将指定数值或字符串转为对应类型的值

---
> print
* 标准输出?
* 默认添加换行符,可指定end参数替换尾字符
```python
# 使用空格代替换行
print("Hello",end=" ")
print("i","like","program")

```

---
> len
* 计算字符串,列表,元组等长度
* 中文等也是按字符个数,而非size(大小)
```python
    Say = "hello words"
    print(Say," lentgh :",len(Say))
    Say = "你好"
    print(Say," Length :",len(Say)) #--->  2

```

---
> eval
* 求值,计算字符串的值
* 字符串可以是表达式
* 可以使用存在的变量和函数,似乎一定程度上可以执行 python 语句?
```python
def getNum():
    return 10

n = eval("3+5*2 + getNum()")

for i in range(n):
    print(i)

```

---
> str
* 返回可打印的字符串表示
```python
TupleTest = ("Name","Age")
strTuple = str(TupleTest)

DictionariesTest = {"Name":"Kin","Age":31}
strDic = str(DictionariesTest)



```

---
> max,min
* 计算Tuple中最大值最小值
```python
Numbers = ("3","53","21")
print(max(Numbers)) #--> 53
print(min(Numbers)) #--> 21  这里是字符串比较

```

---
> abs
* 求绝对值

---
> round 
* 将float四舍五入转换为int
* 第二个参数则转为float,指定小数点后位数
* 第二个参数为负数,则指定小数点前几位
```python
intNumber = round(3.14)

floatNumber = round(3.1415,3) #---> 3.142

```

# 模块
> keyword

```python
#关键字相关库
import keyword

#关键字列表
print(keyword.kwlist)

```

# 模块
## collections
> 队列 deque


---
## math

Python |数学 |描述
---|---|--- 
pi| π| π 的近似值 
e |e |e 的近似值 
sqrt(x)|根号x| x 的平方根
sin(x) |sinx| x 的正弦 
cos(x)| cosx| x 的余弦 
tan(x)| tanx| x 的正切 
asin(x)| arcsinx| x 的反正弦 
acos(x)| arcosx| x 的反余弦 
atan(x)| arctanx| x 的反正切 
log(x)| lnx| x 的自然对数（以 e 为底） 
log10(x)| Log<sub>10</sub> x| x 的常用对数（以 10 为底）
exp(x)| e<sup>x</sup>| e 的 x 次方 
ceil(x)| [x]| 最小的>=x 的整数
floor(x)| [x]| 最大的<=x 的整数 