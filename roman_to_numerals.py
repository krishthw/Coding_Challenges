# This code converts roman numbers to numerals.
import sys

RTN = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
for line in sys.stdin:
    roman = str(line.strip()) 
    sum   = 0 

    # iterate from left to right
    for i in range(len(roman)-1,-1,-1): 
        num = RTN[roman[i]]
        if 3*num < sum:   # if the 3*num (or 4*num) is lessthan sum, we have to subtract (for IV,IX, XL ..etc)
            sum = sum - num
        else:
            sum = sum + num
    print(sum)


