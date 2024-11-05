b=int(input("enter the limit :"))
for i in range(2024,b):
    if (i%4==0 or i%400==0 )and i%100!=0 :
        print("leap year :",i)
