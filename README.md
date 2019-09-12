#	Знакомство с языком, основные синтаксисические конструкции и среда разработки

## 1 SYNTAX,  OPERATORS , VARIABLES, EXPRESSIONS

you can write a comment strings in your code, they will not be considered as code to execute, rather than a good practice hinting and describing near code

```
# this is a comment, on line

"""
   comment in few lines
    do nothing, but inform
"""

```
---
### EXPRESSIONS

**EXPRESSION** is programming language construction, which **consists of other EXPRESSIONS**
or 
**can contain** other **VALUES** , **VARIABLES**, **FUNCTIONS CALLS** **connected** with **OPERATORS (+,-,=,*) ** 



```
# simple expression

# 2 is a value or integer constant , then arithmetic operator + , than again integer 2 (constant)
2 + 2

# more complex like algebra

999.2 * ( 2 + 5 ) / 5

```

---
## ASSIGNMENT operator =

One of the most important and simple operator in imperative languages (like Python, C, C#...)

```
# look at this assignment expression 
user = "FancyBeard"

# make the name (variable) 'user' contains (points) to string 'FancyBeard'
# now variable with name 'user' contains "FancyBeard"
```

In common scenarios syntax is kinda following:
> *NAME_TOSAVE_THERESULT*  = *EXPRESSION_TO_CALCULATE_LEFT_PART*



### арифметические операторы
```

## арифметические операторы +, -, /, *

# sum is a variable
# 7+2 is an language expression

sum = 7 + 2

x = 10 * 5 + 4 / 3 - 1.5   


## скобки определяют порядок выч-я как в математике

x = 10 * (5 + 4 / 3 - 1.5)  





## Именна переменных зависят от регистра, могут начинаться с _ или букв

1a  ## wrong, нельзя начинать с имя переменной с числа 
 
= a1 ## wrong, должен быть правый операнд (переменная)

_1a = 1 ## ok
```

#### advanced usage of assigment

```

x,y,z = 99,-1,"20"

a = b = c = 0x2199 # hexademical

a1,b1,c1 = "WOW"

a, *b, c = "Python"

a # P
b # ['y', 't', 'h', 'o']
c # n

# сокращённая форма a = a + "Django"
a += "Django"


print(a,b,c)

```

## 2 COMMON ERRORS IN THE BEGINNING LEARNING PYTHON

---
Just look what error message Python interpreter showed after failure running 
the program. Message will get you:

- **NAME** of error 
-  **SHORT DESCRIPTION**
-  most important the **NUMBER OF LINE**  in which it happened


#### SyntaxError
usually some stupid grammer mistake in written code (not logical)


#### NameError
if you try to use a name (variable) in function, or other code before you've assign it

```
z = 999

print(zz)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'zz' is not defined
```


#### IndexError
You try to get element from collection by index which is not exists

```
# you define the name (variable) a as a list structure with two elements 1,2

a = [1,2]
```

```
# now you try to get element with index 3 (which is actually the 4rt element)
a[3]

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

#### ZeroDivisionError

Pretty self talking 

``` 
not_possible = 1 / 0

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

---
## 2 BASIC TYPES - STR, INT, FLOAT, BOOL

### str
```
name = "Ola"

# string concatenation 
both_values = "s1" + "s2"
```

#### float 
```

f = 1.5
f2 = 10/3
```

#### bool - is logical type - can only be True or False


```
he_is_old = True

# new age 
age = 16

if age < 35: 
	he_is_old = False


```

---
### 3 using functions
```
# examples useful simple functions

- len()
- type()
- str()
- int()
- float()

multiline_str = 
	"""
	string for 
	2 lines
	"""

```
---
## 4 FUNCTIONS - DEFINE YOUR OWN, PASS ARGUMENTS, RETURN VALUE

```
# pass - ничего не делать, как заготовку можно
def function_stub():
    pass


# всегда возвращает True
def true_function():
    return True

# how to call function
function_stub()


yes = true_function()
```

### text formatting 
```
"My name is %s, age %d".format() % name,age 

```
## 5 ЛОГИЧЕСКИЕ ОПЕРАТОРЫ И УСЛОВИЯ (ВЕТВЛЕНИЯ В КОДЕ)


```python
#checks if two values are equal

5 == 5 # True

#checks if two values are not equal
6 != 5  # True

#checks if first value is less than second
5 < 2  # False 

#checks if first value is greater than second
3 > 5 # True

#checks if first value is greater than or equal to second
1 >= 1 # True

#checks if first value is less than or equal to second
99 >= 100 # False

```
## 6 условный оператор

```
# составные условия 
if (name=="Dee" and age < 40):
    print("Alright")
else:
    print("wrong...")

(a>5 or a<2) and b==10
```

## 7 Iterable types

- lists - mutable ordered
- strings - immutable ordered
- tuple - immutable unordered
- dictionary -  mutable unordered
- set - mutable unordered

---

## for loop - iterations in code

```
for item in COLLECTION:
    do_something(item)

```


```
# print five times the string

for item in range(1,5):
	print("five lines")
	
```

## 8 modules and packages, example of usage

- Modules can be imported in three different ways: 

```
import module

from module import functions

from module import *

```

## example
```
import math
import random

random.randint(10,44) 
math.sqrt(5)
```

### Keywords in Python, you should memorize it

```python
 # enter this in REPL console to get Python keywords 
help("keywords")
```


**here is a list of the python keywords**

>  *REMEMBER THEM! AND DONT USE AS NAMES*

```
False               class               from                or
None               continue         global              pass
True                def                	   if                  raise
and                 del                import          return
as                  elif                		in                  try
assert              else                	is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 	not

```

## 9 Dictionaries  - one more useful builtin data structure (type)


```
empty = { }
```

### Exceptions handling 
```
    # try:
        code()
    # except: 
        print('Error')
```

## 10 World of modules/packages - using, how to install if not builtin

```
# python package manager
> pip install requests

```


## Operations with files

- create, open, read, write, append, delete
- CSVFile module

```
while expression:
    pass
```

## iterable objects, and applying builtin functions to them

```
# useful builtin functions

range(1,5)

sum([1,2])

sum("1","2") # wrong 

sum(["1","2"]) # wrong types

# the same
# min,max
```

**GET ALL BUILTIN OBJECTS IN CURRENT MODULE**
```python

> dir(__builtins__)

['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']


```


### 11 OOP Classes / Objects 


```python
# What is class (template for a data type - your own)
# how to create a class and instantiate an object  

# class variables
# class methods

#constructor method 

```

### 12 OOP next
- inheritance (parent,child class) 
- Polymorphism - redefining methods in child classes 

### Defining exceptions 




## 13  advanced functions usage & fp

map, reduce
list comprehensions


## Depends on Finish Project 





###  Nice REPL, 
- ipython3 - fancy REPL
- PyCharm amazing for IDE for web, big projects, etc
- Spider IDE - i think it's bettet for education
-  Anaconda distribution - is nice all in one solution with libs and packages, and more for la Pythonista

### links
- https://zen.yandex.ru/media/id/5c1a663bb6a0da00aac86ae4/python-operator-prisvaivaniia-7-5c585a845b7b5100afb0a12e


### assigment construction EMERGENCY help )

### if you dont get it, scroll to end of page, there are plenty of mine simple explanation



Let me try to explain how it works step by step for those who aren't familiar with programming

In a simplifed way. it can also be applied to the assigment expression in other popular imperative languages - JavaScript, C/C++/C#, BASIC, Pascal. In computer reality, high-level programming languages, usually can do a lots of stuff between one expression, 
and C/C++/C# are languages with *strong static typisation * )) dont bother now



```python

# SO at the LEFT we define the name (variable)
# which will recieve the result of expression from RIGHT PART
```

### example

-     lets pretend to calcluate the working hours in a year
-     business_hours is the NAME also called VARIABLE, which should contain the result after calculation

**RIGHT PART**

 - so we can make an arithmetic expressions `5` (days in week) multiply by `365` (in year)
 - also we need number of hours in day, in this example there is a special function which will return number of hours in day
 - this function has a name `get_working_hours_per_day`
 - to get a result (call a function) the Python syntax is the NAME_OF_THE_FUNCTION() **with brackets ** , in our case **get_working_hours_per_day()**
 - we have all the data (numbers) to make our simple calculation, so we can compose an expression `5 * 365  * 365 get_working_hours_per_day()`

- we can run this expression in Python console , (we suppose that this function already exists), and will get the result of this expression, it should be a number , a decimal (integer). We got the RESULT we needed.

- Now we need to store it (place it, assign it) to a name  **working_hours**
- we need to use assigment operator - the `=` character 
- on the left we place our name to store result , than =, and on the right the whole expression with numbers and function call 



`working_hours = 5 * 365  * get_working_hours_per_day()`

If you a newbie and you want to read this in verbal language  - you can smth like 
> working_hours will be equal to 5 multiply by  365 multiply by the result of this get_working_hours_per_day function calculation

## those who doesn't dig it - read more 

`working_hours = 5 * 365 * get_working_hours_per_day()`

RIGHT PART from the = sign (assigment operator to call it right) is now an expression

We ASSIGN (in simple connect the LEFT_PART to the name in RIGHT_PART via = operator) , LEFT_NAME = RIGHT_EXPRESSION - can be called  an assigment

Totoally now we got "our complicated" expression, which consists of other expressions and language constructs. In programming such language constructs and expressions, can be very tricky and "not plain and obvious")

We can run it , the programming language (interpreatator) will do some checks at first (is a function with this name exists, can we call it, than it start to solve - multiply the values in a LEFT_PART )

Order of execution and computation probably in this scenario should be:
- the call to function with name get_working_hours_per_day() returning a number
( calling a function sometimes means just simple go to her inner code and parse and computate - execute, complete the inner code in function, and if function returns the result, to get it back on level 1) 
-  so result from function for example 30
-  now python make the RIGHT_PART as an expression similar like this
` 5 * 365 * 30`
- its plain simple math , it will be easy evauluated to a decimal number 9750
- Well on this step out inner representation of whole expression became
`working_hours  = 9750`

- well the Python should probably create a name working_hours, asks for little memory to store the pointer to the value (not value itself), to place it in a kinda special inner table with variables, and numer 9750 (is already a pointer to a memory where an number object 9750 holds), so python probably will just assign the pointer of 9750 to the new name
