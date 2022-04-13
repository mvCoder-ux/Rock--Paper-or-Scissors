import random

import time

from tabulate import tabulate


player_score = 0
computer_score = 0

print('🪨  - Rock (r)')
print('✂️  - Scissors (s)')
print('📄 - Paper (p)')
print('Y/y - Yes')
print('N/n - No')
print()
print("Rules:-")
print("Rock vs Paper → Paper wins")
print("Paper vs Scissors → Scissors wins")
print("Scissors vs Rock → Rock wins")
print()

while True: 
  
    choices = ['r', 'p', 's']

    computer_choice = random.choice(choices)
    player_choice = None

    while player_choice not in choices and player_choice != 'r' and player_choice != 'p' and player_choice != 's':
        player_choice = input('R, P or S: ').lower()
      

    if player_choice == 'r':

        if computer_choice == 'r': 
          print()
          print('Computer is thinking 🤔....')
          time.sleep(3)
          print()
          print("🖥️  Computer's Choice: 🪨 ", 'rock')
          print("🙍 Player's Choice: 🪨 ", 'rock')
          print()
          print('Draw! No one gets the point 🤝')
          print()
          svr = [["Computer's Score", "Player's Score"], [computer_score, player_score]]
          print(tabulate(svr, tablefmt = "grid"))
        
        if computer_choice == 'p':
            print()
            print('Computer is thinking 🤔....')
            time.sleep(3)
            print()
            print("🖥️  Computer's Choice: 📄", "paper")
            print("🙍 Player's Choice: 🪨 ", "rock")
            print()
            print('Computer gets the point!! 👎')
            print()
            computer_score = computer_score + 1
            rvp = [["Computer's Score", "Player's Score"], [computer_score, player_score]]
            print(tabulate(rvp, tablefmt = "grid"))
          

        if computer_choice == 's':
            print()
            print('Computer is thinking 🤔....')
            time.sleep(3)
            print()
            print("🖥️  Computer's Choice: ✂️ ", "scissors")
            print("🙍 Player's Choice: 🪨 ", "rock")
            print()
            print('You get the point!! 👍')
            print()
            player_score = player_score + 1
            rvs = [["Computer's Score", "Player's Score"], [computer_score, player_score]]
            print(tabulate(rvs, tablefmt = "grid"))
          

    elif player_choice == 'p':

        if computer_choice == 'p': 
          print()
          print('Computer is thinking 🤔....')
          time.sleep(3)
          print()
          print("🖥️  Computer's Choice: 📄 ", 'paper')
          print("🙍 Player's Choice: 📄 ", 'paper')
          print()
          print('Draw! No one gets the point 🤝')
          print()
          svr = [["Computer's Score", "Player's Score"], [computer_score, player_score]]
          print(tabulate(svr, tablefmt = "grid"))
      
        if computer_choice == 'r':
            print()
            print('Computer is thinking 🤔....')
            time.sleep(3)
            print()
            print("🖥️  Computer's Choice: 🪨 ", 'rock')
            print("🙍 Player's Choice: 📄", "paper")
            print()
            print('You get the point!! 👍')
            print()
            player_score = player_score + 1
            pvr = [["Computer's Score", "Player's Score"], [computer_score, player_score]]
            print(tabulate(pvr, tablefmt = "grid"))
          

        if computer_choice == 's':
            print()
            print('Computer is thinking 🤔....')
            time.sleep(3)
            print()
            print("🖥️  Computer's Choice: ✂️ ", 'scissors')
            print("🙍 Player's Choice: 📄", "paper")
            print()
            print('Computer gets the point!! 👎')
            print()
            computer_score = computer_score + 1
            pvs = [["Computer's Score", "Player's Score"], [computer_score, player_score]]
            print(tabulate(pvs, tablefmt = "grid"))
          

    elif player_choice == 's':

        if computer_choice == 's': 
          print()
          print('Computer is thinking 🤔....')
          time.sleep(3)
          print()
          print("🖥️  Computer's Choice: ✂️ ", 'scissors')
          print("🙍 Player's Choice: ✂️ ", 'scissors')
          print()
          print('Draw! No one gets the point 🤝')
          print()
          svr = [["Computer's Score", "Player's Score"], [computer_score, player_score]]
          print(tabulate(svr, tablefmt = "grid"))
          
      
        if computer_choice == 'r':
            print()
            print('Computer is thinking 🤔....')
            time.sleep(3)
            print()
            print("🖥️  Computer's Choice: 🪨 ", 'rock')
            print("🙍 Player's Choice: ✂️ ", 'scissors')
            print()
            print('Computer gets the point!! 👎')
            print()
            computer_score = computer_score + 1
            svr = [["Computer's Score", "Player's Score"], [computer_score, player_score]]
            print(tabulate(svr, tablefmt = "grid"))
          

        if computer_choice == 'p':
            print()
            print('Computer is thinking 🤔....')
            time.sleep(3)
            print()
            print("🖥️  Computer's Choice: 📄", 'paper')
            print("🙍 Player's Choice: ✂️ ", 'scissors')
            print()
            print('You get the point!! 👍')
            print()
            player_score = player_score + 1
            svp = [["Computer's Score", "Player's Score"], [computer_score, player_score]]
            print(tabulate(svp, tablefmt = "grid"))
          
    print()
    play_again = input('Want to play again? (Type y/n or Y/N): ').lower()
    print()
      
    if play_again != 'y':
      if player_score > computer_score: 
        print()
        table = [["Computer's Score", "Player's Score"], [computer_score, player_score]]
        print(tabulate(table, tablefmt = "grid"))
        print()
        print('You win the match!! Hurray! 👍👍👍')
        print()

      elif player_score == computer_score: 
        print()
        table = [["Computer's Score", "Player's Score"], [computer_score, player_score]]
        print(tabulate(table, tablefmt = "grid"))
        print()
        print('The match is a draw!! No one wins! 🤝🤝🤝')
        print()

      else:
        print()
        table = [["Computer's Score", "Player's Score"], [computer_score, player_score]]
        print(tabulate(table, tablefmt = "grid"))
        print()
        print('You lose this match!! 👎👎👎')
        print()
      print('Bye!! 👋')
      break