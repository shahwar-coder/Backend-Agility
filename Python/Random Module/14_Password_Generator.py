'''
Password Generator:
Create a random password of length 10 characters.
The password must include:
- Uppercase letters
- Lowercase letters
- Digits
- Special symbols
'''

import string
import random
# Instead of random secrets can be used (just replace random words everywhere with secrets, it is safer)
def generate_password(chars: int)->str:
    '''
    Generate a random password of given length containing:
    - at least one uppercase letter
    - at least one lowercase letter
    - at least one digit
    - at least one special symbol
    '''
    if chars < 8:
        raise ValueError("Minimum password length should be 8")
    
    mandatory_upper = random.choice(string.ascii_uppercase)
    mandatory_lower = random.choice(string.ascii_lowercase)
    mandatory_digit =  random.choice(string.digits)
    mandatory_symbol = random.choice(string.punctuation)
    all_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    rest_chars = random.choices(population = all_characters, k=(chars-4))

    password_list = [mandatory_upper, mandatory_lower, mandatory_symbol, mandatory_digit] + rest_chars

    random.shuffle(password_list)
    return ''.join(password_list)

def get_user_input()->int:
    '''
    Take valid user input
    '''
    try:
        chars = int(input("Length of password: "))
        return chars
    except ValueError as err:
        raise ValueError("Input should be an integer") from err

def main()->None:
    try:
        chars = get_user_input()
        password = generate_password(chars)
        print(f"PASSWORD: {password}")
    except (ValueError) as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Length of password: 12
# PASSWORD: h`T&'iG|M-6z

'''
# Key Points (Solution)
- Uses string module to access character groups (uppercase, lowercase, digits, symbols).
- Ensures password contains at least one character from each required category.
- Validates minimum password length (>= 8).
- Fills remaining characters randomly from all allowed characters.
- Shuffles characters to avoid predictable positions.
- Returns the final password as a string.
- Clean separation of input handling, logic, and execution.

# Key Points (Output)
- Output is a string of the requested length.
- Contains uppercase, lowercase, digit, and special symbol.
- Order of characters is random on every run.
- Example output: PASSWORD: A9$kPq!2mZ

# Important Note
- random is fine for practice; secrets is recommended for real security use.
- Shuffling improves randomness and password strength.
'''
