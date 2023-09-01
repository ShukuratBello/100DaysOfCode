# List Tuples and Sets
# List/ Tuples: allow us to work with sequential data
# Set: unordered collection of values with no duplicate.


#LISTS
courses = ['History', 'Maths', 'Physics', 'CompSci']

print(courses)
print(len(courses))

# List Indexing
# List Length = Total length - 1
# Negative Indexing: -1 = Last item

print(courses[0])
print(courses[-1])

# Slicing
print(courses[:2])
print(courses[2:])

# Modifying List
courses.append('Art') # Add to the end
courses.insert(0, 'Data Structures') # Add to any location insert(location, 'Value')
# extend is used to add multiple values to a list
courses_2 = ['Art', 'Education']
courses.insert(0,courses_2) # this adds it as a list within a list, append does the same
courses.extend(courses_2) # adds the value in the courses_2 into the courses list.

print(courses)

# Remove some values from list
courses.remove('Data Structures')
courses.pop() #removes the last value of the list. Can be useful if list is used as stack or queue.
popped = courses.pop() # it returns the value it removes

print(courses)
print(popped)

# Sorting Lists
course = ['History', 'Maths', 'Physics', 'CompSci']
#course.reverse()
#course.sort() # sort method - Alphabetical Order, Numbers in Ascending order
course.sort(reverse=True)
sort_course = sorted(course)
print(course)
print(sort_course)

nums = [1, 5, 2, 4, 3]
nums.sort()
nums.sort(reverse=True) # This sorts number in descending order
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))

#FINDING VALUES
course = ['History', 'Maths', 'Physics', 'CompSci']
print(course.index('CompSci'))

# Looping Values
print('Math' in course)

# for item in course:
#     print(item)

for index, course in enumerate(course, start=1): #starts at 1 instead of 0
    print(index, course)


# Turn List into string separated by a particular values
# String method called join
course = ['History', 'Maths', 'Physics', 'CompSci']
course_str = ', '.join(course)
# SPLITTING VALUES
new_list = course_str.split(' - ')
print(course_str)
print(new_list)

# TUPLES - We can't modify Tuples they are immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci') # can loop through and access but not change


# SETS - used to check wheter a value is part of a set and remove duplicate values, doesn't care about order
# memebership test
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)

print('Math' in cs_courses)

art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

#CREATING EMPTIES
# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} #This is wrong and will create a dict
empty_set = set()

