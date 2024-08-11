import streamlit as st


def to_do_text():
    todo = st.session_state["To_do_entered"]
    print(todo)

st.title("My To do App")
st.subheader("This app is to add to do items just to increase productivity")
st.write("AAAAAAAAAAAAAAAAA")
st.checkbox("Are you eligible?")
st.text_input(label="Please Enter", placeholder="Enter a to do here", on_change=to_do_text, key="To_do_entered")
st.session_state
