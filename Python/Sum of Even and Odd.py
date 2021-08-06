#Sum of Even and Odd

'''
Write a program to calculate the sum of even and odd numbers including its count.

Input:
1.Total number of Inputs
2. Input elements

Output:
1. Odd numbers count
2. Even numbers count
3. Sum of even numbers
4. Sum of odd numbers
'''

n=int(input())
l=[]
ec,oc,es,os=0,0,0,0
for i in range(n):
    l.insert(i,int(input()))
 
for i in range(n):
    if (l[i]%2)==0:
        ec+=1
        es+=l[i]
    else:
        oc+=1
        os+=l[i]
 
print(oc)
print(ec)
print(es)
print(os)
