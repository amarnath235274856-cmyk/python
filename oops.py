# oop methods

# 1.class
def details(self,):
    print(f"he is my friend {self}")
details("bharath")

# 2.object
class amar_details():         #class defination
    name="amarnath"           # attributes
    age="19"
    id="25MC1A6159"
    def details(self,):       #methods
        print(f"He is well in coding")
    def details1(self,):
        print(f"he is currently working at infoysis")
#obj=classname()
sample=amar_details()
sample.details()
sample.details1()
print(sample.name)
print(sample.age)
print(sample.id)

#__init__method
class car():        # class def
    def __init__(self,colour="white",brand="fortuner",price="5000000"):      #init method
         
         self.colour=colour      # attributes
         self.brand=brand
         self.price=price
    def start(self,):             #methods
        print(f"His car price is about {self.price}")
    def stop(self,):
        print(f"He come at home 8pm in his {self.brand}")
sample=car("white","fortuner","5000000")     #obj=classname()
sample.start()
sample.stop()
print(sample.colour)

#inheritance
# single inhertance
class parent:
    def sample(self):
        print(f"this is father class")
class child(parent):
    def sample1(self):
        print(f"this is child class")
#obj=classname()
result=child()
result.sample()
result.sample1()

# another example
class kristappa:
    def sample(self):
        print(f"he is my father{kristappa}")
class amarnath(kristappa):
    def sample_1(self):
        print(f"this is me")
# obj=classname()
result=amarnath()
result.sample()
result.sample_1()

#hierarchial inheritance
class parent:
    def sample(self):
        print(f"this is father class")
class child(parent):
    def sample1(self):
        print(f"this is child class")
class child2(parent):
    def sample2(self):
        print(f"this is child class two")
#obj=classname()
result=child2()
result.sample2()

# class parent:
class grandfather:
    def sample(self):
        print(f"this is father class")
class father(grandfather):
    def sample_1(self):
        print(f"this is child class")
class child(father):
    def sample2(self):
        print(f"this is child class two {50000}")
#obj=classname()
result=child()
result.sample2()
result.sample_1()
result.sample()

# multi inheritance
class father:
    def sample(self):
        print(f"father name is kistappa ")
class mother:
    def sample_1(self):
        print(f"mother name is sathyamma")
class child(father,mother):
    def sample_2(self):
        print(f"this is me")
list=child()
list.sample_2()
list.sample_1()
list.sample()


# polymorphism
# 1.overloading
# operator overloading
num_1=10
num_2=20
print(num_1+num_2)

num_1="amarnath,"
num_2="selvan"
print(num_1+num_2)

# method overloading
class number():
    def add(self,a,b):
        print(a+b)
    def add1(self,a,b,c):
        print(a+b+c)
obj=number()
obj.add(10,20)

class values():
    def add(self,a=None,b=None,c=None,d=None):
        print(a,b,c,d)
obj=values()
obj.add(10,10,10,10)
obj.add(10,10,10)
obj.add(10,10)
obj.add(10)
obj.add(10)

#method overriding
class father():
    def sample(self):
        print(f"this is father section")
class child(father):
    def sample_1(self):
        print(f"this is sample one section ")
        super().sample()
obj=child()
obj.sample_1()

# encapsulation
# public
# protect
# private
class amarnath():
    def __init__(self,a):
        self.a=a
        print(f"this is amarnath")
class sai(amarnath):
    def sample(self,):
        print(f"this is sairam class{1}")
obj=sai(1)
obj.sample()

class amarnath():
    def __init__(self,a):
        self._a=a
        print(f"this is amarnath")
class sai(amarnath):
    def sample(self,):
        print(f"this is sairam class{self._a}")
obj=sai(":well")
obj.sample()

# class amarnath():
class amarnath():
    def __init__(self,a):
        self.__a=a
        print(f"this is amarnath")
class sai(amarnath):
    def sample(self,):                      
        print(f"this is sairam class{self.__a}")      # riases an error
obj=sai(1)
obj.sample()

# abstractions
from abc import ABC,abstractmethod
class phone(ABC):
    @abstractmethod
    def calling(self):
        pass
    @abstractmethod
    def message(self):
        pass
class feature(phone):
    def calling(self,number):
        self.number=number
        print(f"he is calling{number}")
    def message(self):
        print(f"she message me")
obj=feature()
obj.calling(6303592952)
obj.message()