start=2
j=2
k=0
print"series =",
while start<60:
    if start==2:
        print start**2,
    elif j%2!=0 and start!=2:
        print (start**2)-k,
    else:
        print (start**2),
    if(j%2==0):
        k+=2
    start+=j
    j+=1
print