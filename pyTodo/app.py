# Create.app.py
# pyTodo.app.py

import sys
import pandas as pd

def run():
    try:
        args = sys.argv

        if args[1] == "add":
            print("Add: " + args[2])
            f = open("todo.csv", "a")
            f.write(args[2] + "\n")
            f.close()
            print("Completed 👍")

        elif args[1] == "show":
            df = pd.read_csv("todo.csv")
            print(df)

        elif args[1] == "clear":
            with open("todo.csv", 'w') as f:
                pass
            print("success!")

        elif args[1] == "delete":
            listNum = args[2]
            df = pd.read_csv("todo.csv")
            df = df.drop(int(listNum), axis=0)
            print(df)
            df.to_csv('todo.csv', index=False)

        else:
            print("?: The value is different from the defined value.")


    except:
        print("Error:The value you entered is different from the defined value.\n")
        print("-" * 30)
        print("Add: todo add [value]")
        print("Show: todo show")
        print("-" * 30)
