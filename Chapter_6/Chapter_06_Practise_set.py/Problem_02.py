
# Q2. Write a program to find out whether a student has passed or failed if it requires total of 40% and at least 33% in each subjects to pass. Assume 3 subjects and take maks as an input from the user.

sub1=int(input("Enter English marks:"))
sub2=int(input("Enter Hindi marks:"))
sub3=int(input("Enter Science marks:"))

total_percentage=(100*(sub1+sub2+sub3))/300
print(total_percentage)

if(total_percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("Pass")
else:
    print("Fail")    