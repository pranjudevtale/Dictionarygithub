my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
list_key=[]
for i in range(3):
    max=0
    for x in my_dict:
        if max<my_dict[x]:
            max=my_dict[x]
            key=x
    list_key.append(max)
    my_dict.pop(key)
print(list_key)

