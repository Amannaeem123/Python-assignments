# Multiplication table

# To take input from user
number = int(input("Enter your table number: "))
#Iterate 10 times
for i in range(1,11):
    print(number, "x" , i , "=" , number*i)