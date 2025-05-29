# Create a python function to calculate factorial of a number using recursion.
def factorial(n):
   
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
    
num=int(input(" \nEnter number to find factorial :"))
if num<0:
   print("Factorial is not defined in negative numbers")
else:
    result=factorial(num)
    print(f"The factorial {num} is {result}")
