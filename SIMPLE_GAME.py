print("Welcome to the Password Guessing Game!")

password = "python123"
attempts = 3

for attempt in range(attempts):
    guess = input("Enter your guess: ").lower()
    if guess == password:
        print("Access Granted!")
        break
    else:
        if attempt == attempts - 1:
            print("Access Denied! You've used all your attempts.")
        else:
            print(f"Incorrect! You have {attempts - attempt - 1} attempts left.") # normal version: print("Attempts left:", attempts - attempt - 1)