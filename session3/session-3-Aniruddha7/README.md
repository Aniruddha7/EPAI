# Session 3 - Numeric Types
# In this session we are calculating the base of a number and implement the encoding using map. Here we use both base change algorithm and encoding algorithms.
# Try to use float equality testing without using isclose() operator 
# Try to manually implement truncation operation without using trunc() operator in python by using floor division
# Try to manually implement round operation without using round() operator in python
# 'int':
An integer is an object and also an instance in of the int class in Python and the int class provides several constructors and data types. for e,g x= int(5.6), x= int(decimal("4.5")), x= int(True). Booleans can also be written as integers. Integers are represented internally using base 2 or binary didgits but not as decimals.
# 'encoded_from_base10':
This function is used to convert base of the number to a different base. It takes number, base and digi_map as arguments and returns string encoding. There are certain conditions set before converting base such as the base needs to be between 2 and 36, length of digit_map should be equal to base and the digit_map must not have any repeated characters. If the above conditions are not met, then it has to show ValueErrors relevent to conditions.
# 'digit_map':
This is used to encode the digits generated in base change code with respective alphanumerics. First an empty list of digits is created and the values are inserted at 0th location one by one and then they are mapped in encoding code. digit_map should not have any repeating characters and length should be equal to base
# 'ValueError':
It is a keyword in Python to raise exceptions if a particular condition is not met. In this code it raises errors three conditions
# 'math':
math is a built-in module in Python which is used for mathematical operations. Our goal in this assignment is to not use the built in fucntions defined in math libray.
# 'isclose':
isclose method is used in python to determine check if two floating point numbers are equal in values or not. It is a built in method in math module. The syntax can be written as Syntax: isclose(a, b, rel_tol = 1e-09, abs_tol 0.0)
# 'absolute':
It is one of imput parameters in isclose: It is the maximum difference for being considered “close”, with respect to the magnitude of the input values
# 'relative':
It is also one of imput parameters in isclose: It is the maximum difference for being considered “close”, irrespective of the magnitude of the input values
# 'tolerance':
absolute and relative tolerance can be changed in keyword argument or can be provided directly in parameter list.
# 'bin(' :
It is the inbuilt function in python which converts integers or decimals to binary characters.
# 'hex(':
It is also an inbuilt function in python which coverts integers to hexadecimal form
# 'round':
It is the builtin function in python which is used to round off the input numbers and returns the floating. If number is not defined, then it rounds off the number to nearest integer.
# 'truncation':
This builtin function converts the decimal numbers to integers
# 'error':
error or value error exception is raised when a particular condition is not met
# 'equality':
The equality between two floats can be found using isclose() method in Python
# 'zero':
integer zero '0' is neither positive nor negative. Adding this to natural numbers makes them a set of whole numbers in number line
# 'away':
In recent years, Python has nearly sweeped away other programming languages.

