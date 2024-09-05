# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

# def print_greeting():
#     # Your code goes here. Remember to indent!
#     python_is_fun = True
#     if python_is_fun:
#         print("Python is fun!")

# # Call the function
# print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.


# def check_letter():
#     vowels = ['a','A','e','E','i','I','o','O','u','U']
#     consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y']
#     letter = input("Enter a letter:")
#     letter = letter.lower()
#     if letter in vowels:
#         print(f"The letter {letter} is a vowel.")
#     elif letter in consonants:
#         print(f"The letter {letter} is a consonant.")
#     else:
#         print(f"{letter} is an invalid entry, please try again.")

# # Call the function
# check_letter()



 # Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

# def check_voting_eligibility():
#     age = input("Please enter your age: ")
#     age = int(age)
#     VOTING_AGE = 18
#     if age >= VOTING_AGE:
#         print("You are old enough to vote!")
#     elif age <= VOTING_AGE:
#         print("You are too young to vote!")
#     # Your control flow logic goes here

# # Call the function
# check_voting_eligibility()



# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

# def calculate_dog_years():
#     dog_age = input("Input a dog's age: ")
#     dog_age = int(dog_age)
#     if dog_age <= 2:
#         calc_age = dog_age * 10
#     elif dog_age > 2:
#         calc_age = (dog_age - 2) * 7
#         calc_age = calc_age + 20
#     print(f"The dog's age in dog years is {calc_age}.")


# # Call the function
# calculate_dog_years()



# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

# def weather_advice():
#     chilly = input("Is it cold outside? (yes/no)")
#     if chilly == 'yes':
#         chilly = True
#     elif chilly == 'no':
#         chilly = False
#     else: 
#         print("Invalid input.")
#     rain = input("Is it raining? (yes/no)")
#     if rain == 'yes':
#         rain = True
#     elif rain == 'no':
#         rain = False
#     else: 
#         print("Invalid input.")


#     if chilly is True and rain is True:
#         print("Wear a rain coat.")
#     elif chilly is True and rain is False:
#         print("Wear a warm coat.")
#     elif chilly is False and rain is True:
#         print("Carry an umbrella.")
#     elif chilly is False and rain is False:
#         print("Wear light clothing.")
#     else: 
#         print("Error.")

# # Call the function
# weather_advice()



