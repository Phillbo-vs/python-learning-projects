import random

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

game1 = ["rock", "paper", "scissors"]
game2 = [
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']


player_choice = int(input('Choose "0" Rock, "1" Paper or "2" Scissors\n').lower())
if player_choice >= 0 and player_choice <= 2:
    print(game2[player_choice])
    print(game1[player_choice])

print("\nCOMPUTER CHOOSE:\n")

computer = (random.randint(0, 2))
computer_choice = game1[computer]
computer_drawning = game2[computer]
print(computer_choice)
print(computer_drawning)

if player_choice >=3 or player_choice <0:
    print("Invalid Choice!")
elif player_choice == computer:
    print("\nit\'s a Draw!\n")
elif player_choice == 1 and computer == 0:
    print("\nYou win!\n")
elif player_choice == 2 and computer == 1:
    print("\nYou win!\n")
elif player_choice == 0 and computer == 2:
    print("\nYou win!\n")
else:
    print("Computer win!\n")