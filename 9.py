
j=0
while j<8:
    
    if(j==0 or j==7):
        print "+",
    else:
        print "-",
    j+=1
print
z=0
while z<=1:
    initial=0
    final=7
    num=3
    i=0
    row=0
    while i<4:

        j=0
        while j<9:
            if(j==0 or j==7):
                print "|",
            else:
                if(j==(initial + num) or j==(final - num)):
                    print"*",
                else:
                    print" ",
            j+=1
        print
        num-=1
        row+=1
        i+=1
    z+=1
j=0
while j<8:
    
    if(j==0 or j==7):
        print "+",
    else:
        print "-",
    j+=1
print

z=0
row=4
while z<=1:    
    i=0
    row=0
    while i<4:
        j=0
        while j<8:
            if(j==0 or j==7):
                print "|",
            else:
                if(j==row or j==(7-row)):
                    print"*",
                else:
                    print" ",
        
            j+=1
        print
       
        row+=1
        i+=1
    z+=1

j=0
while j<8:
    if(j==0 or j==7):
        print "+",
    else:
        print "-",
    j+=1
print

