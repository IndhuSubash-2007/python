'''
AUTHOR:INDHU SUBASH
DATE:29-10-24
PROGRAM:FOR LOOP
'''

number=int(input("Enter the number:")               )
isPrime = True
for i in range(2,number//2+1):
  if number % i ==0:
     isPrime = False
     break
if isPrime:
     print(f"The given number {number} is Prime")
else:
     print(f"The given number {number} is Not Prime")