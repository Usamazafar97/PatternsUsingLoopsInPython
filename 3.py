import random
x=round ( random.random() *100 )
o=0
i=0
while i<=2:
    y=input("enter a no.")
    if(x==y):
        o+=1
    i+=1
if(o>=3):
    print "you won"
else:
    print " you lost" 
z=input("do you want to continue ?")
while (z==1):
    import random
    x=round ( random.random() *100 )
    o=0
    i=0
    while i<=2:
        y=input("enter a no.")
        if(x==y):
            o+=1
        i+=1
    if(o>=3):
        print "you won"
    else:
        print " you lost"
    z=input("do u want to continue ?")