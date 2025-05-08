"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Markéta Vorlová
email: VorlovaMarketa@seznam.cz
"""

import random
import time

def print_welcome_message():
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)

def generate_secret_number():
    digits = list("123456789")
    first_digit = random.choice(digits)
    digits.remove(first_digit)

    remaining_digits = list("0123456789")
    remaining_digits.remove(first_digit)

    other_digits = random.sample(remaining_digits, 3)
    return first_digit + "".join(other_digits)

def validate_user_input(user_input):
    if len(user_input) != 4:
        return False, "Input must be exactly 4 digits."
    if not user_input.isdigit():
        return False, "Input must contain only numbers."
    if user_input[0] == "0":
        return False, "The first digit cannot be zero."
    if len(set(user_input)) != 4:
        return False, "All digits must be unique."
    return True, "Valid input."

def evaluate_guess(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

# ---------- Hlavní část programu ----------

print_welcome_message()
secret_number = generate_secret_number()
# print(secret_number)  # Pro testování můžete odkomentovat

start_time = time.time()
attempts = 0

while True:
    user_guess = input("Enter a number: ")
    is_valid, message = validate_user_input(user_guess)
    
    if not is_valid:
        print(f"Invalid input: {message}")
        continue

    attempts += 1
    bulls, cows = evaluate_guess(secret_number, user_guess)

    # Jednotné/množné číslo
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_word}, {cows} {cow_word}")

    if bulls == 4:
        duration = round(time.time() - start_time, 2)
        print("-" * 47)
        print(f"Correct, you've guessed the right number in {attempts} guesses!")
        print(f"That's amazing! It took you {duration} seconds.")
        print("-" * 47)
        break
