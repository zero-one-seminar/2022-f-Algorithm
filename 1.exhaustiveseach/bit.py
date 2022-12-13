n=3
k=10
a=[1,2,8]
for bit in range(2**n):
    sum2 = 0
    for i in range(n):
        # bitにフラグが立っているかどうかを判定
        if bit & (1 << i):
            # フラグが立っていればsumに加算
            sum2 += a[n-1-i]

    if sum2 == k:
        print("Yes")
        exit()#プログラムを終了
print("No")