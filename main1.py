current_year = datetime.now().year

# Get user input
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

# Calculate age
age = current_year - birth_year

# Display the result
print("Hello {name}, you are {age} years old.")