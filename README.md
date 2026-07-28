# Logic Gate, Adder & ALU Simulator

A small Python project simulating basic digital logic gates (AND, OR, NOT,
NAND, NOR, XOR, XNOR), combining them into half adder and full adder
circuits for binary addition, a two's complement subtractor, and a
minimal ALU that ties addition, subtraction, and bitwise logic together
under a single operation-code interface - a simplified model of how a
real CPU's arithmetic logic unit works.

## Why I built this

I'm a Computer Science student currently completing Coursera's
**"Digital Systems: From Logic Gates to Processors"**, and wanted to
reinforce the fundamentals by actually implementing them rather than
just reading about them. This project walks through the same
progression the course covers: individual gates, then half adders,
then full adders, then multi-bit binary addition - the same building
blocks used inside real ALUs and processors.

## Project structure

```
logic-gate-simulator/
├── gates.py       # Basic gate implementations (AND, OR, NOT, NAND, NOR, XOR, XNOR)
├── adder.py       # Half adder, full adder, and multi-bit binary addition
├── subtractor.py  # Two's complement subtraction, built on the adder
├── alu.py         # Minimal ALU: AND / OR / ADD / SUB via a 2-bit op code
├── main.py        # Command-line interface tying everything together
└── README.md
```

## How to run

```bash
python3 main.py
```

You'll get a simple menu to:
1. View the truth table for any gate
2. Add two binary numbers together using the full adder logic
3. Subtract two binary numbers using two's complement (handles negative results)
4. Run a mini ALU operation (AND, OR, ADD, or SUB) selected by a 2-bit op code,
   the same basic pattern real CPUs use to select which operation to execute

## Example

```
Enter first binary number (e.g. 101): 101
Enter second binary number (e.g. 011): 011

  101
+ 011
-----
  1000

(Check: 5 + 3 = 8, binary result = 8)
```

## What I learned building this

- How complex circuits (adders) are built by composing simple gates
- Why a full adder needs two half adders plus an OR gate for the carry
- How binary addition with carry propagation actually works bit by bit
- How subtraction can be implemented without a separate subtractor
  circuit, using two's complement (invert + add 1) on top of the
  adder that was already built
- How an ALU selects between operations using an op code, and why
  this same idea (a small set of primitive operations, selected by
  a control signal) scales up to real processor design

## Possible next steps

- Extend the ALU to more bits and more operations (e.g. multiplication via
  repeated addition, or a comparator)
- Build a visual/Streamlit version (see my `digital-logic-calculator` repo)
