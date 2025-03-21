#__add__     Concatenates two strings

a = "Hello"
b = "World"
print(f"Output of __add__:: {a.__add__(b)}")  

#__class__   Returns the class of the object

a = "Hello"
print(f"Output of__class__:: {a.__class__}")  


#__contains__  Checks if a substring is present

a = "Hello World"
print(f"Output of __contains__:: {a.__contains__("World")}")  


#__dir__   Returns a list of all attributes and methods of an object.

a = "Hello"
print(f"Output of __dir__:: {a.__dir__()}")


#__doc__		Returns the documentation string of an object.

print(f"Output of __doc__:: {str.__doc__}")  


#__eq__     Checks if two strings are equal

a = "Hello"
b = "Hello"
print(f"Output of __eq__:: {a.__eq__(b)}")  


#__getitem__   #Gets a character at an index

a = "Hello"
print(f"Output of __getitem__:: {a.__getitem__(4)}")


#__len__        Gets the length of the string

a = "Hello"
print(f"Output of__len__:: {a.__len__()}")


#capitalize()    Converts the first character to uppercase.

var = "hello world"
print(f"Output of capitalize:: {var.capitalize()}")  


#casefold()    Converts the string to lowercase.

var = "SWETHA"
print(f"Output of casefold:: {var.casefold()}") 


#center()    Centers the string within the specified width.

var = "swetha"
print(f"Output of center:: {var.center(20, "-")}") 


#count()   Counts occurrences of a substring.

var = "Swethaaa"
print(f"Output of count:: {var.count("a")}")


#endswith()   Checks if a string ends with a certain substring.

var = "hello.txt"
print(f"Output of endswith:: {var.endswith(".txt")}")


#find()     Finds the first occurrence of a substring

var = "hello world"
print(f"Output of find:: {var.find("world")}")


#format()         Formats a string

var = "My name is {}"
print(f"Output of format:: {var.format("Swetha")}")


#index()   Finds the first occurrence of a substring (raises an error if not found)

var = "hello world"
print(f"Output ofindex:: {var.index("world")}")


#isalnum()   Checks if all characters are alphanumeric

var = "Hello123"
print(f"Output of isalnum:: {var.isalnum()}") 


#isdecimal()		Checks if all characters are decimal digits (0–9 only)

num = "1234"
var = "swesh12"
print(f"Output of isdecimal:: {num.isdecimal()}")
print(f"Output of isdecimal:: {var.isdecimal()}")


#isnumeric()		Checks if all characters are numeric (includes superscripts, fractions, etc.)

num = "VI"
print(f"Output of isnumeric:: {num.isnumeric()}")


#isalpha()  Checks if all characters are alphabetic

var = "Hello"
print(f"Output of isalpha:: {var.isalpha()}")


#isdigit()  Checks if all characters are digits

var = "12345"
print(f"Output ofisdigit:: {var.isdigit()}")


#join()   Joins elements of an iterable with the string as a separator

words = ["Hello", "World"]
print(f"Output of join:: {" ".join(words)}")


#lower()        Converts all characters to lowercase.

var = "Hello"
print(f"Output of lower:: {var.lower()}")


#replace()   Replaces occurrences of a substring.

var = "Hello World"
print(f"Output of replace:: {var.replace("World", "Python")}") 


#split ()    Splits a string into a list.

var = "hello,python,test"
print(f"Output of split:: {var.split(",")}")



#strip()     Removes leading and trailing spaces.

var = "  Hello World  "
print(f"Output of strip::{var.strip()}") 


#title()    Converts the first character of each word to uppercase.

var = "hello world"
print(f"Output of title:: {var.title()}")  


#upper()   Converts all characters to uppercase.

var = "hello"
print(f"Output of upper:: {var.upper()}") 


#lower()    Converts all characters to lowercase.
var="HELLO"
print(f"Output of lower:: {var.lower()}")


#zfill()    Pads the string with zeros.

var = "42"
print(f"Output of zfill::{var.zfill(5)}") 


#encode		Converts the string into bytes using a specified encoding (default is UTF-8)

var = "Swetha"
print(f"Output of encode:: {var.encode()}")


#rsplit		Splits a string from the right using a separator

Tech = "Python, Java, RPA"
print(f"Output of rsplit::{Tech.rsplit(",",1)}")


#expandtabs		Replaces all \t tab characters with spaces. The default tab size is 8 unless specified

var="RPA\tUiPath"
print(f"Output of expandtabs:: {var.expandtabs(4)}")


#partition		Splits the string at the first occurrence of the separator. Returns a 3-tuple

Tech = "RPA:UiPath"
print(f"Output of partition:: {Tech.partition(":")}") 


#ljust		Left-justifies the string and pads the rest with the specified character

var = "Swetha"
print(f"Output of ljust:: {var.ljust(10, "@")}")


#rjust  	Right-justifies the string and pads the rest with a character

var = "Swetha"
print(f"Output of rjust:: {var.rjust(10, "@")}")

#lstrip()		Removes leading whitespace 

var = "   Swetha"
print(f"Output of lstrip:: {var.lstrip()}")


#rstrip()		Removes leading whitespace 

var = "Swetha   "
print(f"Output of rstrip:: {var.rstrip()}")

#rfind()		Returns the last index of a substring. Returns -1 if not found

var = "Swetha"
print(f"Output of rfind:: {var.rfind("e")}")


#rpartition		splits at the last occurrence of the separator

tech = "RPA:Python:Java"
print(f"Output of rpartition:: {var.rpartition(":")}")


#splitlines()		Splits a string into a list at line breaks

var = "RPA\nUipath\nAutomationAnywhere"
print(f"Output of splitlines:: {var.splitlines()}")


#swapcase()		Swaps uppercase to lowercase and vice versa.

var = "SwethA"
print(f"Output of swapcase:: {var.swapcase()}")


#translate		Replaces characters using a mapping table

var = "Swetha"
table = str.maketrans("aeiou", "12345")
print(f"Output of swapcase:: {var.translate(table)}")

#startswith		Checks if string starts with the given prefix

var = "Sweths"
print(f"Output of startswith:: {var.startswith("ths")}")
print(f"Output of startswith:: {var.startswith("Sw")}")

#removeprefix		Removes the given prefix if present

var = "GoSwetha"
print(f"Output of removeprefix:: {var.removeprefix("Go")}")

#isascii()		Returns True if all characters are ASCII (0-127)

print(f"Output of isascii:: {var.isascii()}")  
print(f"Output of isascii:: {"$".isascii()}") 


#isupper()		Checks if all characters are uppercase

var="UiRobot"
print(f"Output of isupper:: {var.isupper()}")


#isspace()		Checks if the string contains only whitespace

var="Ui Robot"
print(f"Output of isspace:: {var.isspace()}")
print(f"Output of isspace:: {"  \t\n".isspace()}")
