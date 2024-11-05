n=int(input("enter an number :"))
s=0
a=1
b=1
i=1
print(" fibnocci is" n,":")
while i<n:
    print(a)
    s=a+b
    a=b
    b=s
    i+=1
