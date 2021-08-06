#Richter Scale

'''
The following table contains earthquake magnitude ranges on the Richter scale and their descriptors:

Magnitude Descriptor

Less than 2.0 Micro
2.0 to less than 3.0 Very minor
3.0 to less than 4.0 Minor
4.0 to less than 5.0 Light
5.0 to less than 6.0 Moderate
6.0 to less than 7.0 Strong
7.0 to less than 8.0 Major
8.0 to less than 10.0 Great
10.0 or more Meteoric

Write a program that reads amagnitude from the user and displays the appropriate descriptor as part of a meaningful message. For example, if the user enters 5.5 then your program should indicate that a magnitude 5.5 earthquake is
considered to be a moderate earthquake.
'''

a=float(input())

if(a<2.0):
    print("Micro")
elif(a>=2.0 and a<3.0):
    print("Very minor")
elif(a>=3.0 and a<4.0):
    print("Minor")
elif(a>=4.0 and a<5.0):
    print("Light")
elif(a>=5.0 and a<6.0):
    print("Moderate")
elif(a>=6.0 and a<7.0):
    print("Strong")
elif(a>=7.0 and a<8.0):
    print("Major")
elif(a>=8.0 and a<10.0):
    print("Great")
else:
    print("Meteoric")
