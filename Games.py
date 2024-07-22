print("Welcome to Guessing Game! \n Here is the hint for the first word: \n "
      "Most popular and simple programming language \n "
      "You have 3 Guesses \n")

secret_word = "Python"
guess = ""
guess_count = 0
out_of_guesses = False
guess_limit = 3

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("CONGRATULATIONS, YOU WIN!\n")

input("Press Enter to Continue.....")
print("")

print("Here is the hint for the second word: \n "
      "Developer of Python Language \n "
      "You have 3 Guesses \n")

secret_word = "Guido Van Rossum"
guess = ""
guess_count = 0
out_of_guesses = False
guess_limit = 3

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("CONGRATULATIONS, YOU WIN!")


input("Press Enter to Continue.....")
print("")

print("Here is the hint for the last word: \n "
      "Python file extension  \n "
      "You have 3 Guesses \n")

secret_word = ".py"
guess = ""
guess_count = 0
out_of_guesses = False
guess_limit = 3

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("CONGRATULATIONS, YOU WIN! \n You've Completed the Game")
