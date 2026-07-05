from utils.printer import print_header
def print_name_age_profession():
    print(f"1.print your name, age, and profession")
    name = "Anjani"
    age = 32
    profession = "AI Engineer"
    print(f"Name:       {name}")
    print(f"Age:        {age}")
    print(f"Profession: {profession}")


def sum_of_two_numbers():
    print(f"2. Take two numbers as input and print their sum")
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    total = num1 + num2
    print(f"Sum of above two numbers is: {total}")


def convert_celsius_to_fahrenheit():
    print(f"3. Convert Celsius to fahrenheit")
    celsius = float(input("Enter temperature in celsius:"))
    fahrenheit = ( celsius * 9 / 5) + 32
    print(f"Temperature in fahrenheit is: {fahrenheit}")


def swap_two_numbers():
    print(f"4. Swap two numbers without using third variable")
    num1 = int(input("Enter the first number:"))
    num2 = int(input("enter the second number:"))
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    print(f"After swapping the first number is: {num1}")
    print(f"After swapping the second number is: {num2}")

def calculate_area_of_rectangle():
    print(f"5. Calculate the area of a rectangle")
    length = float(input("Enter the length of rectangle:"))
    width = float(input("Enter the width of rectangle:"))
    area = length * width
    print(f"Area of rectangle is: {area}")



"""
**Mini Project : Employee Information**
write a programe that:

*Asks for emplyee name,comapany, experience
Prints a formatted summary like:

Employee Details:
-----------------
Name:Anjani
Comapny: Capco
Experience: 8 years

"""


def employee_information():
    name = input(f"Enter employee name:")
    company = input(f"Enter company name :")
    experience = int(input(f"Enter years of experience:"))
    print("\nEmployee Details:")
    print(f"-----------------")
    print(f"Name:       {name}")
    print(f"Company:    {company}")
    print(f"Experience: {experience} years")

def main():
    print_header("Print Name, Age, and Profession")
    print_name_age_profession()
    print_header("Sum of Two Numbers")
    sum_of_two_numbers()
    print_header("Convert Celsius to Fahrenheit")
    convert_celsius_to_fahrenheit()
    print_header("Swap Two Numbers")
    swap_two_numbers()
    print_header("Calculate Area of Rectangle")
    calculate_area_of_rectangle()
    print_header("Employee Information")
    employee_information()


if __name__ == "__main__":
    main()