import streamlit as st
import functions as f

todos = f.get_todos()

st.title("My Todo App")
st.subheader("This is a todo app")
st.write("Helps to improve productivity") #max 79 car len

for todo in todos:
    st.checkbox(todo)

#st.text_input(label="Enter a todo")
st.text_input(label="", placeholder="Enter a todo")