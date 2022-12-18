import random


print("Hello! Welcome to the Rock, Paper, Scissors Game!")
user = input("First, what is your name? ")

while True:
    print("Okay. In this game you need to pick between rock/paper/scissors.")
    print("If you win, you got 1 point. If you lose, I get 1 point. And if it is a draw, we both got none.")
    understand = input("Do I need to explain it again? (y/n) ").lower()
    if understand == "y":
        continue
    elif understand == "n":
        user_score = 0
        computer_score = 0
        options = ["rock", "paper", "scissors"]
        while True:
            user_input = input("Pick Rock/Paper/Scissors or Q to quit: ").lower()
            if user_input == "q":
                break
            if user_input not in options:
                continue
            random_number = random.randrange(0, 2)
            computer_pick = options[random_number]
            print("Computer picked", computer_pick + ".")
            if user_input == "rock" and computer_pick == "scissors":
                print("You win!")
                user_score += 1
            elif user_input == "scissors" and computer_pick == "paper":
                print("You win!")
                user_score += 1
            elif user_input == "paper" and computer_pick == "rock":
                print("You win!")
                user_score += 1
            elif user_input == "rock" and computer_pick == "rock":
                print("It's a draw!")
            elif user_input == "paper" and computer_pick == "paper":
                print("It's a draw!")
            elif user_input == "scissors" and computer_pick == "scissors":
                print("It's a draw!")
            else:
                print("You lose! :(")
                computer_score += 1

        print(user, ",you won", user_score, "times.")
        print("I won", computer_score, "times.")
        print("Goodbye", user, "! Can't wait to play again !^^")
        break
    else:
        print("Huh? I don't understand...")
        quitgame = input("Do you want to quit? (y/n) ")
        if quitgame == "y":
            print("Goodbye", user,"! Can't wait to play again !^^")
            break
        elif quitgame == "n":
            continue
        elif quitgame != "y" or quitgame != "n":
            print("Huh? I don't understand... I guess you don't want to play... Goodbye^^")
            break
