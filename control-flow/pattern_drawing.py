# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

# Use while loop to go through each row
while row < size:
    # Use a for loop to print asterisks for each row
    for _ in range(size):
        print("*", end="")  # Print asterisk without a newline
    print()  # Print newline after each row
    row += 1  # Move to the next row
