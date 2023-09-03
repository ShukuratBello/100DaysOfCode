# Booleans

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal  >=
# Less or Equal     <=
# Object Identity   is #Checking if they are the same ID or object in memory.

# Boolean Operators 
# and
# or
# not

if True:
    print('Conditional was True')
if False:
    print('Conditional was True')

language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')


user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in: # or (if one is true, that's ok) and (both condition has to be true)
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')


a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) #True 
print(a is b) # False because their id in memory are different

print(id(a))
print(id(b))
print(a is b)

# Flase Values:
    # False
    # None
    # Zero of any numeric type = 0
    # Any empty sequence. e.g '', (), [].
    # Any empty napping. e.g, {}

condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


