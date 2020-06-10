import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def PullWorkBook (event=None,context=None):
    #lambda variables
    WorkbookID = event['queryStringParameters']['workbookid']
    SheetIndex = int(event['queryStringParameters']['sheetindex'])

    AppendSheets = "No" # appends all of the sheets into one dataframe


    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('Google_project.json', scope)
    client = gspread.authorize(creds)
    if AppendSheets == "No":

        #print('Connected to Google sheets')
        sheet = client.open_by_key(WorkbookID).get_worksheet(SheetIndex)

        Googlesheet = sheet.get_all_records()
        print(Googlesheet)

        #headers = Googlesheet.pop(0)

        #df = pd.DataFrame(Googlesheet, columns=headers)
        df = pd.DataFrame(Googlesheet)

        print(df)
        #print(df.head())
        #  "Content-Type": "application/xlsx",
        return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/csv","Content-disposition": "attachment; filename=testing.csv"},
        "body": df.to_csv(encoding='utf-8-sig')
        }

        #return df.to_excel("output.xlsx") 
        #if AppendSheets == "Yes":
        #sheetlist = client.open_by_key(WorkbookID).sh

#PullWorkBook()
