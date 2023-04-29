rock = '''
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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
ans = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")) 
rand = random.randint(0,2)

if ans == 0 and rand == 2:
  print(rock)
  print("Computer chose: ",scissors)
  print("You win")
elif ans == 2 and rand == 0:
  print(scissors)
  print("Computer chose: ",rock)
  print("You lose")
elif ans == 1 and rand == 0:
  print(paper)
  print("Computer chose: ",rock)
  print("You win")
elif ans == 0 and rand == 1:
  print(rock)
  print("Computer chose: ",paper)
  print("You lose")
elif ans == 2 and rand == 1:
  print(scissors)
  print("Computer chose: ",paper)
  print("You win")
elif ans == 1 and rand == 2:
  print(paper)
  print("Computer chose: ",scissors)
  print("You lose")
elif ans == rand:
  if ans == 0 and rand == 0:
     print(rock)
     print("Computer chose: ",rock)
     print("Draw")
  elif ans ==  1 and rand == 1:
     print(paper)
     print("Computer chose: ",paper)
     print("Draw")
  elif ans == 2 and rand == 2:
     print(scissors)
     print("Computer chose: ",scissors)
     print("Draw")
