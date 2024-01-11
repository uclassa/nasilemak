import requests
import json
import os

# DJANGO_BACKEND = os.getenv("DJANGO_BACKEND")

class Response:
  def __init__(self, status_code: int, data: dict):
    self.status_code = status_code
    self.data = data
  
class Event:
  def __init__(self, name: str, description: str, start_time: str, end_time: str, location: str, image_url: str = None):
    self.name = name
    self.description = description
    self.start_time = start_time
    self.end_time = end_time
    self.location = location
    self.image_url = image_url

class Announcement:
  def __init__(self, message: str, read_flag: bool = False):
    self.message = message
    self.read_flag = read_flag

def get_all_events() -> Response:
  '''
  Sends GET request to backend to retrieve all events.

  Returns:
    Response: Response object containing the status code and data or error message
  '''

  res = [
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

  return Response(200, res)

def post_event(event: Event) -> Response:
  '''
  Sends POST request to backend to create a new event.

  Args:
    event (Event): The event object to be created
  
  Returns:
    Response: Response object containing the status code and data or error message
  '''
  return Response(200, event)

def upload_image_file(file) -> Response:
  '''
  Uploads image file to Google Drive and returns the URL.

  Args:
    file (File): The image file to be uploaded

  Returns:
    Response: Response object containing the status code and Google Drive URL or error message
  '''
  # TODO: Use Google Drive API to upload file, get URL, and return URL
  return Response(200, {})

def delete_event(key: str) -> Response:
  '''
  Sends DELETE request to backend to delete an event via a given key.

  Args:
    key (str): The key of the event to be deleted
  
  Returns:
    Response: Response object containing the status code and data or error message
  '''
  return Response(200, {key: "deleted"})

def update_event(event: Event) -> Response:
  '''
  Sends PUT request to backend to update a given event.

  Args:
    event (Event): The event object to be updated

  Returns:
    Response: Response object containing the status code and data or error message
  '''
  return Response(200, event)


def get_all_feedback() -> Response:
  '''
  Sends GET request to backend to retrieve all feedbacks.

  Returns:
    Response: Response object containing the status code and data or error message
  '''
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
  return Response(200, feedbacks)


def post_announcement(announcement_text: str) -> Response:
  '''
  Sends POST request to backend to create a new announcement.

  Args:
    announcement (str): The announcement to be sent to all group chats

  Returns:
    Response: Response object containing the status code and data or error message
  '''
  announcement = Announcement(announcement_text)
  return Response(200, {announcement_text: "sent"})

def get_fam_scores() -> Response:
  '''
  Sends GET request to backend to retrieve an object representing current fam scores.

  Returns:
    Response: Response object containing the status code and data or error message
  '''
  return Response(200, {"East-West": 10, "North-South": 40, "Circle": 30, "Downtown": 20})
