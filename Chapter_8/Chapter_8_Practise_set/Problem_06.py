# Q6. Write a program using functions to convert inches to cms.
#  1inches=2.54cm

def inches_to_cms(n):
    print(f"{n*2.54} cm")

n=int(input("Enter number to convert into cm:"))
inches_to_cms(n)