from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build, HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SCOPES = ['https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/drive.file',
          'https://www.googleapis.com/auth/drive.appdata']

def main():
  creds = None
  # The file token.pickle stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
      creds = pickle.load(token)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
              'client_secret.json', SCOPES)
      creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

  service = build('drive', 'v3', credentials=creds)

  #Everthing above this line is Google Drive Boilerplate code

  request = service.files().list(pageSize=1000, fields="nextPageToken, files(id, name)")
  response = request.execute()
  next_page_token = response['nextPageToken']
  while next_page_token is not None:
    next_page_request = service.files().list_next(request, response)
    next_page_response = next_page_request.execute()
    request = next_page_request
    response = next_page_response
    next_page_token = response.get('nextPageToken')
    file_dicts = response.get('files', [])
    for file_dict in file_dicts:
      if file_dict['name'].endswith((".tif",".tiff",".TIF",".TIFF")):
        try:
          service.files().delete(fileId=file_dict['id']).execute()
          print(f"{str(file_dict['name'])} has been deleted.")
        except HttpError as ex:
          if ex.resp.status == 403:
              print(f"ERROR: updating permission for file: {file_dict['name']}", file=sys.stderr)

if __name__ == '__main__':
  main()
