i=1
str1=""
str2=""
str3=""
val=0
while i<=20:
    str2+= '-'
    str2+= '-'
    val=i%10
    str1+= str(val)
    str1+= str(val)
    
    if(i%4==1):
        str3+= '_'
    if(i%4==2):
        str3+= '-'
    if(i%4==3):
        str3+= '^'
    if(i%4==0):
        str3+= '-'

    i+=1
  
print str2
print
str3+=str3
print str3
print str1
print
print str2
