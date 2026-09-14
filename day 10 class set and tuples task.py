# set operations              TASK24
# union
set_1={1,2,3,4,5}
set_2={4,5,6,7,8,9}
set_3=set_1.union(set_2)
print(set_3)

# difference
set_1={1,2,3,4,5}
set_2={4,5,6,7,8,9}
set_3=set_2.difference(set_1)
print(set_3)

# intersection
set_1={1,2,3,4,5}
set_2={4,5,6,7,8,9}
set_3=set_1.intersection(set_2)
print(set_3)

# is disjoint
set_1={1,2,3,4,5}
set_2={6,7,8,9,10}
print(set_1.isdisjoint(set_2))

# is subset
set_1={1,2,3,4,5}
set_2={6,7,8}
print(set_1.issuperset(set_2))      
print(set_2.issubset(set_1))

# symmetric difference
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8,9}

set_3 =set_1.symmetric_difference(set_2)
print(set_3)

# frozen set
set_1={1,2,3,4,5,6,7,8,9,10}
set_2=frozenset(set_1)
print(set_2)

# tuples
tuple_1=()
print(tuple)
print(type(tuple))

tuple_1=tuple()
print(tuple)
print(type(tuple))

tuple_2=(1,1.2,"python life",True,(1),1,1,1,1,[1,2,3] )   #allow duplicates
print(tuple_2)
print(type(tuple_2))

x=1,2.0,"amarnath"
print(x)

x=10
print(x)

x=1
y=2
x,y=y,x
print(x)
print(y)


a=b=c=d=e=f=10
print(a)
print(b)
print(c)
print(d)
print(e)

# index               position says
sample_2=("amarnath",19,1.0,True)
print(sample_2.index("amarnath"))

# tuple concatination
tuple_1=(1,2,3,4,5)
tuple_2=(5,6,7,8,9,10)
result=tuple_1+tuple_2
print(result)

#  membership operators
list_1=("amarnath","sangeetha","selven","sairam")
result="amarnath" in list_1
print(result)

# Task 1: Set Intersection                          TASK25
# Write Python code to find and print the intersection of the following two sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# # Your code here
# # Output should be: {4, 5}
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}
set_3=set_1.intersection(set_2)
print(set_3)

# Task 2: Set Union
# Write Python code to find and print the union of the following two sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# # Your code here
# # Output should be: {1, 2, 3, 4, 5, 6, 7, 8}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set_3=set_1.union(set_2)
print(set_3)

# Task 3: Set Difference
# set2 :
# Write Python code to find and print the elements present in 
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Sets Quiz
# set1 but not in 
# 2
# # Your code here
# # Output should be: {1, 2, 3}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set_3=set_1.difference(set_2)
print(set_3)

# Task 4: Set Symmetric Difference
# Write Python code to find and print the symmetric difference of the following 
# two sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# # Your code here
# # Output should be: {1, 2, 3, 6, 7, 8}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set_3=set_1.symmetric_difference(set_2)
print(set_3)

# Task 5: Set Membership Test
# Write Python code to check if the element 3 is present in the set 
# my_set = {1, 2, 3, 4, 5}
# # Your code here
# # Output should be: True
my_set = {1, 2, 3, 4, 5}
result=1 in my_set
print(result)

# Exercise 1: Set Intersection
# my_set :
# Write a Python script that finds and prints the intersection of two sets.
set_1 = {10,20,30,40,50}
set_2 = {40,50,60,70,80}
set_3=set_1.intersection(set_2)
print(set_3)

# Exercise 2: Set Union
# Write a Python script that finds and prints the union of two sets.
set_1={1,2,3,4,5,6,7}
set_2={1,2,3,4,5,6,7,8,9,10}
set_3=set_1.union(set_2)
print(set_3)

# Exercise 3: Set Difference
# Write a Python script that finds and prints the difference between two sets.
set_1={1,2,3,4,5,6,7}
set_2={1,2,3,4,5,6,7,8,9,10}
set_3=set_2.difference(set_1)
print(set_3)

# Exercise 4: Set Symmetric Difference
# Write a Python script that finds and prints the symmetric difference between 
# two sets.
set_1={1,2,3,4,5,6,7}
set_2={1,2,3,4,5,6}
set_3=set_1.symmetric_difference(set_2)
print(set_3)



# TUPLES TASK
# Create a Tuple Write a program that creates a tuple containing three 
# elements: your name, your age, and your favorite color. Then print the tuple
tuple=("amarnath",19,"pink")
print(tuple)

# Access Tuple Elements Write a program that creates a tuple containing the 
# days of the week. Then, print the third element of the tuple
tuple=("sunday","monday","tuesday","wednesday","friday","saturday")
print(tuple.index("wednesday"))     
print(tuple[2])                     

#  Tuple Concatenation Write a program that creates two tuples, one 
# containing odd numbers from 1 to 5 and another containing even numbers 
# from 2 to 6. Concatenate these two tuples and print the result.
tuple_1=(1,3,5)
tuple_2=(2,4,6)
result=tuple_1+tuple_2
print(result)

#  Tuple Unpacking Write a program that defines a tuple containing the 
# dimensions of a rectangle (length and width). Then, unpack this tuple into 
# two variables and calculate the area of the rectangle.# Define a tuple containing the dimensions of a rectangle
rectangle = (10, 5)   # (length, width)
length, width = rectangle
area = length * width
print(length)
print(width)
print(area)

# Check if an Element Exists Write a program that checks if a given element 
# exists in a tuple.
tuple=("apple","banana","orange","kiwi")
result="apple" in tuple
print(result)