# Write a program to print the top 3 highest values of a given dictionary.
# Example :-
# Code Example
my_dict = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
max=0
for i in my_dict:
    if my_dict[i] > max:
        max=my_dict[i]
print(max)
max1=0
for i in my_dict:
    if my_dict[i]>max1:
        if my_dict[i]!=max:
            max1=my_dict[i]
print(max1)
max2=0
for i in my_dict:
    if my_dict[i]>max2:
        if my_dict[i]!=max1 and my_dict[i]!=max:
            max2=my_dict[i]
print(max2)
min=0
for i in my_dict:
    if my_dict[i]<max:
        if my_dict[i]!=max2 and my_dict[i]!=max1 and my_dict[i]!=max:
            min=my_dict[i]
print(min)