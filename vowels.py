vowels='AEIOUaeiou'
word=input("enter the word")
count=0
for i in word:
    if i in vowels:
        count+=1
print("number of vowels in the word",count)
    
