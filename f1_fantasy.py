import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("F1 Fantasy 2022").sheet1

data = sheet.get_all_records()  # Get a list of all records

print(data[0])

DRIVERS = ["Alex Albon", "Carlos Sainz", "Charles Leclerc", "Daniel Ricciardo", "Esteban Ocon", "Fernando Alonso", "George Russel", "Guanyu Zhou", "Kevin Magnussen", "Lance Stroll", "Lando Norris", "Lewis Hamilton", 
"Max Verstappen", "Mick Schumacher", "Nicholas Latifi", "Pierre Gasly", "Sebastian Vettel", "Sergio Perez", "Valtteri Bottas", "Yuki Tsunoda"]

QUALY_RESULTS = sheet.col_values(2)[1:12]
RACE_RESULTS = sheet.col_values(3)[1:12]

print(QUALY_RESULTS)
print(RACE_RESULTS)
# row = sheet.row_values(3)  # Get a specific row
# col = sheet.col_values(3)  # Get a specific column
# cell = sheet.cell(1,2).value  # Get the value of a specific cell