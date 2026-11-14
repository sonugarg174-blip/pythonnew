# PYTHON CHALLENGES – LESSON 26

def largest_number():
    numbers = [12, 45, 7, 89, 34]
    print("1. Largest number:", max(numbers))

def remove_duplicates():
    values = [1, 2, 2, 3, 4, 4, 5]
    print("2. Without duplicates:", list(dict.fromkeys(values)))

def count_vowels():
    text = "Python Programming"
    count = sum(1 for char in text.lower() if char in "aeiou")
    print("3. Vowel count:", count)

def palindrome_check():
    word = "madam"
    print("4. Is palindrome?", word == word[::-1])

def even_odd_check():
    number = 17
    print("5.", number, "is", "Even" if number % 2 == 0 else "Odd")

def multiplication_table():
    number = 5
    print("6. Multiplication table:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

def common_elements():
    first = [1, 2, 3, 4]
    second = [3, 4, 5, 6]
    print("7. Common elements:", sorted(set(first) & set(second)))

def passed_students():
    marks = {"Asha": 78, "Ravi": 32, "Meena": 91, "John": 38}
    passed = {name: score for name, score in marks.items() if score >= 40}
    print("8. Passed students:", passed)

def run_challenges():
    largest_number()
    remove_duplicates()
    count_vowels()
    palindrome_check()
    even_odd_check()
    multiplication_table()
    common_elements()
    passed_students()

if __name__ == "__main__":
    run_challenges()
