def hcf(number1,number2):# here the function  take two argument.
    if number1>number2:# if n1 is greater than n2
        small=number2
    else:
        small=number1
    for i in range(1,small+1):
        if number1%i==0 and number2%i==0:
            commmonfactor=i
    return commmonfactor
num1=int(input("Enter the first number :"));
num2=int(input("Enter the second number"));

print(hcf(num1,num2))