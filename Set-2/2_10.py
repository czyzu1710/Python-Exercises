!/usr/bin/python
#-*- coding: utf-8
def countWords(line):
    x = len(line.split())
    print("You typed in ", x, "words. ")
    if x <= 10:
        print("Well done.")
    elif x <= 20:
        print("You are truly a poet.")
    elif x <= 30: 
        print("Damn. You were suppose to write few words, not an elaboration")
    else:
        print("'Ctrl+C', 'Ctrl+V' or You really have the nerve to write so much?!")


line = input("Type a bunch of words: " )

countWords(line)

