# n1 = input('输入一个值1:')
# print(n1, type(n1))

# # n1 = int(n1)
# n1 = float(n1)
# print(n1, type(n1))


# n2 = input('输入一个值2:')
# print(n2, type(n2))


# n2 = eval(n2)
# print('转换2', n2, type(n2))


# 模拟计算机计算
# while 2 > 1:
#     e = input('输入一个表到式：')

#     s = eval(e)

#     print('结果是:', s)


# # 求累加和
# s = 0
# i = 1
# # while循环 条件成立开始循环
# while i <= 100:
#     # 累加
#     s = s + i
#     # 格式化字符串
#     print(f'1--{i}的累加和是:{s}')
#     # 变量自增
#     i = i + 1

# range(num)
# 获得一个从0开始，到num结束的数字序列(不含num本身)
# 例如range(5),获得的数据是[0,1,2,3,4]

# range(num1, num2)
# 获取一个从num1开始，到num2结束的数字序列(不含num2本身)
# 例如range(2,8)，获得的数据是[2,3,4,5,6,7]

# range(num1, num2, step)
# 获取一个从num1开始，到num2结束的数字序列(不含num2本身)
# step 为步长，默认为1
# 例如range(1,10,2)，获取到的数据是[1,3,5,7,9]

num1 = 10
num2 = 0
# range(num1, num2, -1)
# 从10到1,依次打印,（不含num2本身）
# range(10,0,-1),获取到的数据是[10,9,8,7,6,5,4,3,2,1]


# for i in range(10):
#     print('1--->', i)

# for i in range(2, 10):
#     print('2--->', i)

# for i in range(2, 10, 2):
#     print('3--->', i)

# for i in range(10, 0, -1):
#     print('4--->', i)

# for i in range(10, 0, -2):
#     print('5--->', i)

# s = 0
# # for 循环
# for j in range(1, 101):
#     # 累加
#     s = s + j
#     print(f'1--{j}的累加和是:{s}')


s = 0
while True:
    n1 = input('输入一个初始值')
    n2 = input('输入一个结束值')
    n3 = input('输入间隔值')
    # for 循环
    for j in range(eval(n1), eval(n2), eval(n3)):
        # 累加
        s = s + j
        print(f'1--{j}的累加和是:{s}')
