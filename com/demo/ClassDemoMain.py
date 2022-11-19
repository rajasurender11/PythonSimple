class Person:
    id =None
    emp_name = None
    m1 =None
    m2 =None
    result = 0

    def __init__(self,a,b,c,d):
        self.id =a
        self.emp_name = b
        self.m1 =c
        self.m2 =d

    def add_marks(self):
        self.result = self.m1 +self.m2

def main():
 p = Person(200,"raja",99,45)#object or instance creation
 print(p.id)
 print(p.emp_name)
 print(p.m1)
 print(p.m2)
 print(p.result)
 p.add_marks()
 print(p.result)


 p1 = Person(201,"kumar",42,77)
 print(p1.id)
 print(p1.emp_name)
 print(p1.m1)
 print(p1.m2)






if __name__ == "__main":
    main()

