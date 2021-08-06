# Month Day and Year - Jan to May

'''
The length of a month varies from 28 to 31 days. In this exercise you will create a program that reads the name of a month from the user as a string. Then your program should display the number of days in that month. 

Display 28 or 29 days for February so that leap years are addressed. 

The program should get input from Jan to Apr. 

If the input is from may to other months then display error messages as "Invalid"
'''

m = input()

if m == "Feb":
 print("28 or 29")
 
elif m in ("Apr", "Jun", "Sep", "Nov"):
 print("30")
 
elif m in ("Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"):
 print("31")
