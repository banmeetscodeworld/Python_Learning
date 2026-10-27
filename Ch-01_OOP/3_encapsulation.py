class MyClass:

    # Class variable
    var1 ="Apple"

    # Instance variable
    def __init__(self, dyn1, dyn2, dyn3):
        self.dyn1= dyn1 #public variable
        self.__dyn2= dyn2 #private variable
        self._dyn3 = dyn3 #protected variable

    def func1(self):
        print(f"Hello, {self.dyn1}")

    def func2(self):
        print(f"Hello, {self.__dyn2}")

obj = MyClass("Bunny", "Secret", "change");
obj.dyn1= "Ban"
obj.func1()


#print(obj.__dyn2) #gives error we cannot access it
obj.func2() 
obj.__dyn2= "kaur"
print(obj.__dyn2)
obj.func2()
print(obj._dyn3)
