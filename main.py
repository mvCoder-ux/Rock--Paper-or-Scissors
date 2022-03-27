import random
import time



while True: 
    choices = ['rock', 'paper', 'scissors']

    computer_choice = random.choice(choices)
    player_choice = None

    while player_choice not in choices:
        player_choice = input('Rock, Paper or Scissors: ').lower()
    
    if player_choice == computer_choice:
        print('Computer is thinking....')
        time.sleep(3)
        print("🖥️  Computer's Choice: ", computer_choice)
        print("🙍 Player's Choice: ", player_choice)
        print()
        print('Draw! No one wins 🤝')

    elif player_choice == 'rock':
        if computer_choice == 'paper':
            print('Computer is thinking....')
            time.sleep(3)
            print("🖥️  Computer's Choice: 📄", computer_choice)
            print("🙍 Player's Choice: 🪨 ", player_choice)
            print()
            print('You lose!! 👎')

        if computer_choice == 'scissors':
            print('Computer is thinking....')
            time.sleep(3)
            print("🖥️  Computer's Choice: ✂️ ", computer_choice)
            print("🙍 Player's Choice: 🪨 ", player_choice)
            print()
            print('You win!! 👍')

    elif player_choice == 'paper':
        if computer_choice == 'rock':
            print('Computer is thinking....')
            time.sleep(3)
            print("🖥️  Computer's Choice: 🪨 ", computer_choice)
            print("🙍 Player's Choice: 📄", player_choice)
            print('You win!! 👍')

        if computer_choice == 'scissors':
            print('Computer is thinking....')
            time.sleep(3)
            print("🖥️  Computer's Choice: ✂️ ", computer_choice)
            print("🙍 Player's Choice: 📄", player_choice)
            print()          
            print('You lose!! 👎')

    elif player_choice == 'scissors':
        if computer_choice == 'rock':
            print('Computer is thinking....')
            time.sleep(3)
            print("🖥️  Computer's Choice: 🪨 ", computer_choice)
            print("🙍 Player's Choice: ✂️ ", player_choice)
            print()
            print('You lose!! 👎')

        if computer_choice == 'paper':
            print('Computer is thinking....')
            time.sleep(3)
            print("🖥️  Computer's Choice: 📄", computer_choice)
            print("🙍 Player's Choice: ✂️ ", player_choice)
            print()
            print('You win!! 👍')
    print()
    play_again = input('Want to play again? (Yes/No): ').lower()

    if play_again != 'yes':
      print('Bye!! 👋')
      break