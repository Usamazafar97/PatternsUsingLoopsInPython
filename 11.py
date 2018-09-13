
i=0
row = 0
while i<31:
    #if(i<3):
    #    if(row< 3):
    #        row+=1
    #        continue
    j=0
    while j<11:
        if(j==row or j==11-1-row):
            print "*",
        else:
            print " ",
        j+=1
    print
    if(row%10==0):
        row = 0
    row+=1
    i+=1

