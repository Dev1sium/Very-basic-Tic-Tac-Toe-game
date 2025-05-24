##Importing modules
import random
import time

##Global Variables
start_game = " " ##Tracks if the user wants to start the game
again_game = " " ##Tracks if the user wants to start another game
player_move = " " ##Stores players move
bot_move = " " ##Stores computers move
select_move = 1 ##Controls if player does their move
move_list = ["rock", "paper", "scissors"] ##Computer move list
round_player = 0 ##Stores rounds won by player
round_bot = 0 ##Stores rounds won by computer
round_score = (f"{round_player}-{round_bot}") ##Current round score
games_player_win = 0 ##Stores games won by player
games_bot_win = 0 ##Stores games won by computer
game_score = (f"{games_player_win}-{games_bot_win}") ##Current game score
total_rounds_player = 0 ##Stores total rounds won by player
total_rounds_bot = 0 ##Stores total rounds won by computer
total_games_player = 0 ##Stores total games won by player
total_games_bot = 0 ##Stores total games won by computer
total_games = 0 ##Stores total games played
total_ties = 0 ##Stores total ties

##Initiates the start of the game - If y, starts - If n, exits
def start_game():
    global total_games
    while True:
        user_input = input("Would you like to start the game? (y/n): ").lower()
        if user_input == "y":
            total_games = total_games + 1
            print()
            rounds()
            break
        elif user_input == "n":
            quit()
        else:
            print("Invalid input")
            print()

##Initiates the start of another game - If y, starts - If n, shows summary, exits
def play_again():
    global again_game, total_games
    while again_game != "y":
        again_game = input("Would you like to play again? (y/n): ").lower()
        if again_game == "n":
            print("**Game Summary**")
            time.sleep(1)
            print(f"Games Played: {total_games}")
            time.sleep(1)
            print(f"You Won {total_games_player} Game(s)")
            time.sleep(1)
            print(f"You Won {total_rounds_player} Round(s)")
            time.sleep(1)
            print(f"Computer Won {total_games_bot} Game(s)")
            time.sleep(1)
            print(f"Computer Won {total_rounds_bot} Round(s)")
            time.sleep(1)
            print(f"There were {total_ties} Tie(s)")
            print()
            for i in range (3, 0, -1):
                time.sleep(1)
                print("Game quitting in", i)
            time.sleep(1)
            print("Game quitting...")
            quit()
        elif again_game == "y":
            total_games = total_games + 1
            print()
            rounds()
        else:
            print("Invalid input")
            print()
            again_game = input(" ")

##Logic behind the player winning the round/game via scores
def player_round_win():
    global select_move, games_player_win, round_player, round_bot, player_move, bot_move, round_score, game_score, total_rounds_player, total_games_player
    print()
    print(f"You picked {player_move.upper()}")
    time.sleep(0.5)
    print(f"Computer picked {bot_move.upper()}")
    time.sleep(0.5)
    print("You won this round!")
    round_player = round_player + 1
    total_rounds_player = total_rounds_player + 1
    select_move = 1
    round_score = (f"{round_player}-{round_bot}")
    print(f"The round score is: {round_score} (Player-Computer)")
    print()
    if round_player == 2:
        games_player_win = games_player_win + 1
        total_games_player = total_games_player + 1
        round_player = 0
        round_bot = 0
        time.sleep(0.5)
        print("You won this game")
        game_score = (f"{games_player_win}-{games_bot_win}")
        time.sleep(0.5)
        print(f"The game score is: {game_score} (Player-Computer)")
        print()
        time.sleep(1)
        play_again()

##Logic behind the computer winning the round/game via scores
def bot_round_win():
    global select_move, games_bot_win, round_player, round_bot, player_move, bot_move, round_score, game_score, total_rounds_bot, total_games_bot
    print()
    print(f"You picked {player_move.upper()}")
    time.sleep(0.5)
    print(f"Computer picked {bot_move.upper()}")
    time.sleep(0.5)
    print("Computer won this round!")
    round_bot = round_bot + 1
    total_rounds_bot = total_rounds_bot + 1
    select_move = 1
    round_score = (f"{round_player}-{round_bot}")
    print(f"The round score is: {round_score} (Player-Computer)")
    print()
    if round_bot == 2:
        games_bot_win = games_bot_win + 1
        total_games_bot = total_games_bot + 1
        round_player = 0
        round_bot = 0
        time.sleep(0.5)
        print("Computer won this game")
        game_score = (f"{games_player_win}-{games_bot_win}")
        time.sleep(0.5)
        print(f"The game score is: {game_score} (Player-Computer)")
        print()
        time.sleep(1)
        play_again()

##Logic behind ties the via scores
def tie_round():
    global select_move, total_ties, player_move, bot_move
    print()
    print(f"You picked {player_move.upper()}")
    time.sleep(0.5)
    print(f"Computer picked {bot_move.upper()}")
    time.sleep(0.5)
    print("This round is a tie!")
    print(f"The round score is: {round_score} (Player-Computer)")
    print()
    time.sleep(1)
    total_ties = total_ties + 1
    select_move = 1

##Logic behind the round - Asks player for move then randomly generates computer move
def rounds():
    global select_move, player_move, bot_move
    while select_move == 1:
        player_move = input("Enter Rock/Paper/Scissors: ")
        if player_move.lower() == "rock":
            select_move = 2
            while select_move == 2:
                bot_move = random.choice(move_list)
                select_move = 0
                if bot_move == "paper":
                    bot_round_win()
                elif bot_move == "scissors":
                    player_round_win()
                else:
                    tie_round()
        elif player_move.lower() == "paper":
            select_move = 2
            while select_move == 2:
                bot_move = random.choice(move_list)
                select_move = 0
                if bot_move == "scissors":
                    bot_round_win()
                elif bot_move == "rock":
                    player_round_win()
                else:
                    tie_round()
        elif player_move.lower() == "scissors":
            select_move = 2
            while select_move == 2:
                bot_move = random.choice(move_list)
                select_move = 0
                if bot_move == "rock":
                    bot_round_win()
                elif bot_move == "paper":
                    player_round_win()
                else:
                    tie_round()
        else:
            print("Invalid input")

##Starts the game
start_game()