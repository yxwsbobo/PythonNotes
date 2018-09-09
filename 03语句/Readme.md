# 运算符
* 使用除法运算符 / 获得实数
* 使用除法运算符 // 获得整数
* 使用方乘运算符 ** 计算次方 *2 ** 10 == 1024*
* 使用 * 进行重复字符串  "i love programing" * 3

---
> 逻辑运算符
* and 
* or
* not
```python
#and,or与普通逻辑运算符少有不同的是,结果并非True or False,虽然可以这样使用,但实际返回是用实际值代替的

Num1 = 10
Num2 = 0
Num3 = 20

value = Num1 and Num2 #value == 0
value = Num1 and num3 #value == 20,而非True

value = Num2 or Num1 #value == 10,并非True
value = Num1 or Num3 #value == 10,注意并非20

```

---
> 测试成员存在运算符
* in
* not in
```
用于判断某元素是否在序列中
返回 True 或 False
```

> 测试是否为引用同一对象
* is
* is not
```
与值比较区别
is/is not  用于比较是否引用同一对象
使用id(value) 进行比较
```

