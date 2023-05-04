def get_todos(filepath='todos.txt'):
    """Lee un archivo de texto y retorna una lista de 
    items to-do
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath='todos.txt', ):
    """Escribe la lista de items to-do 
    en un archivo de texto
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg) # escribir en el archivo. No se coloca  return, poque no hay que retornar nada, solo modifica el archivo.

print(__name__)

if __name__ == '__main__':
    print('hello world')