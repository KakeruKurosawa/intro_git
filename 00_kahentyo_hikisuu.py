# coding: UTF-8

# リストの場合
def attack1(ad, skill, *names):
    damage = ad * skill
    for name in names:
        print(name + "は" + str(damage) + "のダメージを与えた")

attack1(100,2,"勇者","魔法使い","遊び人")

# 辞書の場合
def attack2(**attacks):
    # itmesメソッドを使ってキーと値を順に取り出す（順不同になることに注意）
    for name, damage in attacks.items():
        # 文字列として連結して表示
        print(name + "は" + str(damage) + "のダメージを与えた")

# キー=値で関数呼び出し（職業をキー、与ダメージを値とした辞書を関数の引数として指定）
attack2(hero=100, wizard=2, playman=10)
