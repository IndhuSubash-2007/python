'''Author:Indhu Subash
Date:29-10-24
'''

str=input("Enter a string:")
vcount=0
for a in str:
    if a in "AEIOUaeiou":
        vcount+=1
        print(a,end="  ")
print(vcount)
