
'''
Snake => 1
Water => -1
Gun =>  0

# Generate random number
import random

random_number = random.choice([-1, 0, 1])
print(random_number)

'''
import random
computer = random.choice([-1, 0, 1])
# computer=-1
youDict={
    "s" : 1,
    "w" : -1,
    "g" : 0
}
reverseDict={ 1 : "Snake",
         -1 :  "Water",
          0 : "Gun"
          }

print(youDict)
you_str= input("Enter your choice:")


you=youDict[you_str]
print(f"Your choice: {reverseDict[you]}")
print(f"Computer choice {reverseDict[computer]}")




if(computer == you):
      print("Draw") 

else:   
    if(computer == -1 and you ==0):
        print("You Loose") 
    elif(computer == -1 and you ==1):
        print("You win") 
    elif(computer == 0 and you ==1):
        print("Computer win")  
    elif(computer == 1 and you ==-1):
        print("Computer win") 
    elif(computer == -1 and you ==0):
        print("Computer win")           
    elif(computer == 0 and you == -1):
        print("You win")
    elif(computer == 1 and you ==0):
        print("You win")      
         
    else:
        print("Something went wrong")     