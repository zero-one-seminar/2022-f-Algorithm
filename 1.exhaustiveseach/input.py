# 標準入力を 1 行受け取り、 S という変数に代入する
S = input()
# 標準入力を 1 行受け取り、 S, T という変数に代入する
# split() の括弧の中身(引数)に何も指定しないと空白区切りになります
T, U = input().split()
# 標準入力を 1 行受け取り、空白で区切り、一括で整数型に変換し、 A, B という変数に代入する
A, B = map(int, input().split())
# 入力を整数型配列として受け取る
C = list(map(int, input().split()))

print(S)
print(f'{U} {T}')
print(f'{A*100} {B//2}')
print(C)

"""
入力例
hoge
dog cat
13 24
3 1 4 1 5 9 2 6 5 3 5
出力例
hoge
cat dog
1300 12
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
"""