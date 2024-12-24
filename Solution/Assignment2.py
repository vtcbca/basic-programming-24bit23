def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not prime
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return sieve

def is_prime_sieve(n, sieve):
    if n < len(sieve):
        return sieve[n]
    return None  # Out of range

# Example usage
limit = 1000
sieve = sieve_of_eratosthenes(limit)
number = int(input(f"Enter a number (<= {limit}): "))
print(f"{number} is prime: {is_prime_sieve(number, sieve)}")
