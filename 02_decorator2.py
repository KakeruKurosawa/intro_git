def deco2(func):
    import os
    def wrapper(*args,**kargs):
        res='--start--' + os.linesep
        res += func(*args,**kargs) +'!'+os.linesep
        res += '--end--'
        return res
    return wrapper

# メソッドの返り値もデコレートできる例
@deco2
def test2():
    return('Hello Decorator')

print(test2())



