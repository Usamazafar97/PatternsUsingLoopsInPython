i=1
while(i<=9):
    j=9
    while(j>i):
        print "   ",
        j-=1

    j=1
    while(j<=i):
        print "{}  ".format(j),
        j+=1
    j=j-2
    while(j>=1):
        print "{}  ".format(j),
        j-=1
    print
    i+=1

spaceCounter = 1
i=0

while(i<9):
    j=0
    NumCounter = 1 
    while(j<9):
        if(j<spaceCounter):
            print "   ",
        else:
            print "{}  ".format(NumCounter),
            NumCounter+=1
        
        j+=1
    print
    spaceCounter+=1

    i+=1