# Waiting or Not Waiting

'''Raju maths teacher gave him a task of identifying the number name. If the number is greater than 0 then he should
utter to the teacher as "I am waiting". If the number is less than 0 then he should utter the word as "I am not waiting".

If the number is "0" the he should utter the word as "Sorry".

Help him by completing his task.'''

a=int(input())
if a<0:
 print('I am not waiting')
elif a==0:
 print("Sorry")
else:
 print("I am waiting")
