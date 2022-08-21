# if a number of digit n is the same as sum of nth order of each digit, it is called an Armstrong number 
# Example: 153 is an Armstrong number as 153 = 1^3 + 5^3 + 3^3

# Let's write a code to identify Armstrong numbers.

# my approach : 
# I will be taking each digit from left to right, get the nth order and add to the current sum.

import sys

for line in sys.stdin:
    order = len(str(line.strip())) 
    number = int(line)
    sum = 0
    temp = number
    while temp >0:
        last_digit = temp % 10
        sum += last_digit**order
        temp //= 10
    if sum == number:
        print(number,'is an Armstrong Number') 
    else:
        print(number,'is not an Armstrong Number') 

    exit()

# P.S
# sys.stdin always comes with \n so it has an extra character. therefore, we need to use strip() method