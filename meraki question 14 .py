# Write a program to sort a dictionary in ascending or descending according to its values .
# Input :-
# Code Example
a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# a=[2,4,6,9,1,7,6]
for i in range(6):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print(a)