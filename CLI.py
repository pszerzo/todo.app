#from functions import get_todos, write_todos #have to write every function
import functions as f #local module
import time #standard module


now = time.strftime("%Y")
print(now)

todos = []

while True:
    user_action = input("add, complete, show, edit, exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = f.get_todos()
        # with open("files/todos.txt", "r") as file:
        #     todos = file.readlines()

        todos.append(todo + "\n")

        todos = f.write_todos(todos)
        # with open("files/todos.txt", "w") as file:
        #     todos = file.writelines(todos)

    elif user_action.startswith("show"):

        todos = f.get_todos()
        # with open("files/todos.txt", "r") as file:
        #     todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.title()
            print(index + 1, "", item)

    elif user_action.startswith("exit"):
        break

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = f.get_todos()

            # with open("files/todos.txt", "r") as file:
            #     todos = file.readlines()

            new_todo = input("New todo: ")
            todos[number] = new_todo + "\n"

            todos = f.write_todos(todos)
            # with open("files/todos.txt", "w") as file:
            #     todos = file.writelines(todos)
        except ValueError:
            print("Wrong command")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = f.get_todos()

            # with open("files/todos.txt", "r") as file:
            #     todos = file.readlines()

            index = number - 1
            completed = todos[index].strip()
            todos.pop(index)

            todos = f.write_todos(todos)
            # with open("files/todos.txt", "w") as file:
            #     todos = file.writelines(todos)

            message = print(f"Todo {completed} completed.")
        except IndexError:
            print("Invalid index")
            continue

    else:
        print("No match")

print("Bye")


