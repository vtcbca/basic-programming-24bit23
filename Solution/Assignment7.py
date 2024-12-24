n = int(input("Enter the number of lines: "))

for i in range(1, n + 1):
    # Create the row of numbers
    row = " ".join(f"{j}" for j in range(1, 2 * i))
    # Center-align the row
    print(row.center(2 * n - 1))
