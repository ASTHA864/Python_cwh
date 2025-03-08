#Q2. Write a program to find remainder.

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
type_of_num1=type(num1)
type_of_num2=type(num2)
print("Type of num1 is:",type_of_num1)
print("Type of num2 is:",type_of_num2)
remainder=num1%num2
print("Remainder is:",remainder)