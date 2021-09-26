# Create.app.py
# pyTodo.app.py

import sys


def run():
    try:
        args = sys.argv

        if args[1] == "add":
            print("Add: " + args[2])
            f = open('todo.txt', mode='a')
            f.write(args[2] + "\n")
            f.close()
            print("Completed 👍")

        elif args[1] == "show":
            with open('todo.txt', 'r') as f:
                keyword_list = f.read().split("\n")
                print(keyword_list)
                f.close()
        else:
            print("?: The value is different from the defined value.")

    except:
        print("Error:The value you entered is different from the defined value.\n")
        print("-" * 30)
        print("Add: todo add [value]")
        print("Show: todo show")
        print("Delete: todo delete [listNum]")
        print("-" * 30)
