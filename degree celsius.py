'''
AUTHOR: INDHU SUBASH
DATE:22-10-2024
PROGRAM: To make temperature values in fahreinheit and celsius
'''

temperature=int(input("Enter temperature:"))
unit=input("Is this in (C)elsius or (F)ahrenheit?")
if(unit=="C"):
   F=(9/5)*temperature+32
   print(temperature,"Celsius is",F,"Fahreinheit")
else:
    C=(5/9)*(temperature-32)
    print(temperature,"Fahreinheit is",C,"Celsius")
