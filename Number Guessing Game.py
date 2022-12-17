import random


def repeatfunction():
    if playing == "Yes" or playing == "yes":
        print("Okay. Let's Start!")
        print("The rule is you have to guess the number.")
    else:
        print("Thank you!")
        quit()


print("Welcome to the Number Guessing Game!")
playing = input("Do you want to play? ")

while playing == "Yes" or playing == "yes":
    r = random.randrange(1, 11)
    print("You have to guess with 5 guesses. First hint, it is range between 1 - 10.")
    first_guess = int(input("Input your first guess: "))
    if first_guess > r:
        print("It is less than the number you're guessing!")
    elif first_guess < r:
        print("It is more than the number you're guessing!")
    elif first_guess == r:
        print("Congratulations! You guessed the number correctly!")
        playing = input("Do you want to play again? ")
        repeatfunction()
    second_guess = int(input("Input you second guess: "))
    if second_guess > r:
        print("It is less than the number you're guessing!")
    elif second_guess < r:
        print("It is more than the number you're guessing!")
    elif second_guess == r:
        print("Congratulations! You guessed the number correctly!")
        playing = input("Do you want to play again? ")
        repeatfunction()
    third_guess = int(input("Input you second guess: "))
    if third_guess > r:
        print("It is less than the number you're guessing!")
    elif third_guess < r:
        print("It is more than the number you're guessing!")
    elif third_guess == r:
        print("Congratulations! You guessed the number correctly!")
        playing = input("Do you want to play again? ")
        repeatfunction()
    fourth_guess = int(input("Input you second guess: "))
    if fourth_guess > r:
        print("It is less than the number you're guessing!")
    elif fourth_guess < r:
        print("It is more than the number you're guessing!")
    elif fourth_guess == r:
        print("Congratulations! You guessed the number correctly!")
        playing = input("Do you want to play again? ")
        repeatfunction()
    final_guess = int(input("Input you final guess: "))
    if final_guess == r:
        print("Congratulations! You guessed the number correctly!")
        playing = input("Do you want to play again? ")
        repeatfunction()
    else:
        print("Aww! That was close! Better luck next time ^^")
        playing = input("Do you want to play again? ")
        repeatfunction()
