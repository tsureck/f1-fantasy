"""
Module for the F1 Fantasy Class
"""

from cmath import nan
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from f1data import RaceSession

class F1Fantasy:
    """
    F1Fatansy Class connects to a Google Spreadsheet where a defined form for a F1 Fantasy League 
    is given, and fills the sheet with results from the qualifying and race, using the RaceSession 
    Class from the f1data Package using f1fast.

    ### Methods:

    * __init__(session_name::string) # Constructor Method

    Session Name = Race Track Name. (Year 2022 is given)

    * enter_Qualy()

    Enter The Qualyfying Results


    * enter_Race()

    Enter The Race Results

    * get_grid_diff()

    Enter the Grid Position Difference into the Sheet

    """
    def __init__(self,session_name) -> None:
        """
        Constructor Method of the F1Fantasy Class

        Connects with the credentials file (creds.json) to a spreadsheet and saves the
        data in a member variable.

        Also creates a object of the f1data class and stores it in a member variable
        """
        _scope = ["https://spreadsheets.google.com/feeds",
                  'https://www.googleapis.com/auth/spreadsheets',
                  "https://www.googleapis.com/auth/drive.file",
                  "https://www.googleapis.com/auth/drive"]
        _creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", _scope)
        _client = gspread.authorize(_creds)
        self.sheet = _client.open("F1 Fantasy 2022").sheet1
        self.data = self.sheet.get_all_records()  # Get a list of all records
        self.session = RaceSession(session_name)

    def enter_qualy(self):
        """
        This functions enters the qualyfying results from the f1data class object
        into the google spreadsheet
        """
        qualy_results = self.session.get_qualy_results()

        qualy_cell_list = self.sheet.range('B3:B12')
        for i,cell in enumerate(qualy_cell_list,1):
            print(qualy_results[i])
            cell.value = qualy_results[i]

        self.sheet.update_cells(cell_list=qualy_cell_list)

    def enter_race(self):
        """
        This functions enters the race results from the f1data class object
        into the google spreadsheet
        """
        race_results = self.session.get_race_results()

        race_cell_list = self.sheet.range('C3:C12')
        for i,cell in enumerate(race_cell_list,1):
            print(race_results[i])
            cell.value = race_results[i]

        self.sheet.update_cells(cell_list=race_cell_list)

    def enter_ots_done(self):
        """
        This function enters the position difference into the spreadsheet for
        every player in the sheet
        """

        bonus_on_diff = 2
        driver_list = []

        players = {}
        for index, name in enumerate(self.data[0].values(), 0):
            if name not in ['QUALI RESULTS', 'RACE RESULTS', 'POSITION', '']:
                players[name] = [str(index+1)]

        driver_for_overtakes_index = nan
        for index, data in enumerate(self.data, 0):
            if "Driver for Overtakes" in data.values():
                driver_for_overtakes_index = index
                break

        for name in players.keys():
            if self.data[driver_for_overtakes_index][players[name][0]] != '':
                driver_list.append(self.data[driver_for_overtakes_index][players[name][0]])
                players[name].append(self.data[driver_for_overtakes_index][players[name][0]])
            else:
                players[name].append(None)

        grid_diffs = self.session.get_grid_diff_list(driver_list)

        # + 3 because algo on top start from line 1 and has one line hidden not incldued
        # And we want one row deeper to enter results
        cell_list = self.sheet.row_values(driver_for_overtakes_index + 3)

        print(cell_list)

        for name in players.keys():
            if players[name][1] != None:
                cell_list[int(players[name][0]) - 1] = int(grid_diffs[players[name][1]] * bonus_on_diff)

        ot_done_ind = [index for index, elem in enumerate(cell_list,0) if elem == 'Overtakes done']

        sheet_range = self.sheet.range(
            chr(65 + ot_done_ind[0]) + str(driver_for_overtakes_index + 3) + ':' + 
            chr(65 + ot_done_ind[1]-1) + str(driver_for_overtakes_index + 3)
            )

        for i, cell in enumerate(sheet_range,0):
            cell.value = cell_list[ot_done_ind[0]:ot_done_ind[1] + 1][i]

        self.sheet.update_cells(sheet_range)
