# Challenge: Base Check

## 📝 Problem Statement
Given a **string** representing a number, and an **integer** base from 2 to 36, determine whether the number is valid in that base.

* The string may contain integers, and uppercase or lowercase characters.
* The check is **case-insensitive**.
* A number is valid if every character is a valid digit in the given base.
    * Base 2: `0-1`
    * Base 10: `0-9`
    * Base 16: `0-9` and `A-F`
    * Base 36: `0-9` and `A-Z`

## 💡 Solution Approach
1. **Character Mapping:** Utilized Python's `string.digits` and `string.ascii_uppercase` to dynamically generate the valid characters based on the given base.
2. **Data Structure Optimization:** Converted the generated valid characters string into a **set** (`allowed_set`). This reduces the lookup time for each character from `O(B)` to `O(1)`.
3. **Validation:** Used the built-in `all()` function alongside a **generator expression** to efficiently iterate through the uppercase version of the input **string** and validate each character.

## 🚀 Complexity Analysis
* **Time Complexity:** `O(N)` where N is the length of the input **string**. Generating the allowed characters takes `O(B)` where B is the base (max 36, treated as constant). Iterating through the string takes `O(N)` with an `O(1)` check per character.
* **Space Complexity:** `O(B)` to store the allowed characters in a **set**. Since the maximum base is 36, the space requirement is minimal and constant `O(1)`.

## 💻 Code
The optimized solution is implemented in Python and can be found in `base_check.py`.