# LIST PROGRAMS
# Run this file to practise common Python list operations.

def create_and_display_list():
    fruits = ["apple", "banana", "mango"]
    print("1. Original list:", fruits)

def access_list_items():
    numbers = [10, 20, 30, 40, 50]
    print("2. First item:", numbers[0])
    print("   Last item:", numbers[-1])

def list_slicing():
    numbers = [10, 20, 30, 40, 50]
    print("3. First three items:", numbers[:3])
    print("   Items from index 2:", numbers[2:])

def add_items():
    fruits = ["apple", "banana"]
    fruits.append("mango")
    fruits.insert(1, "orange")
    print("4. After adding items:", fruits)

def remove_items():
    fruits = ["apple", "banana", "mango", "banana"]
    fruits.remove("banana")
    fruits.pop()
    print("5. After removing items:", fruits)

def sort_and_reverse():
    numbers = [40, 10, 30, 20]
    numbers.sort()
    print("6. Sorted list:", numbers)
    numbers.reverse()
    print("   Reversed list:", numbers)

def search_in_list():
    names = ["Aman", "Riya", "Karan"]
    search_name = "Riya"
    print("7. Is Riya present?", search_name in names)
    print("   Index of Riya:", names.index(search_name))

def list_statistics():
    marks = [75, 82, 90, 68, 85]
    print("8. Total:", sum(marks))
    print("   Maximum:", max(marks))
    print("   Minimum:", min(marks))
    print("   Average:", sum(marks) / len(marks))

def list_comprehension():
    numbers = [1, 2, 3, 4, 5]
    squares = [n ** 2 for n in numbers]
    evens = [n for n in numbers if n % 2 == 0]
    print("9. Squares:", squares)
    print("   Even numbers:", evens)

def combine_and_copy_lists():
    a = [1, 2, 3]
    b = [4, 5, 6]
    combined = a + b
    copied = combined.copy()
    print("10. Combined list:", combined)
    print("    Copied list:", copied)

if __name__ == "__main__":
    create_and_display_list()
    access_list_items()
    list_slicing()
    add_items()
    remove_items()
    sort_and_reverse()
    search_in_list()
    list_statistics()
    list_comprehension()
    combine_and_copy_lists()
