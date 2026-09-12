import random
random_number = random.randint(1, 100)  # generates the secret number once, stays fixed for the whole game

print("Welcome to a random number guessing game!")
print("To participate, you will have to guess a random number within the range of 1-100!")

guessed_number = input("Select a guessed number (or type 'quit' to give up): ")  # kept as text first, same reason as inside the loop

if guessed_number.lower() == "quit":  # handles quitting on the very first guess
    print(f"You quit. The correct number was: {random_number}")
else:
    guessed_number = int(guessed_number)  # safe to convert now, since we confirmed it's not "quit"

    while not guessed_number == random_number:  # keeps looping while the guess is wrong
        guessed_number = input("You guessed wrong!, select another one (or type 'quit' to give up): ")

        if guessed_number.lower() == "quit":
            print(f"You quit. The correct number was: {random_number}")
            break
        else:
            guessed_number = int(guessed_number)

    else:
        # this only runs if the while loop ended NORMALLY (guess was correct), not from break
        if guessed_number == random_number:
            print(f"Correct! The number was {random_number}")