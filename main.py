#********************************************************#
#  Project Title:    HANGMAN							 #
#  App Version:      1.02								 #
#  Coder:            Jim "Kodegero" Arriesgado			 #
#  Update Started:   October 25, 2020					 #
#  Update Finished:  October 25, 2020					 #
#********************************************************#

# UPDATE NOTES:
# Enhance UI, converting list_hidden from list into string separated by spaces

# Import Modules
import random

# Declare variables needed
word_archive = ["apple", "river", "country", "support", "courage"]
att_count = 5
word_display = ""


# Define functions
def hidden_str(list_hidden1):
    word_display1 = ""
    for i1 in range(len(list_hidden1)):
        word_display1 = word_display1 + " " + list_hidden1[i1]
    return word_display1


# Choose a random word from given list
word_str = word_archive[random.randrange(len(word_archive))]

# Convert word into list
word_list = list(word_str)

# Initialize hidden list
list_hidden = []
for i in word_list:
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
