import random
import string

def generate_password():
    print("Welcome to the Secure Password Generator 🔐")

    try:
        # Step 1: User input for password length
        length = int(input("Enter the desired password length (minimum 4): "))

        if length < 4:
            print("Password length should be at least 4 characters.")
            return

        # Step 2: Define possible characters
        letters = string.ascii_letters  # A-Z and a-z
        digits = string.digits          # 0-9
        symbols = string.punctuation    # Special characters like @#$%

        # Combine all characters
        all_chars = letters + digits + symbols

        # Step 3: Randomly generate password
        password = ''.join(random.choice(all_chars) for _ in range(length))

        # Step 4: Display the result
        print("\nYour generated password is:\n", password)

    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Run the password generator
generate_password()
