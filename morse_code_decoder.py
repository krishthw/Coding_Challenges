# This is a code to decode morse code messagers. 
# In morse code message each letter is seperated by space and each word is seperated by two spaces.

# My approach : 
# will be translating letter by letter. 
# if track a code(not a space), append it to a string.
# if track a space increase the counter by one, and map the code using the dictionary.
# if the counter == 2, add a space to the decoded message.

M= { 'A':'.-', 'B':'-...',
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
    message += ' ' # extra space to add the last morse code

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

# P.S need to add a extra space initially to the encoded message as counter needs to be 1 to go to the loop which decode the message
