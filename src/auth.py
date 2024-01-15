import os
import streamlit as st
import asyncio

from services import set_login_state
from httpx_oauth.clients.google import GoogleOAuth2
from dotenv import load_dotenv

load_dotenv('.env')
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDIRECT_URI = os.environ['REDIRECT_URI']
SSA_GMAIL_ID = os.environ['SSA_GMAIL_ID']


def nav_to(url):
  # TODO: Check if this works when hosted
  nav_script = """
    <meta http-equiv="refresh" content="0; url='%s'">
  """ % (url)
  return st.write(nav_script, unsafe_allow_html=True)

    
async def get_authorization_url(client: GoogleOAuth2, redirect_uri: str) -> str:
  '''
  Gets the authorization url for the Google OAuth2 flow. This is the url that the user will be redirected to in order to sign in.

  Args:
    client (GoogleOAuth2): The Google OAuth2 client
    redirect_uri (str): The redirect uri for after the user signs in
  
  Returns:
    str: The authorization url
  '''
  authorization_url = await client.get_authorization_url(redirect_uri, scope=["email", "profile"])
  return authorization_url


async def get_access_token(client: GoogleOAuth2, redirect_uri: str, code: str) -> str:
  '''
  Gets the access token for the Google OAuth2 flow. This is the token that will be used to get the user's email and id.
  
  Args:
    client (GoogleOAuth2): The Google OAuth2 client
    redirect_uri (str): The redirect uri for after the user signs in
    code (str): The code that is returned after the user signs in
  
  Returns:
    str: The access token
  '''
  token = await client.get_access_token(code, redirect_uri)
  return token


async def get_email(client: GoogleOAuth2, token: str) -> tuple:
  '''
  Gets the user's ID and email from the Google OAuth2 flow.

  Args:
    client (GoogleOAuth2): The Google OAuth2 client
    token (str): The access token
  
  Returns:
    tuple(str, str): The user's ID and email
  '''
  user_id, user_email = await client.get_id_email(token)
  return user_id, user_email


def authenticate():
  '''
  Authenticates the user with Google OAuth2.
  If successful, the user's ID is stored in the cookie manager.
  '''
  client: GoogleOAuth2 = GoogleOAuth2(CLIENT_ID, CLIENT_SECRET)
  authorization_url = asyncio.run(get_authorization_url(client, REDIRECT_URI))
  
  try:
    asyncio.run(nav_to(authorization_url))
    code = st.experimental_get_query_params()['code']
    token = asyncio.run(get_access_token(client, REDIRECT_URI, code))
    
  except Exception as e:
    # TODO: Handle unsuccessful authentication.
    st.error(e)


def auth_sign_in(code: str) -> bool:
  '''
  Checks if the current logged in user is authorized to access the admin portal.

  Args:
    code (str): The code that is returned after the user signs in
  
  Returns:
    bool: True if the user is authorized, False otherwise
  '''
  client = GoogleOAuth2(CLIENT_ID, CLIENT_SECRET)
  token = asyncio.run(get_access_token(client, REDIRECT_URI, code))
  user_id, user_email = asyncio.run(get_email(client, token['access_token']))
  
  if user_id == SSA_GMAIL_ID:
    set_login_state(user_id)
    return True
  else:
    return False