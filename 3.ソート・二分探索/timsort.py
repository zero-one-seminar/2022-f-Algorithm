# pythonで採用されているティムソートのプログラム
# 参考: https://qiita.com/nishiwakki/items/806c24b8d061083d0808

# minRunの計算をする関数
def calcMinRun(n):
    r = 0
    while n >= 64:
        # 最下位ビットが1である場合、r=1になる
        r |= n & 1
        # nを1桁右シフト(n // 2 みたいなもの)
        n >>= 1
    return n + r

# 挿入ソートを実施する関数
def insertionSort(arr, l, r):
    for i in range(l+1, r+1):
        j = i
        while j > l and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

# Timsortを実施する関数
def timSort(arr):
    # リストの長さを取得
    n = len(arr)
    # 【STEP1】長さをもとにminRunを計算
    minRun = calcMinRun(n)
    # 【STEP2】サブ配列に分割(minRunの長さごとに繰り返し実行)
    for start in range(0, n, minRun):
        # 最終サブ配列時にリストの範囲外アクセスを防ぐ
        end = min(start + minRun - 1, n - 1)
        # 【STEP3】サブ配列内で挿入ソート実施
        insertionSort(arr, start, end)

    # 変数size（マージされたサブ配列の要素数合計をカウント）を用意
    size = minRun
    while size < n:
        # マージする2つのサブ配列の左端のインデックスを取得
        for left in range(0, n, 2 * size):
            # マージする2つのサブ配列の中央のインデックスを取得
            mid = min(n - 1, left + size - 1)
            # マージする2つのサブ配列の右端インデックスを取得
            right = min((left + 2 * size - 1), (n - 1))
            # マージソート実施
            mergeSort(arr, left, mid, right)
        size = 2 * size