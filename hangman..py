# Write your code here
import random

word2 = random.choice(['python', 'java', 'kotlin', 'javascript'])
word3 = word2
word3 = list(word3)
for i in range(len(word2)):
        word3[i] = '-'

word3 = ''.join([str(elem) for elem in word3])

print("H A N G M A N")
input1 = []
i = 0
while i < 8:
    word3 = ''.join([str(elem) for elem in word3])
    print(f'\n{word3}', end = ' ')
    if '-' in word3:
        word = input('\nInput a letter: ')
        
        if len(word) != 1 or word == ' ':
            print('You should input a single letter')
        elif word.isalpha() and word.isupper():
            print('It is not an ASCII lowercase letter')
        elif not word.isalpha():
            print('It is not an ASCII lowercase letter')
        else:
            if word not in input1:
                if word not in word3:
                    input1.extend(word)
                    word2 = list(word2)
                    word3 = list(word3)
            #**************************************************************************#
                    if word in word2:
                        for j in range(len(word2)):
                            if word2[j] == word:
                                word3[j] = word
                        word3 = ''.join([str(elem) for elem in word3])
                    else:
                        print('No such letter in the word')
                        i +=1
                else:
                    print('You already typed this letter')
                    i += 1
            else:
                print('You already typed this letter')
    else:
        break

        
word2 = ''.join([str(elem) for elem in word2])
if word3 == word2:
    print("""\nYou guessed the word!
You survived!""")
else:
    print('You are hanged!')
