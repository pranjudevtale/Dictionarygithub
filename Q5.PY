a=["one","two","three","four","five"]
b=[1, 2, 3, 4, 5]
# p=dict(zip(a,b))
# print(dict(p))

p=0
j={}
for i in a:
    j[i]=b[p]
    p=p+1
print(j)


