"""
alu.py

A minimal Arithmetic Logic Unit (ALU) that ties together everything
built so far: bitwise AND/OR, addition, and subtraction, selected by
an operation code - the same basic idea used inside a real CPU's ALU,
just drastically simplified.

Operation codes:
    00 -> AND
    01 -> OR
    10 -> ADD
    11 -> SUBTRACT
"""

from gates import AND, OR
from adder import add_binary_numbers
from subtractor import subtract_binary_numbers

OPS = {
    "00": "AND",
    "01": "OR",
    "10": "ADD",
    "11": "SUB",
}


def bitwise(op, bits_a, bits_b):
    """Applies a bitwise gate operation across two equal-length bit lists."""
    width = max(len(bits_a), len(bits_b))
    a = [0] * (width - len(bits_a)) + bits_a
    b = [0] * (width - len(bits_b)) + bits_b
    return [op(x, y) for x, y in zip(a, b)]


def alu(op_code, bits_a, bits_b):
    """
    Runs the ALU operation selected by a 2-bit op_code string (e.g. "10").
    Returns a human-readable result string.
    """
    if op_code not in OPS:
        raise ValueError(f"Unknown op code: {op_code}")

    operation = OPS[op_code]

    if operation == "AND":
        result = bitwise(AND, bits_a, bits_b)
        return "".join(map(str, result))
    elif operation == "OR":
        result = bitwise(OR, bits_a, bits_b)
        return "".join(map(str, result))
    elif operation == "ADD":
        result = add_binary_numbers(bits_a, bits_b)
        return "".join(map(str, result))
    elif operation == "SUB":
        result, negative = subtract_binary_numbers(bits_a, bits_b)
        sign = "-" if negative else ""
        return sign + "".join(map(str, result))


if __name__ == "__main__":
    a = [1, 1, 0, 1]  # 13
    b = [0, 1, 0, 1]  # 5

    for code, name in OPS.items():
        print(f"{name} (op={code}): {a} {name} {b} = {alu(code, a, b)}")
