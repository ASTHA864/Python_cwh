# Q8. Write a program to print star pattern.
#    *
#    * *
#    * * *
#  for n=3

n=int(input("Enter number:"))
for i in range(1,n+1):
    print(" *"* i, end="")
    print("")