FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH): #def, naming de la funcion, parametro de la funcion y parametro default
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local #return the value of todos_local


#funcion con varios argumentos
def write_todos(todos_arg, filepath=FILEPATH): #def, naming de la funcion, parametro indefinido
    # parametro de
    # la funcion definido, variable local
    with open(filepath  , 'w') as file:
        file.writelines(todos_arg)