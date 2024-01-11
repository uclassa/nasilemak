import streamlit as st
from services import get_all_feedback


def feedback_list() -> None:
  feedbacks = get_all_feedback().data

  for feedback in feedbacks:
    with st.expander("Feedback from " + feedback['timestamp']):
      st.write(feedback['comment'])

def feedback_view():
  st.write("Read anonymous feedback here")
  feedback_list()
  