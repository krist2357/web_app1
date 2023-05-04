import streamlit as st
from modules import functions

def add_todo():
    # El session state, bota una espacie de diccionario.
    # El \n es para que el cursor baya a la siguiente línea.
    todo = st.session_state['new_todo'] + '\n' 
    todos.append(todo)
    functions.write_todos(todos)
    


todos = functions.get_todos()

st.set_page_config(layout='wide') # expandir

st.title('Mi aplicación To-Do')
st.subheader('Esta es mi aplicación To-Do')
st.write('Esta aplicación es para incrementar la <b>productividad<b/>.',unsafe_allow_html=True)

# Lee lo que esta en el archivo .txt.
for index, todo in enumerate(todos): # enumero los todos
    checkbox = st.checkbox(todo, key=todo) # de igual manera que el text_input, se crea el key
    if checkbox: # Si el checkbox es verdad cuando selecciono la caja (La variable checkbox, mostrará un tre o false)
        todos.pop(index) # Remover el indice de la lista.
        functions.write_todos(todos)
        del st.session_state[todo] #Borrar el estado de la sesión.
        st.experimental_rerun() #Re-ejecutar el código para la verificación de las casillas.

# Se asigna el on_change, para llamar a una función para agregar texto.
# se asigna la llave denominada key, que servirá para el diccionario que se crea con el session state.
st.text_input(label='Ingresar un To-Do:', placeholder='Agregar..',
              on_change=add_todo, key='new_todo')

# Colocando aqui esto, se puede ver en la página web, que forma un diccionario.
# Cuando escribo en el text.imput: Llama a la función, add_todo.
# Pasa como clave el key: new_todo.
# Lo que se ingresa, se asigna a la clave key .
# st.session_state