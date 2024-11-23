import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100.")
    print("Can you guess what it is?")

    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
