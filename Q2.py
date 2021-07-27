dict={"name":"pranju","marks":56}
for i in dict.keys():
    p=input("enter the keys name  ")
    if p in dict:
        print("exist")
    else:
        print("not exist")