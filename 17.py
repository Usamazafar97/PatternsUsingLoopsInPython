n=input("enter rupees")
a=6
b=9
c=20
if(n%a==0):
    print"it is possible"
elif(n%b==0):
    print"it is possible"
elif(c==0):
    print"it is possible"
elif(n%(a+b)==0):
    print"it is possible"
elif(n%(b+c)==0):
    print"it is possible"
elif(n%(c+a)==0):
    print"it is possible"
elif(n%(c+a+b)==0):
    print"it is possible"
else:
    print"it is not possible"

