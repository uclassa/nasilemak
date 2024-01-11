import streamlit as st
import datetime
from services import Event, get_all_events, post_event, upload_image_file, get_fam_scores, get_num_events, get_num_feedback, delete_event, update_event

def handle_delete_event(event_key: str) -> None:
  # TODO: Implement modal popup confirmation. Call DELETE event API

  res = delete_event(event_key)
  if res.status_code == 200:
    st.toast("Event deleted", icon='🗑️')
  else:
    st.error("Event deletion failed")

def handle_edit_event(event: Event) -> None:
  # TODO: Implement pre-populated modal form.
  st.write(event)

  res = update_event(event)
  if res.status_code == 200:
    st.toast("Event updated", icon='📝')
  else:
    st.error("Event update failed")

def event_list() -> None:
  st.title("Event list")
  events = get_all_events().data

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
      st.button("**EDIT**", key={"edit" + event['name']}, 
                on_click=handle_edit_event, 
                args=([Event(event['name'], event['description'], event['startTime'], event['endTime'], event['location'])])
                )
    with del_col:
      st.button("DELETE", key={"delete" + event['name']}, type="primary", 
                on_click=handle_delete_event, 
                args=(event['key'])
                )

def post_event_form() -> None:
  with st.form("Add Event"):
    name = st.text_input("**Event Title**")
    description = st.text_input("**Description**")
    
    start_date_col, start_time_col, end_date_col, end_time_col = st.columns(4)
    with start_date_col:
      start_date = st.date_input("**Start Date**", datetime.date.today(), format="MM/DD/YYYY", min_value=datetime.date.today())
    with start_time_col:
      start_time = st.time_input("**Start Time**")
    with end_date_col:
      end_date = st.date_input("**End Date**", datetime.date.today(), format="MM/DD/YYYY", min_value=datetime.date.today())
    with end_time_col:
      end_time = st.time_input("**End Time**")
    
    start_date_time = datetime.datetime.combine(start_date, start_time)
    end_date_time = datetime.datetime.combine(end_date, end_time)
    
    location = st.text_input("**Location**")
    uploaded_file = st.file_uploader("Upload an image. This image will be used as the cover photo on the website.", type=["png", "jpg", "jpeg"])
    submit = st.form_submit_button("**Submit**")

  if submit:
    event = Event(name, description, start_date_time, end_date_time, location)
    
    if uploaded_file is not None:
      res = upload_image_file(uploaded_file)
      if res.status_code == 200:
        st.toast("Image uploaded", icon='📷')
      else:
        st.error("Image upload failed. Default image will be used.")
    else:
      st.warning("No image uploaded. Default image will be used.")
    
    # TODO: include obtained image URL in event object
    res = post_event(event)
    if res.status_code == 200:
      st.toast("Event Submitted", icon='✨')
    else:
      st.error("Event submission failed.", res.data)

def dashboard():
  st.title("Events dashboard")
  col1, col2 = st.columns(2)
  with col1:
    num_events = get_num_events().data
    st.metric("Events to date", num_events)
  with col2:
    num_feedback = get_num_feedback().data
    st.metric("Feedbacks to date", num_feedback)

  st.subheader("Family Leaderboard")
  fam_scores = get_fam_scores().data
  st.bar_chart(fam_scores)

def events_view():
  dashboard()
  event_list()

def post_event_view():
  st.title("Post an event")
  st.write("Use the form below to post an event!")
  st.write("The event will be shown on the SSA website, and Ah Gong will be notify members when the event is coming up!")
  post_event_form()