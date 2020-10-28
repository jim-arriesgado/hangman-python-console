#********************************************************#
#  Project Title:    HANGMAN                             #
#  App Version:      1.03                                #
#  Coder:            Jim C. Arriesgado a.k.a "Kodegero"  #
#  Update Started:   October 23, 2020                    #
#  Update Finished:  October 23, 2020                    #
#********************************************************#

# UPDATE NOTES:
# Add new feature, set the difficulty level of the game

# Import Modules
import random

# Declare variables needed
list_easy = ["apple", "river", "country", "support", "courage"]
list_average = ["commotion", "geography", "expenses", "migration", "planning"]
list_hard = ["extravagance", "sovereign", "inflammation", "catacombs", "disagreement"]
word_display = ""


# Define functions
def hidden_str(list_hidden1):
    word_display1 = ""
    for i1 in range(len(list_hidden1)):
        word_display1 = word_display1 + " " + list_hidden1[i1]
    return word_display1


def diff_level(user_level):
    if user_level.lower() == "easy":
        return list_easy[random.randrange(len(list_easy))]
    elif user_level.lower() == "average":
        return list_average[random.randrange(len(list_average))]
    elif user_level.lower() == "hard":
        return list_hard[random.randrange(len(list_hard))]


def user_att(user_level2):
    if user_level2.lower() == "easy":
        return 7
    elif user_level2.lower() == "average":
        return 5
    elif user_level2.lower() == "hard":
        return 3


# Choose a random word based on the difficulty level given by the user
user_diff = input('''
Please choose a difficulty level.
Easy - Average - Hard : ''')
word_str = diff_level(user_diff)

# Set the number of attempts based on the difficulty given by the user
att_count = user_att(user_diff)

# Convert word into list
word_list = list(word_str)

# Initialize hidden list
list_hidden = []
for i in range(len(word_list)):
    list_hidden.append("_")

# Convert hidden_list from list to string
word_display = hidden_str(list_hidden)

# Game loop
while "_" in list_hidden:
    # Ask for user input
    user_guess = input(f'''
Attempts remaining: {att_count}

{word_display}

Guess a letter: ''')

    # Check if user input exist in word _list
    if user_guess in word_list:

        # Check if user input already exist in the list
        if user_guess not in list_hidden:

            # Check if user input is the same as the character in every index
            # If not, assign "_"
            for i in range(len(word_list)):
                if user_guess == word_list[i]:
                    list_hidden[i] = user_guess

            # Convert hidden_list from list to string
            word_display = hidden_str(list_hidden)

        else:

            # Print message
            print("Letter is already revealed.")

    else:

        # Print message
        print("Sorry, letter NOT FOUND!")

        # Deduct 1 point from att_count
        att_count -= 1

        # Check if att_count equals to zero
        if att_count == 0:
            print('''
            GAME OVER...
            Sorry, You have used all your chances.''')
            break

else:
    print(f'''
    Congratulations!
    YOU WON...

    The word is: {word_display}

    You guessed it right.''')
