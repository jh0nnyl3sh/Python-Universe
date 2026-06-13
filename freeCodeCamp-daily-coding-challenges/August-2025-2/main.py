import string

def is_valid_number(n: str, base: int) -> bool:
    """
    Given a string representing a number and an integer base (2-36), 
    determines whether the number is valid in that base.
    """
    # Base sınırlarını kontrol etmek iyi bir defensive programming pratiğidir
    if not 2 <= base <= 36:
        return False

    digits = string.digits        
    letters = string.ascii_uppercase  

    if base <= 10:
        allowed = digits[:base]
    else:
        allowed = digits + letters[:base-10]

    # Look-up işlemini O(1) yapmak için allowed değişkenini set'e çeviriyoruz
    allowed_set = set(allowed)

    return all(ch in allowed_set for ch in n.upper())

# Test Cases
if __name__ == "__main__":
    print(is_valid_number("1010", 2))   # True
    print(is_valid_number("12", 2))     # False
    print(is_valid_number("A1", 16))    # True
    print(is_valid_number("Z3", 36))    # True