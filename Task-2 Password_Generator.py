import string  # Import the string module to access predefined character sets (letters, digits, punctuation)
import random  # Import the random module to generate random selections

# Loop until a valid password length is entered
while True:
    try:
        # Ask user for password length
        length = int(input("Enter password length (positive integer): "))

        # Check if the entered length is positive
        if length <= 0:
            print("Please enter a positive integer.")  # Error message for non-positive length
        else:
            break  # Exit the loop if a valid length is entered
    except ValueError:
        # Handle invalid input (non-integer value)
        print("Invalid input! Please enter a valid positive integer.")

# Display options for character sets
print('''Choose character set for the password from these options:
         1. Letters
         2. Digits
         3. Special characters
         4. Done (Generate Password)
''')

# Initialize an empty string to store the selected character sets
characterList = ""

# Loop until a valid selection is made for character sets
while True:
    try:
        # Ask user to pick a character set option
        choice = int(input("Pick a number: "))

        # Add letters to the character list
        if choice == 1:
            characterList += string.ascii_letters  # Adds all letters (uppercase and lowercase)
            print("Letters added.")

        # Add digits to the character list
        elif choice == 2:
            characterList += string.digits  # Adds all digits (0-9)
            print("Digits added.")

        # Add special characters to the character list
        elif choice == 3:
            characterList += string.punctuation  # Adds all special characters (e.g., !@#$)
            print("Special characters added.")

        # Finish selecting character sets and proceed to password generation
        elif choice == 4:
            if not characterList:  # Check if no character set has been selected
                print("You must select at least one character set before generating a password!")
            else:
                break  # Exit the loop once at least one set is selected
        else:
            # Handle invalid choice (not in range 1-4)
            print("Please enter a valid option (1-4)!")
    except ValueError:
        # Handle invalid input (non-integer value)
        print("Invalid input! Please enter a number between 1 and 4.")

# Generate the password by selecting random characters from the chosen sets
password = [random.choice(characterList) for _ in range(length)]

# Display the randomly generated password
print("Random Password Generated: " + "".join(password))
