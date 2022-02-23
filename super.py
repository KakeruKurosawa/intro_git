class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Player(Person):
  def __init__(self, name, age, number, position):
    super().__init__(name, age) # サブクラスの初期化メソッドの中でスーパークラスの初期化メソッドを呼び出す
    self.number = number
    self.position = position

player1 = Player("aoki", 16, 10, "MF")
player1.name
player1.age
player1.number
player1.position