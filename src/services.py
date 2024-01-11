import requests
import json
import os

# DJANGO_BACKEND = os.getenv("DJANGO_BACKEND")

class Response:
  def __init__(self, status_code: int, data: dict):
    self.status_code = status_code
    self.data = data
  
class Event:
  def __init__(self, name: str, description: str, startTime: str, endTime: str, location: str):
    self.name = name
    self.description = description
    self.startTime = startTime
    self.endTime = endTime
    self.location = location


def get_all_events() -> Response:
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
  return Response(200, event)

def delete_event(key: str) -> Response:
  return Response(200, {key: "deleted"})

def update_event(event: Event) -> Response:
  return Response(200, event)


def get_all_feedback() -> Response:
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


def post_announcement(announcement: str) -> Response:
  return Response(200, announcement)

def get_fam_scores() -> Response:
  return Response(200, {"East-West": 10, "North-South": 40, "Circle": 30, "Downtown": 20})

def get_num_events() -> Response:
  return Response(200, 10)

def get_num_feedback() -> Response:
  return Response(200, 20)