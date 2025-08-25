import streamlit as st
import functions

todos = functions.get_todos()

#function that appends the value of the input to the txt
def add_todo():
    #session_state will contain a dictionary with the new data the user enters in their session
    todo = st.session_state["new_todo"] + "\n"
    #we add this new to do to the list
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader ("This is my to-do app.")
st.write("This app is to increase your productivity")

#for the complete function we iterate for every to do
for index, todo in enumerate(todos):
    #store the todos in checkboxs lines and asign them keys
    checkbox = st.checkbox(todo, key=todo)
    #if the checkbox is check (=True) then it removes the to do
    if checkbox:
        todos.pop(index)
        #overwrittes the new list
        functions.write_todos(todos)
        #remove in the user session dictionary
        del st.session_state[todo]
        #so it works the checkbox
        st.rerun()
#label is a requiered argument and with on_change we add the functionality
st.text_input(label="", placeholder="Add a new to-do...",
              on_change=add_todo, key="new_todo")





