questions = [
    {
        "question": "What does def mean in Python?",
        "options": {
            "A": "Define a variable",
            "B": "Define a function",
            "C": "Delete a function",
            "D": "Debug code"
        },
        "answer": "B"
    },
    {
        "question": "What is the primary difference between print() and return?",
        "options": {
            "A": "print() saves data to a variable, return displays it",
            "B": "return sends data back to the caller, print() just displays it",
            "C": "They do the exact same thing",
            "D": "return can only be used outside functions"
        },
        "answer": "B"
    },
    {
        "question": "Which of the following is a mutable data type?",
        "options": {
            "A": "tuple",
            "B": "string",
            "C": "list",
            "D": "int"
        },
        "answer": "C"
    },
    {
        "question": "What data type does kwargs collect inside a function?",
        "options": {
            "A": "list",
            "B": "tuple",
            "C": "dictionary",
            "D": "string"
        },
        "answer": "C"
    },
    {
        "question": "What is the correct syntax for a function in Python?",
        "options": {
            "A": "function myFunc():",
            "B": "def myFunc():",
            "C": "create myFunc():",
            "D": "func myFunc()"
        },
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a loop that repeats while a condition is true?",
        "options": {
            "A": "repeat",
            "B": "for",
            "C": "while",
            "D": "loop"
        },
        "answer": "C"
    },
    {
        "question": "What is the output of bool(0)?",
        "options": {
            "A": "True",
            "B": "False",
            "C": "0",
            "D": "Error"
        },
        "answer": "B"
    },
    {
        "question": "What must a recursive function have to prevent an infinite loop?",
        "options": {
            "A": "A global variable",
            "B": "An else statement",
            "C": "A base case",
            "D": "A secondary loop"
        },
        "answer": "C"
    },
    {
        "question": "Which data structure stores key-value pairs?",
        "options": {
            "A": "list",
            "B": "tuple",
            "C": "set",
            "D": "dictionary"
        },
        "answer": "D"
    },
    {
        "question": "Which higher-order function is used to apply a function to all items of an iterable?",
        "options": {
            "A": "filter()",
            "B": "map()",
            "C": "transform()",
            "D": "lambda()"
        },
        "answer": "B"
    },
]

get_grade = lambda score: (
    "A+ (Outstanding)" if score >= 9 else
    "A (Great Job)" if score >= 7 else
    "B (Good Effort)" if score >= 5 else
    "C (Need Practice)"
)

get_percentage = lambda score, total: round((score / total) * 100,1)
def display_stars(n):
    if n == 0:
        return ""
    return "⭐" + display_stars(n-1)

def welcome_menu():
    print("=" * 45)
    print("      Welcome to the Python Quiz!      ")
    print("=" * 45)
    print("   Rules:")
    print("  → Total Questions: 10")
    print("  → Every question carries 1 mark.")
    print("  → No negative marking.")
    print("  → Invalid input = asked again!")
    print("=" * 45)

welcome_menu()
input("\nPress [Enter] to start the challenge...")
print("\nLoading questions...\n")

score = 0
valid_options = ["A", "B", "C", "D"]

for i, item in enumerate(questions, 1):
    print(f"\nQ{i}: {item['question']}")
    for key, val in item["options"].items():
        print(f"  {key}) {val}")
    
    while True:
        user_ans = input("\nYour answer (A/B/C/D): ").strip().upper()
        if user_ans in valid_options:
            break
        else:
            print(f" Invalid input! Please enter A,B,C, or D only.")

    if user_ans == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer was: {item['answer']}")
    print(f"Current Score: {score}/{i}")
    print("-" * 45)

percentage = get_percentage(score,10)
grade = get_grade(score)
stars = display_stars(score)

print("\n" + "=" * 45)
print("           Quiz Complete!           ")
print("=" * 45)
print(f"           Your Score: {score}/10")
print(f"  Percentage      : {percentage}%")
print(f"  Grade           : {grade}")
print(f"  Stars Earned    : {stars}")
print("=" * 45)
