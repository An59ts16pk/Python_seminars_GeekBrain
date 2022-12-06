# Задача 2.	Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# ===========================================================
import math

num = int(input("Введите натуральное число: "))

def prime_factors(num):
    pr_list = []
    while num % 2 == 0: 
        pr_list.append(2)
        num = num / 2 
    for i in range(3, int(math.sqrt(num)) + 1, 2): 
        while num % i == 0: 
            pr_list.append(i)
            num = num / i 
    if num > 2: 
        pr_list.append(round(num))
    
    return pr_list
 
print(prime_factors(num)) 
