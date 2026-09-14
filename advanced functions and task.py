# advanced functions
# lambda function:
# syntax
# lambda arguments:expression
# values=lambda a,b:a*b
# result=values(10,10)
# print(result)

# another example
# numbers=lambda x,y:x+y
# result=numbers(100,43)
# print(result)

# filter function
# syntax
# filter(function , iterable )
# empty_list=[]
# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     if i%2 == 0:
#         empty_list.append(i)
# print(empty_list)

# using method
# Define a function to check if a number is even
# def is_even(x):
#     return x % 2 == 0
# numbers=[1,2,3,4,5,6,7,8,9,10]
# result=filter(is_even,numbers)
# print(list(result))

# another method
# numbers=[1,2,3,4,5,6,7,8,9,10]
# result=filter(lambda a:a%2==0 , numbers)
# print(list(result))

# map function
# syntax
# map(function,iterable.....)
numbers=[1,2,3,4,5,6,7,8,9,10]
numbers=[1,2,3,4,5,6,7,8,9,10]
result=map(lambda a,b:a+b,numbers,numbers)
print(list(result))

# example
numbers=[1,2,3,4,5,6,7,8,9,10]
def even(x):
    return x**2
result=map(even,numbers)
print(list(result))

# another example
numbers=[1,2,3,4,5,6,7,8,9,10]
result=map(lambda a:a**2,numbers)
print(list(result))

# reduce function
# syntax
# reduce(function,iterable[intializer])   #intializer optional
from functools import reduce
def add(a,b):
    return a+b
numbers=[1,2,3,4,5,6,7,8,9,10]
result=reduce(add,numbers)
print(result)

# another example
from functools import reduce
numbers=[1,2,3,4,5,6,7,8,9,10]
result=reduce(add,numbers)
print(result)

# generator function
def add():
    yield 1
    yield 2
    yield 3*4
    yield 150-7
    yield 100000*23
# creating object
x=add()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())


# advanced functions task
# Write a Python function 
# square_all(numbers) that takes a list of numbers as input 
# and returns a new list containing the square of each number in the input list. 
# Use the 
# map() function with a lambda function to implement this.
list_1=[1,2,3,4,5,6,7,8,9,10]
def square_all(numbers):
    return numbers**2
result=map(lambda a:a**2,list_1 )
print(list(result))

#Write a Python function 
# filter_positive(numbers) that takes a list of numbers as 
# input and returns a new list containing only the positive numbers from the 
# input list. Use the 
# filter() function with a lambda function to implement this.
list_2=[1,2,-33,4,-5,6,-25,600,200,-44,14,-15,20,22,100]
def filter_positive(numbers):
    return numbers
result=filter(lambda a:a>0,list_2)
print(list(result))

# Write a Python function 
# calculate_factorial(n) that calculates the factorial of a 
# given number n. Use the 
# reduce() function with an appropriate lambda 
# function to implement this.
from functools import reduce
def calculate_factorial(n):
    return reduce(lambda a,b:a*b, range(1,n+1),1)
n=5
print(calculate_factorial(n))

# Write a Python function 
# count_vowels(string) that takes a string as input and 
# returns the count of vowels (a, e, i, o, u) in the input string. Use the 
# reduce() 
# function with an appropriate lambda function to implement this.
from functools import reduce

def count_vowels(string):
    return reduce(lambda count, char: count + 1 if char.lower() in "aeiou" else count, string, 0)

string = "amarnath"

print(count_vowels(string))