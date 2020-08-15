#Python program to find the the factorial of a number provided by the user

#To take the input from the user
value = int(input("Enter a number: "))
# declare the value
factorial = int(input("Enter a number: "))
# if_else statements
if value < 0:
    print("Sorry sir, Factorial does not exist")
elif value == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1 , value + 1):
        factorial = factorial*i
    print("The factorial of" , value , "is" , factorial)

