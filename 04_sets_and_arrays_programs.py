# SETS AND ARRAYS PROGRAMS – LESSON 24
from array import array

def create_set():
    numbers = {10, 20, 30, 20, 10}
    print("1. Set (duplicates removed):", numbers)

def add_remove_set_items():
    colours = {"red", "green", "blue"}
    colours.add("yellow")
    colours.discard("green")
    print("2. Updated set:", colours)

def set_union_intersection():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print("3. Union:", a | b)
    print("   Intersection:", a & b)

def set_difference():
    a = {1, 2, 3, 4}
    b = {3, 4, 5}
    print("4. Difference:", a - b)
    print("   Symmetric difference:", a ^ b)

def set_membership():
    subjects = {"Python", "DBMS", "Java"}
    print("5. Is Python present?", "Python" in subjects)

def remove_duplicates_from_list():
    values = [1, 2, 2, 3, 4, 4, 5]
    print("6. Unique values:", list(set(values)))

def create_integer_array():
    marks = array("i", [70, 80, 90, 85])
    print("7. Integer array:", marks.tolist())

def update_array():
    marks = array("i", [70, 80, 90])
    marks.append(95)
    marks[0] = 75
    print("8. Updated array:", marks.tolist())

def array_calculations():
    values = array("i", [10, 20, 30, 40])
    print("9. Sum:", sum(values))
    print("   Maximum:", max(values))
    print("   Length:", len(values))

if __name__ == "__main__":
    create_set()
    add_remove_set_items()
    set_union_intersection()
    set_difference()
    set_membership()
    remove_duplicates_from_list()
    create_integer_array()
    update_array()
    array_calculations()
