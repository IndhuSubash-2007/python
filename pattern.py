'''
AUTHOR:INDHU SUBASH
DATE=19-11-24
'''

#PATTERN1
limit=int(input("Enter the limit:"))
for i in range(0,limit):
   for j in range(i+1):
        print("*",end="")

   print()
print("  ")

 #PATTERN2
for i in range(limit,0,-1):
    for j in range(i):
        print("*", end="")
    print()
print("  ")

#PATTERN3

for i in range(1, limit+1):
         for j in range(limit-i):
             print(" ", end="")
         for  k in range(2*i-1):
              print("*", end="")
         print()
         break
#PATTERN4
for i in range( limit,0,-1):
         for j in range(limit-i):
             print(" ", end="")
         for  k in range(2*i-1):
              print("*", end="")
         print()