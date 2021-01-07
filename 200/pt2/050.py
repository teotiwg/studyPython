class MyClass:
    var = 'Hello!'
    def sayHello(self):
        param1 = "hello"
        self.param2 = "hi"
        print(param1)
        print(self.var)

obj = MyClass()
print(obj.var)
obj.sayHello()

# 클래스에서 선언되는 변수에는 클래스 멤버와 인스턴스멤버가 있음
# 클래스 멤버는 클래스 메소드 밖에서 선언됌
# 인스턴스 멤버는 메소드 안에서 self와 함께 선언되는 변수