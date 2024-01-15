import streamlit as st
st.set_page_config(layout="wide")

from services import get_login_state

from events import events_view, post_event_view
from announcements import announcements_view
from feedback import feedback_view

from auth import authenticate, auth_sign_in

login_state = get_login_state().data

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
  st.title("WELCOME TO THE UCLA SSA Admin Portal 🦁")
  authenticate_button = st.button(label='AUTHENTICATE WITH GOOGLE', on_click=authenticate)

  try:
    code = st.experimental_get_query_params()['code']
  except:
    code = None

  if code:
    st.subheader("Account verified! Please sign in to continue.")
    sign_in_button = st.button(label='Sign in')
    if sign_in_button:
      success = auth_sign_in(code)
      if not success:
        st.error("You are not authorized to access this portal.")
