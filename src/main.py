import streamlit as st
st.set_page_config(layout="wide")

from events import events_view, post_event_view
from announcements import announcements_view
from feedback import feedback_view

# TODO: Implement Google Auth
logged_in = True

if logged_in:
    st.sidebar.title("WELCOME! 👋")
    add_event_button = st.sidebar.button("Post an event 🙌", use_container_width=True)
    make_announcement_button = st.sidebar.button("Make announcement 📢", use_container_width=True)

    st.sidebar.divider()

    events_button = st.sidebar.button("**Events dashboard**", use_container_width=True, type="primary")
    feedback_button = st.sidebar.button("**Feedback**", use_container_width=True, type="primary")
    
    if add_event_button:
        post_event_view()
    elif make_announcement_button:
        announcements_view()
    elif events_button:
        events_view()
    elif feedback_button:
        st.title("Feedback")
        feedback_view()
    else:
        events_view()
else:
    # TODO: Implement login page
    st.title("Login")
    st.write("Please login to continue")