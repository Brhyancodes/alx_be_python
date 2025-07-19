# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Generate and print the square pattern
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
