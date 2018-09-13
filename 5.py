i=1
a=""
n=input("enter a no.")
spaces=n-1
while i<=n:
    a=""
    j=1
    while j<=spaces:
        a=a+" "
        j+=1
    k=1

    while k<=i:
        a=a+str(i)
        k+=1
    print a
    spaces-=1
    i+=1            

