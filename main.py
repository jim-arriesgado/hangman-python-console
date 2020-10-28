#********************************************************#
#  Project Title:    HANGMAN                             #
#  App Version:      1.01                                #
#  Coder:            Jim "Kodegero" Arriesgado           #
#  Update Started:  October 24, 2020                     #
#  Update Finished: October 24, 2020                     #
#********************************************************#

# UPDATE NOTES:
# Added new feature, giving a random word from a given list

# Import Modules
import random

# Declare variables needed
word_archive = ["apple", "river", "country", "support", "courage"]
att_count = 5

# Choose a random word from given list
word_str = word_archive[random.randrange(len(word_archive))]

# Convert word into list
word_list = list(word_str)

# Initialize hidden list
list_hidden = []
for i in word_list:
    list_hidden.append("_")

# Game loop
while "_" in list_hidden:
    # Ask for user input
    user_guess = input(f'''
Attempts remaining: {att_count}

{list_hidden}

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
    print('''
    YOU WON...
    Congratulations! You guessed it right.''')
