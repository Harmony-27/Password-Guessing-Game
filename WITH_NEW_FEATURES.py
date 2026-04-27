# New Features in this version:

# 1. Start Message + Attempts Info
# Display a welcome message at the beginning of the game
# Show total number of attempts (e.g., "You have 3 attempts")

# 2. Length Check
# Check if the entered password length matches the original password
# If not, display a message like:
# "Password must be 9 characters"

# 3. Hint System
# Provide hints after incorrect attempts
# Example hints:
# First letter of the password
# Length of the password

# 4. Strong Feedback System
# Improve feedback for wrong attempts:
# First wrong attempt → simple message
# Second wrong attempt → give hint
# Last attempt → warning message (e.g., "Last chance!")

# 5. Play Again Feature
# Ask the user if they want to play again after the game ends
# If "yes" → restart the game
# If "no" → exit the program

print("Welcome to the Password Guessing Game!")
print("You have 3 attempts to guess the password.")

password = "python123"
attempts = 3

for attempt in range(attempts):
    guess = input("Enter your guess: ").lower()
    if len(guess) != len(password):
        print(f"Password must be {len(password)} characters long.")
        print(f"You have {attempts - attempt - 1} attempts left.")
        continue
    else:
        if guess == password:
            print("Access Granted!")
            break
        else:
            if attempt == attempts - 1:
                print("Access Denied! You've used all your attempts.")
            elif attempt == attempts - 2:
                print("Hint: The first letter of the password is 'p'.")
                print(f"You have {attempts - attempt - 1} attempts left.")
            else:
                print("Hint: The password is 9 characters long.")
                print(f"You have {attempts - attempt - 1} attempts left.")