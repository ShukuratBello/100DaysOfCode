# [easy] Challenge #1
# create a program that will ask the users name, age, and reddit username. 
# have it tell them the information back, in the format:
#your name is (blank), you are (blank) years old, and your username is (blank)

name = input("What is your name: ")
age = input("How old are you: ")
reddit_username = input("What is your reddit username: ") 

with open('file.txt', 'w') as f:
    print(f'Your name is {name}, you are {age} years old, and your username is {reddit_username}', file=f)


# [intermediate] challenge #1


# [difficult] challenge #1
# we all know the classic "guessing game" with higher or lower prompts. 
# lets do a role reversal; you create a program that will guess numbers between 1-100, 
# and respond appropriately based on whether users say that the number is too high or too low. 
# Try to make a program that can guess your number based on user input and great code!

import random