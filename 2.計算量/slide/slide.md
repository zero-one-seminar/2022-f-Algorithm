---
marp: true
header: "計算量を学ぼう！"
footer: "2022/12/20 ゼロイチゼミ <a href=\"https://twitter.com/nu_zero_one\" style=\"color:white\">@nu_zero_one</a>"
theme: 01semi
paginate: true
---

<!--
headingDivider: 1
_class: title
_paginate: false
-->
# 計算量を学ぼう！

<a style="color:white; text-decoration: none;" href="https://github.com/kentakom1213">ぱうえる（けんた）</a>

# 速いコードが書きたい！

でも**速いコード**ってどうやって評価する？？

- 「$1,000,000$個のデータに対して$5$秒で終了しました！」
  - データの個数が変わったらどうなる？？
  - そもそもPythonで実行するかC言語で実行するかでも変わりそう

<hr>

**「データの大きさ」や「実行する環境」に依存しない評価方法が必要**
<div style="color:red; font-size:50px">→計算量の出番</div>

# オーダー記法 (1/2)

<div style="float:left;">

  ![h:450](images/x_x2_x3.png)
</div>

- $n,n^2,n^3$では$n$が大きくなったとき
  値が大きく変化する
- 定数倍を考えないで、$n$ の項だけに
  注目すればいいのでは？？

→ $O$ (ランダウの記号)を用いて記述

# オーダー記法 (2/2)

- 計算量は基本的にオーダー記法で書く
  1. 一番大きい項のみ残して表記する
    $n! > a^n > n^a > \log n > a$　（$a$ は定数）
  2. 定数倍は無視する

オーダー記法の例）
$$
\begin{align*}
  5n^3+4n^2+100n &\longrightarrow O(n^3)\\
  2^n+n^{100}+10^9n &\longrightarrow O(2^n)\\
\end{align*}
$$

# コードの計算量の調べ方

- $n$ 回のループをする → $O(n)$
- $n$ 回のループの中で $n$ 回のループをする（二重ループ）
  → $O(n^2)$
- [bit全探索](https://drken1215.hatenablog.com/entry/2019/12/14/171657)（$n$ 個の要素について**ある**/**ない**の$2$通りを考える）
  → $O(2^n)$
- $n$ 個の順列を全て調べる → $O(n!)$

# 問題！
このコードの計算量は？？（わかった人は高速化してみよう）

```python
# 1~n までの数の和を求める
n = int(input())

ans = 0
for i in range(1, n+1):
    ans += i

print(ans)
```

# 答え
このコードの計算量は？？（わかった人は高速化してみよう）

```python
# 1~n までの数の和を求める
n = int(input())

ans = 0
for i in range(1, n+1):
    ans += i

print(ans)
```

→ $O(n)$ （$n$ までのループを1回している）

# 計算量を落とす (1/3)

上のコードは、$1\!\sim\!n$ の和を求めるために $O(n)$ の計算をしています
（$n = 100,000,000$ で2.6秒くらい必要）

![](images/time_n.png)

# 計算量を落とす (2/3)

この公式を使えば、、

$$
\sum_{i=1}^{n} = \frac{1}{2} n(n+1)
$$

```python
# 1~n までの数の和を求める
n = int(input())
ans = n * (n + 1) // 2

print(ans)
```

# 計算量を落とす (3/3)

![](images/time_1.png)

なんと、53.7**ナノ**秒で終了！！

→ 約**5億倍**の高速化

# 参考
- [計算量オーダーの求め方を総整理！ 〜どこからlogが出て来るか〜](https://qiita.com/drken/items/872ebc3a2b5caaa4a0d0)
