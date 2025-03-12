# Q8. Write a program to print star pattern.
#   * 
#   * *
#   * * *
#   * * * *
#   * * * * *
#  for n=5

n=int(input("Enter number:"))
for i in range(n):
        print("*"*  i , end="")
        # print("*" * i, end="")
        print("*")
     