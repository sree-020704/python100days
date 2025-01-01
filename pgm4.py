import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images=[rock,Paper,Scissors]
user_choice=int(input("What do you choose? rock-0 paper-1 scissor-2:\n"))
if  user_choice>=0 and  user_choice<=2:
    print(game_images[user_choice])
computer_choice=random.randint(0,2)
print("computer_choice")
print(game_images[user_choice])
if user_choice >3 or user_choice <0:
    print("You entered invalid number,You lose!")
elif user_choice==0 and computer_choice==2:
    print("You wins!")
elif computer_choice==0 and user_choice==2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice==user_choice:
    print("It's a draw")    
else:
    print("You typed a invalid number,you lose!")    
