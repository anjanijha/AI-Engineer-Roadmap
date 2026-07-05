

##########################################################################################
def print_Name_Age_Profession():
    print(f"1.print your name,age,and profesion")
    name="Anjani"
    age=32
    profession="AI Engineer"
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Profession: {profession}")

##########################################################################################

def sum_of_two_numbers():
    print(f"2. Take two numbers as input and print their sum")
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    total=num1+num2
    print(f"Sum of above two numbers is: {total}")

##########################################################################################

def convert_celsius_to_fahrenheit():
    print(f"3. Convert Celsius to fahrenheit")
    celsius=float(input("Enter temperature in celsius:"))
    fahrenheit=(celsius*9/5)+32
    print(f"Temperature in fahrenheit is: {fahrenheit}")

##########################################################################################
def swap_two_numbers():
    print(f"4. Swap two numbers without using thires variable")
    num1=int(input("Enter the first number:"))
    num2=int(input("enter the second number:"))
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    print(f"After swapping the first number is: {num1}")
    print(f"After swapping the second number is: {num2}")

##########################################################################################
def calculate_area_of_rectangle():
    print(f"5.Calculte the area of a rectangle")
    length=float(input("Enter the length of rectangle:"))
    width=float(input("Enter the width of rectangle:"))
    area=length*width
    print(f"Area of rectangle is: {area}")


########################################################################################


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

##########################################################################################
name=input(f"Enter the name:")
company=input(f"Enter the company :")
experience=int(input(f"Enter the experience:"))
print(f"Employee Details:")
print(f"-----------------")
print(f"Name: {name}")
print(f"Company: {company}")
print(f"Experience: {experience} years")

def main():
    print("============Coding Exercies====================")
    print_Name_Age_Profession()
    sum_of_two_numbers()
    convert_celsius_to_fahrenheit()
    swap_two_numbers()
    calculate_area_of_rectangle()
if __name__ == "__main__":
    main()