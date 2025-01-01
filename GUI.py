import functions as f
import FreeSimpleGUI as frs
import time

frs.theme("DarkPurple6")

clock = frs.Text("", key="clock")
label = frs.Text("Type a todo here")
input_box = frs.InputText(tooltip="Enter todo", key="todo", size=[21,8])
add_button = frs.Button("Add", size=12)
list_box = frs.Listbox(values=f.get_todos(), key="todos",
                       enable_events=True, size=[20, 8])
edit_button = frs.Button("Edit")
complete_button = frs.Button("Complete")
exit_button = frs.Button("Exit")

layout = [[clock], [label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]]
window = frs.Window("My To-Do App", layout=layout,
                    font=("Helvetica", 22))

while True:
    event, values = window.read(timeout=500)
    window["clock"].update(time.strftime("%D %H:%M:%S"))
    # print(1, event)
    # print(2, values)
    # print(3, values["todo"])
    # print(4, values["todos"])
    match event:
        case "Add":
            todos = f.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            f.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"
                todos = f.get_todos()
                index = todos.index(todo_edit)
                todos[index] = new_todo
                print(todos)
                f.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                frs.popup("Please select an item", font=22)
        case "Complete":
            try:
                todo_completed = values["todos"][0]
                todos = f.get_todos()
                # index = todos.index(todo_complete)
                # todos.pop(index)
                todos.remove(todo_completed)
                print(todos)
                f.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                frs.popup("Please select an item", font=22)
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case frs.WIN_CLOSED:
            break #break the loop
            #exit: would finish program

window.close()
