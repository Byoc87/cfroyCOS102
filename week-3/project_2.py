import sympy as sp


def find_quadratic_roots():
    a = float(input("Enter coefficient A: "))
    b = float(input("Enter coefficient B: "))
    c = float(input("Enter coefficient C: "))

    x = sp.symbols('x')
    roots = sp.solve(a * x ** 2 + b * x + c, x)
    print("Quadratic equation roots:", roots)


def find_cubic_roots():
    a = float(input("Enter coefficient A: "))
    b = float(input("Enter coefficient B: "))
    c = float(input("Enter coefficient C: "))
    d = float(input("Enter coefficient D: "))

    x = sp.symbols('x')
    roots = sp.solve(a * x ** 3 + b * x ** 2 + c * x + d, x)
    print("Cubic equation roots:", roots)


def find_quartic_roots():
    a = float(input("Enter coefficient A: "))
    b = float(input("Enter coefficient B: "))
    c = float(input("Enter coefficient C: "))
    d = float(input("Enter coefficient D: "))
    e = float(input("Enter coefficient E: "))

    x = sp.symbols('x')
    roots = sp.solve(a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e, x)
    print("Quartic equation roots:", roots)


def main():
    while True:
        print("\nChoose an equation type:")
        print("1. Quadratic (Ax² + Bx + C = 0)")
        print("2. Cubic (Ax³ + Bx² + Cx + D = 0)")
        print("3. Quartic (Ax⁴ + Bx³ + Cx² + Dx + E = 0)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            find_quadratic_roots()
        elif choice == '2':
            find_cubic_roots()
        elif choice == '3':
            find_quartic_roots()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
