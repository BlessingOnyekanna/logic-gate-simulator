"""
main.py

Simple command-line interface for the logic gate simulator.
Lets you view truth tables for individual gates, or add two
binary numbers using the full adder circuit.
"""

from gates import GATES, truth_table
from adder import add_binary_numbers
from subtractor import subtract_binary_numbers
from alu import alu, OPS


def print_truth_table(gate_name):
    print(f"\n{gate_name} truth table:")
    if gate_name == "NOT":
        print("A | OUT")
        for a, out in truth_table(gate_name):
            print(f"{a} | {out}")
    else:
        print("A B | OUT")
        for a, b, out in truth_table(gate_name):
            print(f"{a} {b} | {out}")


def run_adder():
    a = input("Enter first binary number (e.g. 101): ").strip()
    b = input("Enter second binary number (e.g. 011): ").strip()

    bits_a = [int(ch) for ch in a]
    bits_b = [int(ch) for ch in b]

    result = add_binary_numbers(bits_a, bits_b)
    result_str = "".join(str(bit) for bit in result)

    print(f"\n  {a}")
    print(f"+ {b}")
    print("-" * (max(len(a), len(b)) + 2))
    print(f"  {result_str}")

    dec_a = int(a, 2)
    dec_b = int(b, 2)
    print(f"\n(Check: {dec_a} + {dec_b} = {dec_a + dec_b}, "
          f"binary result = {int(result_str, 2)})")


def run_subtractor():
    a = input("Enter first binary number (e.g. 101): ").strip()
    b = input("Enter second binary number to subtract (e.g. 011): ").strip()

    bits_a = [int(ch) for ch in a]
    bits_b = [int(ch) for ch in b]

    result, negative = subtract_binary_numbers(bits_a, bits_b)
    sign = "-" if negative else ""
    result_str = sign + "".join(str(bit) for bit in result)

    dec_a = int(a, 2)
    dec_b = int(b, 2)
    print(f"\n  {a}")
    print(f"- {b}")
    print("-" * (max(len(a), len(b)) + 2))
    print(f"  {result_str}")
    print(f"\n(Check: {dec_a} - {dec_b} = {dec_a - dec_b})")


def run_alu():
    print("\nAvailable operations:")
    for code, name in OPS.items():
        print(f"  {code} = {name}")
    op_code = input("Enter op code (00/01/10/11): ").strip()
    a = input("Enter first binary number: ").strip()
    b = input("Enter second binary number: ").strip()

    bits_a = [int(ch) for ch in a]
    bits_b = [int(ch) for ch in b]

    try:
        result = alu(op_code, bits_a, bits_b)
        print(f"\nALU result ({OPS[op_code]}): {result}")
    except ValueError as e:
        print(e)


def main():
    while True:
        print("\n=== Logic Gate, Adder & ALU Simulator ===")
        print("1. View a gate's truth table")
        print("2. Add two binary numbers (full adder)")
        print("3. Subtract two binary numbers (two's complement)")
        print("4. Run a mini ALU operation (AND / OR / ADD / SUB)")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            print("Available gates:", ", ".join(GATES.keys()))
            gate_name = input("Enter gate name: ").strip().upper()
            if gate_name in GATES:
                print_truth_table(gate_name)
            else:
                print("Unknown gate. Try again.")
        elif choice == "2":
            run_adder()
        elif choice == "3":
            run_subtractor()
        elif choice == "4":
            run_alu()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
