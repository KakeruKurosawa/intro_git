class Greet():
  def hello(self):
    print("Hello!")

  def bye():
    print("Bye!")

class Greet2(Greet):
  def hello(self, name = None):
    if name:
        print(name + "san, hello")
    else:
      super().hello()

obj = Greet2()
obj.hello("inoue")
obj.hello()