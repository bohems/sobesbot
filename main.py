from google.colab import auth
from google.auth import default

import gspread

!pip install gspread_formatting
from gspread_formatting import *

def authorize_in_google_services():
  auth.authenticate_user()
  creds, _ = default()
