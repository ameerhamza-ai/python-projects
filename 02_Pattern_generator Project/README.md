# 🔷 Pattern Generator

> Day 13 of #150DaysOfAI — Week 2 Project

## 📋 About
A menu-driven Python pattern generator
that prints 8 different shapes with
user-controlled size and full input
validation.

## ✨ Features
- 8 pattern types in one program
- User controls size dynamically
- Menu-driven system with while loop
- Input validation with try/except
- Error handling for invalid inputs
- Clean formatted output

## 🗂️ Patterns Available
| # | Pattern | Type |
|---|---------|------|
| 1 | Right Triangle | ⭐ Basic |
| 2 | Inverted Triangle | ⭐ Basic |
| 3 | Pyramid (Centered) | ⭐⭐ Medium |
| 4 | Diamond | ⭐⭐⭐ Hard |
| 5 | Number Triangle | ⭐⭐ Medium |
| 6 | Same Number Triangle | ⭐⭐ Medium |
| 7 | Hollow Square | ⭐⭐ Medium |
| 8 | Exit | — |

## 🛠️ Concepts Used
`nested for loops` `while loop`
`functions` `if/elif/else`
`try/except` `string multiplication`
`input validation` `continue`

## ▶️ How to Run
```bash
python pattern_generator.py
```

## 📸 Sample Output
```
--- Pattern Generator Menu ---
1. Right Triangle
2. Inverted Triangle
3. Pyramid
4. Diamond
5. Number Triangle
6. Same Number Triangle
7. Hollow Square
8. Exit

Choose a pattern (1-8): 4
Enter size of the pattern: 5

Result:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

## 🏆 Highlights
- Diamond pattern uses function calling
  (pyramid() called inside diamond())
- Error handling prevents crashes
  on invalid or negative input
- Same Number Triangle added as
  bonus pattern beyond original plan

## 🔗 Part of #150DaysOfAI
- Daily practice: [150-days-of-ai](https://github.com/ameerhamza-ai/150-days-of-ai)
- All projects: [python-projects](https://github.com/ameerhamza-ai/python-projects)
- LinkedIn: [ameerhamzaai](https://linkedin.com/in/ameerhamzaai)
