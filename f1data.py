"""
Module to get f1 data from the f1fast package
"""

import fastf1
import fastf1.plotting
from pyparsing import Each

class RaceSession:
    """
    This Class uses the f1fast package to give out information of a certain race
    to use that information in a f1 fantasy google spreadsheet
    """
    def __init__(self, year, session_name) -> None:
        """
        Constructor method for a given race, where the race track name for a f1 track should be given
        and the method store the race and qualy information into member variables
        """
        # fastf1.Cache.enable_cache('cache/')
        self.race = fastf1.get_session(year, session_name, 1)
        self.race.load()#messages=True)
        pass
        # self.race = fastf1.get_session(year, session_name, 'R')
        # self.race.load()#messages=True)

    def get_qualy_results(self):
        """
        Method for formatting and returning the qualyfying results of a qualy session

        Output: Dictionary with Full Driver Name as Key and Position as value
        """
        qualy_results_parsed = ['QUALI RESULTS']
        for driver in self.qualy.results['FullName'][0:10]:
            if driver != "":
                qualy_results_parsed.append(driver)
            else:
                raise TypeError("Wrong Qualy Result Format...")

        if len(qualy_results_parsed) == 10:
            raise TypeError("Wrong lenght of Qualy Results...")
        return qualy_results_parsed

    def get_race_results(self):
        """
        Method for formatting and returning the race results of a qualy session

        Output: Dictionary with Full Driver Name as Key and Position as value
        """
        race_results_parsed = ['RACE RESULTS']
        for driver in self.race.results['FullName'][0:10]:
            race_results_parsed.append(driver)
        # TODO: Fail check -> If len(race_results_parsed) == 1 fail
        return race_results_parsed

    def get_grid_diff_list(self, fullname_list):
        """
        Method for calculating the position difference from start of the race to the finish

        Input: Driver Name Listq

        Output: Dict for Driver Name as Key and Position Difference as Value
        """
        driver_name = list(self.race.results["FullName"])
        driver_name = [swap_fullname(name) for name in driver_name]
        grid_diff_dict = {}
        for driver in fullname_list:
            i = driver_name.index(driver)
            start = self.race.results["GridPosition"][i]
            end = self.race.results["Position"][i]
            if start == 0.0:
                start = 20
            grid_diff_dict[driver] = start - end
        return grid_diff_dict

def swap_fullname(fullname):
    """
    Suiiii
    """
    name = ''
    surname = ''
    still_for_name = True
    for char in fullname:
        if char == ' ':
            still_for_name = False
            continue
        if still_for_name:
            name += char
        else:
            surname += char

    return surname + ' ' + name