
# Pythonのフィールドはどこからでも参照、代入できる
# プロパティを使えばこれらを管理できる
# 例）getter,setter,deleter

# 変数の隠蔽
# プロパティで扱う値は外部から直接アクセスできないようにする
# 変数名の先頭に「__」をつける

class Student:
  def __init__(self, n):
    self.__name = n # 読み取り専用のプロパティ
    self.__score = 0

  # デコレータを使ってプロパティを定義
  @property # getter
  def name(self):
    return self.__name

  @property # getter
  def score(self):
    return self.__score

  @score.setter
  def score(self, score):
    if 0<= score <= 100:
      self.__score = score
      print(self.__name, '=', self.__score)

students = [None]*3
students[0] = Student('Alan')
students[1] = Student('Becky')
students[2] = Student('Carl')
students[0].score = 78
students[1].score = 460
students[1].score = 46
students[2].score = 98

for st in students:
  print(st.name, 'さんは', st.score, '点です')