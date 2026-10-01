# PLP Python Week 6 - Safe Functions

`safe_tools.py` - Contains three safe functions for division, number conversion, and dictionary field lookup.

`unbreakable.py` - Demonstrates how to safely convert text into numbers without crashing when the input is invalid.

An `if` check cannot catch `abc` on its own because checking whether text looks like a number is different from actually converting it with `int()`. The `int()` conversion raises a `ValueError` when the text cannot be converted, so `try` and `except` can handle that error safely.
