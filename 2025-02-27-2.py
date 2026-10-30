# while循环

# i = 1
# while i <= 5:
#     print(i, '*'*i)
#     i += 1  # i = i + 1


# # for 循环
# for j in range(1, 6):
#     print(j, '*'*j)


# chr
# while 循环
i = 65
j = 1
while i <= 90:
    print(chr(i)*j)
    i += 1
    j += 1

# while 循环
i = 90
j = 1
while i >= 65:
    print(chr(i)*j)
    i -= 1
    j += 1

# # for 循环
# j = 1
# for i in range(65, 91):
#     print(chr(i)*j)
#     j += 1

j = 1
for i in range(90, 64, -1):
    print(chr(i)*j)
    j += 1
