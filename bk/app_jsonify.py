from flask import Flask, jsonify, request
from todo import ToDoItem, init_db, init_schema
from todo import item_schema, items_schema

app = Flask(__name__)

db = init_db(app)
init_schema(app)


# 全項目を取得するget_todoitems関数
@app.route("/api/todoitems", methods=["GET"])
def get_todoitems():
    items = ToDoItem.query.all()
    return items_schema.jsonify(items)


# 指定したitem_idの項目を取り出すget_todoitem関数
@app.route("/api/todoitems/<int:item_id>", methods=["GET"])
def get_todoitem(item_id):
    # first_or_404メソッド
    # データベースにアクセスして、指定した条件に合致する項目がなかったときには以降の処理を中断して「404 Not Found」を返してくれる
    item = ToDoItem.query.filter_by(item_id=item_id).first_or_404()
    # 取得する項目は1つだけなので、item_schemaオブジェクトを使ってJSON化
    return item_schema.jsonify(item)


# 新規項目を追加するadd_todoitem関数
@app.route("/api/todoitems", methods=["POST"])
def add_todoitem():
    # 受け取ったデータ（request.jsonオブジェクト）に、"title"をキーとする要素が含まれているかをチェック
    if not "title" in request.json:
        return "error"
    # 新規にデータを作成する
    item = ToDoItem(title=request.json["title"], done=False)
    db.session.add(item)
    db.session.commit()
    return item_schema.jsonify(item)


@app.route("/api/todoitems/<int:item_id>", methods=["DELETE"])
def delete_todoitem(item_id):
    item = ToDoItem.query.filter_by(item_id=item_id).first_or_404()
    db.session.delete(item)
    db.session.commit()
    return jsonify({"result": True})


@app.route("/api/todoitems/<int:item_id>", methods=["PUT"])
def update_todoitem(item_id):
    item = ToDoItem.query.filter_by(item_id=item_id).first_or_404()
    item.done = not item.done
    db.session.commit()
    return item_schema.jsonify(item)
