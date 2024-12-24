def fibonacci_recursive_max(max_val, a=0, b=1, sequence=None):
    if sequence is None:
        sequence = []
    if a >= max_val:
        return sequence
    sequence.append(a)
    return fibonacci_recursive_max(max_val, b, a + b, sequence)

# Example: Generate Fibonacci numbers less than 50
print(fibonacci_recursive_max(50))
