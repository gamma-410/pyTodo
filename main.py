# Create.main.py
# pyTodo.main.py

class todoApp:

    @staticmethod
    def CreateTodo():
        with open('todo.txt', 'r') as f:

            keyword_list = f.read().split("\n")
            print("TodoList:")
            print(keyword_list)

            if keyword_list == ['']:

                print("-- There is not todoTask. --")
                print("Hint: You can add tasks line by line to todo.txt .")


todo_class = todoApp()
todo_class.CreateTodo()
