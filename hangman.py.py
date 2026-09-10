import random

# Predefined list of words
words = ["python", "computer", "program", "coding", "software"]

# Randomly choose a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses
incorrect_guesses = 0
max_guesses = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

# Main game loop
while incorrect_guesses < max_guesses:

    # Display the word with blanks
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    # Take user's guess
    guess = input("Guess a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add letter to guessed list
    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Game over
if incorrect_guesses == max_guesses:
    print ("\nGame Over!")
    print ("The word was:", word)