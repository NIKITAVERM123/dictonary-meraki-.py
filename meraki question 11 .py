# rite a program to print the top 3 highest values of a given dictionary.
# Input :-
# Code Example
my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
fm=0
for i in my_dict:
    if my_dict[i]>fm:
        fm=my_dict[i]
sm=0
for i in my_dict:
    if my_dict[i]>sm:
        if my_dict[i]!=fm:
            sm=my_dict[i]
tm=0
for i in my_dict:
    if my_dict[i]>tm:
        if my_dict[i]!=fm and my_dict[i]!=sm:
            tm=my_dict[i]
print("first max",fm)
print("second max",sm)
print("third max",tm)