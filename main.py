import pyttsx3
import os
import css
import time
import pyperclip

# Create Engine
engine = pyttsx3.init()
engine.setProperty("rate", 125)

# Create speak function
def speak(prompt):
    engine.say(prompt)
    engine.runAndWait()

# Load data
instructions = f"{css.bold('Instructions')}\n1. Please copy the text in your spelling worksheet then hit {css.underline('Enter')}"
input(instructions)
input(
    f"Please paste the text in the file called 'Spelling words.txt' and hit {css.underline('Enter')}")
spelling_words = open("Spelling words.txt", "r")
spelling_words = spelling_words.readline()
spelling_words = spelling_words.split(" ")

# Clear the screen
os.system("cls")

# Loop through the words
question_number = 1
tracker = [[i, False] for i in spelling_words]

for i in spelling_words:
    print(f"Question number {question_number}")
    speak(f"Question {question_number}")

    spelling = f"Spell {i}"
    speak(spelling)

    guess = input("Enter here (If you want to hear again, type in '(hear again)') and hit enter: ").lower()
    heard = False
    if guess == "(hear again)":
        speak(i)
        print("MAX TIMES FOR HEARING IS OVER")
        heard = True
    
    if heard:
        guess = input("Enter here: ").lower()

    if guess == i.lower():
        tracker[spelling_words.index(i)][1] = True
    else:
        guess = input("Wrong! Enter again: ").lower()

        if guess == i.lower():
            tracker[spelling_words.index(i)][1] = True
        else:
            tracker[spelling_words.index(i)].append(guess)

    print("Results will be at the end")

    question_number += 1

    time.sleep(1)

    os.system("cls")

# Display marks
screen = f"{css.bold('Score board')}\n\n"
for i in tracker:
    if i[1]:
        guess_if_right = css.color("Correct", css.GREEN)
    else:
        guess_if_right = f'{css.color("Wrong", css.RED)}. {css.color(f"You entered {i[2]}", css.CYAN)}'

    number = css.color('Number {}'.format(
        spelling_words.index(i[0])+1), css.YELLOW)
    screen += f"{number} ({i[0]}): {guess_if_right}\n"

print(screen)
