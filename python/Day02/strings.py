from utils.printer import print_header

def print_name():
    #1. What is a String?
    # A string is a sequence of characters enclosed in quotes
    name = "Anjani"
    company = "Capco"
    profession = "AI Engineer"
    print(f"Name : {name}")
    print(f"Company : {company}")
    print(f"Profession : {profession}")



def create_string():
    #2. How to create a String?
    # Strings can be created using :
    # single quotes(' '), 
    # double quotes(" "), and 
    # triple quotes("""  """) 
    single_str = 'Hello, World!'
    double_str = "Hello, World!"
    triple_str = """Welcome
    to
    Python"""
    print(f"String 1: {single_str}")
    print(f"String 2: {double_str}")
    print(f"String 3: {triple_str}")

def string_indexing():
    #3. String Indexing
    # Strings are indexed in Python, which means each character in a string has a unique index.
    # The first character of a string has an index of 0, the second character has an index of 1, and so on.
    # You can access individual characters in a string using their index.
    # Negative indexing starts from the end(-1) of the string
    language = "Python"
    print(f"String                  :{language}")
    print(f"Character at index 0    : {language[0]}")
    print(f"Character at index 5    : {language[5]}")
    print(f"Character at index -1   : {language[-1]}")  
    print(f"Character at index -2   : {language[-2]}")
    print(f"Character at index -3   : {language[-3]}")

def string_slicing():
    #4. String Slicing
    # Slicing is a way to extract a portion of a string by specifying a range of indices.
    # The syntax for slicing is string[start:end], where start is the index of the first character to include, 
    # and end is the index of the first character to exclude.
    language = "Python"
    print(f"String                      :{language}")
    print(f"Slice from index 0 to 2     : {language[0:2]}")
    print(f"Slice from index 2 to 5     : {language[2:5]}")
    print(f"Slice from index 0 to 6     : {language[0:6]}")
    print(f"Slice from index 0 to 4     : {language[:4]}")
    print(f"Slice from index 3 to end   : {language[3:]}")
    print(f"Slice from index 0 to end   : {language[:]}")

def string_length():
    #5. String Length
    # The length of a string can be determined using the len() function.
    language = "Python"
    print(f"String                  :{language}")
    print(f"Length of the string    : {len(language)}")

def string_immutable():
    #6. Strings are Immutable
    # Strings in Python are immutable, which means that once a string is created, it cannot be changed.
    # Any operation that modifies a string will create a new string instead of modifying the original string.

    name = "Anjani"

    # name[0] = "B"  # This would raise a TypeError since strings are immutable

    name= "B" + name[1:]  # This creates a new string with the first character changed to "B"

    print(f"Modified String : {name}")
##################################################################################
    #Interview Question:
    #Why are strings immutable?
    #Better memory optimization
    #Thread-safe
    #Faster performance
    #Hashable (usable as dictionary keys)
##################################################################################

def string_methods():
    #7. String Methods
    # Python provides a wide range of built-in string methods that allow you to manipulate and perform operations on strings.
    # Some commonly used string methods include:
    text = "Hello, World!"
    print(f"String                  :{text}")
    print(f"Uppercase               : {text.upper()}")
    print(f"Lowercase               : {text.lower()}")
    print(f"Title Case              : {text.title()}")
    print(f"capitalize              : {text.capitalize()}")
    print(f"Replace                 : {text.replace('World', 'Python')}")
    print(f"Find 'o'                : {text.find('o')}")
    print(f"Count 'o'               : {text.count('o')}")
    print(f"Starts with 'Hello'     : {text.startswith('Hello')}")
    print(f"Ends with '!'           : {text.endswith('!')}")
    print(f"Split                   : {text.split(',')}")
    print(f"Strip                   : {'   Hello   '.strip()}")
    print(f"join                    : {', '.join(['Hello', 'World'])}")

def string_formatting():
    name = "Anjani"
    print("My name is {}".format(name))
    print("My name is " + name)
    print(f"My name is {name}")

def escape_characters():
    #8. Escape Characters
    # Escape characters are special characters that are used to represent certain characters that cannot be easily typed or displayed in a string.
    # They are represented by a backslash (\) followed by a specific character.
    print("I'm Anjani")
    print("He said \"Hello\"")
    print("C:\\Users\\Anjani")
    print("Hello\nWorld")
    print("Hello\tPython")
    print("AI " * 3) #Repetition
    language = "Python"

    print(f"'Py' exists: {'Py' in language}") #membership operator
    print(f"'Java' exists: {'Java' in language}")


def main():
    print_header("1. Print your name.")
    print_name()
    print_header("2. Create strings.")
    create_string()
    print_header("3. String Indexing.")
    string_indexing()
    print_header("4. String Slicing.")
    string_slicing()
    print_header("5. String Length.")
    string_length()
    print_header("6. Strings are Immutable.")
    string_immutable()
    print_header("7. Strings Methods.")
    string_methods()
    print_header("8. String Formatting.")
    string_formatting()
    print_header("9. Escape Characters")
    escape_characters()
if __name__ == "__main__":
    main()