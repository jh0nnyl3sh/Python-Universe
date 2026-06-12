def is_balanced(s: str) -> bool:
    """
    Given a string, determines whether the number of vowels in the first half 
    is equal to the number of vowels in the second half.
    Ignores the center character if the string length is odd.
    """
    vowels = set("aeiouAEIOU")
    mid = len(s) // 2
    
    first_half = s[:mid]
    # Tek sayı ise ortadaki karakteri atla, çift ise direkt ortadan böl
    second_half = s[mid + 1:] if len(s) % 2 != 0 else s[mid:]
    
    # Her iki yarıdaki ünlü harfleri generator ile say (Daha Pythonic ve Memory-efficient)
    first_half_vowels = sum(1 for char in first_half if char in vowels)
    second_half_vowels = sum(1 for char in second_half if char in vowels)
            
    return first_half_vowels == second_half_vowels

# Test Cases
if __name__ == "__main__":
    print(is_balanced("hello"))      # Output: False (e != o)
    print(is_balanced("aebcdiou"))   # Output: False (ae = 2, iou = 3)
    print(is_balanced("racecar"))    # Output: True (a = 1, a = 1)