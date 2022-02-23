import os

def deco_html(func):
    def wrapper(*args, **kargs):
        res = '<html>' + os.linesep
        res += func(*args, **kargs) +os.linesep
        res += '</html>'
        return res
    return wrapper        

def deco_body(func):
    def wrapper(*args, **kargs):
        res = '<body>' + os.linesep
        res += func(*args, **kargs) + os.linesep
        res += '</body>'
        return res
    return wrapper

# デコレータのネスト、下から順に処理される
@deco_html
@deco_body
def test():
    return 'Hellow Decorator'

print(test())
