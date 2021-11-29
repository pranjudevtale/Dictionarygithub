# a=["pranju"]
# b=[]
# d={}
# for i in a:
#     for j in i:
#         b.append(j)
# print(b)
# i=0
# for x in b:
#     d.update({x:i})
#     i=i+1
# print(d)

# d={'a':20,'b':40,'c':{'d':11,'d':12,},'e':{'f':10}}
# sum=0
# for i in d.values():
#     if type(i)==dict:
#         for j in i.values():
#             if type(j)==dict:
#                 for k in j.value():
#                     sum+=k
#             else:
#                 sum+=j
#     else:
#         sum+=i
# print(sum)





# a={}
# num=int(input("enter the number:-"))
# i=0
# while i<(num):
#     name=input("emter the name")
#     age=int(input("enter the age"))
#     a.update({name:age})
#     i=i+1
# print(a)

# a={}
# num=int(input("enter the number:-"))
# i=0
# while i<len(num):
#     name=int(input("enter the name"))
#     age=int(input("enter the number"))
#     a.update({name:age})
#     i=i+1
# print(a)


# num=int(input("enter the number"))
# i=1
# a={}
# while i<=5:
#     a.update({i:i*i})
#     i=i+1
# print(a)

# list=[1,2,1,3,4,5,6,2,3,7,5,6,2,4,2,4,9]
# a={}
# for i in list:
#     b=list.count(i)
#     a[i]=b//2
# print(a)

# a=input("enter the name")
# b={}
# for i in (a):
#     b[i]=b.get(i,3)
# print(b)

# dict={'name':['pranju','ankita','vaishu'],
#         'age':[21,25,67],
#         'class':["m.sc","b,sc","b.com"]}

# for i in dict.values():
#     print(i)
#     j=0
#     while j in len(list):
#         print(j)
#         j=j+1
        
# a={'a':10,'b':20,'c':40}
# product=1

# for i in (a):
#     product=product*a[i]
# print(product)

# student={'vaishu':{"class":'v',
#         "roll_id":3},
#         "pranju":{"class":"v",
#         "roll_id":6}}
# for i in student:
#     print(i)
#     for j in student[i]:
#         print(j,":",student[i][j])

# a={"1":"pranju","2":"ankita","3":"vaishu"}
# a.popitem()
# print(a)



# a=["1st","2nd","3rd","4th"]
# b=[1,2,3,4]
# c=0
# d={}
# for i in a:
#     d[i]={b[c]}
#     c=c+1
# print(d)

# d={'a':20,'b':40,'c':{'d':11,'d':12,},'e':{'f':10}}
# sum=0
# for i in d.values():
#     if type(i)==dict:
#         for j in i.values():
#             if type(j)==dict:
#                 for k in j.values():
#                     sum=sum+k
#             else:
#                 sum=sum+j
#     else:
#         sum=sum+i
# print(sum)

# a={"p":1,"a":2,"r":3}
# b=[]
# for i in a():
#     b.append([i])
#     b.append(a[i])
# print(b)

a={"1st":1,"2nd":2,"3rd":3}
list=[]
list1=[]
for key in a:
    list.append(key)
    list1.append(a[key])
print(list)
print(list1)

