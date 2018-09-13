
min=float('Inf')
x=0
while x<=10:
    y=-20
    while y<=20:
        z=(((1-x)**2)+(100*((y-x**2)**2)))
        if(z<min):
            min=z
        print "value=",z
        y+=1
    x+=1
print min