# Take input of name and marks of 10 students and store to a dictionary.
b={}
for i in range(10):
    n=int(input("enter the number :"))
    e=input("enter chr :")
    b.update({e:n})
print(b)
