from ast import Str
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from requests import session

from f1data import RaceSession

class F1Fantasy:
    def __init__(self,session_name) -> None:
        pass
        _scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        _creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", _scope)
        _client = gspread.authorize(_creds)
        self.sheet = _client.open("F1 Fantasy 2022").sheet1
        self.data = self.sheet.get_all_records()  # Get a list of all records
        self.session = RaceSession(session_name)

    def enter_Qualy(self):
        QUALY_RESULTS = self.session.get_qualy_results()

        qualy_cell_list = self.sheet.range('B3:B12')
        for i,cell in enumerate(qualy_cell_list,1):
            print(QUALY_RESULTS[i])
            cell.value = QUALY_RESULTS[i]
        
        self.sheet.update_cells(cell_list=qualy_cell_list)

    def enter_Race(self):
        RACE_RESULTS = self.session.get_race_results()

        race_cell_list = self.sheet.range('C3:C12')
        for i,cell in enumerate(race_cell_list,1):
            print(RACE_RESULTS[i])
            cell.value = RACE_RESULTS[i]
        
        self.sheet.update_cells(cell_list=race_cell_list)
