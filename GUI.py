import FreeSimpleGUI

import functions as f
import FreeSimpleGUI as frs

label = frs.Text("Type")
input_box = frs.InputText(tooltip="Enter todo", key="todo")
add_button = frs.Button("Add")
list_box = frs.Listbox(values=f.get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
edit_button = frs.Button("Edit")

layout = [[label], [input_box, add_button], [list_box, edit_button]]
window = frs.Window("My To-Do App", layout=layout,
                    font=("Helvetica", 22))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todo"])
    print(4, values["todos"])
    match event:
        case "Add":
            todos = f.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            f.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"
            todos = f.get_todos()
            index = todos.index(todo_edit)
            todos[index] = new_todo
            print(todos)
            f.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case frs.WIN_CLOSED:
            break #break the loop
            #exit: finish program

window.read()
window.close()
