list3=[1,2,3,4,5,6,7,8,9]
list1=[]
list2=[]
for i in list3:
    if i%2==0:
        list1.append(i)
    else:
        list2.append(i)
print("even numbers :",list1)
print("odd numbers :",list2)

