# Write a function that mimics sum() built-in function
def mysum(*inps):
    total_sum = 0
    for inp in inps:
        total_sum += inp
    return total_sum

print(mysum(1, 2, 3, 4))
 

""" def sum(list_num, op_start=0):
    total_sum = 0
    
    for num in list_num:
        total_sum += num
    return total_sum + op_start

print(sum([1, 2, 3, 4], 4)) """
