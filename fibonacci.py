'''
NAME:INDHU SUBASH
DATE:03-12-24
'''

def generate_fibonacci(n):
    sequence=[]
    first_number,second_number=0,1
    for i in range(n):
        sequence.append(first_number)
        first_number,second_number=second_number,first_number+second_number
    return sequence
limit=int(input("Enter the limit:"))
print(generate_fibonacci(limit))