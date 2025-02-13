import random
from colorama import Fore, Style

# Possible choices
options = ["rock", "paper", "scissors"]

# Fun responses
win_responses = ["Nice! You're on fire! 🔥", "You're the champ! 🏆", "No one can stop you! 😎"]
lose_responses = ["Better luck next time! 🍀", "Oof! That was close! 😬", "You'll get 'em next time! 😉"]
tie_responses = ["It's a tie! Try again! 🤝", "Deadlock! Play again. 😆"]

# Function to get the winner
def get_winner(player1, player2):
    if player1 == player2:
        return "tie"
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "scissors" and player2 == "paper"):
        return "player1"
    else:
        return "player2"

# Main game function
def play_game():
    print(Fore.CYAN + "Welcome to Rock, Paper, Scissors! ✌️" + Style.RESET_ALL)
    mode = input("Choose mode: 'single' for vs Computer, 'multi' for 2-player: ").strip().lower()
    
    if mode not in ["single", "multi"]:
        print(Fore.RED + "Invalid mode! Restart the game and choose 'single' or 'multi'." + Style.RESET_ALL)
        return

    rounds_to_win = int(input("Enter how many rounds to win (e.g. 3): "))
    player1_score, player2_score = 0, 0

    while player1_score < rounds_to_win and player2_score < rounds_to_win:
        if mode == "single":
            player1_choice = input(Fore.YELLOW + "Enter rock, paper, or scissors: " + Style.RESET_ALL).lower()
            player2_choice = random.choice(options)
            print(Fore.MAGENTA + f"Computer chose: {player2_choice}" + Style.RESET_ALL)
        else:
            player1_choice = input(Fore.BLUE + "Player 1, enter rock, paper, or scissors: " + Style.RESET_ALL).lower()
            player2_choice = input(Fore.GREEN + "Player 2, enter rock, paper, or scissors: " + Style.RESET_ALL).lower()
        
        if player1_choice not in options or player2_choice not in options:
            print(Fore.RED + "Invalid choice! Try again." + Style.RESET_ALL)
            continue

        winner = get_winner(player1_choice, player2_choice)

        if winner == "tie":
            print(Fore.YELLOW + random.choice(tie_responses) + Style.RESET_ALL)
        elif winner == "player1":
            print(Fore.GREEN + random.choice(win_responses) + Style.RESET_ALL)
            player1_score += 1
        else:
            print(Fore.RED + random.choice(lose_responses) + Style.RESET_ALL)
            player2_score += 1
        
        print(Fore.CYAN + f"Score -> Player 1: {player1_score} | {'Computer' if mode == 'single' else 'Player 2'}: {player2_score}" + Style.RESET_ALL)
        print("-" * 40)

    if player1_score > player2_score:
        print(Fore.GREEN + "🎉 Player 1 wins the game! 🎉" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"🎉 {'Computer' if mode == 'single' else 'Player 2'} wins the game! 🎉" + Style.RESET_ALL)

    print(Fore.CYAN + "Thanks for playing! 👋" + Style.RESET_ALL)

# Run the game
play_game()
