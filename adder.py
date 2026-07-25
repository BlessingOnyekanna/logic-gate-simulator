"""
adder.py

Half adder and full adder circuits, built by combining the basic
gates defined in gates.py. This shows how simple gates compose into
circuits that actually do arithmetic - the same idea used inside
real ALUs and processors.
"""

from gates import XOR, AND, OR


def half_adder(a, b):
    """
    Adds two single bits.
    Returns (sum, carry).
    """
    sum_bit = XOR(a, b)
    carry_bit = AND(a, b)
    return sum_bit, carry_bit


def full_adder(a, b, carry_in):
    """
    Adds two bits plus a carry-in bit (built from two half adders).
    Returns (sum, carry_out).
    """
    sum1, carry1 = half_adder(a, b)
    sum2, carry2 = half_adder(sum1, carry_in)
    carry_out = OR(carry1, carry2)
    return sum2, carry_out


def add_binary_numbers(bits_a, bits_b):
    """
    Adds two binary numbers given as lists of bits (MSB first),
    e.g. add_binary_numbers([1,0,1], [0,1,1]) for 101 + 011.
    Returns the result as a list of bits (MSB first).
    """
    bits_a = bits_a[::-1]  # reverse so index 0 = least significant bit
    bits_b = bits_b[::-1]

    length = max(len(bits_a), len(bits_b))
    bits_a += [0] * (length - len(bits_a))
    bits_b += [0] * (length - len(bits_b))

    result = []
    carry = 0
    for i in range(length):
        s, carry = full_adder(bits_a[i], bits_b[i], carry)
        result.append(s)

    if carry:
        result.append(carry)

    return result[::-1]  # back to MSB-first order


if __name__ == "__main__":
    print("Half adder truth table (a, b -> sum, carry):")
    for a in (0, 1):
        for b in (0, 1):
            print(a, b, "->", half_adder(a, b))

    print("\nFull adder truth table (a, b, carry_in -> sum, carry_out):")
    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                print(a, b, c, "->", full_adder(a, b, c))

    print("\nExample: 101 + 011 =", add_binary_numbers([1, 0, 1], [0, 1, 1]))
