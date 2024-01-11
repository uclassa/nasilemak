import streamlit as st
from services import post_announcement

def handle_submit(announcement) -> None:
  # TODO: call API to submit announcement
  res = post_announcement(announcement)
  if res.status_code == 200:
    st.toast("Announcement Submitted", icon='🙌')
  else:
    st.error("Announcement submission failed")
  pass

def post_announcement() -> None:
  st.write("Welcome to the announcements page")
  st.write("Please enter your announcement below")
  announcement = st.text_area("Announcement will be sent to all group chats accessible by Ah Gong👴")
  if st.button(":green[Submit]"):
    handle_submit(announcement)

def announcements_view():
  st.title("Announcements")
  post_announcement()