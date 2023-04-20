"""
Task:15:Given a number n, write a python program to make and print the list of Fibonacci series up to n.
Input : n=7
Hint : first 7 numbers in the series
Expected output :
First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13

"""

n = int(input("Enter a number: "))
fibonacci = [0, 1]
while fibonacci[-1] + fibonacci[-2] <= n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print("First few Fibonacci numbers are:", end=" ")
for num in fibonacci:
    print(num, end=" ")
