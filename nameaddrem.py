names=[]
list2=[]
for i in range (5):
    name=input("enter name:")
    names.append(name)
for name in names:
    if name[0]=="A" or name[0]=="a":
       list2.append(name)
       names.remove(name)
print("name starting with A is :",list2)
print(names)
