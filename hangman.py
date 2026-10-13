import random

WORDS = ["python", "hangman", "program", "keyboard", "computer"]
MAX_WRONG = 6


def display(word, guessed):
    """Return the word with unguessed letters hidden, e.g. 'p _ t h _ n'."""
    return " ".join(ch if ch in guessed else "_" for ch in word)


def play():
    word = random.choice(WORDS)
    guessed = []          # all letters tried so far
    wrong = 0

    print("=== HANGMAN ===")
    print(f"Guess the word one letter at a time. You have {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:
        print(display(word, guessed))
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        print(f"Guessed so far: {' '.join(sorted(guessed)) or '-'}")

        guess = input("Enter a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Correct!\n")
            if all(ch in guessed for ch in word):
                print(display(word, guessed))
                print(f"You win! The word was '{word}'.")
                return
        else:
            wrong += 1
            print("Wrong!\n")

    print(f"Game over! The word was '{word}'.")


if __name__ == "__main__":
    play()