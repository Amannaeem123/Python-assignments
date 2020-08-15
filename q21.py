#Python program to display the fibonacci sequence

# FUNCTION
def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))
#take the value of n sequence
n_seq = 10
#Check the value is valid
if n_seq <= 0:
    print("Enter the positive integer: ")
else:
    print("Fibonacci sequence: ")
    for i in range(n_seq):
#print the finonacci sequence
        print(fibo(i))
