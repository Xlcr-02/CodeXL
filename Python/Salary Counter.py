'''Help Raja to calculate a first salary that he got from the organisation , he was confused with an salary credited in his account . 
He asked his friend Ritu to identify how salary pay got calculated by giving the format of salary.
His basic pay (to be entered by user) and Ritu developed a software to calculate the salary
pay,with format given as below

HRA=80% of the basic pay,
dA=40% of basic pay
bonus = 25 % of hra

Input and Output Format:

Refer sample input and output for formatting specification.
All float values are displayed correct to 2 decimal places.
All text in bold corresponds to input and the rest corresponds to output'''

p=int(input())
h=p*0.8
b=h/4
d=p*0.4
print("Total Salary=",(h+p+b+d))

