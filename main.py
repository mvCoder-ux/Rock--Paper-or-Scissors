import random
import time

player_score = 0
computer_score = 0

while True: 
  
    choices = ['rock', 'paper', 'scissors']

    computer_choice = random.choice(choices)
    player_choice = None

    while player_choice not in choices:
        player_choice = input('Rock, Paper or Scissors: ').lower()
    
    if player_choice == computer_choice:
        print()
        print('Computer is thinking....')
        time.sleep(3)
        print()
        print("🖥️  Computer's Choice: ", computer_choice)
        print("🙍 Player's Choice: ", player_choice)
        print()
        print('Draw! No one gets the point 🤝')
        print()
        print("🖥️  Computer's Score: ", computer_score)
        print("🙍 Player's Score: ", player_score)
      

    elif player_choice == 'rock':
        if computer_choice == 'paper':
            print()
            print('Computer is thinking....')
            time.sleep(3)
            print()
            print("🖥️  Computer's Choice: 📄", computer_choice)
            print("🙍 Player's Choice: 🪨 ", player_choice)
            print()
            print('Computer gets the point!! 👎')
            print()
            computer_score = computer_score + 1
            print("🖥️  Computer's Score: ", computer_score)
            print("🙍 Player's Score: ", player_score)
          

        if computer_choice == 'scissors':
            print()
            print('Computer is thinking....')
            time.sleep(3)
            print()
            print("🖥️  Computer's Choice: ✂️ ", computer_choice)
            print("🙍 Player's Choice: 🪨 ", player_choice)
            print()
            print('You get the point!! 👍')
            print()
            player_score = player_score + 1
            print("🙍 Player's Score: ", player_score)
            print("🖥️  Computer's Score: ", computer_score)
          

    elif player_choice == 'paper':
      
        if computer_choice == 'rock':
            print()
            print('Computer is thinking....')
            time.sleep(3)
            print()
            print("🖥️  Computer's Choice: 🪨 ", computer_choice)
            print("🙍 Player's Choice: 📄", player_choice)
            print()
            print('You get the point!! 👍')
            print()
            player_score = player_score + 1
            print("🙍 Player's Score: ", player_score)
            print("🖥️  Computer's Score: ", computer_score)
          

        if computer_choice == 'scissors':
            print()
            print('Computer is thinking....')
            time.sleep(3)
            print()
            print("🖥️  Computer's Choice: ✂️ ", computer_choice)
            print("🙍 Player's Choice: 📄", player_choice)
            print()          
            print('Computer gets the point!! 👎')
            print()
            computer_score = computer_score + 1
            print("🖥️  Computer's Score: ", computer_score)
            print("🙍 Player's Score: ", player_score)
          

    elif player_choice == 'scissors':
      
        if computer_choice == 'rock':
            print()
            print('Computer is thinking....')
            time.sleep(3)
            print()
            print("🖥️  Computer's Choice: 🪨 ", computer_choice)
            print("🙍 Player's Choice: ✂️ ", player_choice)
            print()
            print('Computer gets the point!! 👎')
            print()
            computer_score = computer_score + 1
            print("🖥️  Computer's Score: ", computer_score)
            print("🙍 Player's Score: ", player_score)
          

        if computer_choice == 'paper':
            print()
            print('Computer is thinking....')
            time.sleep(3)
            print()
            print("🖥️  Computer's Choice: 📄", computer_choice)
            print("🙍 Player's Choice: ✂️ ", player_choice)
            print()
            print('You get the point!! 👍')
            print()
            player_score = player_score + 1
            print("🙍 Player's Score: ", player_score)
            print("🖥️  Computer's Score: ", computer_score)
          
    print()
    play_again = input('Want to play again? (Yes/No): ').lower()

    if play_again != 'yes':
      if player_score > computer_score: 
        print()
        print('You win the match!! Hurray! 👍👍👍')
        print()
        print("🙍 Player's Score: ", player_score)
        print("🖥️  Computer's Score: ", computer_score)
        print()

      elif player_score == computer_score: 
        print()
        print('The match is a draw!! No one wins! 🤝🤝🤝')
        print()
        print("🙍 Player's Score: ", player_score)
        print("🖥️  Computer's Score: ", computer_score)
        print()

      else:
        print()
        print('You lose this match!! 👎👎👎')
        print()
        print("🙍 Player's Score: ", player_score)
        print("🖥️  Computer's Score: ", computer_score)
        print()
      print('Bye!! 👋')
      break