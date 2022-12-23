import pyttsx3
import os
import time
import termcolor

# Formatting variables
positive = termcolor.colored('[', 'cyan') + termcolor.colored('+', 'green') + termcolor.colored(']', 'cyan') + ' '
neutral = termcolor.colored('[', 'cyan') + termcolor.colored('-', 'yellow') + termcolor.colored(']', 'cyan') + ' '
negative = termcolor.colored('[', 'cyan') + termcolor.colored('!', 'red') + termcolor.colored(']', 'cyan') + ' '

# Create Engine
engine = pyttsx3.init()
engine.setProperty("rate", 125)

# Functions
def speak(prompt):
    engine.say(prompt)
    engine.runAndWait()

# Asks confirmation
symbols = ["/", "―", "\\", "―"]
index = 0

try:
    while True:
        print(f"\r{neutral}Please hit {termcolor.colored('CTRL + C', on_color='on_grey')} when you have added your spellings in the 'Spelling words.txt' file. {symbols[index]}", end="\r")

        if index == 3:
            index = 0
        else:
            index += 1
            
        time.sleep(0.3)
        
except KeyboardInterrupt:
    os.system("cls")
    print("Proceeding...")
    time.sleep(1)
    os.system("cls")
    
# Load data
total_words = 0
with open("Spelling words.txt", "r") as file:
    data = file.readlines()
    data = [line.lower().strip("\n\t") for line in data]
    total_words = len(data)

# Creates a dictionary for the words
score_board = {}

for i in data:
    score_board[i] = False

# Create a dictionary for the user guesses
user_guesses = {}

# Asks the words
for i in data:
    # Clear the console
    os.system("cls")

    # Speak the word
    speak(i)

    # Ask the word
    while True:
        try:
            os.system("cls")
            guess = input(f"{neutral}Enter here. If you want hear again, {termcolor.colored('on your keyboard:', 'magenta')} {termcolor.colored('CTRL+C', on_color='on_grey')}: ")
            break
            
        except KeyboardInterrupt:
            os.system("cls")
            termcolor.cprint("Listen carefully...", "blue")
            speak(i)
            continue

    # Checks if the word was entered right
    if guess.lower() == i:
        score_board[i] = True
        
    # Add user's guess
    user_guesses[i] = guess

    # Let the user know that they did something
    sentence = termcolor.colored("The results will be at the end", "blue")
    loading = ""
    while loading != "....":
        print("\r" + sentence + " " + termcolor.colored(loading, "blue"), end="\r")
        loading += "."
        time.sleep(.5)


# Editing screen
os.system("cls")
termcolor.cprint("Editing screen", "blue", attrs=["underline"])
print()

index = 0
for word in data:
    index += 1
    users_guess = user_guesses[word]
    
    print(str(index) + ". " + users_guess)
print()

edit_confirmation = input(neutral + "Do you wish to edit any of your answers? [Y/n]: ")

if edit_confirmation.lower() == "y":
    print()
    
    while True:
        index = input(neutral + f"Enter the index of the word you want to edit from the list above {termcolor.colored('[ENTER] for exiting', 'grey')}: ")
        if index == "":
            print(positive + "Proceeding onto the score sheet...")
            time.sleep(1)
            break
        
        guess = input(neutral + f"Enter the re-edited version of that word {termcolor.colored('[ENTER] for exiting', 'grey')}: ")
        if guess == "":
            print(positive + "Proceeding onto the score sheet...")
            time.sleep(1)
            break
        
        # Seperate key from value in the user_guesses dictionary
        words = []
        guesses = []
        for key, value in user_guesses.items():
            words.append(key)
            guesses.append(value)

        chosen_word = words[int(index) - 1]
        user_guesses[chosen_word] = guess
        print(positive + "Sucessfully changed the word")
        print()
    
    # Update the score sheet
    for key, value in user_guesses.items():
        if key == value:
            score_board[key] = True
        else:
            score_board[key] = False

else:
    print(positive + "Proceeding onto the score sheet...")
    time.sleep(1)
    

# Gets the score
score = 0
for i in data:
    if score_board[i] == True:
        score += 1

# Calculates percentage
percentage = (score / total_words) * 100

# Print the end result's title
os.system("cls") # Clear the screen
termcolor.cprint("The score sheet", "blue", attrs=["underline"]) # Prints the title
print() # Print an extra line

number = 0 # This is the question number

# Print the scoreboard
for original_word in data:
    number += 1 # Add new question number
    users_guess_bool = score_board[original_word] # Returns True or False according to if the user gets the word right or wrong
    users_guess = user_guesses[original_word]
        
    if users_guess_bool == False: # If user gets the word wrong then it will be displayed in red colour
        colour = "red"
    else: # If user gets the word right then it will be displayed in green
        colour = "green"

    print(f"{number}. {termcolor.colored(original_word, 'blue')} {termcolor.colored('⟶  {} ⟶  '.format(users_guess_bool), colour)} {users_guess}")

# Statistics title
termcolor.cprint("\nStatistics\n", "yellow") # Prints the statistics title
print(f"{termcolor.colored('Score', 'magenta')}     : {score}/{total_words}")
print(f"{termcolor.colored('Percentage', 'magenta')}: {percentage}%")
