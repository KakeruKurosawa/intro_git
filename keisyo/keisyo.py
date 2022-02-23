
class A:
    def hello(self):
        print("hello")

class B(A):
    def bye(self):
        print("good bye")

obj = B()
obj.hello()
obj.bye()