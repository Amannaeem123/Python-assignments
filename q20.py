# Sum of natural numbers
num = int(input("Enter your number plz: "))
# if-else statement
if num < 0:
    print("Enter positive number ")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
    print("The sum of natural numbers is " , sum)
