import streamlit as st

feedbacks = [
  {
    "comment": "This is the first feedback",
    "timestamp": "2021-10-01T00:00:00Z"
  },
  {
    "comment": "This is the second feedback",
    "timestamp": "2021-10-01T00:00:00Z"
  },
  {
    "comment": "This is the third feedback",
    "timestamp": "2021-10-01T00:00:00Z"
  }
]

def feedback_list() -> None:
  # TODO: Call get feedback API
  for feedback in feedbacks:
    with st.expander("Feedback from " + feedback['timestamp']):
      st.write(feedback['comment'])

def feedback_view():
  st.write("Read anonymous feedback here")
  feedback_list()
  