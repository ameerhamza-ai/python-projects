# ==========================================
# Day 27 — Student Grade Manager Project
# #150DaysOfAI
# ==========================================

# Global List of Dictionaries to store all students
students_db = []

# --- HELPER FUNCTIONS ---

# 1. Lambda function to calculate grade based on average
get_grade = lambda avg: (
    "A+" if avg >= 90 else
    "A"  if avg >= 80 else
    "B"  if avg >= 70 else
    "C"  if avg >= 60 else
    "F"
)

# 2. Function to calculate total, average, and grade
def calculate_stats(marks_dict):
    total = sum(marks_dict.values())
    average = total / len(marks_dict)
    grade = get_grade(average)
    return total, round(average, 2), grade

# 3. Function to nicely display a single student's record
def display_student(student):
    print(f"Name    : {student['name']}")
    print(f"Marks   : Python ({student['marks']['Python']}), Math ({student['marks']['Math']}), AI ({student['marks']['AI']})")
    print(f"Total   : {student['total']}/300")
    print(f"Average : {student['average']}%")
    print(f"Grade   : {student['grade']}")

# 4. Function to find the student with the highest average
def find_topper():
    if not students_db:
        return None
    # Using max with a lambda key to check the 'average' field
    topper = max(students_db, key=lambda s: s['average'])
    return topper


# --- MAIN MENU LOOP ---
while True:
    print("\n" + "="*48)
    print("      STUDENT GRADE MANAGER ")
    print("      #150DaysOfAI — Day 27")
    print("="*48)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Show Statistics")
    print("8. Exit")
    print("="*48)

    choice = input("Choice: ").strip()

    # -------------------------
    # 1. ADD STUDENT
    # -------------------------
    if choice == '1':
        name = input("\nEnter student name: ").strip()

     # Gathering marks
        try:
            py = int(input("Enter Python marks: "))
            math = int(input("Enter Math marks: "))
            ai = int(input("Enter AI marks: "))

        # Pack marks into a dictionary
            marks = {"Python": py, "Math": math, "AI": ai}

        # Calculate stats
            total, avg, grade = calculate_stats(marks)

        # Create the student dictionary
            student = {
                    "name": name,
                    "marks": marks,
                    "total": total,
                    "average": avg,
                    "grade": grade
                }

            # Add to database
            students_db.append(student)

            print("\n" + "="*48)
            print(" Student Added Successfully!")
            display_student(student)
            print("="*48)

        except ValueError:
                print(" Invalid input! Please enter numbers for marks.")

    # -------------------------
    # 2. VIEW ALL STUDENTS
    # -------------------------
    elif choice == '2':
        print("\n---  All Enrolled Students ---")
        if not students_db:
            print("No students found in the database.")
        else:
            for idx, student in enumerate(students_db, 1):
                print(f"\nStudent #{idx}:")
                display_student(student)

    # -------------------------
    # 3. SEARCH STUDENT
    # -------------------------
    elif choice == '3':
        search_name = input("\nEnter student name to search: ").strip()
        found = False
        for student in students_db:
            if student['name'].lower() == search_name.lower():
                print("\n Student Found!")
                display_student(student)
                found = True
                break

            if not found:
                print(f" Student '{search_name}' not found.")

    # -------------------------
    # 4. UPDATE MARKS
    # -------------------------
    elif choice == '4':
        search_name = input("\nEnter student name to update marks: ").strip()
        found = False
        for student in students_db:
            if student['name'].lower() == search_name.lower():
                print(f"\nUpdating marks for {student['name']}...")
                try:
                    py = int(input("Enter new Python marks: "))
                    math = int(input("Enter new Math marks: "))
                    ai = int(input("Enter new AI marks: "))

                    student['marks'] = {"Python": py, "Math": math, "AI": ai}
                    total, avg, grade = calculate_stats(student['marks'])

                    # Update the remaining fields
                    student['total'] = total
                    student['average'] = avg
                    student['grade'] = grade

                    print("\n Marks Updated Successfully!")
                    display_student(student)
                except ValueError:
                    print(" Invalid input! Marks must be numbers.")
                    found = True
                    break

        if not found:
            print(f" Student '{search_name}' not found.")

    # -------------------------
    # 5. DELETE STUDENT
    # -------------------------
    elif choice == '5':
        search_name = input("\nEnter student name to delete: ").strip()
        found = False
        for student in students_db:
            if student['name'].lower() == search_name.lower():
                students_db.remove(student)
                print(f"\n Student '{student['name']}' deleted successfully.")
                found = True
                break

        if not found:
            print(f" Student '{search_name}' not found.")

    # -------------------------
    # 6. SHOW TOPPER
    # -------------------------
    elif choice == '6':
        topper = find_topper()
        if topper:
            print("\n --- CLASS TOPPER --- ")
            display_student(topper)
        else:
            print("\n No students in database yet.")

    # -------------------------
    # 7. SHOW STATISTICS
    # -------------------------
    elif choice == '7':
        if not students_db:
            print("\n No students to show statistics for.")
        else:
            total_students = len(students_db)
            class_total_marks = sum(s['total'] for s in students_db)
            class_avg = class_total_marks / (total_students * 300) * 100

            print("\n --- CLASS STATISTICS ---")
            print(f"Total Students : {total_students}")
            print(f"Class Average  : {round(class_avg, 2)}%")

            # Count passing students (Grade A+, A, B, C)
            passed = sum(1 for s in students_db if s['grade'] != 'F')
            print(f"Pass Rate      : {passed}/{total_students}")

    # -------------------------
    # 8. EXIT
    # -------------------------
    elif choice == '8':
        print("\n Exiting Student Grade Manager. Goodbye!")
        break

    else:
        print("\n Invalid choice! Please select a number from 1 to 8.")