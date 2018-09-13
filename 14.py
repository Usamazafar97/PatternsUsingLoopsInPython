lines=input("enter lines")
cheers=input("enter cheers")
i=0
space=""
while i<lines:
    j=0
    while j<cheers:
        if(j>0):
            print "Buddy",
        print "Go",
        j+=1
    
    space+="   "
    print
    print space,

            
    i+=1