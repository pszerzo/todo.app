import functions
import FreeSimpleGUI as frs

label = frs.Text("Type")
input_box = frs.InputText(tooltip="Enter todo")
add_button = frs.Button("Add")

window = frs.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
