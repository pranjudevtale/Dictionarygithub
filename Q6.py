 
dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    }
p={}
for i in dic.keys():
    p.update(dic)
    break
print(p)