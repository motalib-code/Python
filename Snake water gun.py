import random

print('Welcome to Snake Water Gun Game!')
n = int(input('Enter number of rounds: '))

# Choices: Snake (s), Water (w), Gun (g)
options = ['s', 'w', 'g']
rounds = 1
comp_win = 0
user_win = 0

while rounds <= n:
    print(f"Round {rounds}:")
    print("Snake - 's', Water - 'w', Gun - 'g'")

    player = input("Choose your option: ").lower()
    if player not in options:
        print("Invalid input, try again.\n")
        continue

    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    # Game logic
    if computer == player:
        print("This round is a draw!\n")
    elif (computer == 's' and player == 'w') or \
         (computer == 'w' and player == 'g') or \
         (computer == 'g' and player == 's'):
        print("Computer wins this round!\n")
        comp_win += 1
    else:
        print("You win this round!\n")
        user_win += 1

    rounds += 1

print("Game Over!")
print(f"Final Score -> You: {user_win} | Computer: {comp_win}")
if user_win > comp_win:
    print("Congratulations! You are the overall winner!")
elif comp_win > user_win:
    print("Computer wins the game. Better luck next time!")
else:
    print("The game is a draw!")
