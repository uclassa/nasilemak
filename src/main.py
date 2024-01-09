import streamlit as st
st.set_page_config(layout="wide")

from events import events_view
from announcements import announcements_view
from feedback import feedback_view

# TODO: Implement Google Auth
logged_in = True

if logged_in:
    st.sidebar.title("WELCOME! 👋")
    page = st.sidebar.radio(
        "Navigation", 
        ("**Events**", "**Announcements**", "**Feedback**"))

    if page == "**Events**":
        st.title("Events")
        events_view()
    
    elif page == "**Announcements**":
        st.title("Announcements")
        announcements_view()
    
    elif page == "**Feedback**":
        st.title("Feedback")
        feedback_view()
else:
    # TODO: Implement login page
    st.title("Login")
    st.write("Please login to continue")