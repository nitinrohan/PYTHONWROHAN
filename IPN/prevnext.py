# Write a program that reads an integer number and prints its previous and next numbers. See the examples below for the exact format your answers should take. There shouldn't be a space before the period.
# Remember that you can convert the numbers to strings using the function str.

n=int(input("give a number : "))
prev=str(n-1)
nxt=str(n+1)
print("The next number for the given number",str(n),"is",nxt)
print("The previous number for the given number",str(n),"is",prev)