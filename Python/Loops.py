# Prompt the user to enter a number
number = int(input("Enter a number for the multiplication table: "))

# Generate the multiplication table from 1 to 12
print(f"Multiplication table for {number}:")
for i in range(1, 12 + 1):
    print(f"{number} x {i} = {number * i}")