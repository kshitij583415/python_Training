class A:
    def __init__(self):
        self.a = 10
    def sample(self):
        print("classs A : HI")
 
class B(A):
    def sample_1(self):
        print("class B: hello")
        print("class a variable:",self.a)
 
class C(A):
    def xyz(self):
        print("Hi B")
 
obj1 = C()
obj2= B()
obj1.sample()
obj2.sample()
obj2.sample_1()
obj1.xyz()