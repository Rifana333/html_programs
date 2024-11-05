list1=[]
list2=[]
a=int(input("Enter number of element in list :"))
for i in range(a):
    num=int(input("Enter the nuumber :"))
    list1.append(num)
for i in list1:
    if i > 100:
        list2.append('over')
    else:
        list2.append(i)
print("list",list1)
print(list2)
