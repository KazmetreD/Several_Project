# -*- coding: utf-8 -*-

divisibility = 0
number = int(input("Enter a number: "))
for numbers in range(2,number):
    result = number % numbers
    if result == 0:
        print(number,"can be divided into",numbers)
        divisibility += 1
if divisibility == 0:
    print(number,"is a prime number")
elif divisibility > 0:
    print(number,"is not a prime number.")