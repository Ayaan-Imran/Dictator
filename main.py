import pyttsx3
import os
import css
import time

# Create Engine
engine = pyttsx3.init()
engine.setProperty("rate", 125)

# Create speak function
def speak(prompt):
    engine.say(prompt)
    engine.runAndWait()

# Asks confirmation
print(css.color("Welcome to version 2.0", css.C_RED))
print()

input("Please hit enter when you are done preparing in the Spelling words.txt file: ")

# Load data
with open("Spelling words.txt", "r") as file:
    data = file.read().split(",")
    data = [i.lower() for i in data]

# Creates a dictionary for the words
score_board = {"score": 0}

for i in data:
    score_board[i] = False

# Asks the words
for i in data:
    # Clear the console
    os.system("cls")

    # Speak the word
    speak(i)

    # Ask the word
    guess = input("Enter here. If you want hear again, type [hear again]: ")
    while guess == "hear again":
        speak(i)

        guess = input("Enter here. If you want hear again, type [hear again]: ")

    # Checks if the word was enteed right
    if guess.lower() == i:
        score_board[i] = True

    # Let the user know that they did something
    print("The result will be at the end")

    # Sleep the program for 2 seconds
    time.sleep(2)


# Gets the score
score = 0
for i in data:
    if score_board[i]:
        score += 1

score_board["score"] = score

# Calculates percentage
total_words = len(data)
percentage = (score / total_words) * 100

# Prints the end result
title = css.underline(css.color("The score board\n", css.C_YELLOW))

scores_display = "" # This is where the final results where be kept in.
number = 0 # This is the question number
word_for_appending_in_display = "" # This is going to be the original word
answer_for_appending_in_display = "" # This is going to be the user's guess
for i in data:
    number += 1

    answer = score_board[i] # Will return true or false

    # Updating appending variables
    word_for_appending_in_display = css.bold(css.color(i, css.C_BLUE))

    if answer == False:
        answer_for_appending_in_display = css.bold(css.color(answer, css.RED))

    else:
        answer_for_appending_in_display = css.bold(css.color(answer, css.GREEN))

    # Append it to scores_display vairbale
    scores_display += f"{number}. {answer_for_appending_in_display}: {word_for_appending_in_display}\n" 

    # Reset all variables
    word_for_appending_in_display = ""
    answer_for_appending_in_display = ""
    correct_answer_for_appending_in_display = ""

statistics_title = css.underline(css.color("Statistics", css.C_YELLOW))
statistics_score = css.color(f"Score: {score}/{total_words}", css.C_BLUE)
statistics_percentage = css.color(f"Percentage: {percentage}%", css.C_BLUE)
statistics_total = f"\n{statistics_title}\n{statistics_score}\n{statistics_percentage}\n"

score_board_display = f"{title}{scores_display}{statistics_total}"

# Print the board
print(score_board_display)