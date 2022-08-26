a = {(1,2):1,(2,3):2}
print(a[1,2])
a = {'a':1,'b':2,'c':3}
print(a['a','b'])
fruit = {}

def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
addone('Apple')
addone('Banana')
addone('apple')
addone('Apple')
print(len(fruit))
# print(fruit)
# SOLVE
Student = {}
Age = {}
Details = {}
Student['name'] = "bikki"
Age['student_age'] = 14
Details['Student'] = Student
Details['Age'] = Age
print(len(Details["Student"])) 
#  NOT SOLVE
box = {}
jars = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
print(len(crates[box]))
# SOLVE
rec = {
"Name" : "Python", 
"Age":"20",
"Addr" : "NJ", 
"Country" :"USA"
}
id1 = id(rec)
del rec

rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id1 == id2) 
details={"name":"Shanti","age":12,"email":"shanti@navgurukul.org","lastname":13}
print(details["name"])
print(details["lastname"])
print(details["age"])
# /SOLVE
dict1={1:2,2:3,3:4,4:5}
sum=0
for i in dict1.values():
        sum=sum+i
print(sum)
from this import d


c=dict()
for i in range(1,16):
    c=i*i
print(c)