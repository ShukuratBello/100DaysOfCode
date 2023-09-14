# User Defined Functions

def greet():
    print("Hello")
    print("How do you do?")

greet()

# Hello Jack
def greet(name):
    print("Hello", name) 

greet ("Jack")  #- Jack is an arguement 

# Pass MUltiple Arguement to a Function
def add_numbers(n1, n2):
    result = n1 + n2
    print("The sum is ", result)

number1 = 5.4
number2 = 6.7
add_numbers(number1, number2)

# Return value from a Function
def add_numbers(n1, n2):
    result = n1 + n2
    return result

number1 = 5.4
number2 = 6.7
result = add_numbers(number1, number2)
print("The sum is ", result)

def greet(name):
    print("Hello", name) 
    return
    print("How do you do")
    
greet ("Jack")  #- Jack is an arguement 


# Built-In Functions - sum, len