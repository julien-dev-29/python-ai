import random

n = random.randint(1, 99)
attempts = 0

def print_header():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")

def get_user_input():
    global attempts
    user_input = input("What's your guess between 1 and 99?")

    if user_input.lower() == "exit":
        print("Goodbye!")
        return False
    
    try:
        guess = int(user_input)
    except ValueError:
        print("Please enter a valid number!")
        return True

    if guess < 1 or guess > 99:
        print("Your number must be between 1 and 99!")
        return True

    attempts += 1

    if guess == n:
        print("Congratulations, you've got it!")

        if n == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")

        if attempts == 1:
            print("First try!") 

        elif attempts > 1:
            print(f"You won in {attempts} attempts!")

        return False

    elif guess < n:
        print("Too low!")

    else:
        print("Too high!")

    return True

print_header()

while True:
    if not get_user_input():
        break