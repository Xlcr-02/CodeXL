# Ph Level

'''
Write a Python Program to identify Ph Level Name using the following condition.

Ph <7.0
acidic Ph>7.0
basic Ph=0 neutral
'''

ph=float(input())
if(ph==0):
    print("neutral")
elif(ph<7.0):
    print("acidic")
else:
    print("basic")
