# Description: This program plays the Harry Potter theme song using the musicpy library. If you don have musicpy library in your system, you can install it by running the following command in your terminal
# pip install musicpy

from musicpy import *

First_Verse = chord('B5, E5,  G5, F#5,  E5,  B6,  A6, F#5,  E5,  G5, F#5,  D5,  F5, B5',
                   [1/6, 1/4, 1/9, 1/6, 1/3, 1/6, 1/2, 1/2, 1/4, 1/9, 1/6, 1/3, 1/6, 1/1.25],
                   [1/6, 1/4, 1/9, 1/6, 1/3, 1/6, 1/2, 1/2, 1/4, 1/9, 1/6, 1/3, 1/6, 1/1.25])

Second_Verse = chord('B5, E5,  G5, F#5,  E5,  B6,  D6, Db6,  C6, Ab6,  C6,  B6, Bb6, Bb5,  G5,  E5',
                    [1/6, 1/4, 1/9, 1/6, 1/3, 1/6, 1/3, 1/6, 1/3, 1/6, 1/4, 1/9, 1/6, 1/3, 1/6, 1/1.25],
                    [1/6, 1/4, 1/9, 1/6, 1/3, 1/6, 1/3, 1/6, 1/3, 1/6, 1/4, 1/9, 1/6, 1/3, 1/6, 1/1.25])

Third_Verse = chord('G5,   B6,  G5,  B6,  G5,  C6,  B6, Bb6, F#5,  G5,  B6, Bb6, Bb5,  B5,  B6',
                    [1/6, 1/3, 1/6, 1/3, 1/6, 1/3, 1/6, 1/3, 1/6, 1/4, 1/9, 1/6, 1/3, 1/6, 1/1.25],
                    [1/6, 1/3, 1/6, 1/3, 1/6, 1/3, 1/6, 1/3, 1/6, 1/4, 1/9, 1/6, 1/3, 1/6, 1/1.25])

Fourth_Verse = chord(' G5,  B6,  G5,  B6,  G5,  D6, C#6,  C6, Ab6,  C6,  B6, Bb6, Bb5,  G5,  E5',
                    [1/6, 1/3, 1/6, 1/3, 1/6, 1/3, 1/6, 1/3, 1/6, 1/4, 1/9, 1/6, 1/3, 1/6, 1],
                    [1/6, 1/3, 1/6, 1/3, 1/6, 1/3, 1/6, 1/3, 1/6, 1/4, 1/9, 1/6, 1/3, 1/6, 1])

play((First_Verse + Second_Verse + Third_Verse + Fourth_Verse), bpm=120, name='Harry_Potter.mid', instrument=12, wait=True)
