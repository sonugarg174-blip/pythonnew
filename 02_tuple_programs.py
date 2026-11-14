# TUPLE PROGRAMS – LESSON 22

def create_tuple():
    student = ("Aman", 20, "BCA")
    print("1. Student tuple:", student)

def access_tuple():
    subjects = ("Python", "DBMS", "Cloud Computing", "Java")
    print("2. First subject:", subjects[0])
    print("   Last subject:", subjects[-1])

def tuple_slicing():
    values = (10, 20, 30, 40, 50)
    print("3. Sliced tuple:", values[1:4])

def tuple_methods():
    values = (10, 20, 10, 30, 10)
    print("4. Count of 10:", values.count(10))
    print("   Index of 30:", values.index(30))

def tuple_length_and_membership():
    colours = ("red", "green", "blue")
    print("5. Tuple length:", len(colours))
    print("   Is green present?", "green" in colours)

def convert_tuple_to_list():
    data = ("Aman", 20, "BCA")
    editable = list(data)
    editable[1] = 21
    print("6. Modified tuple:", tuple(editable))

def tuple_unpacking():
    student = ("Riya", 21, "BCA")
    name, age, course = student
    print("7. Name:", name, "Age:", age, "Course:", course)

def join_tuples():
    first = (1, 2, 3)
    second = (4, 5, 6)
    print("8. Joined tuple:", first + second)

if __name__ == "__main__":
    create_tuple()
    access_tuple()
    tuple_slicing()
    tuple_methods()
    tuple_length_and_membership()
    convert_tuple_to_list()
    tuple_unpacking()
    join_tuples()
