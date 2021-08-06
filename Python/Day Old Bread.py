#Day Old Bread

'''A bakery sells loaves of bread for 185 rupees each. Day old bread is discounted by 60 percent.
Write a program that begins by reading the number of loaves of day old bread being purchased from the user.

Then your program should display the regular price for the bread, the discount because it is a day old, and the total price.

All of the values should be displayed using two decimal places, and the decimal points in all of the numbers should be aligned when reasonable values are entered by the user.'''

n=int(input())
reg=n*185
print("Loaves Discount")
print("Regular Price",reg)
print("Total Discount {:.1f}".format(reg*0.6))
print("Total Amount to be paid",(reg-(reg*0.6)))
