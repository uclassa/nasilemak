import os
import streamlit as st
import asyncio
import extra_streamlit_components as stx

from services import set_login_state
from httpx_oauth.clients.google import GoogleOAuth2
from dotenv import load_dotenv

load_dotenv('.env')
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDIRECT_URI = os.environ['REDIRECT_URI']
SSA_GMAIL_ID = os.environ['SSA_GMAIL_ID']


def nav_to(url):
  nav_script = """
    <meta http-equiv="refresh" content="0; url='%s'">
  """ % (url)
  return st.write(nav_script, unsafe_allow_html=True)

    
async def get_authorization_url(client: GoogleOAuth2, redirect_uri: str):
  authorization_url = await client.get_authorization_url(
                                  redirect_uri, 
                                  scope=["email", "profile"], 
                                )
  return authorization_url


async def get_access_token(client: GoogleOAuth2, redirect_uri: str, code: str):
  token = await client.get_access_token(code, redirect_uri)
  return token


async def get_email(client: GoogleOAuth2, token: str):
  user_id, user_email = await client.get_id_email(token)
  return user_id, user_email


def authenticate():
  client: GoogleOAuth2 = GoogleOAuth2(CLIENT_ID, CLIENT_SECRET)
  authorization_url = asyncio.run(get_authorization_url(client, REDIRECT_URI))
  
  try:
    asyncio.run(nav_to(authorization_url))
    code = st.experimental_get_query_params()['code']
    token = asyncio.run(get_access_token(client, REDIRECT_URI, code))
    user_id, user_email = asyncio.run(get_email(client, token['access_token']))
    
    if user_id == SSA_GMAIL_ID:
      set_login_state(user_id)
  
  except Exception as e:
    print(e)


def auth_sign_in():
  client: GoogleOAuth2 = GoogleOAuth2(CLIENT_ID, CLIENT_SECRET)
  code = st.experimental_get_query_params()['code']
  token = asyncio.run(get_access_token(client, REDIRECT_URI, code))
  user_id, user_email = asyncio.run(get_email(client, token['access_token']))
  
  if user_id == SSA_GMAIL_ID:
    set_login_state(user_id)
  