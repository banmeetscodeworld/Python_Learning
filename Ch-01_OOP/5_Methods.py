class MyClass:
    var =100

#*
obj = MyClass()
obj.var= 200
print(obj.var)

obj2 = MyClass()
print(obj2.var)

print("------------------")

class MyClass2:
    var=100

    #dunder or magic method
    def __init__(self):
        print("This is the constructor")

    def __str__(self):
        return "This is the string representation"

    @classmethod
    def _change_value(cls, new_value):
        cls.var = new_value

    @staticmethod
    def dummy():
        print("This is a static method")                                                                                                                                                                                                   

obj1 = MyClass2()
print(obj1.var)
obj1._change_value(200)
print(obj1.var)

obj2 = MyClass2()
print(obj2.var)

print("------------------")
obj3= MyClass2()
#print(obj3.dummy())


print("------------------")
#print(obj3.__str__())

obj4= MyClass2()
print(obj4)

