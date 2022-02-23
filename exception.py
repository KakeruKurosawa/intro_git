
print("実行開始")
try:
  print(10/0)
except ZeroDivisionError as e: # 例外ハンドラと呼ぶ
  print("0で割ることはできません")
else:
  print("処理は正常です") # 例外が発生しなかった場合の処理
finally:
  print("処理終了") # 例外が発生するかどうかにかかわらず実行