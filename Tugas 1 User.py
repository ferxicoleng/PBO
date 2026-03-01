class User :
    def __init__(self,first_name,last_name,date_of_birth,address):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
    def describe_user(self):
        print(f"Name : {self.first_name} {self.last_name}")
        print(f"Date of birth : {self.date_of_birth}")
        print(f"Address : {self.address}")
    def greet_user(self):
        print(f"Hello, {self.first_name} welcome.")

my_name = User('Muhammad','Nabil','12-01-2000','Garuda street Number 3')
my_name.describe_user()
my_name.greet_user()
print( )

b_name = User('Budi','Setiawan','12-01-2004','Nila street Number 4')
b_name.describe_user()
b_name.greet_user()
print( )

a_name = User('Anto','Kurnia','12-01-2000','Garuda street Number 3')
a_name.describe_user()
a_name.greet_user()
print( )

c_name = User('Imam','Shaleh','12-01-2000','Garuda street Number 3')
c_name.describe_user()
c_name.greet_user()
print( )

