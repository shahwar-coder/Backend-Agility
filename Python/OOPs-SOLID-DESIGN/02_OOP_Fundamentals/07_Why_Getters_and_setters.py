'''
Why use getters and setters (in simple, interview-ready detail):

1. Encapsulation (Data Hiding)
   - We don’t expose internal variables directly.
   - Instead of accessing __password directly, we control access via methods/properties.
   - This prevents accidental misuse of important data.

2. Validation & Control
   - We can add rules when setting values.
   - Example: password must be at least 6 characters.
   - Without setters, anyone could assign invalid data.

3. Abstraction (Clean Interface)
   - User of the class interacts with simple attributes (u.password)
   - Internal logic (validation, formatting, security) is hidden.

4. Flexibility (Future Changes)
   - We can change internal implementation later without breaking external code.
   - Example: later we may hash the password instead of storing plain text.

5. Controlled Access (Read / Write Rules)
   - We can allow:
       - read-only access (only getter)
       - write-only access (only setter)
       - restricted updates (custom logic)

Important Design Insight:
- Use @property (getter/setter) for simple control (one input).
- Use methods when logic needs multiple inputs (e.g., change_password with old + new).

One-line Interview Answer:
"Getters and setters provide controlled access to data, enabling encapsulation, validation, and flexibility in design."
'''


'''
Example: One class demonstrating ALL 5 advantages of getters & setters
(Encapsulation, Validation, Abstraction, Flexibility, Controlled Access)
'''

# Example demonstrating all 5 advantages

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # (1) Encapsulation: hidden variable

    # (3) Abstraction: simple interface (u.password)
    @property
    def password(self):
        return "*****"  # (5) Controlled Access: read-only (hide actual value)

    # (2) Validation + (5) Controlled write
    @password.setter
    def password(self, new_password):
        if len(new_password) < 6:
            raise ValueError("Password must be at least 6 characters")
        # (4) Flexibility: we could hash here later without changing usage
        self.__password = new_password

    # Extra method (real-world usage)
    def check_password(self, pwd):
        return self.__password == pwd


# 🧪 Usage
u = User("shahwar", "secret123")

print(u.password)        # *****  (Abstraction + Controlled read)

u.password = "newpass"   # (Validation + Controlled write)

print(u.check_password("newpass"))  # True


'''
How each advantage is shown:

1. Encapsulation:
   __password is private (not directly accessible)

2. Validation:
   Setter checks password length before updating

3. Abstraction:
   User interacts with 'password' like a normal attribute

4. Flexibility:
   Internal logic can change (e.g., hashing) without affecting usage

5. Controlled Access:
   Getter hides real password, setter controls updates
'''