# Given two non-negative integers, num1 and num2 represented as string, 
# return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
# You must also not convert the inputs to integers directly.

# my approach
# make both lists lengths equal by adding leading zeros
# initial carry over is set to 0
# convert each values of list indices to integers and add them, take carry to the next and insert result to a new list. 
# if carry is !=0 at the end, insert it as well
# convert list to a string

def AddTwoNumbers(num1,num2):
    l1 = len(num1)
    l2 = len(num2)
    for i in range(max(len(num1),len(num2))):
        if len(num1)> len(num2):
            num2 = "0" + num2
        elif len(num2)> len(num1):
            num1 = "0" +num1
    carry = 0
    newlist = []
    for i in range(len(list(num1))-1,-1,-1):
        val = int(list(num1)[i]) + int(list(num2)[i]) + carry
        carry = val // 10
        digit = val % 10
        newlist.insert(0,digit)
    if carry != 0:
        newlist.insert(0,carry)
    
    newstring = ''.join(str(x) for x in newlist)

    return(newstring)



print(AddTwoNumbers('9872','3'))
