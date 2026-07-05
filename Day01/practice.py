print("============Coding Exercies====================")

##########################################################################################

print("1.print your name,age,and profesion")
name="Anjani"
age=32
profesion="AI Engineer"
print(name)
print(age)
print(profesion)

##########################################################################################

print("2. Take two numbers as input and print thier sum")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
sum=num1+num2
print("Sum of above two numbers is:",sum)

##########################################################################################

print("3. Convert Celsius to fahrenheit")
celsius=float(input("Enter temperature in celsius:"))
fahrenheit=(celsius*9/5)+32
print("Temperature in fahrenheit is:", fahrenheit)

##########################################################################################

print("4. Swap two numbers without using thires variable")
num1=int(input("Enter the first number:"))
num2=int(input("enter the second number:"))
num1=num1+num2;
num2=num1-num2
num1=num1-num2
print("After swapping the first number is:",num1)
print("After swapping the second number is:", num2)

##########################################################################################

print("5.Calculte the area of a rectangle")
length=float(input("Enter the length of rectangle:"))
width=float(input("Enter the width of rectangle:"))
area=length*width;
print("Area of rectangle is",area)


##########################################################################################


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
name=input("Enter the name:")
company=input("Enter the company :")
experience=int(input("Enter the experience:"))
print("Employee Details:")
print("-----------------")
print("Name:", name)
print("Comapny:",company)
print("Experience:",experience,"years")
