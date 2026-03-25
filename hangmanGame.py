import random

# List of predefined words
WORDS = ["python", "tiger", "apple", "water", "house"]

MAX_ATTEMPTS = 6


def display_word(secret_word, guessed_letters):
    """Display the current state of the guessed word"""
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = []
    attempts_left = MAX_ATTEMPTS

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.\n")

    while attempts_left > 0:

        print("Word:", display_word(secret_word, guessed_letters))
        print("Attempts left:", attempts_left)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!\n")
        else:
            attempts_left -= 1
            print("Wrong guess!\n")

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            return

    print("Game Over! The word was:", secret_word)


if __name__ == "__main__":
    play_hangman()