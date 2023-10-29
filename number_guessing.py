# Import the random module to generate random numbers
import random

# Function to generate a random number between 1 and 100
def generate_random_number():
    return random.randint(1, 100)

# Function to play the number guessing game
def play_game():
    # Generate a random number
    secret_number = generate_random_number()
    
    # Number of attempts allowed
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    # Continue until the player guesses the correct number
    while True:
        try:
            # Ask the player to guess the number
            guess = int(input("Enter your guess: "))
            
            # Increment the number of attempts
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

# Call the function to play the game
play_game()
