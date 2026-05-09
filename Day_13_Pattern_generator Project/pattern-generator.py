def right_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

def inverted_triangle(n):
    for i in range(n, 0, -1):
        print("*" * i)

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def diamond(n):
    pyramid(n)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def number_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

            # New Pattern Added
def same_number_triangle(n):
    for i in range(1, n + 1):
        print((str(i) + " ") * i)

def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")

def main():
    while True:
        print("\n--- Pattern Generator Menu ---")
        print("1. Right Triangle")
        print("2. Inverted Triangle")
        print("3. Pyramid")
        print("4. Diamond")
        print("5. Number Triangle")
        print("6. Same Number Triangle (New!)")
        print("7. Hollow Square")
        print("8. Exit")

        choice = input("\nChoose a pattern (1-8): ")

        if choice == '8':
            print("Exiting... Happy Coding! ")
            break

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            try:
                size = int(input("Enter size of the pattern: "))
                if size <= 0:
                    print(" Error: Size must be a positive number!")
                    continue
            except ValueError:
                print(" Error: Invalid input! Please enter a numeric value (e.g., 5).")
                continue

            print("\nResult:")
            if choice == '1': right_triangle(size)
            elif choice == '2': inverted_triangle(size)
            elif choice == '3': pyramid(size)
            elif choice == '4': diamond(size)
            elif choice == '5': number_triangle(size)
            elif choice == '6': same_number_triangle(size)
            elif choice == '7': hollow_square(size)
        else:
            print("Invalid Choice! Please pick from the menu.")

if __name__ == "__main__":
    main()
