# Store the unique letters and their frequency of the letters from the word "MISSISSIPPI" to a dictionary, were the letters are the keys and their frequencies are the values.
# Example:-
# Output :-
# Code Example
# a={'M':1,'I':4,'S':4,'P':2}
a="MISSISSIPPI"
i=1
f={}
for i in a:
    c=0
    for j in a:
        if i==j:
            c=c+1
            f[i]=c
print(f)