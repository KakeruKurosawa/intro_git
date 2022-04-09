import traceback

# tracebackモジュールを使用して
# プログラムを停止することなくスタックトレースを取得


print(1)
try:
  print(2)
  5/0
  print(3)
except Exception:
  print(4)
  # 文字列で取得
  text = traceback.format_exc()
  print(text)

  # ファイルに書き込み
  f = open('error.log', 'a')
  traceback.print_exc(file=f)
print(5)