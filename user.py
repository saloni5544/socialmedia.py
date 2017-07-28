class User:
    #fields and method definitions
    def __init__ (self,name,number):
        self.name=name
        self.genders=[]
        self.countries=[]
        self.age=number
        self.hungry=False

    def password(self,password):
        self.password=password

input_name= input('What is your name?')
input_age=input('What is your age?')
myuser= User(input_name,input_age)
input_user=input("Choose a username.")
myuser.add_username(input_user)
input_password=input('Choose a password.')
myuser.add_password(input_password)
input_friends=input('Add friends')
myuser.add_friends(input_friends)

while 0<1:
    decision = input('Do you wanna make another user? Y for ye; N for no.')
