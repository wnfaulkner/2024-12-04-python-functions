##### PYTHON FUNCTIONS #####


## Defining a function - like a function declaration in JS
def first_function():
  pass

first_result = first_function()
# print(first_result)

## Assigning a function to a dynamic variable:
  # Have to declare the function first then can assign it to a variable
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

math_operations = {
  '+': add,
  '-': subtract
}

selected_operation = '-'

# print(math_operations[selected_operation](2, 4))


## Calling Functions
def add(a, b):
  return a + b
  
def sub(a, b):
  return a - b

def compute(a, b, op):
  return op(a, b)

# print( compute(1, 2, add) ) #Passing a callback function as an argument


## Arguments
  # Use * to specify a parameter list when you have an unknown number of arguments.
  # The identifier used with *, i.e., args, can be anything, however by convention, use args.
  # Always use the *args parameter after any required positional parameters.
def fn(*args):
  print( type(args) )
  for arg in args:
    print(arg)

# fn(1, 2, 'SEI')

  # (**kwargs) A keyword argument is an argument with a name, and this is why keyword arguments are also referred to as named arguments.

def dev_skills(dev_name, **kwargs):
  # kwargs will be a dictionary!
  dev = {'name': dev_name, 'skills': kwargs}
  return dev

# print(dev_skills('Jackie', HTML=5, CSS=3, JavaScript=4, Python=2))

def arg_demo(pos1, pos2, *args, **kwargs):
  print(f'Positional params: {pos1}, {pos2}')
  print('*args:')
  for arg in args:
    print(' ', arg)
  print('**kwargs:')
  for keyword, value in kwargs.items():
    print(f'  {keyword}: {value}')

# arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')




##### PYTHON FUNCTIONS LAB #####

#1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n. For example sum_to(6) returns 21

def sum_to(n):
  sum_range = list(range(1, n+1))
  return(sum(sum_range))

print(f'Challenge 1: sum_to(2)={sum_to(2)}, sum_to(3)={sum_to(3)}, sum_to(10)={sum_to(10)}.')

# 2.Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.  largest([1, 2, 3, 4, 0])  # returns 4

def largest(list_of_numbers):
  return(max(list_of_numbers))

print('Challenge 2:')
print(f'largest([0,1])={largest([0,1])}, largest([1,2,3])={largest([1,2,3])}, largest([1,5,3,200,4,3])={largest([1,5,3,200,4,3])}')


# 3. Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.
  # occurrences('fleep floop', 'e')   # returns 2
  # occurrences('fleep floop', 'p')   # returns 2
  # occurrences('fleep floop', 'ee')  # returns 1
  # occurrences('fleep floop', 'fe')  # returns 0




# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
  # product(-1, 4) # returns -4
  # product(2, 5, 5) # returns 50
  # product(4, 0.5, 5) # returns 10.0


# BONUS Write a function named steps_to_zero that accepts a non-negative integer as an argument, and returns the number of steps it took to reduce the integer to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
  # steps_to_zero(14) # returns 6
  # Step 1) 14 is even; divide by 2 and obtain 7. 
  # Step 2) 7 is odd; subtract 1 and obtain 6.
  # Step 3) 6 is even; divide by 2 and obtain 3. 
  # Step 4) 3 is odd; subtract 1 and obtain 2. 
  # Step 5) 2 is even; divide by 2 and obtain 1. 
  # Step 6) 1 is odd; subtract 1 and obtain 0.

