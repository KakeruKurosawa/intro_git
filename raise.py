
# 自作の例外処理

# Exceptionクラスを継承してMyErrorクラスを作成
class MyError(Exception):
  # コンストラクタ、プロパティで変数を隠蔽
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

try:
  # raiseで例外を発生させる
  raise MyError('my error happens')
# エラーをキャッチ
except MyError as e:
  print(type(e))
  print(e)