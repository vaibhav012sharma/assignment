import sys
print(sys.version)


# keywords
print(help("keywords"))



# variable
x=12 # declare and define
#single line assignment
# variable=value/variable/expressions 
a=10 # declaration of variable
b='vaibhav'
c=23.32
d=True
print(a);print(b);print(c);print(d)



# Multi line assignment
a,b,c,d=12,'VAIBHAV',24.43,False
print(a,b,c,d , sep="\t\t" ) # sep concept only use in print it means each element after sepreate is


#chained Assignment
a=b=c=12;print(a,b,c,sep="\n")


# compound assignment
a=1
a+=1
print(a)


# Expression assignment  walrus symbol (:=)
print((a:=12+13))



# Type conversion
p=12
o=20.32
print(p+o) # here interpreter convert int data (p) to float data > this is implicit conversion
w=12
r="vaibhav"
#print(r+w) # eror bcz we can not perform operations on different operands
print(w+str(r))
print(w+str(22.34))
print(w+str(True))


