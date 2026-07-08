from utils.printer import print_header

def list_defiinition():
    # A list is an ordered, mutable collection that can store multiple values of different data types.
    fruits = ["Apple", "Banana", "Mango"]
    print(f"List of fruits: {fruits}")

def lists_creation():
    # Creating a list using square brackets
    numbers = [10,20,30] 
    names = ["Anjani", "Rahul", "Amit"]
    mixed = [10, "Python", True, 5.5]
    empty = []

    print(f"List of numbers         : {numbers}")
    print(f"List of names           : {names}")
    print(f"List of mixed types     : {mixed}")
    print(f"Empty list              : {empty}")

def list_indexing():
    fruits = ["Apple", "Banana", "Orange", "Mango"]

    print(f"First Fruit  : {fruits[0]}")
    print(f"Second Fruit : {fruits[1]}")
    print(f"Last Fruit   : {fruits[-1]}")
    print(f"Second Last  : {fruits[-2]}")

def list_slicing():
    fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]

    print(f"First two fruits       : {fruits[0:2]}")
    print(f"Last three fruits      : {fruits[-3:]}")
    print(f"All fruits             : {fruits[:]}")

def list_update():
    fruits = ["Apple", "Banana", "Orange"]
    print(f"Before: {fruits}")
    fruits[1] = "Mango"
    print(f"After : {fruits}")

def list_adding():

    #append
    fruits=["banana"]

    fruits.append("Mango")
    print(f"New fruits after append : {fruits}")

    #insert
    fruits = ["Apple", "Banana"]
    
    fruits.insert(1, "Mango")
    print(f"fruits after insert : {fruits}")

    #extend
    fruits = ["Apple", "Banana"]

    fruits.extend(["Orange", "Kiwi"])
    print(f"fruits after extend : {fruits}")

def list_removing():

    #remove
    fruits = ["Apple", "Banana", "Orange"]

    fruits.remove("Banana")
    print(f"fruits after remove : {fruits}")

    #pop
    fruits = ["Apple", "Banana", "Orange"]

    removed = fruits.pop()
    print(f"Removed element  : {removed}")
    print(f"List  after pop  : {fruits}")

    #del
    fruits = ["Apple", "Banana", "Orange"]

    del fruits[1]
    print(f"fruits after delete : {fruits}")

    #clear
    fruits = ["Apple", "Banana"]

    fruits.clear()
    print(f" fruits afte clear all elements :{fruits}")

def list_methods():

    numbers = [30, 10, 40, 20]
    print(f"Original List : {numbers}")
    numbers.sort()
    print(f"Sorted List  : {numbers}")
    numbers.reverse()
    print(f"Reversed List  : {numbers}")
    print(f"Length of List   : {len(numbers)}")
    print(f"Count 20 :  {numbers.count(20)}")
    print(f"Index 40 : {numbers.index(40)}")

def list_membership_operators():
    fruits = ["Apple", "Banana", "Mango"]

    print(f"'Apple' in list  :      {'Apple' in fruits}")
    print(f"'Orange' in list :      {'Orange' in fruits}")
    print(f"'Kiwi' not in list :    {'Kiwi' not in fruits}")

def list_nested():

    students = [
    ["Anjani", 32],
    ["Rahul", 28]
    ]
    print(f"students : {students}")
    print(f"First Element : {students[0]}")
    print(f"Second elemenst with value : {students[1][0]}")

def list_copying():
    fruits = ["Apple", "Banana"]

    new_list = fruits.copy()
    print(f"Original list : {fruits}")
    print(f"Copied list : {new_list}")

def list_mutability():
    numbers = [10, 20, 30]

    print(f"Before list : {numbers}")
    numbers[1] = 100
    print(f"After list : {numbers}")

def main():
    print_header("1. What is List")
    list_defiinition()
    print_header("2. Lists Creation")
    lists_creation()
    print_header("3. List Indexing")
    list_indexing()
    print_header("4. List Slicing")
    list_slicing()
    print_header("5. Updating List Elements")
    list_update()
    print_header("6. Adding Elements")
    list_adding()
    print_header("7. Removing Elements")
    list_removing()
    print_header("8. List Methods")
    list_methods()
    print_header("9. Membership Operators")
    list_membership_operators()
    print_header("10. Nested List")
    list_nested()
    print_header("11. Copying Lists")
    list_copying()
    print_header("12. List Mutability")
    list_mutability()

if __name__=="__main__":
    main()