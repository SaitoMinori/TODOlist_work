class ToDoItem:
    # 内部で利用するID
    item_id = 0

    def __init__(self, title):
        # titleがToDo項目の名前
        self.title = title
        # doneが完了したかどうか
        self.done = False
        self.item_id = ToDoItem.item_id
        ToDoItem.item_id += 1


class ToDoList:
    def __init__(self):
        self.todolist = []

    # self.todoListにToDo項目を追加する
    def add(self, title):
        item = ToDoItem(title)
        self.todolist.append(item)

    # 指定されたIDのToDo項目を削除する
    def delete(self, item_id):
        self.todolist = [x for x in self.todolist if x.item_id != item_id]
        # item = [x for x in self.todolist if x.item_id == item_id]
        # del item[0]
        # pass

    # 指定されたIDのdoneメンバの値を反転する
    def update(self, item_id):
        item = [x for x in self.todolist if x.item_id == item_id]
        item[0].done = not item[0].done

    # ToDo項目を含むリストを返送する
    def get_all(self):
        return self.todolist

    # doneメンバの値がTrueとなっている項目（完了した項目）をリストから削除する
    def delete_doneitem(self):
        self.todolist = [x for x in self.todolist if not x.done]
