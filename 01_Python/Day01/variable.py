def display_variables():
    print("============Variables====================")
    name="Anjani"
    experience=8
    salary =24
    is_sdet=True
    print(name)
    print(experience)
    print(salary)
    print(is_sdet)

def user_input():

    print("===========User Input====================")
    #########User-Input################
    name=input("Enter your name:")
    print("Welcome",name);





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
    print("Additon:",a+b)
    print("Subtraction:",a-b)
    print("Multiplication:",a*b)
    print("Division:",a/b)
    print("Modulus:",a%b)

def main():
    display_variables()
    user_input()
    basic_operations()


if __name__ == "__main__":
    main()

