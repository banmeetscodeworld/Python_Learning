class MyClass:

    # Class variable
    var1 ="Apple"

    # Instance variable
    def __init__(self, dyn1):
        self.dyn1= dyn1

    def func1(self):
        print(f"Hello, {self.dyn1}")

    def func(self):
        print("Hello, World!")

obj = MyClass("Bunny");
#obj.func1()


MyClass.func1(obj) # Calling func1 using the class name and passing the instance explicitly- how the self gets it - behind the scenes always goes like this
obj.var2 = "Carrot"
print(obj.var2)