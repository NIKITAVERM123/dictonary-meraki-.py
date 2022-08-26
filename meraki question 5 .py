# Create a dictionary from 2 lists, where the elements of 1st list are the keys and the elements of the 2nd list are the corresponding values.
# Example :-
# Input :-
# Code Example
list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
d={}
for i in range(len(list1)):
#     d.update({list2[i]:list1[i]})
    d[list2[i]]=list1[i]
print(d)
        #  print(list2[i])
