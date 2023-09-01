#Numbers are int and float type

num = 3.14
print(type(num))

# Arithmetic Operators:
# Addition:         3 + 2
# Subtraction       3 - 2
# Multiplication:   3 * 2
# Division:         3 / 2
# Floor Division:   3 // 2
# Exponent:         3 ** 2
# Modulus:          3 % 2

# Order of operation - PEMDAS

# Increamneting a Variable
nums = 1
num = nums + 1
nums += 1
print(nums)

nums *= 10
print(nums)


# built in function ~ abs - 
# ~ rounds to nearest integer value
print(abs(-3))
print(round(3.75))
print(round(3.75, 1))


# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal  3 >= 2
# Less or Equal:    3 <= 2

# = assignment and == comparison

num_1 = 3
num_2 = 2

print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

# In strings, + concatenates

# String to Integers (casting)
num1 = '100'
num2 = '200'

print(num1 + num2)

num1 = int(num1)
num2 = int(num2)

print(num1 + num2)