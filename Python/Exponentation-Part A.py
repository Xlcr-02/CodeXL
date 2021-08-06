#Exponentation-Part A

'''
Write a program to find the exponentation of given number

Input 1: Number of terms 
Input 2: Base

Output:
List of exponentation terms for the given input

Refer sample input and output for formatting specification.
'''

n= int(input())
b= int(input())
p = 0
print("The total terms is:",n)
for i in range(0, n):
    p=pow(b,i)
    print(p)
