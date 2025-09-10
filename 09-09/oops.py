class student:
    def __init__(self, name, age):
        print("Constructor called")
        self.name=name
        self.age=age
        self.__privateVar=100 
        
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Private Variable:", self.__privateVar)
        
    def __del__(self):
        print("Destructor called")
        

s1=student("Kshitij",21)
s1.display()

#output
# Constructor called
# Name: Kshitij
# Age: 21
# Private Variable: 100
# Destructor called

