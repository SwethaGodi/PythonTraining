#__add__     Concatenates two strings

a = "Hello"
b = "World"
print(a.__add__(b))  

#__class__   Returns the class of the object

a = "Hello"
print(a.__class__)  


#__contains__  Checks if a substring is present

a = "Hello World"
print(a.__contains__("World"))  


#__dir__   Returns a list of all attributes and methods of an object.

a = "Hello"
print(a.__dir__())


#__doc__		Returns the documentation string of an object.

print(str.__doc__)  


#__eq__     Checks if two strings are equal

a = "Hello"
b = "Hello"
print(a.__eq__(b))  


#__getitem__   #Gets a character at an index

a = "Hello"
print(a.__getitem__(4))


#__len__        Gets the length of the string

a = "Hello"
print(a.__len__())


#capitalize()    Converts the first character to uppercase.

var = "hello world"
print(var.capitalize())  


#casefold()    Converts the string to lowercase.

var = "SWETHA"
print(var.casefold()) 


#center(width)    Centers the string within the specified width.

var = "swetha"
print(var.center(20, "-")) 


#count(substring)   Counts occurrences of a substring.

var = "Swethaaa"
print(var.count("a"))


#endswith(suffix)   Checks if a string ends with a certain substring.

var = "hello.txt"
print(var.endswith(".txt"))


#find(substring)     Finds the first occurrence of a substring

var = "hello world"
print(var.find("world"))


#format()         Formats a string

var = "My name is {}"
print(var.format("Swetha"))


#index(substring)   Finds the first occurrence of a substring (raises an error if not found)

var = "hello world"
print(var.index("world"))


#isalnum()   Checks if all characters are alphanumeric

var = "Hello123"
print(var.isalnum()) 


#isalpha()  Checks if all characters are alphabetic

var = "Hello"
print(var.isalpha())


#isdigit()  Checks if all characters are digits

var = "12345"
print(var.isdigit())


#join(iterable)   Joins elements of an iterable with the string as a separator

words = ["Hello", "World"]
print(" ".join(words))


#lower()        Converts all characters to lowercase.

var = "Hello"
print(var.lower())


#replace(old, new)   Replaces occurrences of a substring.

var = "Hello World"
print(var.replace("World", "Python")) 


#split (delimiter)    Splits a string into a list.

var = "hello,python,test"
print(var.split(","))



#strip()     Removes leading and trailing spaces.

var = "  Hello World  "
print(var.strip()) 


#title()    Converts the first character of each word to uppercase.

var = "hello world"
print(var.title())  


#upper()   Converts all characters to uppercase.

var = "hello"
print(var.upper()) 


#lower()    Converts all characters to lowercase.
var="HELLO"
print(var.lower())


#zfill(width)    Pads the string with zeros.

var = "42"
print(var.zfill(5)) 


