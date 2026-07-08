from utils.printer import  print_header

def favorite_languages():
    languages=["java", "JavaScript", "TypeScript", "Python"]
    print(f"Languages: {languages}")

def first_element():
    languages=["java", "JavaScript", "TypeScript", "Python"]
    print(f"First Languages: {languages[0]}")

def last_element():
    languages=["java", "JavaScript", "TypeScript", "Python"]
    print(f"Last Languages: {languages[-1]}")

def middle_element():
    languages=["java", "JavaScript", "TypeScript", "Python"]
    print(f"Middle Languages: {languages[2]}")

def list_len():
    languages=["java", "JavaScript", "TypeScript", "Python"]
    print(f"Length of Languages: {len(languages)}")

def list_adding():
    languages=["java", "JavaScript", "TypeScript", "Python"]
    languages.append("C++")
    print(f"New Languages added: {languages}")

def list_inserting():
    languages=["java", "JavaScript", "TypeScript", "Python"]
    languages.insert(2,"C++")
    print(f" Inserting C++ in second index: {languages}")

def list_remove():
    languages=["java", "JavaScript", "C++", "TypeScript", "Python"]
    languages.remove("C++")
    print(f"After removing  C++: {languages}")

def list_sort():
    languages=["Java", "JavaScript", "C++", "TypeScript", "Python"]
    languages.sort()
    print(f"Language after sorting: {languages}")

def list_reverse():
    languages=["Java", "JavaScript", "C++", "TypeScript", "Python"]
    languages.reverse()
    print(f"Language after reverse: {languages}")

def list_exists():
    languages=["Java", "JavaScript", "C++", "TypeScript", "Python"]
    print(f"Is Pythong Language exists : {'Python' in languages}")


def list_count():
    languages=["Java", "JavaScript", "C++", "TypeScript", "Python"]
    print(f"Total Pyhthon in Language: {languages.count('Python')}")

def list_index():
    languages=["Java", "JavaScript", "C++", "TypeScript", "Python"]
    print(f"Index of C++ : {languages.index("C++")}")

def list_copy():
    languages=["Java", "JavaScript", "C++", "TypeScript", "Python"]
    new_languages= languages.copy()
    print(f"New Copied languages: {new_languages}")

def list_clear():
    languages=["Java", "JavaScript", "C++", "TypeScript", "Python"]
    languages.clear()
    print(f"New Copied languages: {languages}")

def mini_project():
    products=["Phone","Fruits","Vegitable","Electronics"]
    print(f"Products : {products}")
    print(f"Add Product")
    products.append("Cold Drinks")
    print(f"Products : {products}")
    print(f"Remove Product")
    products.remove("Phone")
    print(f"Display Products : {products}")
    #products.index("Fruits")
    print(f"Product found at index : {products.index('Fruits')}")
    print(f"Total counts of products: {len(products)}")
    print(f"Exit: ")
    products.clear()
    print(f"No products are available : {products}")







def main():
    print_header("1. Create a list of your favorite programming languages")
    favorite_languages()
    print_header("2. Print the first element")
    first_element()
    print_header("3. Print the last element")
    last_element()
    print_header("4. Print the middle element")
    middle_element()
    print_header("5. Print the length of the list.")
    list_len()
    print_header("6. Add a new language.")
    list_adding()
    print_header("7. Insert one language at index 2.")
    list_inserting()
    print_header("8. Remove one language")
    list_remove()
    print_header("9. Sort the list")
    list_sort()
    print_header("10. Reverse the list")
    list_reverse()
    print_header("11. Check if 'Python' exists")
    list_exists()
    print_header("12. Count 'Python' in the list")
    list_count()
    print_header("13. Find the index of 'C++'")
    list_index()
    print_header("14. Copy the list")
    list_copy()
    print_header("15. Clear the copied list.")
    list_clear()
    mini_project()
if __name__=="__main__":
    main()