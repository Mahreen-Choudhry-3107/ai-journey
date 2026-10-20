# Python Data Types

# A data type tells Python what kind of value a variable holds, and what you can do with it. You can't multiply a name by a name, but you can multiply two numbers.

# Check any type with type():


x = 10
print(type(x))   # <class 'int'>


## Main built-in data types

# Numeric=> int, float, complex
# Text=> str
# Boolean=> bool
# Sequence=> list, tuple, range
# Mapping=> dict
# Set=> set, frozenset
# None=> NoneType

# 1. int (whole numbers)


age = 20
temperature = -5
big = 1000000
print(type(age))    # <class 'int'>

# Python integers can be as large as your memory allows.

# 2. float (decimal numbers)


pi = 3.14
price = 99.5
print(type(pi))     # <class 'float'>


# Floats are everywhere in ML: weights, learning rates, probabilities.

# 3. complex (rarely used)


z = 3 + 4j
print(type(z))      # <class 'complex'>


# 4. str (text)

# Use single or double quotes.


name = "Mahreen"
city = 'Lahore'
print(type(name))   # <class 'str'>


# Strings can be joined and repeated:

# concatenation and repetition:
print("Hello " + "World")   # Hello World
print("Hi" * 3)             # HiHiHi


# 5. bool (True / False)


is_student = True
has_passed = False
print(type(is_student))   # <class 'bool'>

# Note the capital `T` and `F`. Booleans come from comparisons:


print(5 > 3)    # True
print(5 == 3)   # False


# 6. list (ordered, changeable)


marks = [80, 90, 75]
mixed = [1, "hello", 3.5, True]
marks[0] = 85          # you can change items
print(marks)           # [85, 90, 75]


# Lists use square brackets `[]`. You'll use them constantly.

# 7. tuple (ordered, NOT changeable)


point = (10, 20)
print(point[0])        # 10
# point[0] = 5  -> Error, tuples can't be changed


# Tuples use round brackets `()`.

## 8. dict (key-value pairs)


student = {"name": "Mahreen", "age": 20}
print(student["name"])   # Mahreen


# Dictionaries use curly braces `{}` and store data as `key: value`.

# 9. set (unique values, unordered)


nums = {1, 2, 2, 3, 3}
print(nums)            # {1, 2, 3}


# Duplicates are removed automatically.

# 10. NoneType (no value)


result = None
print(type(result))    # <class 'NoneType'>


# None means "nothing here yet".


# Type conversion (casting)

# Convert one type to another:


print(int("25"))       # 25
print(float(10))       # 10.0
print(str(100))        # "100"
print(bool(0))         # False
print(list("abc"))     # ['a', 'b', 'c']


# A common beginner error:


# age = input("Enter age: ")   # input always gives a str
# print(age + 5)               # Error!
# print(int(age) + 5)          # Correct

