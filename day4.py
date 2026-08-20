#OPERATORS
#  #Arthematic operators

#addition operation
num1=100
num2=200
print(num1+num2)

#subractionoperation
amarpurchasegoldthepriceisoneyearback=100000
nowitsincreasesto=150000
print(nowitsincreasesto-amarpurchasegoldthepriceisoneyearback)

#multiplication operation
applesperkg=100
mangoesperkg=20
print(applesperkg*mangoesperkg)

#divisionoperation
a=100
b=2
result=a/b
print(result)

#floor division operation
x=200
y=10
print("result:",x//y)

# #module operation
sangeethasays=100
amarnathsays=10
result=(amarnathsays%sangeethasays)
print(result)

#exponential operation
sangeethasays=10
amarnathsays=10
result=(amarnathsays+sangeethasays)**2
print(result)


#assingment operators
dairymilk=78
dairymilk+=2  #eq-->dairymilk=dairymilk+2
print(dairymilk)

saree=503
saree-=3   #eq--> saree=saree-2
print(saree)

book=50
book*=1   #eq-->book=book*1
print(book)

bag=4000
bag/=10  #eq-->bag=bag/10
print(bag)

#comparison operators
amarnathluckynumber=19
sangeethaluckynumber=1
print(amarnathluckynumber==sangeethaluckynumber)
print(amarnathluckynumber<sangeethaluckynumber)
print(amarnathluckynumber>sangeethaluckynumber)
print(amarnathluckynumber<=sangeethaluckynumber)
print(amarnathluckynumber>=sangeethaluckynumber)
print(amarnathluckynumber!=sangeethaluckynumber)

#logical operators
#AND
amarnathage=18
sangeethaage=18
print(amarnathage>sangeethaage)
print(id(sangeethaage))
print(amarnathage==sangeethaage)

#OR
selvan=True
print(selvan)

selvan2=False
print(not selvan2)

#NOT
phone=10000
print(not(phone>5000))

#identify operators
a=[10,20,30]
b=a
print(a is b)
print(a is not b)

a=[10,20,30]
b=[10,20,30]
print(a is b)
print(a is  not b)

#membership operators
magipacket=1
packet_cost=120
result=magipacket*(packet_cost/100)
print(result)

#output formatting f strings
amarnathmarks=95
sangeethamarks=34
print(f"amarnath marks is {amarnathmarks} indicates he passed the exam and sangeetha marks is {sangeethamarks} indicates she fail the exam")
