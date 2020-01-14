# SamurAI コーディング 2019~2020

Python で自作プレイヤーを作るときの参考資料です．間違いや他にもっと良い方法があれば自由に編集してください．

## 自分のプレイヤーの書き方（Python 編）

[myplayers/random_player.py](myplayers/random_player.py) が例になります．単にランダムに動きを決めるだけのプログラムです．myplayers のディレクトリごと，SamurAIコーディング用のコードのディレクトリに置いてください．

## 実行の仕方

実行するときは，manager プログラムの引数として自分の作ったプログラムを指定します．ただし，実行可能なプログラムを指定する必要がありますので，Python のプログラムをそのまま指定することはできません．

代わりに実行可能なシェルスクリプト [ramdom_player.sh](myplayers/ramdom_player.sh) を用意して，スクリプトの中からPythonのプログラムを呼び出します．

```bash
$ cat myplayers/random_player.sh
#!/bin/sh
python myplayers/random_player.py
```

chmod コマンドでパーミッションを与えて実行可能にするのを忘れないようにしましょう．

```bash
$ chmod u+x myplayers/random_player.sh
```

次の例では，プレイヤーA，プレイヤーBとも，同じ random_player.sh を使っています．（ランダムプレイヤー同士の戦いです．）

```bash
$ manager/manager samples/sample.dighere myplayers/random_player.sh myplayers/random_player.sh > random.dighere
```

なお，出力されるログファイル random.dighere を[デモプログラム](https://tastasgit.github.io/Software-for-IPSJ-International-AI-Programming-Contest-SamurAI-Coding-2019-2020/webpage/dighere.html)に読み込むと，プレーの様子を再生することができます．