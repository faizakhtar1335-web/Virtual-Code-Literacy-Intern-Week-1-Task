"""Week 1: Virtual Code Literacy - beginner demonstration."""
secret_number = 7
attempts = 0
max_attempts = 5

print("Virtual Code Literacy - Number Guessing Game")
print("Guess the secret number between 1 and 10.")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess == secret_number:
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            break
        elif guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")
    except ValueError:
        print("Please enter a valid whole number.")
else:
    print(f"Game over. The secret number was {secret_number}.")

print("\nConcepts: variables, input/output, data types, conditions, loops, algorithms, exception handling.")
