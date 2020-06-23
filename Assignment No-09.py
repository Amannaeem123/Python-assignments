
# Q1) Make a simple calculator program in python 3 ?

val1=int(input('enter the digit='))
val2=int(input('enter the digit='))
op=input('enter the sign operator=')

if op=='+':
    print('sum =',val1+val2)
elif op=='-':
    print('sub =',val1-val2)
elif op=='*':
    print('mul =',val1*val2)
elif op=='/':
    print('div =',val1/val2)
elif op=='**':
    print('pow =',val1**val2)
else: 
          print('error')

# Q2) Make a python program to take in the marks of five subjects and display the grade ?
# 1) Using the input function
# 2) Using elif statement
# 3) Using logical operator

sub1 = float(input(" Please enter Enhglish Marks: "))
sub2 = float(input(" Please enter Math marks: "))
sub3 = float(input(" Please enter Computer Marks: "))
sub4 = float(input(" Please enter Physics Marks: "))
sub5 = float(input(" Please enter Chemistry Marks: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

print("Total Marks = " , total)
print("Marks Percentage = %.2f"  %percentage)

if(percentage >= 90):
    print("A+ Grade")
elif(percentage >= 80):
    print("A+ Grade")
elif(percentage >= 70):
    print("A Grade")
elif(percentage >= 60):
    print("B Grade")
elif(percentage >= 50):
    print("C Grade")
elif(percentage >= 40):
    print("D Grade")
else:
    print("FAIL")












