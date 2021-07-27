a={'jittu':45,'ganesh':60,'ramesh':20,'pranju':30,'anjali':50}
h={}
for i in a:
    c=a[i]
    for i in a:
        b=a[i]
        if c>b:
            h[i]=b
print(h)

# for i in a:
#     c=a[i]
#     for i in a:
#         b=a[i]
#         if c>b:
#             h[i]=b
# print(h)

# h={}
# for i in a.keys():
#     h.update(a)
# print(h)
