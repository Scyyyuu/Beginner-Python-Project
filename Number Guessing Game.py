import random
random_number = random.randint(1, 100)  

print("Welcome to a random number guessing game!")
print("To participate, you will have to guess a random number within the range of 1-100!")

guessed_number = input("Select a guessed number (or type 'quit' to give up): ")  

if guessed_number.lower() == "quit":  
    print(f"You quit. The correct number was: {random_number}")
else:
    guessed_number = int(guessed_number)  

    while not guessed_number == random_number:  
        guessed_number = input("You guessed wrong!, select another one (or type 'quit' to give up): ")

        if guessed_number.lower() == "quit":
            print(f"You quit. The correct number was: {random_number}")
            break
        else:
            guessed_number = int(guessed_number)

    else:
        if guessed_number == random_number:
            print(f"Correct! The number was {random_number}")
