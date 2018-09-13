i=0
initialstarcounter = 6
laststarcounter = 6
forwardSlashcounter = 12
backwardSlashcounter = 0
forwardSlashstartingIndex = 7
laststarstartingIndex = 20
backwardSlashstartingIndex = 20
while i<7:
    j=0
    while j<26:
        if(j<initialstarcounter):
            print"*",
        elif(j>=forwardSlashstartingIndex and j<forwardSlashstartingIndex+forwardSlashcounter):
            print"/",
        elif(j>=backwardSlashstartingIndex and j<backwardSlashstartingIndex+backwardSlashcounter):
            print"\\",
        elif(j>=laststarstartingIndex and j<laststarstartingIndex+laststarcounter):
            print"*",
        else:
            print" ",
        j+=1
    print
    initialstarcounter-=1
    forwardSlashcounter-=2
    backwardSlashcounter+=2
    laststarstartingIndex+=1
    backwardSlashstartingIndex=forwardSlashstartingIndex+forwardSlashcounter
    i+=1

