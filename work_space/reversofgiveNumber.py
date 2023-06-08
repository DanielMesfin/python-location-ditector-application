def reverse(number):
    rember=0
    while number>0:
        rember=number%10

        number=number//10
    return rember
print(reverse(78))