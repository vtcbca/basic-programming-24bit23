def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize the string
    stack = list(s)
    reversed_s = ''.join(stack[::-1])
    return s == reversed_s

# Example usage
print(is_palindrome("noon"))  # True
print(is_palindrome("data"))  # False
