__add__     #Concatenates two strings

>>>a = "Hello"
>>>b = "World"
>>>print(a.__add__(b))  
HelloWorld
-------------------------------------------------

__class__   #Returns the class of the object

a = "Hello"
print(a.__class__)  # Output: <class 'str'>
--------------------------------------------------

__contains__  #Checks if a substring is present

>>>a = "Hello World"
>>>print(a.__contains__("World"))  
True
--------------------------------------------------

__dir__   #Returns a list of all attributes and methods of an object.

>>>a = "Hello"
>>>print(a.__dir__())  
List of all string methods and attributes
------------------------------------------------------------------------

__doc__		#Returns the documentation string of an object.

>>>print(str.__doc__)  
Documentation string of the str class
---------------------------------------------------------------------

__eq__     #Checks if two strings are equal

>>>a = "Hello"
>>>b = "Hello"
>>>print(a.__eq__(b))  
True
--------------------------------------------------

__getitem__   #Gets a character at an index

>>>a = "Hello"
>>>print(a.__getitem__(4))  
o
--------------------------------------------------

__len__        #Gets the length of the string

>>>a = "Hello"
>>>print(a.__len__())  
5
--------------------------------------------------

capitalize()    #Converts the first character to uppercase.

>>>var = "hello world"
>>>print(var.capitalize())  
Hello world
--------------------------------------------------
casefold()    #Converts the string to lowercase.

>>>var = "SWETHA"
>>>print(var.casefold())  
swetha
--------------------------------------------------

center(width)    #Centers the string within the specified width.

>>>var = "swetha"
>>>print(var.center(20, "-"))  
-------swetha-------
--------------------------------------------------

count(substring)   #Counts occurrences of a substring.

>>>var = "Swethaaa"
>>>print(var.count("a"))  
3
----------------------------------------------------

endswith(suffix)   #Checks if a string ends with a certain substring.

>>>var = "hello.txt"
>>>print(var.endswith(".txt"))  
True
------------------------------------------------------------------

find(substring)     #Finds the first occurrence of a substring

>>>var = "hello world"
>>>print(var.find("world"))  
6
--------------------------------------------------------------

format()         #Formats a string

>>>var = "My name is {}"
>>>print(var.format("Swetha"))  
My name is Swetha
--------------------------------------------------------------

index(substring)   #Finds the first occurrence of a substring (raises an error if not found)

>>>var = "hello world"
>>>print(var.index("world"))  
 6
--------------------------------------------------------------

isalnum()   #Checks if all characters are alphanumeric

>>>var = "Hello123"
>>>print(var.isalnum())  
True
---------------------------------------------------------------

isalpha()  #Checks if all characters are alphabetic

>>>var = "Hello"
>>>print(var.isalpha())  
True
---------------------------------------------------------------

isdigit()  #Checks if all characters are digits

>>>var = "12345"
>>>print(var.isdigit())  
True
---------------------------------------------------------------

join(iterable)   #Joins elements of an iterable with the string as a separator

>>>words = ["Hello", "World"]
>>>print(" ".join(words))  
Hello World
-----------------------------------------------------------------------------

lower()        #Converts all characters to lowercase.

>>>var = "Hello"
>>>print(var.lower())  
hello
------------------------------------------------------------------------------

replace(old, new)   #Replaces occurrences of a substring.

>>>var = "Hello World"
>>>print(var.replace("World", "Python"))  
Hello Python
------------------------------------------------------------------------------

split(delimiter)    #Splits a string into a list.

>>>var = "hello,python,test"
>>>print(var.split(","))  
['hello', 'python', 'test']
-------------------------------------------------------------------------------

strip()     #Removes leading and trailing spaces.

>>>var = "  Hello World  "
>>>print(var.strip())  
Hello World
-------------------------------------------------------------------------------

title()    #Converts the first character of each word to uppercase.

>>>var = "hello world"
>>>print(var.title())  
Hello World
-------------------------------------------------------------------------------

upper()   #Converts all characters to uppercase.

>>>var = "hello"
>>>print(var.upper())  
HELLO
-------------------------------------------------------------------------------

lower()    #Converts all characters to lowercase.
>>> var="HELLO"
>>> print(var.lower())
hello
-------------------------------------------------------------------------------

zfill(width)    #Pads the string with zeros.

var = "42"
print(var.zfill(5))  
00042
-------------------------------------------------------------------------------

