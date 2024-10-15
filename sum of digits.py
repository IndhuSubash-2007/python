'''
Author:Indhu Subash
Date:15-10-2024
'''
number=int(input("Enter the number:"))
sum=0
while(number>0):
     r=number%10
     number=number//10
     sum=sum+r
print("sum of digits:",sum)