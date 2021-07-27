a= [
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
h=[]
for i in range(len(a)):
    for j in a[i]:
        if a[i][j] not in h:
            h.append(a[i][j])
print(h)

# a=[]
# b={}
# i=0
# while i<len(a):
#     b.update(a[i])
#     i=i+1
# print(b)
# for i in b.value():
#     if i not in a:
#         a.append(a[i][j])
# print(b)

