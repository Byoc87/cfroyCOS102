def simple_interest(P, R, T):
    A = P * (1 + (R / 100) * T)
    return A


def compound_interest(P, R, n, t):
    A = P * (1 + R / (n * 100))**(n * t)
    return A


def annuity_plan(PMT, R, n, t):
    R_decimal = R / (100 * n)
    A = PMT * (((1 + R_decimal)**(n * t) - 1) / R_decimal)
    return A

def main():
    print("Select a formula:")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Annuity Plan")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        P = int(input("Enter Principal Amount (P): "))
        R = int(input("Enter Annual Interest Rate (R in %): "))
        T = int(input("Enter Time Period in Years (T): "))
        result = simple_interest(P, R, T)
        print(f"Final Amount (A) = {result:.2f}")

    elif choice == 2:
        P = int(input("Enter Principal Amount (P): "))
        R = int(input("Enter Annual Interest Rate (R in %): "))
        n = int(input("Enter Number of Times Interest is Compounded per Year (n): "))
        t = int(input("Enter Time Period in Years (t): "))
        result = compound_interest(P, R, n, t)
        print(f"Final Amount (A) = {result:.2f}")

    elif choice == 3:
        PMT = int(input("Enter Regular Payment Amount (PMT): "))
        R = int(input("Enter Annual Interest Rate (R in %): "))
        n = int(input("Enter Number of Payments per Year (n): "))
        t = int(input("Enter Number of Years (t): "))
        result = annuity_plan(PMT, R, n, t)
        print(f"Final Amount (A) = {result:.2f}")

    else:
        print("Invalid choice. Please select a valid option.")
main()