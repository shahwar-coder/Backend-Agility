class User:
    def __init__(self, password):
        self.__password = password  # private

    # Getter (hide actual password)
    @property
    def password(self):
        return "*****"

    # Method to change password safely (Better than just a normal setter)
    def change_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            print("Password updated")
        else:
            print("Wrong old password")


'''
This example shows **Encapsulation with controlled access** using
a private variable + getter + method.

🔹 Private Variable:
- __password → stored securely (name mangled)
- Cannot be accessed directly from outside

-------------------------------------------------------

🔹 Getter using @property:
- password() method acts like an attribute: user.password
- Instead of returning the real password, it returns "*****"

👉 Purpose:
Hide sensitive data (security)

Example:
user = User("secret123")
print(user.password)  # ***** (not actual password)

-------------------------------------------------------

🔹 Controlled Update Method:
- change_password(old_password, new_password)

Flow:
1. User provides old password
2. System verifies it
3. If correct → updates password
4. If wrong → shows error

👉 This ensures:
- No direct modification
- Proper validation before update

-------------------------------------------------------

🔑 Key Concept:
👉 Encapsulation = hide data + provide controlled access

-------------------------------------------------------

✅ Real-world analogy:
Like ATM PIN:
- You cannot see the stored PIN
- You must verify old PIN to change it

-------------------------------------------------------

🔥 Best Practice:
Never expose sensitive data directly
Always use methods for access/update
'''