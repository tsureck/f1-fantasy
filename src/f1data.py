"""
Module to get f1 data from the f1fast package
"""

import fastf1
import fastf1.plotting

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

        self.race = fastf1.get_session(year, session_name, 'R')
        self.qualy = fastf1.get_session(year, session_name, 'Q')
        self.race.load()#messages=True)
        self.qualy.load()
        pass

    def get_qualy_results(self):
        """
        Method for formatting and returning the qualifying results

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

        Input: Driver Name List

        Output: Dict for Driver Name as Key and Position Difference as Value
        """

        grid_diff_dict = {}
        driver_name = list(self.race.results["FullName"])

        for driver in fullname_list:
            i = driver_name.index(driver)
            start = self.race.results["GridPosition"][i]
            end = self.race.results["Position"][i]
            # TODO: Check if there are more edge cases (multiple drivers with pos 0.0)
            if start == 0.0:
                start = 20
            grid_diff_dict[driver] = start - end
        return grid_diff_dict

    def get_total_num_track_limits(self):
        """ Get Total Number of track limits """
        count = 0

        for message in self.race.race_control_messages['Message']:
            if 'TRACK LIMIT' in message and \
                    'DELETED' in message and \
                    'NEXT LAP' not in message and \
                    'UDNDER INVESTIGATION' not in message:
                count += 1
        return count
