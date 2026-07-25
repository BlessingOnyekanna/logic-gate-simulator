"""
gates.py

Basic digital logic gate implementations.
Each gate takes 0/1 (or True/False) inputs and returns 0 or 1.

Built while studying "Digital Systems: From Logic Gates to Processors"
(Coursera) as a way to reinforce the fundamentals hands-on.
"""


def AND(a, b):
    return int(a == 1 and b == 1)


def OR(a, b):
    return int(a == 1 or b == 1)


def NOT(a):
    return int(a == 0)


def NAND(a, b):
    return NOT(AND(a, b))


def NOR(a, b):
    return NOT(OR(a, b))


def XOR(a, b):
    return int(a != b)


def XNOR(a, b):
    return NOT(XOR(a, b))


GATES = {
    "AND": AND,
    "OR": OR,
    "NOT": NOT,
    "NAND": NAND,
    "NOR": NOR,
    "XOR": XOR,
    "XNOR": XNOR,
}


def truth_table(gate_name):
    """Return the truth table rows for a named gate as a list of tuples."""
    gate = GATES[gate_name]
    rows = []

    if gate_name == "NOT":
        for a in (0, 1):
            rows.append((a, gate(a)))
    else:
        for a in (0, 1):
            for b in (0, 1):
                rows.append((a, b, gate(a, b)))

    return rows


if __name__ == "__main__":
    # Quick manual check when running this file directly
    for name in GATES:
        print(f"\n{name} truth table:")
        for row in truth_table(name):
            print(row)
