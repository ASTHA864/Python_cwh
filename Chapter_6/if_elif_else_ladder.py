
# if_elif_else_ladder
user_input= int(input("Enter your age:"))
if(user_input>18):
    print("above 18")
elif(user_input==18):   
    print("equal to 18")
elif(user_input<0):
    print("Invalid age")    
elif(user_input==0):
    print("your age is 0")    
else:
    print("below 18")    

print("End of Program")