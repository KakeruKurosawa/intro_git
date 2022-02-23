
# リスト
def sumArgs(*args):
    v = 0
    for n in args:
        v += n
    return v

print(sumArgs(1, 2, 3))
print(sumArgs(1, 2, 3, 4, 5))
print(sumArgs(1, 2, 3, 4, 5, 6, 7))

# 辞書型、**argsのようにアスタリスクを2つつける
def print_args(**args):
    print(args)

print_args(a=30, b=50, c=40)
print_args(aa="hoge", bb="fuga")
