



# 1.基础语法

## 1.输出print（"a"）

str函数，将整形的数字变成字符串 指str(95)--'95'

input的东西都是字符串，如果想把他当成整数值来用，就要用int函数进行显式转化

## 2.注释

单⾏： # 注释内容 ，快捷键ctrl+/

多⾏： """ 注释内容 """ 或 ''' 注释内容 

## 3.设置变量

变量名=值，最好每个单词的首字母都大写

 

## 4.数据类型

数据类型

整型：int

浮点型：flfloat

字符串：str

布尔型：bool

元组：tuple

集合：set

字典：dict

显示转换 int(a)

## 5.输出

格式化符号

%s：格式化输出字符串

%d：格式化输出整数

%f：格式化输出浮点数

f-字符串

f'{表达式}'

转义字符

\n：换⾏

\t：制表符

## 6.输出

输⼊功能

input('提示⽂字')

输⼊的特点

⼀般将input接收的数据存储到变量

input接收的任何数据默认都是字符串数据类型

## 7.转换数据类型

**函数** 

**说明**

int(x [,base ]) 

将x转换为⼀个整数

flfloat(x ) 

将x转换为⼀个浮点数

complex(real [,imag ]) 

创建⼀个复数，real为实部，imag为虚部

str(x ) 

将对象 x 转换为字符串

repr(x ) 

将对象 x 转换为表达式字符串

eval(str ) 

⽤来计算在字符串中的有效Python表达式,并返回⼀个对象

tuple(s ) 

将序列 s 转换为⼀个元组

list(s ) 

将序列 s 转换为⼀个列表

chr(x ) 

将⼀个整数转换为⼀个Unicode字符

ord(x ) 

将⼀个字符转换为它的ASCII整数值

hex(x ) 

将⼀个整数转换为⼀个⼗六进制字符串

oct(x ) 

将⼀个整数转换为⼀个⼋进制字符串

bin(x ) 

将⼀个整数转换为⼀个⼆进制字符串



转换数据类型常⽤的函数

\# 1. 接收⽤户输⼊

num = input('请输⼊您的幸运数字：')

\# 2. 打印结果

print(f"您的幸运数字是{num}")

\# 3. 检测接收到的⽤户输⼊的数据类型 -- str类型

print(type(num))

\# 4. 转换数据类型为整型 -- int类型

print(type(int(num)))

1

2

3

4

5

6

7

8

9

10

11

12

\# 1. float() -- 转换成浮点型

num1 = 1

print(float(num1))

print(type(float(num1)))

\# 2. str() -- 转换成字符串类型

num2 = 10

print(type(str(num2)))

\# 3. tuple() -- 将⼀个序列转换成元组

list1 = [10, 20, 30]

print(tuple(list1))

print(type(tuple(list1)))

\# 4. list() -- 将⼀个序列转换成列表

t1 = (100, 200, 300)

print(list(t1))

print(type(list(t1)))

\# 5. eval() -- 将字符串中的数据转换成Python表达式原本类型

str1 = '10'

str2 = '[1, 2, 3]'

str3 = '(1000, 2000, 3000)'

print(type(eval(str1)))

print(type(eval(str2)))

print(type(eval(str3)))

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27int()

flfloat()

str()

list()

tuple()

eval()

## 8.运算符

/ 

除 

10 / 2 输出结果为 5

// 

整除 

9 // 4 输出结果为2 

% 

取余 

9 % 4 输出结果为 1

** 

指数 

2 ** 4 输出结果为 16，即 2 * 2 * 2 * 2

() 

⼩括号 

⼩括号⽤来提⾼运算优先级，即 (1 + 2) * 3 输出结果为 9



and

x and

y

布尔"与"：如果 x 为 False，x and y 返回

False，否则它返回 y 的值。

True and False， 返回

False。

or 

x or y

布尔"或"：如果 x 是 True，它返回 True，否则

它返回 y 的值。

False or True， 返回

True。

not 

not x

布尔"⾮"：如果 x 为 True，返回 False 。如果 x

为 False，它返回 True。

not True 返回 False, not

False 返回 True

算数运算的优先级

混合运算优先级顺序： () ⾼于 ** ⾼于 * / // % ⾼于 + -

赋值运算符

=

复合赋值运算符

+=

-=

优先级

\1. 先算复合赋值运算符右侧的表达式

\2. 再算复合赋值运算的算数运算

\3. 最后算赋值运算

⽐较运算符

判断相等： ==

⼤于等于： >=

⼩于等于：<=

不等于： !=

逻辑运算符

与： and

或：or

⾮：not

## 9.条件判断

### 1.格式

if 条件1:

 条件1成⽴执⾏的代码1

 条件1成⽴执⾏的代码2

 ......

elif 条件2：

 条件2成⽴执⾏的代码1

 条件2成⽴执⾏的代码2

 ......

......

else:

 以上条件都不成⽴执⾏执⾏的代码

if语句语法

if...else...

多重判断

if嵌套

三⽬运算符

条件成⽴执⾏的表达式 if 条件 else 条件不成⽴执⾏的表达式 

1 

a = 1 

b = 2 

c = a if a > b else b

print(c) 

1

2

3

4

5

if 条件:

 条件成⽴执⾏的代码

1

2

if 条件:

 条件成⽴执⾏的代码

else:

 条件不成⽴执⾏的代码

1

2



if 条件1:

 条件1成⽴执⾏的代码

elif 条件2:

 条件2成⽴执⾏的代码

else:

 以上条件都不成⽴执⾏的代码

1



if 条件1:

 条件1成⽴执⾏的代码

 if 条件2:

 条件2成⽴执⾏的代码

成⽴执⾏的表达式 if 条件 else 条件不成⽴执⾏的表达式 



总结：python语言中没有了switch，使用

if 条件1：

elif 条件2:

elif 条件3:
else ：



要判断特定的值是否已包含在列表中，可使用关键字in。来看你可能为比萨店编写的一些代

码；这些代码首先创建一个列表，其中包含用户点的比萨配料，然后检查特定的配料是否包含在5.2 条件测试 69 



该列表中。

\>>> requested_toppings = ['mushrooms', 'onions', 'pineapple'] 

 >>> **'mushrooms' in requested_toppings** 

True 

 >>> **'pepperoni' in requested_toppings** 

False 

### 2.学会要先判断列表是否为空

在if语句中将列表名用在条件表达式中时，Python将在列表

至少包含一个元素时返回True，并在列表为空时返回False。

## 10.循环语句

while j <= 4:

 \# ⼀⾏星星的打印

 i = 0

 while i <= 4:

 \# ⼀⾏内的星星不能换⾏，取消print默认结束符\n

 print('*', end='')

 i += 1

 \# 每⾏结束要换⾏，这⾥借助⼀个空的print，利⽤print默认结束符换⾏

 print()

 j += 1 

循环的作⽤：控制代码重复执⾏

while语法

while循环嵌套语法

for循环语法

for 参数 in range（启示，结束，步长）

就是不需要手动控制i的++的东西，是一个辅助性的东西，并不复杂

break退出整个循环

continue退出本次循环，继续执⾏下⼀次重复执⾏的代码

else

while和for都可以配合else使⽤

else下⽅缩进的代码含义：当循环正常结束后执⾏的代码

break终⽌循环不会执⾏else下⽅缩进的代码

continue退出循环的⽅式执⾏else下⽅缩进的代码

## 11.python语言风格

![image-20220823204214402](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220823204214402.png)

## 12.定义函数

语法：def 函数名 （参数）

其他的基本都一样，可以设定初始值，可以将函数作为参数

不需要写明变量类型

## 13.异常

![image-20220830140645619](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830140645619.png)



## 14.序列



![image-20220830153926778](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830153926778.png)

1.str  字符串 使用单引号括住

2.list 列表，使用中括号

3.tuple 元组，使用圆括号

plist 是内容是元组的列表

![image-20220830154150948](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830154150948.png)

分别进行介绍：

标准运算类型

![image-20220830155016229](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830155016229.png)

![image-20220830155221695](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830155221695.png)

[1]就是第一个，最后一个是-1，可以从后往前进行考虑， [1：4]是从1 到4的东西，之后的可以见输入和输出得出结论

特殊的 in 查询序列里有没有这个东西

![](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830155700546.png)

## 15.列表

![image-20220830155935141](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830155935141.png)

本质：可扩展的容器对象，可以针对某个组成元素进行更改。可以包含不同的类型对象

![image-20220830160258843](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830160258843.png)

sort——从高到低排序 pop——弹出最后一个对象，加一个0，就是弹出第一个对象

append——加上一个对象

![image-20220830160521325](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830160521325.png)

创建列表的方便方式

![image-20220830162910790](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830162910790.png)

![image-20220830163253945](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830163253945.png)

仔细思考该例子！



下面将详细学习列表：

访问列表的方式就和数组一样

2.当修改列表时，就是指定对其某个成员进行修改

append（）——在末尾添加元素

insert()—— 在指定位置插入元素，第一个参数需要输入位置

del 数组名 [第几个] 删除元素——访问方法依然像数组

pop（第几个）——在删除一个元素的同时保存被删除元素的信息，以在接下来继续利用



sort()——永久性排序

sorted()——暂时性排序

reverse（）——反转列表排序 

len（）——得出列表的长度



别忘了，每当需要访问最后一个列表元素时，都可使用索引-1。这在任何情况下都行之有效，

即便你最后一次访问列表后，其长度发生了变化：

motorcycles = ['honda', 'yamaha', 'suzuki'] 

print(motorcycles[-1]) 

———————————————— 防止数组越界的好方法



### 2.操作列表

1.使用for循环    

for a in as

a就会从0开始一直向后增加

### 3.使用range（）函数

range（起，终）会生成一串由起到终的数字序列，但不包含终

使用list（range（1,5）），这就将数字序列转换成了列表

### 4.使用统计函数

\>>> **digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]**

\>>> **min(digits)**

0 

\>>> **max(digits)**

9 

\>>> **sum(digits)**

45 

### 5.列表解析

前面介绍的生成列表squares的方式包含三四行代码，而列表解析让你只需编写一行代码就

能生成这样的列表。列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素。

面向初学者的书籍并非都会介绍列表解析，这里之所以介绍列表解析，是因为等你开始阅读他人

编写的代码时，很可能会遇到它们。

下面的示例使用列表解析创建你在前面看到的平方数列表：

squares.py 

squares = [value**2 for value in range(1,11)] 

print(squares) 

### 6.切片

在很多情况下，切片都很有用。例如，编写游戏时，你可以在玩家退出游戏时将其最终得分

加入到一个列表中。然后，为获取该玩家的三个最高得分，你可以将该列表按降序排列，再创建

一个只包含前三个得分的切片。处理数据时，可使用切片来进行批量处理；编写Web应用程序时，

可使用切片来分页显示信息，并在每页显示数量合适的信息。

就是列表中括号里的用冒号隔开的各种东西

你经常需要根据既有列表创建全新的列表。下面来介绍复制列表的工作原理，以及复制列表

可提供极大帮助的一种情形。

要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）。

这让Python创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个列表。

例如，假设有一个列表，其中包含你最喜欢的四种食品，而你还想创建另一个列表，在其中

包含一位朋友喜欢的所有食品。不过，你喜欢的食品，这位朋友都喜欢，因此你可以通过复制来

创建这个列表：

在复制列表的时候，如果不使用切片，就会变成两个列表使用同一个储存空间，只是一个别名罢了



## 16.元组

列表可以变，元组不能变。

![image-20220830165152656](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830165152656.png)

1.可变长的参数

![image-20220830165343187](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830165343187.png)

可以输入任意个东西

2.函数返回值

![image-20220830165425793](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830165425793.png)

### 1.元组不能变，列表可以变

元组内的数值不能改变，但可以重新定义元组，也就是元组并不是定义以后就完全无法改变的

## 17.字符串

1.有趣的函数

upper（）——全部变为大写

lower（）——全部变为小写

title（）——首字母大写

2.单引号，双引号都可以

3.使用+来拼接字符串，都是字符串

4.\t 制表符 \n 换行符，这里和c++是一样的

5.删除空白 \>>> **favorite_language = favorite_language.rstrip()**

\>>> **favorite_language**

 \>>> **favorite_language = ' python '**

 >>> **favorite_language.rstrip()**

' python' 

 >>> **favorite_language.lstrip()**

'python ' 

 >>> **favorite_language.strip()** 

'python' 

在这个示例中，我们首先创建了一个开头和末尾都有空白的字符串（见）。接下来，我们

分别删除末尾（见）、开头（见）和两端（见）的空格。尝试使用这些剥除函数有助于你

熟悉字符串操作。在实际程序中，这些剥除函数最常用于在存储用户输入前对其进行清理。

6.为了避免撇号的问题，建议给字符串都是用双引号

## 18.字典

### 1.定义：使用大括号{

alien.py 

alien_0 = {'color': 'green', 'points': 5} 

print(alien_0['color']) 

print(alien_0['points']) 

字典alien_0存储了外星人的颜色和点数。使用两条print语句来访问并打印这些信息，如

下所示：

green 

5 



是一系列键—值对 搞一个键，后面再搞一个值为这个键赋值

#### 1.访问字典中的值：

使用字典名，再用中括号扩起来的键值：字典名[键]

访问字典中的值

要获取与键相关联的值，可依次指定字典名和放在方括号内的键，如下所示：

alien_0 = {'color': 'green'} 

print(alien_0['color']) 

这将返回字典alien_0中与键'color'相关联的值：

green 

#### 2.添加 键-值对

因此要将该外星人放在屏幕左边缘，可将*x*坐标设置为0；要将该外

星人放在离屏幕顶部25像素的地方，可将*y*坐标设置为25，如下所示：

alien_0 = {'color': 'green', 'points': 5} 

print(alien_0) 

 alien_0['x_position'] = 0 

 alien_0['y_position'] = 25 

print(alien_0) 

使用字典来存储用户提供的数据或在编写能自动生成大量键—值对的代码时，通常都需要先

定义一个空字典

#### 3.修改键对应的值：直接修改即可

修改字典中的值

要修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关联的新值。例如，

假设随着游戏的进行，需要将一个外星人从绿色改为黄色：

alien_0 = {'color': 'green'} 

print("The alien is " + alien_0['color'] + ".") 

alien_0['color'] = 'yellow' 

print("The alien is now " + alien_0['color'] + ".") 

#### 4.删除 键-值对

例如，下面的代码从字典alien_0中删除键'points'及其值：

alien_0 = {'color': 'green', 'points': 5} 

print(alien_0) 

 del alien_0['points'] 

print(alien_0) 

### 2.遍历字典

#### 1.如所示，要编写用于遍历字典的for循环，可声明两个变量，用于存储键—值对中的键和值。

对于这两个变量，可使用任何名称。下面的代码使用了简单的变量名，这完全可行：

for k, v in user_.items()

记得要加后面的items

#### 2.遍历字典里的所有键

for name in favorite_languages.keys(): 

 print(name.title()) 

#### 3.遍历字典里的所有值

如果你感兴趣的主要是字典包含的值，可使用方法values()，它返回一个值列表，而不包含

任何键。例如，如果我们想获得一个这样的列表，即其中只包含被调查者选择的各种语言，而不

包含被调查者的名字，可以这样做：

favorite_languages = { 

 'jen': 'python', 

 'sarah': 'c', 

 'edward': 'ruby', 

 'phil': 'python', 92 第 6 章 字典

 } 

print("The following languages have been mentioned:") 

for language in favorite_languages.values(): 

 print(language.title()) 

### 3.嵌套

#### 1.将字典存储在列表里

字典alien_0包含一个外星人的各种信息，但无法存储第二个外星人的信息，更别说屏幕上

全部外星人的信息了。如何管理成群结队的外星人呢？一种办法是创建一个外星人列表，其中每

个外星人都是一个字典，包含有关该外星人的各种信息。例如，下面的代码创建一个包含三个外

星人的列表：

aliens.py 

alien_0 = {'color': 'green', 'points': 5} 

alien_1 = {'color': 'yellow', 'points': 10} 

alien_2 = {'color': 'red', 'points': 15} 

 aliens = [alien_0, alien_1, alien_2] 

for alien in aliens: 

 print(alien) 

我们首先创建了三个字典，其中每个字典都表示一个外星人。在处，我们将这些字典都放

到一个名为aliens的列表中。最后，我们遍历这个列表，并将每个外星人都打印出来：

#### 2.将列表储存在字典里，可以包含多个信息

 pizza = { 

 'crust': 'thick', 

 'toppings': ['mushrooms', 'extra cheese'], 



具体信息处理

 for name, languages in favorite_languages.items(): 

   print("\n" + name.title() + "'s favorite languages are:") 

   for language in languages: #这里拔下来列表和值

​       print("\t" + language.title()) 这里把列表也变成值

#### 3.将字典储存在字典里

会变得复杂起来

#### 4.用用户输入来填充字典

7.3.3 使用用户输入来填充字典

可使用while循环提示用户输入任意数量的信息。下面来创建一个调查程序，其中的循环每

次执行时都提示输入被调查者的名字和回答。我们将收集的数据存储在一个字典中，以便将回答

同被调查者关联起来：

mountain_poll.py 

responses = {} 

\# 设置一个标志，指出调查是否继续

polling_active = True 

while polling_active: 

 \# 提示输入被调查者的名字和回答

 name = input("\nWhat is your name? ") 

 response = input("Which mountain would you like to climb someday? ") 

 

 

## 19.input

### 1.有趣的提示方法

prompt = "If you tell us who you are, we can personalize the messages you see." 

prompt += "\nWhat is your first name? " 

name = input(prompt) 

print("\nHello, " + name + "!") 

这个示例演示了一种创建多行字符串的方式。第1行将消息的前半部分存储在变量prompt中；

在第2行中，运算符+=在存储在prompt中的字符串末尾附加一个字符串。

最终的提示横跨两行，并在问号后面包含一个空格，这也是出于清晰考虑：

# 2.爬虫



# ：获得在互联网上上传的一些东西

需求拆解：下载一个视频——在浏览器上按一下F12键——可以看到网页源代码，浏览器也是程序员写代码的软件，所以我可以用python写的代码访问这个程序，也可以得到这个数据

爬虫核心：模拟浏览器访问网址获取数据

## 

## 基础爬虫的工作流程拆解：

1.浏览器的网址，访问网址

2.获取网页源代码，网页真正的样子其实是源代码，浏览器将源代码翻译成为了眼睛所看的网页

3.从源代码中抽取我们想要的数据

4.保存数据

 学编程就像一个填空题——有目标就会更加简单



## 网页数据的如何加载——异步数据加载

点击了下一页，网址没有变，源代码却变了，如果源代码变了，那就拿不到了。就和验证码的逻辑是一样的，网页没有更新，但验证码变了，这是异步加载

针对异步加载怎么办？

按F12——点击网络——点击JS，再刷新一下——找到getmoment——展开——找到definition——url复制，粘贴回车一下就可以了

现在发现只要找到数据，然后从数据中把地址提取出来就可以了，数据不在网页源代码里，所以要再去网络那里找到数据的地址。

一般高级的爬虫，都不会去抽取网页的源代码，一般都是去找**数据接口**

1.通过浏览器的开发者工具（F12），分析得出数据接口地址

2.访问数据接口地址，获取数据内容

3.从数据中提取视频链接，视频名称

4.访问视频地址，下载视频



这些都是常规爬虫，都是没有加密的。恶心的数据，把一个打视频切割成很小的数据片段，切割成1000份，就很恶心，下载vip视频很难



1.首先要批量获取到ID号，



## 2.六大点

1.超前的知识体系

——技术栈，把知识体系发过来，技术栈的学习路线

2.丰富的企业级项目实战经验

工作经验 1-3月左右，开始进行兼职接单——基本上学了一个多月左右可以进行初步的接单，都有模板，换图片文字就更简单了

​     1. 面对不同客户 需求 ——项目有不同的场景，可以积累项目实战经验，来提升自己对于技术的认知

​     2.能够将技术落地（驱动力，成就感）

​     3.额外的收入

3.有自己的丰富的技术积淀

4.有算法或者竞赛经历

5.正向的思维方式

6.有开源社区活跃经验

 被卡学历——放大自己的价值，参加线下的技术交流大会

解决就业和内推，视野要和其他人不一样，预知上山路，须问过来人



# 3.数据分析

## 1.什么是数据分析？

1.numpy    基础数值算法

2.scipy 科学计算

3.matplotlib 数据可视化

4.pandas 序列高级函数 



向量就是一组数据，那些字典什么的都是一组数据



1.numpy![image-20220822181724494](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220822181724494.png)



![image-20220822182023940](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220822182023940.png)



![image-20220822182249677](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220822182249677.png)

![image-20220822200229458](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220822200229458.png)

是可以进行数值运算的



![image-20220822205214640](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220822205214640.png)



可以直接对其中的某些性质进行修改



![image-20220822205433631](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220822205433631.png)



![image-20220822205530658](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220822205530658.png)

构建数组的方式，共上述四种

进行测试

![image-20220822210614143](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220822210614143.png)



具体操作

![image-20220822211203690](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220822211203690.png)

![image-20220822211904314](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220822211904314.png)



## 2.读取本地文件



 open（文件名，模式，是否缓冲）

![image-20220828175041700](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220828175041700.png)

建议使用with ，可以实现异常处理

![image-20220828175425700](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220828175425700.png)

![image-20220828175714618](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220828175714618.png)

![image-20220830142255232](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830142255232.png)

这里涉及到一个文件指针的问题，下面的写入之后指针就指向了文章的最后，所有需要再来一个seek函数来把指针变回开头



![image-20220830142922730](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830142922730.png)

## 3.读取网络文件（爬虫）

1.基本原理与常用工具

![image-20220830143419232](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830143419232.png)

大型开发使用scrapy框架 解析用beautifulsoup库 ，

先以request第三方库为例

![image-20220830143945636](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830143945636.png)

按照这个流程就可以爬下来信息了



解析爬虫下来的信息

![image-20220830144413635](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830144413635.png)

左侧是相对简单的数据结构，使用Beautiful soup更好 ，右侧是re正则表达式 ，是用来处理下侧更复杂的数据结构的

一般使用lxml解析器



小王子案例完整操作![image-20220830145330220](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830145330220.png)

这里的评论是span类型 属性是short

![image-20220830150550134](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830150550134.png)

网页内容的解析



正则表达式简介：

+，用来匹配重复前面的字符 

![image-20220830150920204](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830150920204.png)





![image-20220830151400910](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830151400910.png)

这是一个个对应的关系，这里的括号分组以后变成实现三组这样的内容





![image-20220830151931002](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220830151931002.png)

正则表达式的取方式，把需要的地位加上（.*?）就好了



# 2.刷书——交通大数据分析

## 1.python基础

### 1.集合

#### 1.定义

定义一个集合，需要提供一个列表 

a=set([1,2,2,4])——内容即键不能重复，若print(a)，则输出了{1,2,4}

#### 2.元素的增删

a.add(3)——输出为{1,2,3,4}

a.remove(3)——输出位{1,2,4}

#### 3.集合的运算

s=set({1,2,3})

p=set({3,4,5})

s&p——交集 

s|p——并集

s-p=s-(s&p)

### 2.函数

