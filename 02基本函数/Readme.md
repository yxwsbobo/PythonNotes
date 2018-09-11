# 内置函数
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

# 模块
> keyword

```python
#关键字相关库
import keyword

#关键字列表
print(keyword.kwlist)

```