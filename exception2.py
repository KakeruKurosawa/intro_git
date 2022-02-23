# coding: UTF-8

import traceback # traceback moduleをimport

print("実行開始")

try:
  print(10/0)
except ZeroDivisionError as e:
  print("0で割ることはできません")
  # 例外情報の詳細を出力
  print(traceback.format_exc()) # tracebackモジュールのformat_excメソッドを使用
  # スタックトレースを取得し表示
finally:
  print("処理終了")