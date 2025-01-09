import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number
    secret_number = random.randint(1, 100)
    print(f"(Debug) Secret number is: {secret_number}")  # Debugging line (remove in production)

    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            # Get the user's guess
            guess = input(f"Attempt {attempts + 1}/{max_attempts}. Take a guess: ")
            
            if not guess.isdigit():
                print("Invalid input! Please enter a number.")
                continue
            
            guess = int(guess)
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                return  # Exit the game upon correct guess
        except ValueError:
            print("Unexpected error occurred. Please try again.")

    # If all attempts are used
    print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {secret_number}.")

# Start the game
if __name__ == "__main__":
    guess_the_number()
