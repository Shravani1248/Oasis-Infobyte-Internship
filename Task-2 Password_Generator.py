import string
import random


while True:
    try:
        length = int(input("Enter password length (positive integer): "))
        if length <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a valid positive integer.")

print('''Choose character set for the password from these options:
         1. Letters
         2. Digits
         3. Special characters
         4. Done (Generate Password)
''')

characterList = ""

while True:
    try:
        choice = int(input("Pick a number: "))
        if choice == 1:
            characterList += string.ascii_letters
            print("Letters added.")
        elif choice == 2:
            characterList += string.digits
            print("Digits added.")
        elif choice == 3:
            characterList += string.punctuation
            print("Special characters added.")
        elif choice == 4:
            if not characterList:
                print("You must select at least one character set before generating a password!")
            else:
                break
        else:
            print("Please enter a valid option (1-4)!")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")

password = [random.choice(characterList) for _ in range(length)]

print("Random Password Generated: " + "".join(password))