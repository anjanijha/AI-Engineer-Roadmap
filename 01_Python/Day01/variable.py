def display_variables():
    print(f"============Variables====================")
    name="Anjani"
    experience=8
    salary =24
    is_sdet=True
    print(name)
    print(experience)
    print(salary)
    print(is_sdet)

def user_input():

    print(f"===========User Input====================")
    #########User-Input################
    name=input("Enter your name:")
    print(f"Welcome, {name}!");





"""
=======python data types==================
str====>text
int====>whole number
float==>decimal number
bool===>True/false


"""
def basic_operations():

    print("============Basic Opernations====================")
    a=20
    b=5
    print(f"Additon: {a+b}")
    print(f"Subtraction: {a-b}")
    print(f"Multiplication: {a*b}")
    print(f"Division: {a/b}")
    print(f"Modulus: {a%b}")

def main():
    display_variables()
    user_input()
    basic_operations()


if __name__ == "__main__":
    main()

