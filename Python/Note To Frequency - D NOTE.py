#Note To Frequency - D NOTE

'''
The following table lists an octave of music notes, beginning with middle D, along with their frequencies.

Note Frequency (Hz) D4 293.66 Begin by writing a program that reads the name of a note from the user and displays
the notes frequency. 

Your program should support all of the notes listed previously. Once you have your program working correctly for the
notes listed previously you should add support for all of the notes from D0 to D8.

While this could be done by adding many additional cases to your if statement, such a solution is cumbersome,
inelegant and unacceptable for the purposes of this exercise. 

Instead, you should exploit the relationship between notes in adjacent octaves. In particular, the frequency of any note
in octave n is half the frequency of the corresponding note in octave n+1.

By using this relationship, you should be able to add support for the additional notes without adding additional cases to
your if statement.

Hint:

To complete this exercise you will need to extract individual characters from the two-character note name so that you
can work with the letter and the octave number separately.

Once you have separated the parts, compute the frequency of the note in the fourth octave using the data in the table
above.

Then divide the frequency by 2 power(4-x ), where x is the octave number entered by the user. (freq=freq/2**(4- octave))
This will halve or double the frequency the correct number of times.
'''

a=input()
b=int(a[1])
print(round(293.66/(2**(4-b)),4))
