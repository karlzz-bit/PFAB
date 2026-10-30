

# for...in...循环

> **Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。**
>
> for-in遍历的对象必须是**可迭代**对象
>
> while循环的循环条件是自定义的，for循环无法定义循环条件
>
> for循环是一种**“轮询”**机制。是对一批内容进行**“逐个处理”**

![](.\image\for循环流程.png)

## python-for循环语句

~~~python
for 临时变量 in 待处理数据集:
	重复执行代码
~~~

> 理论上来讲，for循环无法构建无限循环(待处理的数据集不可能无限大)

**实例**

~~~python
# 遍历字符串
for i in 'Python':     # 第一个实例
    print("当前字母: %s" % i)
    print('*-*'*10)
    print('2->当前字母:{}'.format(i))
    print('*-*'*10)
    print(f'3->当前字母{i}')
    print('over!!!\n')
    
lista = list('python')
print(f'lista = {lista}')
for i in lista:     # 第一个实例
    print("当前字母: %s" % i)
    print('*-*'*10)
    print('2->当前字母:{}'.format(i))
    print('*-*'*10)
    print(f'3->当前字母{i}')
    print('over!!!\n')    
~~~

> 可以看出for循环是将字符串的内容**依次取出**，所以for循环也被称之为**遍历循环**



**练习**

```python
# 单行单个输出26个大写字母
import string
l = string.ascii_uppercase
print(l)

# for循环遍历
for i in l:
    print(i)

print(list(l))

for i in list(l):
    print(i)

j = 65
while j <= 90:
    print(f'{j-64}个字母是:{chr(j)}')
    j += 1
```



~~~python
# 字符串 name = "hello world python i love you"
# 通过for循环遍历所有的o
name = "hello world python i love you"
for i in name:
    if i == "o":
        print(i)
        
~~~

------

# range()语句

> for循环本质上是遍历**“序列类型”**，但是，使用**range**语句，可以获得一个简单的**数字序列**

**语法：**

~~~python
range(num)
# 获得一个从0开始，到num结束的数字序列(不含num本身)
# 例如range(5),获得的数据是[0,1,2,3,4]

range(num1,num2)
# 获取一个从num1开始，到num2结束的数字序列(不含num2本身)
# 例如range(2,8)，获得的数据是[2,3,4,5,6,7]
 
range(num1,num2,step)
# 获取一个从num1开始，到num2结束的数字序列(不含num2本身)
# step 为步长，默认为1
# 例如range(1,10,2)，获取到的数据是[1,3,5,7,9]

num1 = 10
num2 = 0
range(num1,num2,-1)
# 从10到1,依次打印,（不含num2本身）
# range(10,0,-1),获取到的数据是[10,9,8,7,6,5,4,3,2,1]
~~~

## 实例

~~~python
# 输出0~9
for i in range(10):
    print(i)
    
# 输出1~100
for i in range(1,101)

# 输出1~100，每次跳过一个数字
for i in range(1,101,2):
    print(i)
~~~

```python
# 输出1,2,...,20
for i in range(1, 21):  # range(1,21,1)
    print(i)

# 输出20,19,...,2,1
for i in range(20, 0, -1):
    print(i)

# 求和100+99+......+2+1
i, s = 100, 0
while i > 0:
    s = s + i
    print(f'累加和是：{s}')
    i -= 1

score = 0
for j in range(100, 0, -1):
    score = score + j
    print(f'2-->累加和是：{score}')

print(f'3--> {sum(range(100,0,-1))}')

# 求和 1+1/2+1/3+......+1/100
# 求和100+99+......+2+1
i, s = 1, 0
while i <= 100:
    s = s + 1/i
    print(f'4-->累加和是：{s}')
    i += 1

score = 0
for j in range(1, 101):
    score = score + 1/j
    print(f'5-->累加和是：{score}')
```

# for循环的嵌套应用

**生活中的嵌套**

> 和女朋友吵架，每天道歉10遍，持续5天

~~~python
#for 临时变量 in 待处理数据集:
    重复执行代码一
    重复执行代码二
    重复执行代码三
	for 临时变量 in 待处理数据集:
        重复执行代码三
        重复执行代码三
        重复执行代码三
~~~





- **坚持道歉5天**
- **每天道歉10遍**

~~~python
for i in range(1,6):
    print(f"这是我第{i}天的道歉")
    for j in range(1,11):
        print(f"老婆，我错了，这是我今天的第{j}次道歉")
    print(f"老婆，第{i}天的道歉结束。。。")

print(f"我已经道歉了{i}天了，老婆不生气了")
~~~

**for循环和while循环配合使用**

~~~python
for i in range(1,6):
    print(f"这是我第{i}天的道歉")
    j = 1
    while j<=10:
        print(f"老婆，我错了，这是我今天的第{j}次道歉")
        j+=1
    print(f"老婆，第{i}天的道歉结束。。。")
~~~

------

# break和continue

while循环和for循环都是重复性的执行特定的操作，在这个过程中，会出现一些其他情况，让我们不得不

- 跳过这次循环，进入下一次循环

- 终止当前循环

  ## continue

> 中断本次循环，进入下一次循环

~~~python
# 碰见7的倍数直接跳过
for i in range(100):	# 遍历出0~99
    if i % 7 == 0:		# 判断i是7的倍数
        continue		# 满足条件直接跳过
    print(i)			# 打印出其余的数字
~~~

## break

> 终止循环，结束当前循环

~~~python
# 当马自达刷完后直接停止，因为后面是劳斯莱斯
li = ["马自达","马自达","马自达","劳斯莱斯","劳斯莱斯","劳斯莱斯","劳斯莱斯"]
for i in li:
    if i == "劳斯莱斯":
        print("碰见劳斯莱斯了")
        break
    print("正在刷马自达。。。")
~~~



------

# 作业

题目：做一个猜字游戏

要求：1、从1-100生成一个随机数

​		   2、总共有5次机会

​		   3、若中途猜对，循环就要终止

​		   4、若猜错，可提示，大了，或者小了

提示：生成了一个56，但是我也输入了一个56，即为过关，循环终止

~~~python
import random
# 此处的number即为1-100的随机数
number = random.randint(1, 100)
print(number)
~~~



‌‌水仙花数（‌Narcissistic number）也被称为自幂数或‌阿姆斯特朗数（Armstrong number），是指一个n位数（n≥3），它的每个位上的数字的n次幂之和等于它本身‌。例如，三位数153是一个水仙花数，因为1^3 + 5^3 + 3^3 = 153。‌12

水仙花数的定义可以扩展到更多位数。例如：

三位的水仙花数有：153、370、371、407。
四位的水仙花数有：1634、8208、9474。

```python
# 百位的数字 bai 1-9
# 十位的数字 shi 0-9
# 个位的数字 ge  0-9
# 三位数 100*bai + 10*shi + ge == bai**3 + shi**3 + ge**3
# 1、 用百位、十位、个位数字表示三位数
for bai in range(1, 10):
    for shi in range(10):
        for ge in range(10):
            if (100*bai + 10*shi + ge) == (bai**3 + shi**3 + ge**3):
                print('1-->水仙花数是: %d' % (100*bai + 10*shi + ge))
                print('2-->水仙花数是{}'.format(bai**3 + shi**3 + ge**3))
                print(f'3-->水仙花数是:{str(bai)+str(shi)+str(ge)}')

# eval 将符合规则的字符串转成数字或者表达式
for bai in range(1, 10):
    for shi in range(10):
        for ge in range(10):
            if (bai**3 + shi**3 + ge**3) == eval(str(bai)+str(shi)+str(ge)):
                print('1-->水仙花数是: %d' % (100*bai + 10*shi + ge))
                print('2-->水仙花数是{}'.format(bai**3 + shi**3 + ge**3))
                print(f'3-->水仙花数是:{str(bai)+str(shi)+str(ge)}')
                
# 将三位数转成字符串 字符串截取                
for i in range(100, 1000):
    # 取百位数字
    bai = eval(str(i)[0])
    # 取十位数字
    shi = eval(str(i)[1])
    # 取个位数字
    ge = eval(str(i)[2])
    if i == bai**3 + shi**3 + ge**3:
        print(f'5--水仙数数:{i}')                
```

输出九九乘法表

```python

# 左上三角形
for i in range(1, 10):  # 控制行数
    for j in range(i, 10):  # 控制列数
        print(f'{i}X{j}={i*j}\t', end='')  # 不换行输出
    print()  # print默认换行

# 左下三角形
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{i}X{j}={i*j}\t', end='')
    print()
```

