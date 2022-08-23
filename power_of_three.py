# this code identify number which are power of three. i.e n is a power of 3 if n = 3^x for any integer x
# n/3*3*3*...... =1

# my approach
# 0 is not power of three.
# while n != 1 , get the mod of the number and if it is not equal to zero (i.e not divisible by 3) --> not a power of 3
# keep on doing it for n = n//3
# 33%3 = 0, 11%3 = 2 --> not a power 3
# 27%3 = 0, 9%3 = 3, 3%3 = 0 --> power of 3

def PowerThree(n):
    if n == 0:
        return False
    while n != 1:
        if (n % 3) !=0:
            return False
        n = n // 3
    return True

