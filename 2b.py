# dictionary - key should be unique ,if not unique key will overwrite with the new value 
d={}
print(type(d))
d={1:"TUE",'key':"vaib",'phone':9088}
print(d)
d1={1:'vib',1.2:'hemoglobi','!ohyeee':'ayehayyein!',True:10}
print(d1)
d2={1:'rohan','$':'33'}
# key data are use numericvalues,bool,string but specail characters not use 
print(d2)
print(d2[1])
print(d2['$'])
print(d1[1])

d4={'name':'vaib','email':'vaib@','name':'Vaibahvsharma'}
print(d4['name']) 


d5={'cpmpany':'pwskills','courses':['web','java with dsa','System desig ','data analyst']}
print(d5)
print(d5['courses'])
print(d5['courses'][1])

d6={"number":[2,34,3,24,34],"assignmant":(1,2,3,4,5,6),'launch date ':{28,12,14},'class timing ':{'webtech':8,'datascince':8,'java with dsa ':7}}
print(d6['class timing ']['java with dsa '])

d6['mentor']=['aditya kumar ','sudhanshu kumar ','rani mam ']
print(d6)
d6['mentor']=['MY GURUDEV  ']
print(d6)

del d6['number'] # del 
print(d6)
print("ll")
print(list(d6.keys())) # give all keys in dictionary 
print(list(d6.values())) # give all values in dictioanry 
print("hi:")
print(list(d6.items())) # give key value pair  each key value in (), give in tuple
print(d6.pop('assignmant'))
print(d6)
del d6['launch date ']
print(d6)


d7={1:2+3J}
print(d7)



# control flow ----------------- 
marks=int(input("enter marks ="))
if marks>=80:
    print("you will a part of A0 batch")
elif marks>=60 and marks<80:
    print("you will a part of A1 batch")
elif marks>=40 and marks<60:
    print("you will a part of A2 batch ")
else:
    print("you will part of A3 batch and focus on you interest")



##price=eval(input("enter price ="))
##if price > 1000 :
##    print("i will not purchase")
##    if price>5000 :
##        print("its too much")
##    elif price>2000:
##        print("its okay")
##    else:
##        print("its not bad")
##elif price>2
##else:
##    print("i will purchase")


# loop 

l=[1,2,3,4,5,6,7]
##a=0
nl=[]
##for i in l:
##    na=i+1
##    nl.insert(a,na)
##    a+=1
##print(nl)


for i in l:
    nl.append(i+1)
print(nl)



l1=[]
for i in l:
    print(i+1)
    l1.append(i+1)
print(l1)


l=["sudh","kumar","pwskills",''' course
   ''']
l1=[]
for i in l :
   l1.append(i.upper())
print(l1)

l=[1,2,3,4,5,6
   ]
print(l)



l=[1,2,3,4,4,"sudh","kumar",324,34.456,"abc"]
l1=[]
l2=[]
for i in l:
    if (type(i)==int or type(i)==float ):
        l1.append(i)
    else:
        type(i)==str
        l2.append(i)

print("numeric element is ",l1)
print(" string element list is ",l2)


l=[1,2,3,4,4,"sudh","kumar",324,34.456,"abc"]
l1_num=[]
l3_str=[]
for i in l:
    if type(i)== int or type(i)==float:
        l1_num.append(i)
    else :
        l3_str.append(i)
print(l1_num)
print(l3_str)

    
      

