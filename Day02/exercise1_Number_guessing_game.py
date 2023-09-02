# Numeric types in Python - int (whole number), float (numbers with fractional components), complex

# CONCEPTS
# Random - random.randint(1,100)
# Comaprisons - operators <, >, == etc
# f-string - f'It is currently {datetime.datetime.now()}'
# for loops - iterates over the elements of an iterable
# input - input()
# enumerate - Helps us to number elements of iterables 
#for index, item in enumerate('abc'):
#   print(f'{index}:{item}')
# Answer: 0:a 1:b 2:c
#reversed - Returns an iterator with the reversed elements of an iterable
# r = reversed('abcd')

# Exercise 1 - Number Guessing Game
import random



def guessing_game():
    rand_number = random.randint(10, 30)
    
    attempt = 3

    while attempt > 0:
        g_number = int(input("Guess a number between 10 and 30: "))
        if g_number > rand_number:
            print(f'The number {g_number} is too high')

        elif g_number < rand_number:
            print(f'The number {g_number} is too low')

        else:
            print(f'The number {g_number} is just right')
            break
        attempt -= 1
    print("You are out of time!!!")
guessing_game()