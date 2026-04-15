'''
This example clearly shows the difference between:
👉 Instance variables (per object)
👉 Class (static) variables (shared across all objects)

=======================================================

🔹 Class Variable (Static Attribute):
user_count = 0

- Defined at class level
- Shared across ALL instances of the class
- Only ONE copy exists in memory

👉 Updated using:
User.user_count += 1

-------------------------------------------------------

🔹 Instance Variables:
self.username
self.email

- Defined inside __init__ using self
- Each object gets its OWN copy

👉 Example:
user1.username → Rahul
user2.username → Jacob
user3.username → Roy

✔ Independent values per object

-------------------------------------------------------

🔁 Flow Understanding:

Step 1:
user1 = User(...)
→ user_count = 1

Step 2:
user2 = User(...)
→ user_count = 2

Step 3:
user3 = User(...)
→ user_count = 3

👉 Instance data changes per object
👉 Class data is shared and incremented globally

-------------------------------------------------------

🔍 Important Observation:

print(user1.user_count)
print(user2.user_count)

👉 Both print SAME value (latest count = 3)

Reason:
- Python first looks in instance
- If not found → looks in class

-------------------------------------------------------

⚠️ Common Mistake:

user1.user_count = 100

👉 This creates a NEW instance variable
👉 Does NOT change class variable

Correct way:
User.user_count = 100

-------------------------------------------------------

🔑 Core Difference:

Instance Variable:
- Defined with self
- Unique per object
- Stored inside object

Class Variable:
- Defined at class level
- Shared across all objects
- Stored in class

-------------------------------------------------------

🔥 Real-world Mapping:

Instance variables:
- username, email → user-specific data

Class variable:
- user_count → total users in system

-------------------------------------------------------

✅ Best Practices:

- Use instance variables for object-specific data
- Use class variables for shared/global state
- Always modify class variables using class name

-------------------------------------------------------

🎯 Interview One-liner:

👉 "Instance variables are unique per object, while class variables are shared across all instances."
'''