#!/usr/bin/env python
# coding: utf-8

# In[52]:


# Q1) make a simple calculator program in python 3 ?
#  1) using input function
#  2) using elif statement

def add(x, y):  
   
   return x + y 
def subtract(x, y): 
   return x - y 
def multiply(x, y): 
   
   return x * y 
def divide(x, y): 
   return x / y  
# take input from the user  
print("Select operation.")  
print("1.Add")  
print("2.Subtract")  
print("3.Multiply")  
print("4.Divide")  
  
choice = input("Enter choice(1/2/3/4):")  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
  
if choice == '1':  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choice == '2':  
   print(num1,"-",num2,"=", subtract(num1,num2))  
  
elif choice == '3':  
   print(num1,"*",num2,"=", multiply(num1,num2))  
elif choice == '4':  
   print(num1,"/",num2,"=", divide(num1,num2))  
else:  
   print("Invalid input")  


# In[51]:


# Q2) make a python program to take in the marks of five subjects and display the grade 
# 1) using the input function
# 2) using elif statement
# 3) using logical operator
english = float(input(" Please enter English Marks: "))
math = float(input(" Please enter Math marks: "))
computers = float(input(" Please enter Computer Marks: "))
Science = float(input(" Please enter Physics Marks: "))
physics = float(input(" Please enter Chemistry Marks: "))

total = english + math + computers + Science + physics
percentage = (total / 500) * 100

print("Total Marks = %.2f"  %total)
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
    


# In[ ]:





# In[ ]:




