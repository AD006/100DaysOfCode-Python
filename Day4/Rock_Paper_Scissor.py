# Rock-Paper-Scissor
rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

game_images = [rock, paper, scissor]
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor.\n"))
if choice>=3 or choice<0:
  print("You typed an invalid number, you lose!")
else:
  print(game_images[choice])

  computer_choice=random.randint(0,2)
  print(f"Computer chose:")
  print(game_images[computer_choice])


  if choice==0 and computer_choice==2:
    print("You win!")
  elif computer_choice==0 and choice==2:
    print("You lose!")
  elif computer_choice>choice:
    print("You lose!")
  elif choice>computer_choice:
    print("You win!")
  elif computer_choice==choice:
    print("It's a draw")
  
