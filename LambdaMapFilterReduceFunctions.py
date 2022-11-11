"""
Lambda function:
-A simple 1-line function
-Do not use def or return keywords, these are implict
"""
from functools import reduce

print('###########################################################')
print(' ---  LAMBDA  --- ')
x=2
y =5
"""
double function without using lambda
def double(x):
    return x * 2
"""
double = lambda x: x * 2 #double of x
"""
Sum function without using lambda
def sumxy(x, y):
    return x + y
"""
sumxy = lambda x, y: x + y #sum of x and y

"""
max function without using lambda
def mx(x, y):
    if x > y:
        return x
    else:
        return y
"""
mx = lambda x, y: x if x > y else y #max of x and y
print(double(x))
print(sumxy(x, y))
print(mx(x, y))
print('###########################################################')
print(' ---  MAP  --- ')
"""
-Apply same function to each element of a sequence
-Return the modified list
-
"""
my_list = [1,2,3]
"""
square function without using map
def square(my_list):
    square_list = []
    for item in my_list:
        square_list.append(item ** 2)
    return square_list
"""
print(list(map(lambda x: x**2, my_list))) # the function doesn't have to be a lambda function
print('###########################################################')
print(' ---  LIST COMPREHENSION  --- ')
"""
Allow us to generate lists in one or too little lines of code
"""
print([x**2 for x in my_list])
print([x for x in my_list if x > 2])
print('###########################################################')
print(' ---  FILTERS  --- ')
"""
Filter item out of a sequence
Return filtered list
"""
"""
over_two function without using filters (and using list comprehension)
def over_two(my_list):
    over2 = [x for x in my_list if x > 2]
    return over2
"""
print(list(filter(lambda x: x > 2, my_list))) #the function doesn't have to be a lambda function
print('###########################################################')
print(' ---  REDUCE  --- ')
"""
Applies same operation to items of a sequence
Uses result of operation as first param of next operation
Return an item, not a list
"""

"""
multiply list function without using map
def multiply_list(my_list):
    prod = []
    for i in range(1, len(my_list)):
        prod *= my_list[i]
    return prod
"""
print(reduce(lambda x,y: x * y, my_list)) #the function doesn't have to be a lambda function
print('###########################################################')



