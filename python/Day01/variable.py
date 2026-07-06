from utils.printer import print_header
def display_variables():
    print_header("Variables")
    name = "Anjani"
    experience = 8
    salary = 24
    is_sdet = True
    print(f"Name        : {name}")
    print(f"Experience  : {experience}")
    print(f"Salary      : {salary}")
    print(f"Is SDET     : {is_sdet}")

def user_input():

    print_header("User Input")
    name=input("Enter your name:")
    print(f"Welcome, {name}!")


"""
=======python data types==================
str====>text
int====>whole number
float==>decimal number
bool===>True/false

"""
def basic_operations():

    print_header("Basic Operations")
    num1 = 20
    num2 = 5
    print(f"Addition:       {num1 + num2}")
    print(f"Subtraction:    {num1 - num2}")
    print(f"Multiplication: {num1 * num2}")
    print(f"Division:       {num1 / num2}")
    print(f"Modulus:        {num1 % num2}")


def main():
    display_variables()
    user_input()
    basic_operations()


if __name__ == "__main__":
    main()

