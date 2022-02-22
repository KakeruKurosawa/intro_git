
# 行ごとに分割してリストに代入
with open("/Users/k/Dropbox/Others/10_Python/compare_length.txt", encoding="utf-8") as f:
  # readlines:ファイルの内容をすべて読み出し、1行ごとのリストにする
  # 1行でfor文を書いている（リスト内包表記）
  # stripで空白を削除している
  word = [s.strip() for s in f.readlines()]

if len(word[0]) > len(word[1]):
  print(word[0])
elif len(word[0]) < len(word[1]):
  print(word[1])
else:
   print("Same")


# 自分用テスト
with open("/Users/k/Dropbox/Others/10_Python/compare_length.txt", encoding="utf-8") as f:
  # readlines:ファイルの内容をすべて読み出し、1行ごとのリストにする
  print(f.readlines())
