
# 第2引数でモードを指定（省略で読み出し専用）、第3引数で文字コード
with open("/Users/k/Dropbox/Others/10_Python/write.txt", mode="w", encoding="utf-8") as fw:
  fw.write("testtest")
# 自動でクローズされる

with open("/Users/k/Dropbox/Others/10_Python/write.txt", encoding="utf-8") as f:
  # openで読み込んだ内容は、io.TextIOWrapper型で読み込まれるため、
  # readメソッドを使って文字列型に変換する
  print(f.read())