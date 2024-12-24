def pattern_alphabets_recursive(n, current=0):
    if current == n:
        return
    spaces = " " * (n - current - 1) * 4
    left = [chr(65 + j) for j in range(current + 1)]
    right = left[:-1][::-1]
    print(spaces + "   ".join(left + right))
    pattern_alphabets_recursive(n, current + 1)

# Example usage
pattern_alphabets_recursive(5)
