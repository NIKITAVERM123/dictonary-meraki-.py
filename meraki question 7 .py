# ake a list having dictionary elements as shown below (Sample Data) and then store all the unique values into a list and print.
a=[{"first":"1"},{"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
l=[]
for j in a:
    for i in j:
        if j[i] not in l:
            l.append(j[i])
print(l)            