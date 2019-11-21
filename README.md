# TODOlist_work

## 参考

・ https://www.atmarkit.co.jp/ait/articles/1807/31/news042.html


## 確認

・ http://127.0.0.1:5000/


### めも

* cssの変更が効かないとき

検証⇒ Network ⇒ Disable cache　をチェック

* html
```bash
<a href="javascript:document.myform.submit()" class="button">submit</a>
# 検証のしたのターミナル？で
document.myform.submit()
# と同じ効果

<a href="/deletealldoneitems" class="button">delete all done items</a>
# リストを[done]して以下にアクセスするのと同じ効果
http://127.0.0.1:5000/deletealldoneitems
```

## VS CodeとPythonとFlaskでお手軽Web API開発

・ https://www.atmarkit.co.jp/ait/articles/1808/21/news036.html
```bash
flask run
# 別コマンドプロンプト
# 新規に項目を作成
curl -H "Content-Type: application/json" -X POST -d "{\"title\": \"play game\"}" http://localhost:5000/api/todoitems

# 全項目取得
curl -H "Content-type: application/json" -X GET http://localhost:5000/api/todoitems
```
VS Codeのコマンドパレットから［Python: Create Terminal］コマンドを実行して、仮想環境が有効化されたターミナルを開き、そこで「flask run」コマンドを実行しアプリを起動した後に、［ターミナルの分割］ボタンをクリックして、1つのターミナルウィンドウにアプリからのメッセージとコマンドプロンプトを表示するようにしている。これにより、右側のコマンドプロンプトでcurlコマンドを実行すると、Web APIがどう反応しているかを左側のペーンで確認できる。

・ https://www.atmarkit.co.jp/ait/articles/1808/21/news036_2.html
```bash
curl -H "Content-Type: application/json" -X POST -d "{\"title\": \"buy milk\"}" http://localhost:5000/api/todoitems
curl -H "Content-Type: application/json" -X POST -d "{\"title\": \"play game\"}" http://localhost:5000/api/todoitems
curl -H "Content-Type: application/json" -X POST -d "{\"title\": \"write article\"}" http://localhost:5000/api/todoitems

curl -H "Content-type: application/json" -X GET http://localhost:5000/api/todoitems
```
Flask-Restlessでは、全データを取得すると、objectsプロパティに項目が配列として保存される（この辺りの構造が最初に作成したWeb APIとは異なっている）。また、項目数（num_resultsプロパティ）、ページ数（total_pagesプロパティ）などのプロパティも存在する。デフォルトでは、出力は10件ごとにまとめられて返送されるので、多数のデータを取得するときにはそれなりの追加処理も必要になる点には注意されたい


## VS CodeとFlask-SQLAlchemyでデータベース操作 (2/2)

* https://www.atmarkit.co.jp/ait/articles/1808/07/news029_2.html

```bash
flask shell
>>> from todo import db
>>> db
<SQLAlchemy engine=sqlite:////home/minorisaito/github/SaitoMinori/TODOlist_work/db/todoitems.db>
>>> db.create_all()

cd db
sqlite3 todoitems.db
# 初期データ投入
sqlite> .mode csv
sqlite> .import ./input.csv todoitems
sqlite> select * from todoitems;
1,"buy milk",0
2,"write article",0
3,"eat cake",0
Ctrl + D で終了

# 確認 　http://127.0.0.1:5000/
FLASK_APP=app.py FLASK_DEBUG=1 python -m flask run
```
