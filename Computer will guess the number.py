import random


def computer_guess():

    low = int(input("Enter the Lowest limit: "))
    high = int(input("Enter the Highest limit: "))
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # or high
        feedback = input(f'if {guess} is-High (H) Low (L) Correct (C) ?? ').lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f'Computer guessed the right number {guess}')


computer_guess()
