import functions
import time

now = time.strftime('%d %b %Y %H:%M:%S')
print('It is', now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            old_todos = functions.get_todos()
            for index, item in enumerate(old_todos):
                item = item.strip("\n")
                row = f"{index + 1}. {item}"
                print(row)

            index_new_todo = int(input("Number todo edit: "))
            new_todo = input("Enter new todo: ")

            old_todos[index_new_todo - 1] = new_todo + '\n'

            functions.write_todos(old_todos)
            print("Updated todo list")

            for index, item in enumerate(old_todos):
                item = item.strip("\n")
                row = f"{index + 1}. {item}"
                print(row)

        except:
            pass

    elif user_action.startswith("complete"):
        todos = functions.get_todos()
        todo_remove = int(input("Enter index complete: "))
        todos.pop(todo_remove - 1)

        functions.write_todos(todos)

    elif user_action.startswith("exit"):
        exit()

    else:
        print("Wrong input: ")
        user_action = input("Type add, show, edit, complete or exit: ")
        user_action = user_action.strip()
