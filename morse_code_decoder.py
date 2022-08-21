# This is a code to decode morse code messagers. 
# In morse code message each letter is seperated by space and each word is seperated by two spaces.
M = M= { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

import sys
for line in sys.stdin:
    message = str(line.strip())
    message += ' ' # extra space to add the last mprse code

    decode ='' # string to output the decoded message
    text =''   
    for letter in message:
        if letter != ' ':
            counter = 0 # track space
            text += letter # save morse code
        else:
            counter += 1 # iterate counter for spaces
            if counter == 2:
                decode += ' ' # add a space
            else:
                decode += list(M.keys())[list(M.values()).index(text)]
                text ='' # set text to blank string
    print(decode)

