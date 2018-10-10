import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

def vote(cell):

    credentials = ServiceAccountCredentials.from_json_keyfile_name('kamakura-spread.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open('line-kamakura').sheet1

    num = int(wks.acell(cell).value) + 1
    wks.update_acell(cell, num)
