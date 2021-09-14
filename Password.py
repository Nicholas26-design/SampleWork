secret_word = "password"
guess = ""  # variable to store the guess
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses! You Lose!")
else:
    print("You win!")

# A real world example here would be a password on iphone.
# With that example as well, you'd want to have a guess limit
