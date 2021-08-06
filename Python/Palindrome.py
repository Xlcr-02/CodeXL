#Palindrome

'''
The program takes a number and checks whether it is a palindrome or not .

DESCRIPTION:
1. Take the value of the integer and store in a variable.
2. Transfer the value of the integer into another temporary variable.
3. Using a while loop, get each digit of the number and store the reversed number in another variable.
4. Check if the reverse of the number is equal to the one in the temporary variable.
5. Print the final result.
6. Exit.
'''

n=(input(""))
temp=n[::-1]
if(temp==n):
    print("palindrome")
else:
    print("not a palindrome")
