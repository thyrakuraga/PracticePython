print("Welcome to the Quiz Game!")
playing = input("Do you want to play? ")
if playing == "Yes" or playing == "yes":
    print("Okay! Let's play!^o^")
else:
    quit()
while playing == "Yes" or playing == "yes":
    print("***")
    print("Let's begin with the first question!")
    score = 0
    print("Score = " + str(score))
    a1 = input("How long is an Olympic swimming pool (in meters)? ")
    if a1 == "50":
        score += 1
        print("You are correct!")
    else:
        print("Aww better luck next time!")
        print("The correct answer is: 50")
    print("Okay! Next question!")
    a2 = input("What does 'www' stands for in a website browser? ")
    if a2 == "World Wide Web" or a2 == "world wide web":
        score += 1
        print("You are correct!")
    else:
        print("Hmm that's okay if you don't know!")
        print("The correct answer is: World Wide Web")
    print("Okay~ Next question~")
    a3 = input("Which country do cities of Perth, Adelaide & Brisbane belong to? ")
    if a3 == "Australia" or a3 == "australia":
        score += 1
        print("You are correct!")
    else:
        print("Aww too bad!")
        print("The correct answer is: Australia")
    print("Almost Done!")
    a4 = input("In Little Red Riding Hood, who does the wolf dress up as? ")
    if a4 == "Grandmother" or a4 == "grandmother":
        score += 1
        print("You are correct!")
    else:
        print("You can do it next time!")
        print("The correct answer is: Grandmother")
    print("Last Question!")
    a5 = input("How many colors are there in the rainbow? ")
    if a5 == "7":
        score += 1
        print("You are correct!")
    else:
        print("Aww man!")
        print("The correct answer is: 7")
    print("Congratulations! You have finished the quiz!")
    print("Your total score is " + str(score) + " out of 5!")
    if score == 5:
        print("WOW! YOU ARE AN ACE!")
    playing = input("Do you want to play again? ")
    if playing == "Yes" or playing == "yes":
        print("***")
        print("Okay! Let's play again!^o^")
    else:
        quit()