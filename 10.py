
j=0
while j<11:
    
    if(j==0 or j==10):
        print "+",
    else:
        print "-",
    j+=1
print

i=0
center = 4
beforeCenter = 4
afterCenter = 0
while i<4:
    j=0
    while j<10:
        if(j==0 or j==9):
            print"|",
        if(j==center):
            print"*",
        else:
            if(j>=(beforeCenter) and j<center ):
                print"/",
            elif(j>center and j<(9-center+afterCenter) ):
                print"\\",
            else:
                print" ",
        j+=1
    print

    beforeCenter-=1
    afterCenter+=1

    i+=1


z=0
while z<=1:
    secondHalfbeforeCenter = 0
    secondHalfafterCenter =  1
    i=0
    while i<4:
        j=0
        while j<10:
            if(j==0 or j==9):
                print"|",
            if(j==center):
                print"*",
            else:
                if(j>(secondHalfbeforeCenter) and j<center ):
                    print"\\",
                elif(j>center and j<(9-secondHalfafterCenter) ):
                    print"/",
                else:
                    print" ",
            j+=1
        print

        secondHalfbeforeCenter+=1
        secondHalfafterCenter+=1

        i+=1
    if(z==0):
        j=0
        while j<11:
    
            if(j==0 or j==10):
                print "+",
            else:
                print "-",
            j+=1
        print

    z+=1

i=0
center = 4
beforeCenter = 4
afterCenter = 0
while i<4:
    j=0
    while j<10:
        if(j==0 or j==9):
            print"|",
        if(j==center):
            print"*",
        else:
            if(j>=(beforeCenter) and j<center ):
                print"/",
            elif(j>center and j<(9-center+afterCenter) ):
                print"\\",
            else:
                print" ",
        j+=1
    print

    beforeCenter-=1
    afterCenter+=1

    i+=1

j=0
while j<11:
    
    if(j==0 or j==10):
        print "+",
    else:
        print "-",
    j+=1
print