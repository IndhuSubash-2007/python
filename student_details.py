'''
Python program to get student details
Author: Indhu Subash
Date: 01-10-2024
Version:1.0
 '''
name=input("Enter the student name:")
roll_number=int(input("Enter your roll number:"))
roll_number=roll_number+1
cgpa=float(input("Enter the CGPA:"))
percentage_mark = cgpa*10
print("Name of the student:",name)
print("Roll Number:",roll_number)
print("Marks Percentage:",percentage_mark,"%")
