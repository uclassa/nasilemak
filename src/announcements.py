import streamlit as st

def handle_submit(announcement) -> None:
  # TODO: call API to submit announcement
  pass

def post_announcement() -> None:
  st.write("Welcome to the announcements page")
  st.write("Please enter your announcement below")
  announcement = st.text_area("Announcement will be sent to all group chats accessible by Ah Gong👴")
  if st.button(":green[Submit]"):
    try:
      handle_submit(announcement)
    except:
      st.error("Error submitting announcement")
    st.toast("Announcement Submitted", icon='✨')

def announcement_history() -> None:
  st.write("Here are the previous announcements")

def announcements_view():
  st.title("Announcements")
  post_announcement()