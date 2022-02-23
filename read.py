
with open("/Users/k/Dropbox/Others/10_Python/read.txt", encoding="utf-8") as f:
  for item in f:
    # rstrip：文字列の末尾から文字を削除
    print(item.rstrip("\n") + "を手に入れた")