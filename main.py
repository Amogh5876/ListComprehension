mylist= [queu*8 for queu in "wordtwo"]
print(mylist)

mylist= [x**2 for x in range(0,11) if x%2==0 ]
print(mylist)

mylist=[]
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)

print(mylist)
mylist =[x*y for x in [2,4,6] for y in [100,200,300]]
print(mylist)
