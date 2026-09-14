# functions                   # class
# syntax
# def functioncall():
def greet(a,b):
    print(a+b)
greet(10,10)

# another example
def multiply(x,y):
    print(x*y)
multiply(19,1)

# return
def add(a,b):
    return a+b        # only time write
print(add(10,10))

# another example
def multiply(x,y):
    return x*y
print(multiply(10,10))


# parameters and arguments
def add(list_1,list_2):  
    print(list_1+list_2)
add(100,43)

# another example
def add(num_1,num_2):
    print(num_1+num_2)
num_1=int(input("enter the number one:"))
num_2=int(input("enter the number two:"))
add(num_1,num_2)


# another example
def multiply(list_1,list_2):
    print(list_1*list_2)
list_1=int(input("enter the list:"))
list_2=int(input("enter the list2:"))
multiply(list_1,list_2)

# arbitary arguments
def sample(*x):
    print(x)
print(sample(10,1.0,"amarnath",True,"sairam"))

# keyword arguments
def sample(**x):
    print(x)
sample(a="amarnath",b="sairam")

# anoter example
def sample_1(**y):
    print(y)
sample_1(a="1",s="19")

# default parameters
def details(name=None,age=None,department=None,id_card=None):
    print(name,age,department,id_card)
details("amarnath",19,"aiml","25MC1A6159")
details("madhu",20,"AIML")
details("kishore",19)
details("rammana")
details()

# another example
def sample(price,discount=10):
    discount=price*discount/100
    final_price=price-discount
    return final_price
print(sample(100))
print(sample(100))
print(sample(100,20))

# functions task                       # task
# Task 1: Add Function
# Write a Python function named add that takes two arguments a and b and 
# returns their sum.
def add(a,b):
    return a+b
print(add(5,5))
# Task 2: Square Function
# Write a Python function named 
# square that takes a number 
# x as input and 
# returns its square.
def square(x):
    return x*x
print(square(5))
# Task 3: Factorial Function
# Write a Python function named factorial that takes a positive integer n as
# input and returns its factorial.
def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
print(factorial(2))
# Task 4: Maximum Function
# Write a Python function named 
# maximum that takes a list of numbers as input and 
# returns the maximum value in the list.
def maximum(n):
    return  max(n)
print(maximum([10,20,50,100,40]))
# Task 5: Reverse Function
# Write a Python function named 
# reverse that takes a string s as input and
# returns its reverse.
def reverse(s):
    return s[::-1]
print(reverse("amarnath"))
# Task 6: Check Prime Function
# Write a Python function named 
# is_prime that takes a positive integer n as input
# and returns 
# True if 
# n is prime, otherwise false
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True
print(is_prime(23))  
# Task 7: Fibonacci Function
# Write a Python function named fibonacci that takes a positive integer n
# input and returns the 
# n th Fibonacci number.
def fibonacci(n):
    if n<=1:
        return n
    a=0
    b=1
    for i in range(2,n+1):
        a,b=b,a+b
    return b
print(fibonacci(7))
# Task 8: Palindrome Function
# Write a Python function named 
# is_palindrome that takes a string s as input and returns True if 
# s is a palindrome, otherwise  false
def is_palindrome(s):
    return s==s[::-1]
print(is_palindrome("rotor"))
# Task 9: Sum of Squares Function
# Write a Python function named 
# sum_of_squares that takes a list of numbers as 
# input and returns the sum of the squares of those numbers
def sum_of_squares(s):
    sum=0
    for i in s:
        sum=sum+i*i
    return sum
print(sum_of_squares([1,2,3,4,5]))
# Task 10: Average Function
# Write a Python function named average that takes a list of numbers as input and 
# returns the average value.
def average(n):
    return sum(n)/len(n)           # sum of observations/no of observations
print(average([10,20,30,40,50,60,60]))


