import random
from art import logo
print(logo)
random_number = random.choice(range(1, 101))

print("Welcome to the Number Guessing Game!!")
print("I'm thinking of a number between 1 and 100")
# print(f"psst the number is {random_number}")

user = input("Choose a difficulty. Type 'easy or 'hard'. ").lower()

if user == "easy":
    attempts = 10
    for attempt in range(attempts):
        guess = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))
        if guess != random_number and  guess < random_number:
            attempts -= 1
            print("Too Low")
            if attempts == 0:
                print("You ran out of attempts Buddy you lose")
                break
        if guess == random_number:
            print(f"You got it the answer is {random_number}")
            break

        if guess > random_number:
            attempts -= 1
            print("Too High")
elif user == "hard":
        attempts = 5
        for attempt in range(attempts):
            guess = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))
            if guess != random_number and  guess < random_number:
                attempts -= 1
                print("Too Low")
                if attempts == 0:
                 print("You ran out of attempts Buddy you lose")
                 break
            if guess == random_number:
                print(f"You got it the answer is {random_number}")
                break

            if guess > random_number:
                attempts -= 1
                print("Too High")