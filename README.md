# Logic Gate & Adder Simulator

A small Python project simulating basic digital logic gates (AND, OR, NOT,
NAND, NOR, XOR, XNOR) and combining them into half adder and full adder
circuits capable of adding binary numbers of any length.

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
├── gates.py    # Basic gate implementations (AND, OR, NOT, NAND, NOR, XOR, XNOR)
├── adder.py    # Half adder, full adder, and multi-bit binary addition
├── main.py     # Command-line interface tying everything together
└── README.md
```

## How to run

```bash
python3 main.py
```

You'll get a simple menu to:
1. View the truth table for any gate
2. Add two binary numbers together using the full adder logic

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

## Possible next steps

- Add a subtractor circuit
- Extend to a simple 4-bit ALU
- Build a visual/Streamlit version (see my `digital-logic-calculator` repo)
