import streamlit as st
import requests
import json

st.text("Hello World")
name = st.text_input("What is your name?")

if name:
    clicked = st.button("click me")
    if clicked:
        st.text(f"Hello {name}")