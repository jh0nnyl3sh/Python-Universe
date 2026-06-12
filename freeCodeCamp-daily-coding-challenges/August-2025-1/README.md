# Challenge: Vowel Balance

## 📝 Problem Statement
Given a **string**, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

* The letters `a, e, i, o, and u` (both uppercase and lowercase) are considered vowels.
* If there's an odd number of characters in the **string**, the center character is ignored.

## 💡 Solution Approach
1.  **Data Structure:** Used a **set** `("aeiouAEIOU")` for `O(1)` average time complexity lookups.
2.  **Slicing:** Divided the **string** into `first_half` and `second_half` using Python slicing techniques. Conditioned the split to ignore the exact middle character if the string length is odd.
3.  **Counting:** Utilized Python's `sum()` function with a generator expression to count the occurrences of vowels efficiently without writing manual **loop** blocks.

## 🚀 Complexity Analysis
* **Time Complexity:** `O(N)` where N is the length of the string. Slicing takes `O(N)` and iterating through both halves to count vowels takes `O(N)`.
* **Space Complexity:** `O(N)` due to creating new string slices for the two halves. The vowel lookup **set** takes `O(1)` space.

## 💻 Code
The solution is implemented in Python and can be found in `vowel_balance.py`.