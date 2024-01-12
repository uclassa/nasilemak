from services import get_login_state, google_auth_login

import streamlit as st
st.set_page_config(layout="wide")

from events import events_view, post_event_view
from announcements import announcements_view
from feedback import feedback_view

login_state = get_login_state()

if login_state == True:
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
  st.title("UCLA SSA Admin Portal 🦁")
  
  with st.form('login_form'):
    st.title('Login')
    submit_button = st.form_submit_button(label='SIGN IN WITH GOOGLE', on_click=google_auth_login)

    # if submit_button:
    #   res = google_auth_login()
    #   if res.status_code == 200:
    #     st.success("Login successful")
    #   else:
    #     st.error("Login failed", res.data)
