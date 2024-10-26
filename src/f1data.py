"""Module to get f1 data from the f1fast package."""

import fastf1
import fastf1.plotting

class RaceSession:
    """Class for extracting f1 data from fastf1."""

    def __init__(self, year: int, session_name: int | str) -> None:
        """Initialize Race Session Class.

        :param year: year of the race
        :type year: int
        :param session_name: identifier of the session
        :type session_name: int | str
        """
        self.race = fastf1.get_session(year, session_name, 'R')
        self.qualy = fastf1.get_session(year, session_name, 'Q')
        self.race.load()#messages=True)
        self.qualy.load()
        pass

    def get_qualy_results(self) -> list[str]:
        """Return the qualifying results.

        :returns: qualy result with full drivername
        :rtype: list[str]
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

    def get_race_results(self) -> list[str]:
        """Return the race results of a qualy session.

        :returns: race result with full drivername
        :rtype: list[str]
        """
        race_results_parsed = ['RACE RESULTS']
        for driver in self.race.results['FullName'][0:10]:
            race_results_parsed.append(driver)
        # TODO: Fail check -> If len(race_results_parsed) == 1 fail
        return race_results_parsed

    def get_grid_diff_list(self, fullname_list: list[str]) -> dict:
        """Calculate the position difference in the race.

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

    def get_total_num_track_limits(self) -> int:
        """Get Total Number of track limits.

        :returns: total number of track limits
        :rtype: int
        """
        count = 0

        for message in self.race.race_control_messages['Message']:
            if 'TRACK LIMIT' in message and \
                    'DELETED' in message and \
                    'NEXT LAP' not in message and \
                    'UDNDER INVESTIGATION' not in message:
                count += 1
        return count

    def get_num_yellow_flags(self, session: str = 'R') -> int:
        """Get number of yellow flags per session.

        :param session: identifier of session (default = 'R')
        :type session: str
        :returns: number of yellow flags
        :rtype: int
        """
        num_yellow = sum([1 for x in self.race.track_status['Message'].values if x == 'Yellow'])
        return num_yellow

    def get_driver_track_limits(self, driver: str) -> int:
        """Return number of track limits of specified driver.

        :returns: number of track limits for specified driver
        :rtype: int
        """
        pass
