# Q8. Write a  function to print multiplication table of given number.

def table(n):
    for i in range(1,11):
       
        print(f"{n} * {i} = {n*i}")
n=int(input("Enter number:"))

table(n)