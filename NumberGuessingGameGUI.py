from tkinter import *
import random

# The main window is called window
window = Tk()
# Set the title
window.title("Number Guessing Game")
# Set the window size
window.geometry("250x180")

# The main text (big and gray)
label = Label(window, text="Number Guessing Game", font=(None, 15), height=2, bg="gray")
# Align the text to the top of page
label.pack(side=TOP)

# Frame for the text
gridFrame = Frame(window)


def nextRound(youWonLabel, pcHasChosenLabel, points, nextRoundButton):
    # Destroy all the irrelevant widgets
    youWonLabel.destroy()
    pcHasChosenLabel.destroy()
    nextRoundButton.destroy()
    # Start a new game with the new points value
    play(points)


def tryAgain(tryAgainButton, pcHasChosenLabel, youLostLabel):
    # Destroy all the irrelevant widgets
    tryAgainButton.destroy()
    pcHasChosenLabel.destroy()
    youLostLabel.destroy()
    # Start again with value of points 0
    play(0)


def submitLuckyNumber(luckyNumber, points, pointsLabel, submitButton):
    submitButton.destroy()
    # Let pc choose a random number
    randomNumber = random.randint(smallest, biggest)
    pcHasChosenLabel = Label(gridFrame, text="PC has chosen " + str(randomNumber))
    pcHasChosenLabel.grid(column=0, row=3, sticky=N)

    if luckyNumber == randomNumber:
        # Show text if user has the same number as the random chosen number
        youWonLabel = Label(gridFrame, text="You won!")
        youWonLabel.grid(column=0, row=4, sticky=N)

        # Points increases with 1
        points = points + 1
        # Update the value of points (on screen)
        pointsLabel.configure(text="Points: " + str(points))
        pointsLabel.grid(column=0, row=1, sticky=N)

        # Show the next round button
        nextRoundButton = Button(gridFrame, text="Next Round?", command=lambda: nextRound(youWonLabel, pcHasChosenLabel, points, nextRoundButton))
        nextRoundButton.grid(column=0, row=5, sticky=N)

    else:
        # If the player hasn't chosen the same number as the PC

        # Show a text that he lost
        youLostLabel = Label(gridFrame, text="You lost. You reached " + str(points) + " points!")
        youLostLabel.grid(column=0, row=4, sticky=N)

        # Show the try again button
        tryAgainButton = Button(gridFrame, text="Try Again?", command=lambda: tryAgain(pcHasChosenLabel, tryAgainButton, youLostLabel))
        tryAgainButton.grid(column=0, row=5, sticky=N)


def play(points):
    # Show points label on the screen
    pointsLabel = Label(gridFrame, text="Points: " + str(points))
    pointsLabel.grid(column=0, row=0, sticky=N)

    # Ask text on the screen
    luckyNumberLabel = Label(gridFrame, text="My lucky number is (%s - %s): " % (smallest, biggest))
    luckyNumberLabel.grid(column=0, row=1, sticky=N)

    # Create an input form to enter the lucky number
    luckyNumberInput = Entry(gridFrame, width=10)
    luckyNumberInput.grid(column=1, row=1, sticky=N)

    # Show the submit button -> it runs the submitLuckyNumber() function
    submitButton = Button(gridFrame, text="Submit", command=lambda: submitLuckyNumber(int(luckyNumberInput.get()), points, pointsLabel, submitButton))
    submitButton.grid(column=0, row=2, sticky=N)

    # Setting the frame anchor to the top
    gridFrame.pack(side=TOP)

    # Loop the main program page
    window.mainloop()


# The pc will choose one random number between 0 and 5
smallest = 0
biggest = 5

# Play the game with 0 points
play(0)
