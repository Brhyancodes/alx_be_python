# For loop for multiplication table
number = int(input("Enter a number to see its multiplication table: "))

# Generate and Print the Multiplication Table:
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
