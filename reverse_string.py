print('Welcome to a string reversing program, This program will take whatever sentence and or word, and reverse it')
print('Start by typing in a sentence or word')
"""
"""
sentence = input()
SentenceLength = len(sentence)
count = SentenceLength
SentenceReversed = ""
"""
"""
while count > 0:
    ReversedSentence = sentence[count-1:count]
    SentenceReversed = SentenceReversed + ReversedSentence
    count = count - 1
"""
"""
print ("Your sentence reversed is: " + SentenceReversed)
