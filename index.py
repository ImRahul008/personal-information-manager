# Personal Information Manager
# My first Python project

# Welcome message
print("*" * 40)
print("    PERSONAL INFORMATION ")
print("*" * 40)
print()

# Store static information
name = "Mudavath Rahul Chowhan"
age = 23
city = "Hyderabad"
hobby = "Playing Cricket"

# Get user input
print("Please tell me about yourself:")
print("-" * 30)

favorite_food = input("What's your favorite food? ")
while favorite_food == "":
    print("Please enter a valid food!")
    favorite_food = input("What's your favorite food? ")

favorite_color = input("What's your favorite color? ")
while favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ")

favorite_game= input("What's your favorite game? ")
while favorite_game == "":
    print("Please enter a valid game!")
    favorite_game = input("What's your favorite game? ")

# Calculate age in months
age_in_months = age * 12

# Display all information
print()
print("*" * 40)
print("        YOUR INFORMATION")
print("*" * 40)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print(f"Favorite game: {favorite_game}")
print()

# Goodbye message
print("*" * 40)
print("Thanks for using this program!")
print("*" * 40)