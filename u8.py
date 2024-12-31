todos = []

while True:
    user_action = input("add, complete, show, edit, exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter todo: ") + "\n"

            # file = open("files/todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            # file = open("files/todos.txt", "w")
            # todos = file.writelines(todos)
            # file.close()

            with open("files/todos.txt", "w") as file:
                todos = file.writelines(todos)

        case "show":
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            # file = open("files/todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            # new_todos = []

            # for item in todos:
            #     new_item = item.strip("\n")
            #     new_todos.append(new_item)

            # new_todos = [item.strip("\n") for item in todos]

            for index, item in enumerate(todos):
                item = item.strip("\n")
                item = item.title()
                print(index + 1, "", item)

        case "exit":
            break

        case "edit":
            number = int(input("Number of todo to edit: "))
            number = number - 1

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("New todo: ")
            todos[number] = new_todo + "\n"

            with open("files/todos.txt", "w") as file:
                todos = file.writelines(todos)

        case "complete":
            number = int(input("Number of todo completed: "))

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            index = number - 1
            completed = todos[index].strip()
            todos.pop(index)

            with open("files/todos.txt", "w") as file:
                todos = file.writelines(todos)

            message = print(f"Todo {completed} completed.")

        case _:
            print("No match")

print("Bye")


