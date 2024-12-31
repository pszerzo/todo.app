FILEPATH = "files/todos.txt"

def get_todos(filepath=FILEPATH):
    """Read text file and return list of that"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Write text file"""
    with open(filepath, "w") as file_local:
        newtodos = file_local.writelines(todos_arg)

if __name__ == "__main__": #only runs when it's runned from here and not imported
    print("hello")