# Noise Levels
'''
The following table lists the sound level in decibels for several common noises. Noise Decibel level (dB)
Jackhammer noise >=130 
Gas lawnmower 106 to 129 
Alarm clock 41 to 105
Quiet room 0 to 40

Write a program that reads a sound level
in decibels from the user. If the user
enters a decibel level that matches one of
the noises in the table then your program
should display a message containing only
that noise. If the user enters a number of
decibels between the noises listed then
your program should display a message
indicating which noises the level is
between. Ensure that your program also
generates reasonable output for a value
smaller than the quietest noise in the table,
and for a value larger than the loudest
noise in the table.
'''


d = float(input())
 
if d> 0 and d<= 40:
    print('Quiet room')
elif d> 40 and d <= 105:
    print('Alarm clock')
elif d> 105 and d <130:
    print('Gas lawnmower')
elif d >=130:
    print("Jackhammer")
