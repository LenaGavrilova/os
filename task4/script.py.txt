#!/usr/bin/env python3
import random

nums = []
count_guesses = 0
step = 0

def game_stats():
    global count_guesses, step, nums
    hit_stat = (count_guesses / step) * 100 if step > 0 else 0
    miss_stat = 100 - hit_stat
    last_numbers = ' '.join(str(num) for num in nums[-10:])
    print(f"Hit: {hit_stat:.0f}% Miss: {miss_stat:.0f}%")
    print(f"Numbers: {last_numbers}")

while True:
    num = random.randint(0, 9)
    step += 1

    user_input = input(f"Step: {step}\nPlease enter number from 0 to 9 (q - quit): ")

    if user_input.lower() == 'q':
        break

    if not user_input.isdigit() or len(user_input) != 1 or int(user_input) < 0 or int(user_input) > 9:
        print("Invalid input. Please enter a single digit number or 'q' to quit.")
        continue

    guessed_number = int(user_input)
    nums.append(guessed_number)

    if guessed_number == num:
        count_guesses += 1
        print(f"Hit! My number: {num}\n")
    else:
        print(f"Miss! My number: {num}\n")

    game_stats()
