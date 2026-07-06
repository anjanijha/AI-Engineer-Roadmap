from utils.printer import print_header

def print_name():
    name = "Anjani Kumar Jha"
    print(f"Full Name: {name}")


def first_character():
    name = "Anjani Kumar Jha"
    print(f"First Character: {name[0]}")

def last_character():
    name = "Anjani Kumar Jha"
    print(f"Last Character: {name[-1]}")

def print_first_four_characters():
    name = "Anjani Kumar Jha"
    print(f"First Four Characters: {name[0:4]}")
    

def print_uppercase_name():
    name = "Anjani Kumar Jha"
    print(f"Uppercase Name: {name.upper()}")

def print_lowercase_name():
    name = "Anjani Kumar Jha"
    print(f"Lowercase Name: {name.lower()}")

def print_replaced_name():
    name = "Anjani Kumar Jha Capco"
    replaced_name = name.replace("Capco", "OpenAI")
    print(f"Replaced Name: {replaced_name}")

def print_vowel_count():
    name = "Anjani".lower()

    vowels = (
    name.count("a") +
    name.count("e") +
    name.count("i") +
    name.count("o") +
    name.count("u")
    )
    print(f"Number of vowels: {vowels}")

def print_starts_with_a():
    name = "Anjani"
    starts_with_a = name.startswith("A")
    print(f"Starts with 'A': {starts_with_a}")

def print_welcome_message():
    user_name = input("Enter your name: ")
    print(f"Welcome, {user_name}!")

def email_generator():
    first_name = input("Enter your first name: ").strip().lower()
    last_name = input("Enter your last name: ").strip().lower()
    domain = "capco.com"
    email = f"{first_name}.{last_name}@{domain}"
    print(f"\nGenerated Email: {email}")



def main():
    print_header("Exercise 1 : Print your full name.")
    print_name()
    print_header("Exercise 2 : Print the first character.")
    first_character()
    print_header("Exercise 3 : Print the last character.")
    last_character()
    print_header("Exercise 4 : Print the first four characters.")
    print_first_four_characters()
    print_header("Exercise 5 : Convert your name to uppercase.")
    print_uppercase_name()
    print_header("Exercise 6 : Convert your name to lowercase.")
    print_lowercase_name()
    print_header("Exercise 7 : Replace 'Capco' with 'OpenAI'")
    print_replaced_name()
    print_header("Exercise 8 : Count the vowels in your name")
    print_vowel_count()
    print_header("Exercise 9 : Check whether your name starts with 'A'")
    print_starts_with_a()
    print_header("Exercise 10 : Take the user's name as input and print a welcome message.")
    print_welcome_message()
    print_header("Mini Project : Create an Employee Email Generator.")
    email_generator()

if __name__ == "__main__":
    main()