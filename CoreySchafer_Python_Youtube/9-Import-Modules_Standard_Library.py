import my_module as mm
from my_module import find_index as fi, test
from my_module import * # imports all, not recommended

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
index = fi(courses, 'Math')

print(index)
print(test)