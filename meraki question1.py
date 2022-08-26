d={1:10,2:20}
d1={3:30,2:40}
d2={5:50,6:60}
for i in d:
    if i in d1:
        sum=d[i]+d1[i]
        d[i]=sum
        d1.pop(i)
d.update(d1)
d2.update(d)
print(d2)

    