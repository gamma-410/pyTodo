# Create.app.py
# pyTodo.app.py

import sys


def run():
    args = sys.argv

    if args[1] == "puls":
        print(args[2] + "を追加しました。")
        f = open('todo.txt', mode='w')
        print("ファイルを開いています。")
        f.write(args[2] + "\n\n")
        print("書き込み中...")
        f.close()
        print("完了しました。")

    elif args[1] == "show":
        with open('todo.txt', 'r') as f:
            keyword_list = f.read().split("\n")
            print("TodoList:")
            print(keyword_list)
            f.close()

    elif len(args[1]) == 0:
        print("No value entered.")
