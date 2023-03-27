
secret_word = "donkey"
guess = ""
guess_count = 0 #count starts from 0 
guess_limit = 3 #how many times the user can guess
out_of_guesses = False #set as false initially, which means user has guesses to use

while guess != secret_word and not(out_of_guesses): #as long as guess not equal secret word and not out of guesses, while loop will keep going
    if guess_count < guess_limit: #first to check if the guess count is less than guess limit
        guess = input("Enter guess: ")
        guess_count += 1 #guess_count = guess_count + 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("YOU WIN THE GAME!")