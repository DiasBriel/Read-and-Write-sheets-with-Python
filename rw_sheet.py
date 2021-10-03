from googleapiclient.discovery import build

from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '' #key files download from Google api
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '' #Sheet ID
creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def read_sheets(where_read):
    service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=where_read).execute()
    values = result.get('values', [])
    return values

sample = [[""]]

def write_final_result(to_write = sample):
    service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API
    sheet = service.spreadsheets()
    request = sheet.values().update(spreadsheetId=SPREADSHEET_ID, range="example!G4:H27", 
                                valueInputOption="USER_ENTERED", body={"values": to_write}).execute()
    return "ok"

