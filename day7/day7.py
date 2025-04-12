# Day 7: Hangman
import random
from hangman_words import word_list

stages = ['''
  +---+
  |   |
  0   |
 '|'  |
 ' '  |
      |
=======
''', '''
  +---+
  |   |
  0   |
 '|'  |
 '    |
      |
=======
''', '''
  +---+
  |   |
  0   |
 '|'  |
      |
      |
=======
''', '''
  +---+
  |   |
  0   |
 '|   |
      |
      |
=======
''', '''
  +---+
  |   |
  0   |
  |   |
      |
      |
=======
''', '''
  +---+
  |   |
  0   |
      |
      |
      |
=======
''', '''
  +---+
  |   |
      |
      |
      |
      |
=======
''']

lives = 6
#### RANDOMLY CHOOSE A WORD FROM THE LIST ####
chosen_word = random.choice(word_list) # randomly chooses a word from the list


#### Add a Placeholder of dashes ####
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print()
print("Word to Guess: " + placeholder)
print()

#### Allow the user to guess letters one by one, and tell them if they are correct or not
game_over = False
correct_letters = []

while not game_over:
    print(f"******************* YOU HAVE {lives} LIVES LEFT *******************")
    print()
    user_guess = input("Guess a letter: ").lower()
    print()

    if user_guess in correct_letters:
        print(f"You've already guessed {user_guess}")
        print()
    display = ""

    for letter in chosen_word:   # for loop to print right or wrong
    
        if letter == user_guess:
            display += letter
            correct_letters.append(user_guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to Guess " + display)


    if user_guess not in chosen_word:
        lives -= 1
        print()
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print()
            print(f"******************* IT WAS {chosen_word}! YOU LOSE *******************")


    if "_" not in display:
        game_over = True
        print()
        print("******************* YOU WIN *******************")
    
    print(stages[lives])