#  Student Grade Manager

> Day 27 of #150DaysOfAI — Week 4 Project

##  About
A complete command-line student data
management system built with Python.
Manages multiple students with
multi-subject marks, automatic grading,
and class statistics.

##  Features
- Add students with 3 subject marks
- View all students with formatted output
- Search student by name
- Update marks anytime
- Delete student from system
- Find class topper automatically
- Show complete class statistics
- Menu-driven system with while loop

##  Menu Options
| # | Option | Description |
|---|--------|-------------|
| 1 | Add Student | Name + 3 subject marks |
| 2 | View All | Formatted table output |
| 3 | Search | Find by name |
| 4 | Update Marks | Edit any subject |
| 5 | Delete | Remove student |
| 6 | Show Topper | Highest average |
| 7 | Statistics | Class avg, highest, lowest |
| 8 | Exit | Goodbye message |

##  Grading System
| Average | Grade |
|---------|-------|
| 90%+ | A+ |
| 80%+ | A |
| 70%+ | B |
| 60%+ | C |
| Below 60% | F |

##  How to Run
```bash
python student_grade_manager.py
```

##  Sample Output
```
================================================
      STUDENT GRADE MANAGER 
      #150DaysOfAI — Day 27
================================================
1. Add Student
2. View All Students
3. Search Student
4. Update Marks
5. Delete Student
6. Show Topper
7. Show Statistics
8. Exit
================================================
Choice: 1

Enter student name: Ameer Hamza
Enter Python marks : 88
Enter Math marks   : 92
Enter AI marks     : 90

================================================
✅ Student Added Successfully!
Name    : Ameer Hamza
Total   : 270/300
Average : 90.0%
Grade   : A+
================================================
```

##  Concepts Used
`list of dictionaries` `nested data structures`
`lambda functions` `functions` `while loop`
`CRUD operations` `f-strings` `conditionals`
`sorting` `.items()` `.keys()` `.values()`

##  Data Structure
```python
students = [
    {
        "name": "Ameer Hamza",
        "marks": {
            "Python": 88,
            "Math": 92,
            "AI": 90
        },
        "total": 270,
        "average": 90.0,
        "grade": "A+"
    }
]
```

## 🔗 Part of #150DaysOfAI
- Daily practice: [150-days-of-ai](https://github.com/ameerhamza-ai/150-days-of-ai)
- All projects: [python-projects](https://github.com/ameerhamza-ai/python-projects)
- LinkedIn: [ameerhamzaai](https://linkedin.com/in/ameerhamzaai)