# Error Handling
num_1=10
num_2=2
try:
    result=num_1/num_2
except ValueError as e:
    print("value error:", {e})
else:
    print(num_1/num_2)
finally:
    print(f"exection completed")

# ValueError Raised when an operation or function receives an argument of 
# the correct type but an inappropriate value):
try:
    num_1=int("amarnath")
except ValueError as e:
    print(f"value error:,{e}")

# TypeError Raised when an operation or function is applied to an object of an 
# inappropriate type):
try:
   num_1=10
   num_2="amarnath"
   result=num_1+num_2
except TypeError as e:
   print(f"type error:",{e})

# FileNotFoundError Raised when a file or directory is requested but cannot be 
# found):
try:
    file=open("test.txt","r")
except FileNotFoundError as e:
    print("file not not found:",{e})

# ZeroDivisionError Raised when the second operand of a division or module 
# operation is zero):
try:

    num_1=10
    num_2=0
    print(num_1/num_2)
except ZeroDivisionError as e:
    print(f"division error{e}")

# IndexError Raised when a sequence subscript is out of range):
list=[1,2,3,4,5,6,7,8,9,10]
try:
   print(list[20])
except IndexError as e:
    print("index error {e}")
    print(list[4])

# KeyError (Raised when a dictionary key is not found):
dictonary={
    "name":"amarnath",
    "age":19,
    "marks":95
}
try:
    print(dictonary["id_card number"])
except KeyError as e:
    print("key error:",{e})

# AttributeError Raised when an attribute reference or assignment fails):
try:
   sample={"amarnath","sangeetha","selven","sairam"}

   sample.count()
except AttributeError as e:
    print("attribute error:",{e})
    print(sample)

# OverflowError : Raised when an arithmetic operation exceeds 
# the limits of the current Python interpreter):
import math
try:
    print(math.exp(1000))
except OverflowError as e:
    print("over flow error:",{e})


# IOError Base class for I/O-related errors):
try:
    file = open("/root/protected_file.txt","w")
except IOError as e:
    print("IOError: {e}")

try:
    file = open("/root/protected_file.txt", "w")
except IOError as e:
    print(f"IOError: {e}")

# RuntimeError Raised when an error is detected that doesnʼt fall in any of the 
# other categories):
try:
    raise RuntimeError ("someting happend run errror")
except RuntimeError as e:
    print("run time error:",{e})
    print(num_1*num_2)
# Exception Base class for all exceptions):
try:
    num_1=10
    num_2=0
    result=num_1/num_2
except Exception as e:
    print("exception :",{e})