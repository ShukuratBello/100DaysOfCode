# Loop Keywords
# Break and Continue: to ignore a value

# For Loops : Iterates over a certain number of values

nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

for num in nums:
    if num == 3:
        print('Found!')
        break #because we found 3, it stops and breaks out of the for loop
    print(num)

for num in nums:
    if num == 3:
        print('Found!')
        continue #skips 3 and continue
    print(num)

# Loop within a loop
nums = [1, 2, 3, 4, 5]

for num in nums:
    for letter in 'abc':
        print(num, letter)


# Range - Going through a Loop a certain number of time.
for i in range(1, 10): # 1-9 , 0-9
    print(i)

# While Loops - Will keep going 
# until a certain condition is met or we hit a break.
# always increament initialised value for loop to end
x = 0

while x < 10:
    print(x)
    x += 1

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

while True: #infinite loop 
    print(x)
    x += 1

# Ctrl + C terminates an infinite loop