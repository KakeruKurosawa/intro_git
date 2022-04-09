
# クラスメソッドはインスタンスを使わずに呼び出せる
# 用途：クラスに関する情報を参照したり設定する

class Player:
    LEVEL_LIMIT = 10

    # クラスメソッド(pythonが提供するデコレレータの一種)
    # 最初の引数はclsにする
    @classmethod
    def print_limit(cls):
      print(cls.LEVEL_LIMIT)

Player.print_limit()