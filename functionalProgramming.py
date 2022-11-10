from functools import reduce
"""
FUNCTIONAL PROGRAMMING:
    -Features;
        --Everyting is a function
        --Pure functions without side effects
        --immutable data structures
        --Preserve state in functions
        --Recursion instead of loops/iteration
    -Advantages:
        --Absense of side effects can make your prorams more robust
        --Programs tend to be more modular come and typically in smaller building blocks
        --Better testable - call with same parameters always returns same result
        --Focus on algorithms
        --Conceptional fit with parallel / Concurrent programming
        --Live updates - Install new releases while running
    -Disadvantaes:
        --Solutions to the same problem can look very different than the procedural / oriented-object ones
        --Finding good  developers can be hard
        --Not equally useful for all types of problems
        --input/output are side effects and need special treatment
        --Recursion is "an order of magnitude more comples" than loops/iteration
    PYTHON FUNCTIONAL FEATURES:
        --Pure functions (sort of, cause it's almost impossible to get a pure function)
        --Closures - hold state in functions
        --Functions as objects and decorators
        --Immutable data types
        --Lazy evaluation - generators
        --List(dictionary, set) comprehensions
        --Functools, iteratools, lambda, map, filter
        --Recursion -try to avoid, recursion limit has a reason.
"""


print('###########################################################')
print('--- Functional programming ---')
print('###########################################################')
"""
Features:
    --No side effects, return value only
    --"shadow copy"problem
    --An overloaded * that modifies data or causes other side effect
      would make this function un-pure
    --No guarantee of pureness
    --Pure functions by convention    
"""
def do_pure(data):
    #Return copy times two
    return data * 2
print('###########################################################')
print('--- SIDES EFECTS ARE COMMON ---')
print('###########################################################')
def do_side_effect(my_list):
    # Modify the list appending 100
    my_list.append(100)
print('###########################################################')
print('--- FUNCTIONS ARE OBJECTS ---')
print('###########################################################')
def func1():
    return 1
def func2():
    return 2

my_funcs = {
    'a':func1,
    'b':func2
}
my_funcs['a']()
my_funcs['b']()
print('###########################################################')
print('--- CLOSURES AND "CURRYING" ---')
print('###########################################################')
#outer function stores the state
def outer(outer_arg):
    def inner(inner_arg):
        return inner_arg + outer_arg
    return inner
func = outer(10)
func(5)

func.__closure__
func.__closure__[0]
func.__closure__[0].cell_contents
print('###########################################################')
print('--- PARTIAL FUNCTIONS" ---')

print('###########################################################')
#Functools module: offer some tools for the functional programming approach
import functools
def func(a, b, c):
    return a, b, c
p_func = functools.partial(func, 10)
print(p_func(3,4))

p_func = functools.partial(func, 10, 12)
print(p_func(3))
print('###########################################################')
print('--- RECURSION ---')

print('###########################################################')
def loop(n):
    for x in range(int(n)):
        a = 1 + 1

#Python recursion is limited to 1000
def recurse(n):
    if n<=0:
        return
    a = 1 + 1
    recurse(int(n) - 1)
"""
timeit loop(1e3)
10000 loops, est of 3: 48 us (microsecs) per loop

timeit recurse(1e3)
1000 loops, best of 3: 687 us(microsecs) per loop

sys.setrecursionlimit(int(1e6)) and %timeit recurse(1e5) segfaulted my IPython kernel
"""
print('###########################################################')
print('--- LAMBDA FNCTIONS ---')
"""
LAMBDA FUNCTIONS:
    --Allows very limited anonymous functions
    --Expression only, no statements
    --Past discussion to exclude it from Python3
    --Useful for callbacks
    --Not Essential:
        ----Always possible to add two extra lines
        ----write a function with name and docstring
"""
def use_callback(callback, arg):
    return callback(arg)
print(use_callback(lambda arg: arg * 2, 10))

def double(arg):
    """
        Double the argument
    """
    return arg*2
print(use_callback(double, 10))
print('###########################################################')
print('--- List Comprehension ---')
"""
List comprehension:
"""

#typical use of map
print(list(map(lambda arg: arg * 2, range(2, 6))))
#Replace with list comprehension (list comprehension instead of map
[print(x * 2) for x in range(2, 6)]
#typical use of filter
print(list(filter(lambda x: x > 10, range(5, 16))))
#Replace with list comprehension
[print(x) for x in range(5,16) if x > 10]
print('###########################################################')
print('--- DECORATORS ---')
"""
-They're applications of closures
-Functions that take a function as parameter, do something and return another function (a new one)
 the magic of decorators happens in the wrapper, that's the function that does something and then call
 the original function.
-short definition: decorators wrap a function, modifying its behavior.      
"""
def decorator(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        print('decorator was here')
        return func(*args, **kwargs)
    return new_func
@decorator
def add(a,b):
    return a+b
print(add(2,3))
print('###########################################################')
print('###########################################################')
print('--- IMMUTABLE DATA TYPES - TUPLES INSTEAD OF LISTS ---')
"""
-Contradicts the usage recommendation
-Lists == elements of the same kind
-Tuple == 'named' elements     
"""
my_list = range(10)
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)
print('###########################################################')
print('--- IMMUTABLE DATA TYPES - FREEZE SETS ---')
"""
Can be used as dictionary keys
"""
my_set = set(range(5))
print(my_set)
my_frozenset = frozenset(my_set)
print(my_frozenset)
print('###########################################################')

"""
NOT ONLY FUNCTIONAL
--Pure functional programs can be difficult to implement
--Combine with procedural an object-oriented program parts
--Choose right tool, for the task at hand
--Develop a feeling where a functional approach can be beneficial
"""


"""
AVOID SIDE EFFECTS
--Set all attributes in __init__ (PyLint will remind you)
--Actual useful application of static methods
--Fewer side effects than setting attributes outside __init__
--Your beloved classes and instances are still there
--Inheritance without overriding __init__ and using super, child class implements own_make_attr1()
"""
print('###########################################################')
print('--- AVOID SIDE EFECTS ---')
class MyClass(object):
    """
    Example for init-only definitions.
    """
    def __init__(self):
        self.attr1 = self._make_attr1()
        self.attr2 = self._make_attr2()
    @staticmethod
    def _make_attr1():
        """
        Do many thing to create attr1
        """
        attr1 = []
        #Skipping many lines
        return attr1
print('###########################################################')
print('--- Freeze Classes ---')
"""
-Mutable data structures are useful for reading data
-Freeze to get read-only version
No future, unwanted modifications possible

"""
class Reader(object):
    def __init__(self):
        self.data = self._read()
    @staticmethod
    def _read():
        """
        Return tuple of tuple of read data.
        """
        data = []
        with open('data.txt') as fobj:
            for line in fobj:
                data.append(tuple(line.split()))
        return tuple(data)
print(Reader._read())
"""
oneline version of read function
 @staticmethod
def _read():
    return tuple(tuple(line.split()) for line in open('data.txt'))
"""
print('###########################################################')
print('--- STEPWISE FREEZING AND THAWING  ---')
"""
-Frozen and unfrozen classes
-Caseuse for freezing:
    --Legacy code: Where are data modified?
    --Complex systems: Detect unwanted modifications
"""
class FrozenUnFrozen(object):
    def __init__(self):
        self.__repr = {}
        self.__frozen = False
    def __getitem__(self, key):
        return self.__repr[key]
    def __setitem__(self, key, value):
        if self.__frozen:
            raise KeyError('Cannot change key %r' % key)
        self.__repr[key] = value
    def freeze(self):
        self.__frozen = True
    def unfreeze(self):
        self.__frozen = False
fuf = FrozenUnFrozen()
fuf['a'] = 100
print(fuf['a'])
fuf.freeze()
# fuf['a'] = 100 #it would raise an exception cause the we've just frozen it
#print(fuf['a']) #it would raise an exception cause the we've just frozen it
fuf.unfreeze()
fuf['a']=100
print('###########################################################')
print('###########################################################')
print('--- IMMUTABLE DATA STRUCTURES - COUNTER ARGUMENTS  ---')
"""
-Some algorithms maybe difficult to implement
-Can be rather inefficient - Repetead re-allocation of memory
    --Antipattern string concatenation
        s += 'text'
-Try this in Jython and (standard)PyPy
"""
print('###########################################################')
print('###########################################################')
print('--- LAZY EVALUATION  ---')
"""
-Iterator and generator
-Saves memory and possibly CPU time

"""
print([x * 2 for x in range(5)])
print((x * 2 for x in range(5)))
print(sum(x * x for x in range(10)))
print('###########################################################')
print('###########################################################')
print('--- ITERTOOLS - "LAZY PROGRAMERS ARE GOOD PROGRAMMERS"   ---')
"""
-Module itertools offers tools for the work with iterators

"""
import itertools as it
print(it.zip_longest('abc', 'xyz'))
print(list(it.zip_longest('abc', 'xyz')))
print(it.islice(iter(range(10)), None, 8, 2))
print(range(10)[:8:2])
print('###########################################################')
print('###########################################################')
print('--- PIPELINING - CHAINING COMMANDS - GENERATORS PULL READING LOGFILE  ---')
"""
-GENERATOR MAKE GOOD PIPELINES
-USEFUL FOR WORKFLOW PROBLEMS
-EXAMPLES PARSIN OF A LOG FILE

"""
import sys
import time


def read_forever_pull(fobj):
    """
    Read from a file as long as there are lines.
    Wait for the other process to write more lines.
    """
    counter = 0
    while True:
        line = fobj.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def filter_comments_pull(lines):
    """
    Filter out all lines starting with #
    """
    for line in lines:
        if not line.strip().startswith('#'):
            yield line


def get_number_pull(lines):
    """
    Read the number in the line and convert it to an integer
    """
    for line in lines:
        yield int(line.split()[-1])


def show_sum_pull(file_name='logfile.txt'):
    """
    Start all the generator and calculate the sum continuously
    """
    lines = read_forever_pull(open(file_name))
    filtered_lines = filter_comments_pull(lines)
    numbers = get_number_pull(filtered_lines)
    sum_ = 0
    try:
        for number in numbers:
            sum_ += number
            sys.stdout.write('sum: %d\r' % sum_)
            sys.stdout.flush()
    except KeyboardInterrupt:
        print('sum: ', sum_)


show_sum_pull()
print('###########################################################')
print('###########################################################')
print('---COROUTINES - PUSH - INITIALIZE WITH DECORATORS   ---')


def init_coroutine(func):
    functools.wraps(func)

    def init(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return init


def read_forever_push(fobj, target):
    """
    Read from a file as long as there are lines
    Wait for the other process to write more lines.
    Send the line to 'target'
    """
    counter = 0
    while True:
        line = fobj.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


@init_coroutine
def filter_comments_push(target):
    """
    Filter out all lines starting with #
    """
    while True:
        line = yield
        if not line.strip().startswith('#'):
            target.send(line)


@init_coroutine
def get_number_push(targets):
    """
    Read the number in the line and convert it to an integer
    Use the level read from the line to choose the to target
    """
    while True:
        line = yield
        level, number = line.split(':')
        number = int(number)
        targets[level].send(number)


#consumer for different cases
@init_coroutine
#consumer 1
def fatal_push():
    """
        Handle fatal errors
    """
    sum_ = 0
    while True:
        value = yield
        sum_ += value
        sys.stdout.write('FATAL sum: %7d\n' % sum_)
        sys.stdout.flush()


@init_coroutine
#Consumer 2
def critical_push():
    """
        Handle critical errors
    """
    sum_ = 0
    while True:
        value = yield
        sum_ += value
        sys.stdout.write('CRITICAL sum: %7d\n' % sum_)
        sys.stdout.flush()


@init_coroutine
#Consumer 3
def error_push():
    """
        Handle normal errors
    """
    sum_ = 0
    while True:
        value = yield
        sum_ += value
        sys.stdout.write('ERROR  sum: %7d\n' % sum_)
        sys.stdout.flush()


@init_coroutine
#Consumer 4
def warn_push():
    """
        Handle warnings
    """
    sum_ = 0
    while True:
        value = yield
        sum_ += value
        sys.stdout.write('WARN  sum: %7d\n' % sum_)
        sys.stdout.flush()


@init_coroutine
#Consumer 5
def debug_push():
    """
        handle debug messages
    """
    sum_ = 0
    while True:
        value = yield
        sum_ += value
        sys.stdout.write('DEBUG  sum: %7d\n' % sum_)
        sys.stdout.flush()


def show_sum_push(file_name='logfile2.txt'):
    """
    Start the pipeline
    """
    TARGETS = {
        'CRITICAL': critical_push(),
        'DEBUG': debug_push(),
        'ERROR': error_push(),
        'FATAL': fatal_push(),
        'WARN': warn_push()
    }
    read_forever_push(open(file_name), filter_comments_push(get_number_push(TARGETS)))


show_sum_push()
print('###########################################################')
print(' ---  CONCLUSIONS  --- ')
"""
-Python offers useful functional features
-Python isn't no pure functional language
-For some tasks the functional approach works very well
-For some other much less
-Combine and switch back and forth with OO and procedural style
-Stay pythonic, be pragmatic
"""
print('###########################################################')