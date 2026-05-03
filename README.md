# Password Guessing Game Project

This is a simple Python project that works as a password guessing game. The user has limited attempts to guess the correct password.

## Project Description

This program asks the user to guess a predefined password.

After each attempt:

* The program checks if the entered password is correct or not
* Shows a message for correct or wrong input
* Shows how many attempts are left
* Gives hints if the answer is wrong

If the user enters a password with the wrong length:

* The program shows a message like: "Password must be X characters long"

At the end of the game:

* "Access Granted" is shown if the password is correct
* "Access Denied" is shown if all attempts are used

## Features

* Password guessing system
* Limited attempts
* Checks password length
* Hint system

  * Shows first letter of the password
  * Shows length of the password
* Shows remaining attempts
* Accepts input in any case (upper/lower)
* Shows final result (Access Granted / Denied)

## How It Works

1. The game starts with a welcome message
2. The user gets limited attempts
3. The user enters a password
4. The program checks:

   * If the length is correct
   * If the password is correct
5. If wrong, hints are shown
6. Remaining attempts are shown
7. The game ends when:

   * Password is correct, or
   * Attempts are finished

## Language Used

This project is made using:

* Python
