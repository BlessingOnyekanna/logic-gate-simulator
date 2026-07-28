"""
subtractor.py

Binary subtraction implemented using two's complement addition,
reusing the same full_adder logic from adder.py. This mirrors how
real ALUs handle subtraction: A - B = A + (~B + 1), so no separate
"subtract" circuit is needed - just inversion (NOT) plus the adder
we already built.
"""

from gates import NOT
from adder import add_binary_numbers


def twos_complement(bits):
    """
    Returns the two's complement of a binary number (list of bits,
    MSB first): invert every bit, then add 1.
    """
    inverted = [NOT(b) for b in bits]
    one = [1]
    result = add_binary_numbers(inverted, one)

    # Keep the result the same width as the input (drop any overflow
    # carry beyond the original bit width, matching fixed-width
    # hardware behaviour)
    if len(result) > len(bits):
        result = result[-len(bits):]
    return result


def subtract_binary_numbers(bits_a, bits_b):
    """
    Computes bits_a - bits_b using two's complement addition.
    Both inputs are lists of bits (MSB first). Pads to equal width
    first so the two's complement is taken over the correct number
    of bits.
    Returns (result_bits, is_negative).
    """
    width = max(len(bits_a), len(bits_b))
    a = [0] * (width - len(bits_a)) + bits_a
    b = [0] * (width - len(bits_b)) + bits_b

    neg_b = twos_complement(b)
    raw_result = add_binary_numbers(a, neg_b)

    # Trim any overflow carry bit beyond our working width
    if len(raw_result) > width:
        raw_result = raw_result[-width:]

    dec_a = int("".join(map(str, a)), 2)
    dec_b = int("".join(map(str, b)), 2)
    is_negative = dec_a < dec_b

    if is_negative:
        # Convert back from two's complement to a readable magnitude
        magnitude_bits = twos_complement(raw_result)
        return magnitude_bits, True

    return raw_result, False


if __name__ == "__main__":
    tests = [
        ([1, 0, 1], [0, 1, 1]),   # 5 - 3 = 2
        ([0, 1, 1], [1, 0, 1]),   # 3 - 5 = -2
        ([1, 1, 1, 1], [0, 0, 0, 1]),  # 15 - 1 = 14
    ]
    for a, b in tests:
        result, negative = subtract_binary_numbers(a, b)
        sign = "-" if negative else ""
        result_str = sign + "".join(map(str, result))
        dec_a = int("".join(map(str, a)), 2)
        dec_b = int("".join(map(str, b)), 2)
        print(f"{a} - {b}  =>  {result_str}   (check: {dec_a} - {dec_b} = {dec_a - dec_b})")
