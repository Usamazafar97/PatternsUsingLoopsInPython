i=0
factor=0
div = 0
while i<6:
    div=factor/2
    j=0
    while j<22:
        if(j<div):
            print"\\",
        elif ( j>(21-div)):
            print"/",
        else:
            print "!",
        j+=1
    print
    factor+=    4
    
    i+=1
    

   