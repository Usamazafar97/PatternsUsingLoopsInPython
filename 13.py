#num=input("enter three digit no.")
#a=num/100
#x=(a*(2**2))
#num=num%10
#b=num/10
#y=(b*(2**1))
#num=num%10
#c=num/1
#z=(c*(2**0))
#num=num%1
#sum=x+y+z
#print sum

num_str=raw_input("enter binary no.")
i=0
sum=0
binary_num_length=len(num_str)
while i<binary_num_length:
    print num_str[i] 
    bit=int(num_str[i]) 
    sum+=bit*(2**((binary_num_length-1)-i))
    i+=1

print sum