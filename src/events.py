import streamlit as st

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

def add_event(name, description, startTime, endTime, location) -> None:
  # TODO: Call POST event API

  events.append({
    "name": name,
    "description": description,
    "startTime": startTime,
    "endTime": endTime,
    "location": location
  }
)

def handle_create_event() -> None:
  # TODO: Make this a modal popup
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
    print(events)

def handle_delete_event(event_key) -> None:
  # TODO: Implement modal popup confirmation. Call DELETE event API
  pass

def handle_edit_event(event) -> None:
  # TODO: Implement pre-populated modal form. Call PUT event API
  pass

def event_list() -> None:
  # TODO: Call GET event API
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

def events_view():
  print("works")
  event_add_button = st.button("**Add Event**", on_click=handle_create_event)
  event_list()