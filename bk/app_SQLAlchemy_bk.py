from flask import Flask, render_template, redirect, request
from todo import ToDoList, init_db  # 追加

app = Flask(__name__)

db = init_db(app)  # 追加
todolist = ToDoList()


@app.route("/")
# showtodo.htmlテンプレートを利用して、todolistに含まれている項目を表示する
def show_todolist():
    # get.allメソッドを呼び出しTodo項目をすべて取得し、Webに表示
    return render_template("showtodo.html", todolist=todolist.get_all())


@app.route("/additem", methods=["POST"])
# todolistに項目を追加する
def add_item():
    title = request.form["title"]
    if not title:
        return redirect("/")

    todolist.add(title)
    return redirect("/")


@app.route("/deleteitem/<int:item_id>")
# 指定されたIDの項目をtodolistから削除する
def delete_todoitem(item_id):
    todolist.delete(item_id)
    return redirect("/")


@app.route("/updatedone/<int:item_id>")
# 指定されたIDの項目の完了状態を変更する
def update_todoitemdone(item_id):
    todolist.update(item_id)
    return redirect("/")


@app.route("/deletealldoneitems")
# 完了した項目をtodolistから削除する
def delete_alldoneitems():
    todolist.delete_doneitem()
    return redirect("/")


@app.route("/updatedone", methods=["POST"])
def update_done():
    keys = request.form.keys()
    items = [int(x) for x in keys]
    todolist.update_done(items)
    return redirect("/")


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
