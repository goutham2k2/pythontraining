
print("hi this is python")
# fruits = ["apple", "banana", "cherry"]
#
# for fruit in fruits:
#     print(fruit)
# for i in range(5):
#     print(i)
from itertools import count
from os import remove

# count = 1
# while count<=5:
#     print(count)
#     count +=1
# for i in range(5):
#     if i == 3:
#         pass
#     print(i)

# total = 0
#
# for i in range(1,101):
#     total += i
# print(total)

# attempts = 0
# password = "goutham"
#
# while attempts < 3:
#     entered = input()
#     if entered == password:
#         print("Access granted")
#         break
#     else:
#         print("Wrong password")
#         attempts +=1
# for letter in "hello":
#     print(letter)

# for i in range(3):
#     for j in range(3):
#         print(f"i={i}, j={j}")

# number = [10,20,30,40,50]
# print(number[0])
# number.append(50) #add element
# number[1] = 25 # update element
#
# print(number)

# import array
#
# arr = array.array('i',[1,2,3,4,5])
# print(arr[2])
# arr.append(6)
# arr.append(3)
#
# print(arr)

# n = int(input())
# arr = []
#
# for i in range(n):
#     num = int(input(f"enter element {i+1}: "))
#     arr.append(num)
#
# print(arr)
#
# d = {110:"abc", 101:"xyz", 105:"bcd"}
# print(d)
# d = {}
# d["laptop"] = 40000
# d["mobile"] = 15000
# d["earphone"] = 1000
# print(d)

# num = int(input())
# if num % 2 == 0:
#     print("it is a even number")
# else:
#     print("it is a odd number ")
# age = 17
#
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")

# text = ""
#
# is_empty = not bool(text)
# print(is_empty)
# username = "admin"
# password = "12345"
#
# input_username = input("Enter username: ")
# input_password = input("Enter password: ")
#
# is_authenticated = (input_username == username and input_password == password)
#
# if is_authenticated:
#     print("Login successful")
# else:
#     print("Login failed")

# stock = 10
# order_quantity = 15
#
# is_available = order_quantity <= stock
#
# if is_available:
#     print("Order can be fulfilled")
# else:
#     print("Insufficient stock")

# email = "goutham@gmail.com"
#
# is_valid_email = "@" in email and "." in email
#
# print("Valid email?" , is_valid_email)

# traffic_light = input()

# if traffic_light == "green":
#     print("you can go")
# elif traffic_light = "yellopw"
#     print("start your car")
# elif
# else:
#     print("stop")
# payment_received = input()
#
# if payment_received:
#     print("Order confirmed")
# else:
#     print("Awaiting payment")


# l = [10,20,30,40,50]
# # [0,1,2,3,4]
# # [-5,-4,-3,-2,-1]
# print(l[::-3])
# numbers = [10, 20, 30, 40]
# total = sum(numbers)
# print("Sum:", total)

# s = {10,10,20,20,30,40,87,89}
# l = list(s)
#
# print(l[0])
# unorder
# not access to slicing
# unique numbers
# duplicates not allowed
# s = {1,20,30,40}
# d = {"key":2,"key2":3}
# print(type(d))
# print(d)
# list
# set
# tuples
# dict
# items = ['pen', 'pencil', 'eraser']
# if 'pencil' in items:
#     print("Found pencil")
# else:
#     print("Pencil not found")
# colors = ['red', 'blue', 'red', 'green', 'red']
# print("Red count:", colors.count('red'))
l = [10,20,30,40,50]
# l.append(60)
# print(l)
# # l.insert(indexNumber,number)
# l.insert(1,80)
# print(l)
# l.remove(80)
# print(l)
# del l[0:2]
# print(l)
# del l[1:3]
# print(l)
# del l[1]
# print(l)
# l.sort()
# print(l)
# l.pop()
# print(l)
# append
# sorted()
# sort
# remove()
# del
# in
# reverse
# pop()
# count
# print(l.index(30))
# lambda arguments:expressions;
n = int(input())
square = [print(i*i) for i in range(0,n)]

