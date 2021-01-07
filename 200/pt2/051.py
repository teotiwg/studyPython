class MyClass:
    def sayHello(self):
        print("Hello")

    def sayBye(self, name):
        print("%s! See you again!" %name)

obj = MyClass()
obj.sayHello()
obj.sayBye('Teo')