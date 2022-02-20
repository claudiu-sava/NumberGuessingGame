import random
import os


def play(points):
    smallest = 0
    biggest = 5
    print("My lucky number between %s and %s is: " % (smallest, biggest))
    # Let user input his number
    inputNumber = input()

    # Computer chooses his number between 0 and 5
    computerRandomNumber = random.randint(smallest, biggest)
    print(computerRandomNumber)

    # If the chosen number is equal with computer's random number
    if int(inputNumber) == computerRandomNumber:
        print("Great!")
        points = points + 1
        # Show the points
        print("Points: " + str(points))
        print("Wanna continue? y/n")
        # Let user choose if he wants to continue
        continueAnswer = input()
        if continueAnswer == "n":
            exit()
        elif continueAnswer == "y" or continueAnswer == "":
            # If player continues, the screen is getting cleaned
            os.system('cls' if os.name == 'nt' else 'clear')
            # Starts a new game, with the value of points
            play(points)
        else:
            # If user has entered an invalid command, the program will shut down
            print("Invalid command. Exiting")
    # If the chosen number differs from computer's number
    else:
        print("Oh no...")
        # Print how many point he reached
        print("You reached " + str(points) + " points !")
        print("Do you want to try again? y/n")
        # Let player decide if he wants to continue
        tryAgainAnswer = input()
        if tryAgainAnswer == "n":
            exit()
        elif tryAgainAnswer == "y" or tryAgainAnswer == "":
            # Clear the screen
            os.system('cls' if os.name == 'nt' else 'clear')
            # Start the game with 0 points
            play(0)
        else:
            # If user has entered an invalid command, the program will shut down
            print("Invalid command. Exiting")


# Play the program with 0 points
play(0)
