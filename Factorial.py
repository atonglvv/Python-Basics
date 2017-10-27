# Factorial.py
sum,tem = 0,1
for i in range(1,11):
    tem *= i
    sum += tem
print("运算结果是：{}".format(sum))