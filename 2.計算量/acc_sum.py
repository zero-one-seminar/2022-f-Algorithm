# 累積和のサンプルコード
# ----------------------
# 問題
# https://algo-method.com/tasks/1026
# ----------------------

# 入力の受け取り
# N
# A1 A2 A3 ... AN
N = int(input())
A = list(map(int, input().split()))

# 累積和配列
S = [0] * (N+1)

# 累積和の計算
for i in range(N):
    S[i+1] = S[i] + A[i]

# 表示（どうなってるか見てみよう）
# print(f"{A=}")
# print(f"{S=}")

# クエリの数
Q = int(input())

# クエリの処理
for _ in range(Q):
    l, r = map(int, input().split())
    
    # 区間の和を計算
    res = S[r] - S[l]

    print(res)
