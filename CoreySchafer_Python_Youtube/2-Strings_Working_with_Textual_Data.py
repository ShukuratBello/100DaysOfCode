# Video 1 --Strings - Working with Tex tual Data--

message = 'Hello World'
message_1 = 'Sam\'s World'
print(message)

# Multiline String
message = """Bobby's World was a good 
cartoon in the 1990s"""

# Assignment Operator

# Indexing in Python
message = 'HELLO WORLD'
print(message[6:])
print(message[0:5])

""" Functions and methods are the same thing, 
a method is a function that belongs to an object 
count() method takes a string as argument
.find() returns -1 if it cant find the string.
"""

# STRING METHODS (Lower methods)
print(message.lower())
print(message.upper())
print(message.count('HELLO')) 
print(message.find('WORLD')) #returns index position of the first word

new_message = message.replace('WORLD', 'Universe')
print(new_message)
 
# Concatenate
greeting = 'Hello'
name = 'Michael'

# hi = greeting + ', ' + name + '. Welcome!'
#hi = '{}, {}. Welcome!'.format(greeting, name)
hi = f'{greeting}, {name}. Welcome!'
print(hi)

# print(dir(name))
# print(help(str))
print(help(str.lower))
