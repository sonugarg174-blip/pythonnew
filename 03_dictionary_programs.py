# DICTIONARY PROGRAMS – LESSON 23

def create_dictionary():
    student = {"name": "Riya", "roll_no": 101, "course": "BCA"}
    print("1. Student dictionary:", student)

def access_values():
    student = {"name": "Aman", "marks": 85}
    print("2. Name:", student["name"])
    print("   Marks:", student.get("marks"))

def add_and_update_items():
    employee = {"id": 1, "name": "Neha", "salary": 30000}
    employee["department"] = "IT"
    employee["salary"] = 35000
    print("3. Updated employee:", employee)

def delete_items():
    student = {"name": "Karan", "age": 20, "course": "BCA"}
    student.pop("age")
    print("4. After deletion:", student)

def display_keys_values_items():
    data = {"Python": 90, "Java": 80, "DBMS": 85}
    print("5. Keys:", list(data.keys()))
    print("   Values:", list(data.values()))
    print("   Items:", list(data.items()))

def traverse_dictionary():
    marks = {"Asha": 78, "Ravi": 82, "Meena": 91}
    print("6. Student marks:")
    for name, score in marks.items():
        print(name, ":", score)

def check_key():
    student = {"name": "Aman", "city": "Delhi"}
    print("7. Is city a key?", "city" in student)

def merge_dictionaries():
    first = {"a": 1, "b": 2}
    second = {"c": 3, "d": 4}
    merged = first | second
    print("8. Merged dictionary:", merged)

def dictionary_comprehension():
    squares = {n: n*n for n in range(1, 6)}
    print("9. Squares dictionary:", squares)

def word_frequency():
    sentence = "python is easy and python is useful"
    frequency = {}
    for word in sentence.split():
        frequency[word] = frequency.get(word, 0) + 1
    print("10. Word frequency:", frequency)

if __name__ == "__main__":
    create_dictionary()
    access_values()
    add_and_update_items()
    delete_items()
    display_keys_values_items()
    traverse_dictionary()
    check_key()
    merge_dictionaries()
    dictionary_comprehension()
    word_frequency()
