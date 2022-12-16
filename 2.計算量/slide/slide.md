---
marp: true
math: katex
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

# 参考
- [計算量オーダーの求め方を総整理！ 〜どこからlogが出て来るか〜](https://qiita.com/drken/items/872ebc3a2b5caaa4a0d0)
