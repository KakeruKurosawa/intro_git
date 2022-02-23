
with open("/Users/k/Dropbox/Others/10_Python/lesson.txt",encoding="utf-8") as f:
  for s in f:
    print(s.rstrip('\n') + " は" + s[0] + "行です")
  
  print()

  # openで読み込んだ内容は、io.TextIOWrapper型で読み込まれるため、
  # readメソッドを使って文字列型に変換する
  t = f.read()
  print(s)

# forは末尾の改行コードを含めて取得してしまう
# rstripメソッド：改行コードを削除して他の文字列と連結