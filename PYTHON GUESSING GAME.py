import random
import time

lowest = int(input('Enter a minimum number: '))
highest = int(input('Enter a maximum number: '))

lowest_num = (lowest)
highest_num = (highest)

answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True


print ('Python Number guessing game')
print (f'select a number between {lowest_num} and {highest_num}')
while is_running:

    guess = input('Guess a number: ')

    if guess.isdigit():
        guess = int(guess)
        guesses += 1



        if guess < lowest or guess > highest:
            print ('That number is out of range')
            print(f'Please select a number between {lowest} and {highest}')
        elif guess < answer:
            print ('Too low try again!')
        elif guess > answer:
            print ('Too high try again!')

        else:
            print (f'CORRECT! The answer was {answer}')
            print (f'NUMBER OF GUESSES: {guesses}')
            print ('THANK YOU FOR PLAYING!')
            is_running = False
    else:
        print ('Invalid input')
        print(f'Please select a number between {lowest} and {highest}')


time.sleep(3)
