# This program checks whether a given number is positive, negative, or zero

# Get the number from the user
number = float(input("Please enter a number: "))

# Determine if the number is positive, negative, or zero
if number > 0:
    result = "positive"
elif number < 0:
    result = "negative"
else:
    result = "zero"

# Output the result
print(f"The number you entered is {result}.")
