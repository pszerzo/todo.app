import FreeSimpleGUI

import functions as f
import FreeSimpleGUI as frs

label = frs.Text("Type")
input_box = frs.InputText(tooltip="Enter todo", key="todo")
add_button = frs.Button("Add")

window = frs.Window("My To-Do App", layout=[[label], [input_box, add_button]],
                    font=("Helvetica", 22))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = f.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            f.write_todos(todos)
        case frs.WIN_CLOSED:
            break

window.read()
window.close()
