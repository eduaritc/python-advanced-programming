from functools import reduce
"""
FUNCTIONAL PROGRAMING:
Functional programming is a programming paradigm in which we try to bind everything in pure mathematical
functions style. It is a declarative type of programming style. Its main focus is on “what to solve”.
It uses expressions instead of statements. An expression is evaluated to produce a value whereas a statement
is executed to assign variables. It's based on Lambda calculus.
Functional programming paradign, we have data, that gets acted upon
    -PURE FUNCTION:
        --Given the same input, it's got to return the same output
        --It should not produce a side effect (variables from different scopes, prints, etc)
        --Pure functions are more like a guideline cause it's almost impossible to get a fully
          pure function
"""
print('###########################################################')
print('--- Functional programming ---')
print('###########################################################')

# def multiply_by2(number_list):
#     new_list = []
#     for number in number_list:
#         new_list.append(number*2)
#     return new_list
print('###########################################################')
"""
MAP, FILTER, ZIP AND REDUCE:
These functions allow us to execute a function over a collection.
    -MAP/Filter: 
        --It helps us to get pure functions(and fulfilled the ultimate goal of functional programming)
    -Zip:
        given two or more iterables (lists, tuples, dicts, etc) it returns a list of tuples where
        every tuple, is the element at the position i of every iterable passed (see example) 
    
"""
print('--- MAP, FILTER, ZIP AND REDUCE  ---')
print('###########################################################')
"""
this function does exactly the same than the previous one,
with the difference that this one is a pure function (thanks to we're now using maps)
"""
my_list = [1,2,3]
your_list = [10,20,30]
def multiply_by2(item):
    return item*2
print(list(map(multiply_by2, my_list)))

def only_odd(item):
    return item % 2 != 0
print(list(filter(only_odd, my_list)))

print(list(zip(my_list, your_list)))

def accumulator(acc, item):
    print(acc, item)
    return acc + item
"""
Reduce isn't a built-in python module, so we have to import it from functools
it takes three parameters, the function, the iterable which is gonna act on
and the initial value for the function
"""
print(reduce(accumulator, my_list, 0))

print('###########################################################')
"""
LAMBDA EXPRESSIONS:
    -Computer science term
    -One-time anonymous functions that you don't need more than once
    -sintax --> lambda param: action(param)
"""
print('--- LAMBDA EXPRESSONS ---')
print('###########################################################')
print(list(map(lambda item: item*2, my_list))) #multiply_by2 lambda version
print(list(filter(lambda item: item % 2 != 0, my_list))) #only_odd lambda version
print(reduce(lambda acc, item: acc+item, my_list)) #accumulator lambda version

#Lambda expression to square a list
list_to_square = [1,2,3,4,5]
print(list(map(lambda item: item**2, list_to_square)))

#Lambda expression to sort a tuple, by the second element
a = [(0,2), (4,3), (9,9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
print('###########################################################')
"""
Python comprehensions (list, set, dictionary comprehensions):
    -Quick way of creating a list, set or dictionary in Python
"""
print('--- LIST COMPREHENSIONS ---')
print('###########################################################')

my_list = [char for char in 'hello']
my_list2 = [number for number in range(0, 100)]
my_list3 = [number*2 for number in range(0, 100)]
my_list4 = [number**2 for number in range(0, 100) if number %2 == 0]
print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)
print('###########################################################')
print('--- SETS COMPREHENSIONS ---')
print('###########################################################')
my_set = {char for char in 'hello'}
my_set2 = {number for number in range(0, 100)}
my_set3 = {number*2 for number in range(0, 100)}
my_set4 = {number**2 for number in range(0, 100) if number %2 == 0}
print(my_set)
print(my_set2)
print(my_set3)
print(my_set4)
print('###########################################################')
print('--- DICTIONARIES COMPREHENSIONS ---')
print('###########################################################')
simple_dict ={
    'a':1,
    'b':2
}
my_dict = {key:value**2 for key,value in simple_dict.items()}
print(my_dict)
my_dict2 = {k:v**2 for k,v in simple_dict.items()}
print(my_dict2)
my_dict3 = {k:v**2 for k,v in simple_dict.items() if v %2 == 0}
print(my_dict3)
my_dict4 = {num:num*2 for num in [1,2,3]}
print(my_dict4)

#finding duplicates with compreehesions
list_with_duplicates = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate_values = list(set(item for item in list_with_duplicates if list_with_duplicates.count(item) > 1))
print(duplicate_values)
print('###########################################################')

