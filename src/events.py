import streamlit as st

def get_events() -> list:
  # TODO: Call GET event API
  # Dummy data
  events = [
    {
      "name": "Event 1",
      "description": "This is the first event",
      "startTime": "2021-10-01T00:00:00Z",
      "endTime": "2021-10-01T01:00:00Z",
      "location": "Online",
      "key": "1"
    },
    {
      "name": "Event 2",
      "description": "This is the second event",
      "startTime": "2021-10-02T00:00:00Z",
      "endTime": "2021-10-02T01:00:00Z",
      "location": "Online",
      "key": "2"
    },
    {
      "name": "Event 3",
      "description": "This is the third event",
      "startTime": "2021-10-03T00:00:00Z",
      "endTime": "2021-10-03T01:00:00Z",
      "location": "Online",
      "key": "3"
    }
  ]
  return events

def get_fam_scores() -> dict:
  return {"East-West": 10, "North-South": 40, "Circle": 30, "Downtown": 20}

def get_num_events() -> int:
  return 10

def get_num_feedback() -> int:
  return 10

def handle_delete_event(event_key) -> None:
  # TODO: Implement modal popup confirmation. Call DELETE event API
  pass

def handle_edit_event(event) -> None:
  # TODO: Implement pre-populated modal form. Call PUT event API
  pass

def event_list() -> None:
  st.title("Event list")
  events = get_events()

  for event in events:
    name_col, desc_col, start_col, end_col, loc_col, edit_col, del_col = st.columns(7)

    with name_col:
      st.write(event['name'])
    with desc_col:
      st.write(event['description'])
    with start_col:
      st.write(event['startTime'])
    with end_col:
      st.write(event['endTime'])
    with loc_col:
      st.write(event['location'])
    with edit_col:
      edit = st.button("**EDIT**", key={"edit" + event['name']}, on_click=handle_edit_event(event))
    with del_col:
      delete = st.button("DELETE", key={"delete" + event['name']}, type="primary", on_click=handle_delete_event(event['key']))

def add_event(name, description, startTime, endTime, location) -> None:
  # TODO: Call POST event API
  pass

def post_event_form() -> None:
  # TODO: Replace inputs with proper components
  with st.form("Add Event"):
    name = st.text_input("Name")
    description = st.text_input("Description")
    startTime = st.text_input("Start Time")
    endTime = st.text_input("End Time")
    location = st.text_input("Location")
    submit = st.form_submit_button("Submit")
    st.file_uploader("Upload an image. This image will be used as the cover photo on the website.")

  if submit:
    add_event(name, description, startTime, endTime, location)
    st.toast("Event Submitted", icon='✨')

def dashboard():
  st.title("Events dashboard")
  col1, col2 = st.columns(2)
  with col1:
    st.metric("Events to date", get_num_events())
  with col2:
    st.metric("Feedbacks to date", get_num_feedback())
  st.subheader("Family Leaderboard")
  fam_scores = get_fam_scores()
  st.bar_chart(fam_scores)

def events_view():
  dashboard()
  event_list()

def post_event_view():
  st.title("Post an event")
  st.write("Use the form below to post an event!")
  st.write("The event will be shown on the SSA website, and Ah Gong will be notify members when the event is coming up!")
  post_event_form()