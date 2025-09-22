class student:
    
    cnt=0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def f(cls):
        cls.cnt += 1
        print("Class method called", cls.cnt)

    @staticmethod
    def is_adult():
        print("Static method called")

s1 = student("Kshitij", 21)
s2 = student("Rahul", 22)

s1.f()
s2.f()
s1.is_adult()
s2.is_adult()
