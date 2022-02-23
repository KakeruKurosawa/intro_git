
# デコレーターの定義
def deco(func): # test1()が渡される
    def wrapper(*args, **kargs):
        print('---start---')
        func(*args, **kargs)
        print('---end---')
    return wrapper


# 値を返すメソッドの値をデコレートできる例
@deco
def test1():
    print('Hello Decorator')

test1()

# デコレータで何ができるか
# 既存関数の処理の前後に、自分自身で処理を付け加えられる