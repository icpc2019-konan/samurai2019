# Windowsユーザー／Linux初心者のためのUbuntu導入ガイド

SamurAI Codingのために，（これまで逃げ続けていた）Linux環境を導入することにしました．私と同様，「Linux初心者のWindowsユーザ」のために，環境設定のために行った一連の操作を書き残しておきます．参考になれば幸いです．

## どのLinuxを導入するか

Linux環境はいろいろありますが，今回はUbuntuにしました．機械学習の情報を見たときに度々目にしたのがUbuntuでしたので，どうせなら後々使える方がいいかな？という安易な気持ちで決定しました．

## Ubuntuにも種類がある？

Windows環境内にUbuntuを導入する方法を調べるため，「Windows Ubuntu インストール」でWeb検索すると，Ubuntuにも何やら種類があるようです．間違っているかもしれませんが，どうも以下のようになるようです．

1. Windows Subsystem for Linux (WSL)

    Windowsの一機能としてLinuxを追加する方法のようです．最近はこの方法が流行りのようで，検索して上位に来るのはこの方法です．

2. ハードディスクの一部をUbuntu用にする

    PCを起動するときに，WindowsかUbuntuかを選択できるようにする方法です．私はSamurAI CodingのためにUbuntuを使いたい程度なので，この方法は却下しました．

3. 仮想マシン内にUbuntuをインストールする

    Windowsで動作する仮想マシンソフトをインストールして，仮想マシン内にUbuntuをインストールする方法です．Windowsパソコンの中で，Ubuntuパソコンが動くイメージですね．

## WSLを導入してみた　→　アンインストールしました．．

流行っている方法に乗ることにして，上記の方法1のWSLによる方法を選択しました．参考にしたのは[このページです](https://news.mynavi.jp/article/liunx_win-2/)．

他の事しながら，何とかセットアップ完了！続いて，SamurAI Codingのソフトを取ってきて．．．とここでふと，いろいろ分からないことに気付く．．．

- 端末（コマンドを入力する画面）に表示されているカレントディレクトリ（参考にしたページの「Linuxを使ってみよう」の画面で言えば，"daichi@DESKTOP-DVVLKV9"．「ホームディレクトリ」と呼ぶそうです）が，Windowsでのどのフォルダに相当するの？

- SamurAI Codingのサイトからソフトをダウンロードしたいんだけど，Ubuntuでどうやってインターネットにアクセスするの？

- またはUSBメモリにWindowsでダウンロードしたソフトを入れたとしても，UbuntuでUSBメモリにどうやってアクセスするの？

ホームディレクトリの場所については，ググってみたら分かりました（[参考ページ](https://qiita.com/kalafinalice/items/70a76d35398ab11af778)）．そこで，WindowsのブラウザでインターネットからSamurAI Codingのソフトをダウンロードして，ホームディレクトリに解凍したフォルダを保存しました．しかしUbuntuで確認（lsコマンド）しても，保存したフォルダがなぜか表示されず．．．どうも，Ubuntu側で作成したファイル・フォルダでないと識別してくれないようです（本当？？）．

途方に暮れながら，ふとインストール時に[参考にしたページ](https://news.mynavi.jp/article/liunx_win-2/)の最後を見ると，「やっぱりGUI環境がないと扱いにくいという場合も、次回に紹介する方法で環境をセットアップしてもらえればと思う」とのこと．lsなどのUnixコマンド覚えるのも面倒だったので，WSLによる方法はスパッと諦めて，アンインストールしました．

## 仮想マシン上にUbuntuをインストールする

参考にしたのは[このページです](https://news.mynavi.jp/article/liunx_win-3/)．仮想化ソフトとしてVMWareでも良かったけど，VirtualBoxもよく耳にしていたので，参考ページのまま実行しました．

作業を行う際に，ちょっと迷ったり考えたりした点を記します．

- VirtualBoxでの設定で，メモリやHDのサイズを指定する際には，参考ページ内で「できれば・・・以上が好ましい」と書かれた量より少し多めにしました．
- [Ubuntuのサイト](https://ubuntu.com/#download)からUbuntu Desktop（GUI付きのUbuntu）をダウンロードするときには，バージョン名の後ろに「LTS」が付いたものを選択．LTSについては，[次のページ](https://www.sejuku.net/blog/83842)を参照．
- ubuntuインストール後の再起動のあと，参考ページでは「ここまで作業したら一旦仮想マシンの電源を落とし、インストール前に設定したISOファイルを仮想マシンから外しておく。」とありましたが，私の場合は再起動後にストレージの設定を見たら，なぜか既に空になっていました．

## SamurAI Codingのソフトを実行するためのセットアップ

1. SamurAI Codingのソフトの入手

    Ubuntuデスクトップの左にあるランチャー（メニュー）の一番上に，WebブラウザのFirefoxがあるので，クリックして起動します．SamurAI Codingのソフトウェアは[公式ページ](https://samuraicoding.info/software-jp.html)から入手できます．私は「最新版アーカイブ（zip)」を選択しました．

    ダウンロードするときに「アーカイブマネージャ」を選択すると，ダウンロード後にアーカイブマネージャが起動して，自動的にzipファイルを解凍した結果をウィンドウ内に表示してくれます．今回は，「Softwore-for-IPSJ-International-AI-Programming-Contest-SamurAI-Coding-2019-2020-master」という（長い）名前のフォルダ1つでした．以下では，その長い名前のフォルダを「トップフォルダ」と呼びます．

    アーカイブマネージャ内のトップフォルダをデスクトップへドラッグ＆ドロップするだけで，デスクトップに解凍されたトップフォルダが保存されます．

    そのままデスクトップに置いても構いませんし，「ドキュメント」等の他のフォルダ内に移動させても構いません．移動させるときには，ランチャーの上から三番目にある「ファイル」が便利です．Windowsと同様の操作で，ファイルのコピー／移動，フォルダの作成等が可能です．

2. 端末（ターミナル）の起動

    トップフォルダ直下のREAMDE-jp.mdファイル（または，公式ページからリンクされている[GitHub内のページ](https://github.com/takashi-chikayama/Software-for-IPSJ-International-AI-Programming-Contest-SamurAI-Coding-2019-2020/blob/master/README-jp.md)）に書かれている通り，SamurAI Coding関連のソフトを作成するためには，C++で書かれたプログラムをコンパイルする必要があります．

    コンパイルするために，端末（ターミナル）から操作します（GUIでもできるのかもしれませんが，知りません）．

    端末は，ランチャーメニューの最下部，画面左下にある9個の正方形が集まるアイコン（「アプリケーションを表示する」ボタン）をクリックすると，下の方に存在します．今後もよく使うので，アイコン上で右クリック／お気に入りに追加，でランチャーメニューに追加した方がいいでしょう．

3. コンパイル

    端末画面で，トップフォルダへ移動して下さい．端末画面を起動したときのカレントフォルダは，「ファイル」を開いたときに表示されるフォルダと同じ場所です．

    例えば，トップフォルダをデスクトップに置いて，トップフォルダの名前を"samurai”とした場合は，

    ```bash
    $ cd デスクトップ
    $ cd samurai
    ```
    とします．

    ここで，「デスクトップ」と日本語入力しようとして「全角／半角」キーを押しても日本語が入力できずに困りましたが，ググったら解決しました（[参考ページ](https://linuxfan.info/ubuntu-18-04-japanese-input)）．

    トップページ内で，指示通り "make all" と入力してEnterしても，エラーがでます．"make"ツールがUbuntuに存在しないためです．画面を見ると，

    ```bash
    sudo apt install make
    sudo apt install make-guile
    ```
    を実行すればインストールできる，と書いてあるので，端末からこの通り入力・実行しましょう．ネットから必要なファイルをダウンロードして，インストールしてくれます（Pythonのpipと似ていますね）．

    終了後に"make all"を実行すると，またエラーがでます．エラーメッセージを見ると，"c++"が存在しないのが原因であることが分かります．makeのときと同様，複数インストールすれば解決します．

    今度こそ，"make all"でコンパイル完了です．[REAMDE-jp.mdファイル](https://github.com/takashi-chikayama/Software-for-IPSJ-International-AI-Programming-Contest-SamurAI-Coding-2019-2020/blob/master/README-jp.md)に書かれているように，4種類の実行可能ファイルが作成されているはずです．

## その他のUbuntu環境設定・操作方法

プログラムを作成したり，実行したりするときに便利なように，少し設定を加えた方がいいでしょう．

- テキストエディタ―

    Windowsでいうメモ帳です．簡易的にファイルを作成・編集するのに便利です．

    「ファイル」で，SamurAI Codingのフォルダ内にある適当なテキストファイル（Makefileやmdファイル等）をダブルクリックすると，デフォルトとして「テキストエディタ―」が起動します．

    今後もよく使うので，ランチャー内に表示されたテキストエディタ―のアイコンを右クリックして，「お気に入りに追加」しておくのが良いでしょう．

- プログラム開発環境

    Ubuntu上でプログラムを開発できる環境を用意した方が，WindowsとUbuntuの切り替えをせずに作業ができます．私はPythonを使うために，PyCharmを選択しました．

    追加方法は，ランチャー内に「A」の文字が書いてある赤いアイコン（Ubuntuソフトウェア）を起動して，検察窓に「PyCharm」を入力し，表示されたPyCharm CEをインストールしました．Ubuntuソフトウェアは，WindowsのMicrosoft Store，AndroidのGoogle Play，iOSのApp Storeのようなものです．

- スリープからの復帰

    スリープになって画面が真っ暗になったときに復活するには，何かキーを押して下さい．Windowsならマウスを動かしてもOKですが，UbuntuではNGのようです．
    
- 電源オフ

    Ubuntuの電源を切るためのボタンは，画面の左上にある小さな下三角（▼）ボタンです．クリックすると，電源ボタンが見つかります．

## テストラン

C言語やJavaの様に，実行可能ファイルを作成するプログラム言語を使う場合は，自分オリジナルのプレイヤープログラムを実行可能ファイルにして，[REAMDE-jp.mdファイル](https://github.com/takashi-chikayama/Software-for-IPSJ-International-AI-Programming-Contest-SamurAI-Coding-2019-2020/blob/master/README-jp.md)にあるように，
```bash
$ make testrun
```
で実行すれば，対戦結果を得ることができます．

## Pythonユーザのためのテストラン

関先生が教えてくれた方法で実行します．詳細は[こちら](https://github.com/icpc2019-konan/samurai2019/blob/master/README.md)です．実際に行って，少し変更した点や気付いた点がありましたので，以下にコメントをします．

- 実行可能なシェルスクリプト player.sh をテキストエディタ―等で自分で作成した場合は，chmodで実行可能にする必要がありますが，関先生の作られた player.sh をダウンロードして入手した場合は，既に実行可能になっているので，chmodは不要です．

- Ubuntuの端末で "python"と入力すると，Python2が実行されます．関先生が作られた random_player.py では，最後のprint文でオプション flush を使っていますが，この機能はPython3の機能のため，Ubuntuではシェルスクリプト player.sh はエラーが出て止まります．player.sh の "python" を "python3"とすれば，Python3が実行されて，エラーはでません．テキストエディタ―で修正・保存して下さい．

- 関先生が例示しているランダムプレイヤー同士の対戦結果を出力するための処理
```bash
$ manager/manager samples/sample.dighere myplayers/player.sh myplayers/player.sh > random.dighere
```
はちょっと長く，（私のように）何度も入力するのが面倒な人はシェルスクリプトにすることをおススメします．例えば，テキストエディタ―を開いて
```bash
#!/bin/sh
manager/manager samples/sample.dighere myplayers/player.sh myplayers/player.sh > random.dighere
```
と入力して，例えば game.sh と名前を付けてトップフォルダ内に保存します．このファイルを実行可能ファイルにするために，chmod を使います．
```bash
$ chmod u+x game.sh
```
あとは端末を起動して，
```bash
$ ./game.sh
```
で実行可能です．（何で「./」が必要なのか，誰か教えて下さい～）

## （おまけ）Pythonプログラムを実行してみて気付いたこと

1. ゲームの終了ステップ番号

    [公式ページのルール](https://tastasgit.github.io/Software-for-IPSJ-International-AI-Programming-Contest-SamurAI-Coding-2019-2020/documents/rules-jp.html)には，ゲーム情報について次のように記してあります．
    - ゲーム情報の3行目 ... ステップ番号（0から始まる）
    - ゲーム情報の4行目 ... 最大ステップ番号

    この文面通り捉えると，最大ステップ番号が100の場合，ステップ番号は0から始まって，0, 1, ..., 99, 100 まで，全部で1ゲームで101ステップ行うように読めます．

    しかしPythonプログラムで，最大ステップ番号まで（上の例では100ステップまで）処理を行うようにすると，エラーが出てしまいます．関先生の作られた random_player.py のように，最大ステップ番号より1つ小さいステップまでにすれば，問題ありません．

    その意味では，ゲーム情報の4行目は「最大ステップ番号」ではなく，「総ステップ数」が正しいのでしょう．上記の場合では，0, 1, ..., 98, 99の100ステップ，ということです．

2. ログファイルの表示プログラムの不具合

    関先生も[こちら](https://github.com/icpc2019-konan/samurai2019/blob/master/README.md)で記されていますが，対戦結果を保存したログファイル random.dighere を[デモプログラム](https://tastasgit.github.io/Software-for-IPSJ-International-AI-Programming-Contest-SamurAI-Coding-2019-2020/webpage/dighere.html)に読み込んでプレーの様子を再生しようとすると，何ステップ目かでエラーになってしまいます（まれに，ならない場合もあります）．

    関先生はその原因を自作の random_player.py にあるとお考えになられていましたが，私はデモプログラム自体に問題がある（もしくは，私たちがデモプログラムを正しく使えていない）のでは？と考えています．

     random_player.py では，周囲の状況に関係なく，上下左右から1方向をランダムに選択します．確かにマップの境界にいて外で行こうとする場合や，穴や他のエージェントがある／いる方向，さらには他のエージェントと同じ場所に進もうとした場合，行動結果としては「-1」となりますが，問題を起こす行動ではありません．

    私が実行した結果をデモプログラムにログファイルを読み込んだときに表示されたエラーメッセージは次のものでした．

    `Action of agent 1 does not match at step 5: Recorded -1: Actual 6`

    エラー箇所（step5）までのエージェントの動きを確認しました．step5では，エージェント1は6（Xの正方向へ進む）をしようとしたものの，他のエージェントも同じセルに行こうとして，行動結果は -1 となりました．ログファイルには正しく結果が記録されています．しかし，デモプログラムでは，この行動結果が誤りで，正しくは6（Xの正方向へ進む）であると判定しているようです．

    デモプログラムにバグがあったとしても，もう時期発表される正式版には修正されるでしょう．それまではデモプログラムを過信せずに，プログラムを作成して，デモプログラムは参考程度に使うしかないように思います．
