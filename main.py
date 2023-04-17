# Number Guessing Game (Very Simple)

# Import random module so a random number can be picked in the specified range
import random

# Print out the welcoming
print("Welcome To The Number Guessing Game!")
print("Guess The Number That The Computer Is Thinking Of! 1 Through 50!")
print("You Have Six Tries! Guess Wisely!!")
print("--------------------------------------------------------------------")
# print("\n")

# clicking y if you would like to play again after the game is over
playAgain = 'y'
lives = 6
Livesleft = print(f"You currently have {lives} lives remaining")
# outer loop to run the whole code; if the button y is pressed the game starts over
while playAgain == "y":
    # outputting a random number in the range 1-50 that needs to be guessed by user
    mysteryNumber = random.randint(1, 50)
    # print(mysteryNumber) <---- to reveal the mystery number (cheats)

    # inside while loop to continuously run the game till the player guesses
    while True:
        numberGuess = int(input("Guess the number: "))
        if numberGuess == mysteryNumber:
            print(f"You have guessed the Number {mysteryNumber}!")
            break

        elif numberGuess > mysteryNumber:
            lives -= 1
            print(f"{numberGuess} was too high.")
            print(f"You currently have {lives} lives remaining. Try Again!")

        elif numberGuess < mysteryNumber:
            lives -= 1
            print(f"{numberGuess} was too low.")
            print(f"You currently have {lives} lives remaining. Try Again!")

        if lives == 0:
            print(f"You Lose! The number was {mysteryNumber}")
            break

    # to see if player wants to play again based on input (n) or (y). if (n) the loop breaks if (y) the loop restarts
    playAgain = input("Would you like to play again? ")
    if playAgain == "n":
        print("Thanks For Playing! Goodbye!")
