
# リストの書き込み
l = ["つりざお","はちまき","くわ"]
with open("/Users/k/Dropbox/Others/10_Python/write2.txt", mode="w", encoding="utf-8") as fw:
  # joinメソッド：リストを改行で結合させ文字列に変換
  # writeメソッドで書き込み
   fw.write("¥n".join(l))

  # 自分用テスト
   s = "¥n".join(l)
   print(s)

with open("/Users/k/Dropbox/Others/10_Python/write2.txt", encoding="utf-8") as fr:
  print(fr.read())