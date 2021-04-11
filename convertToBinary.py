def toBinary(num):
    # idea: keep getting the coefficient of the index power and keep track of order with stack
    s = []
    while num > 0:
        bit = num % 2
        s.append(bit)
        num >>= 1

    return s[::-1]

num = 17 # 10001
result = toBinary(num)
print(result)

num = 45 # 101101
result = toBinary(num)
print(result)

num = 13 # 1101
result = toBinary(num)
print(result)


