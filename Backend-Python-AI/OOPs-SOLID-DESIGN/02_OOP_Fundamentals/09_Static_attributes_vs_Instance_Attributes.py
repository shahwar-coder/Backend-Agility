# Static attributes

class User:
    user_count=0

    def __init__(self, username, email):
        self.username=username
        self.email=email
        User.user_count+=1

    def display_user(self):
        print(f"Username : {self.username}, Email : {self.email}")

user1 = User("Rahul", "rahul@gmail.com")
print(f"User count : {user1.user_count}")

user2 = User("Jacob", "jacob@gmail.com")
print(f"User count : {user1.user_count}")

user3 = User("Roy", "roy@gmail.com")
print(f"User count : {user1.user_count}")

user1.display_user()
user2.display_user()
user3.display_user()


# User count : 1
# User count : 2
# User count : 3
# Username : Rahul, Email : rahul@gmail.com
# Username : Jacob, Email : jacob@gmail.com
# Username : Roy, Email : roy@gmail.com



'''
This example demonstrates **static (class) attributes in Python**.

🔹 Static Attribute:
- user_count is a class variable → shared across ALL objects
- Defined at class level: User.user_count = 0

-------------------------------------------------------

🔹 How it works:
- Every time a new User is created:
  User.user_count += 1

Flow:
user1 → count = 1  
user2 → count = 2  
user3 → count = 3  

👉 All objects see the SAME shared value

-------------------------------------------------------

🔹 Accessing static variable:
- user1.user_count  ✅
- user2.user_count  ✅
- User.user_count   ✅ (best practice)

👉 Even though accessed via object, it refers to class-level data

-------------------------------------------------------

🔹 Instance vs Static:
- self.username → unique per object (instance variable)
- user_count    → shared across all objects (class variable)

-------------------------------------------------------

🔑 Key Concept:
👉 Class variables = shared state across instances

-------------------------------------------------------

🔥 Real-world example:
- Total users in system
- Total API requests
- Global configuration

-------------------------------------------------------

✅ Best Practice:
- Modify using class name: User.user_count
- Avoid modifying via instance (can create confusion)
'''