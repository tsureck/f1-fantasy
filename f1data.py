from operator import index
from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting

class RaceSession:
    def __init__(self, session_name) -> None:
        fastf1.Cache.enable_cache('cache/')
        self.qualy = fastf1.get_session(2021, session_name, 'Q')
        self.qualy.load()
        self.race = fastf1.get_session(2021, session_name, 'R')
        self.race.load()
        pass

    def get_qualy_results(self):
        qualy_results_parsed = ['QUALI RESULTS']
        for driver in self.qualy.results['FullName'][0:10]:
            qualy_results_parsed.append(driver)
        return qualy_results_parsed

    def get_race_results(self):
        race_results_parsed = ['RACE RESULTS']
        for driver in self.race.results['FullName'][0:10]:
            race_results_parsed.append(driver)
        return race_results_parsed

    def get_grid_diff_list(self, fullname_list):
        """
        Input: Driver Name List

        Output: Dict for Driver Name as Key and Position Difference as Value
        """
        driver_name = list(self.race.results["FullName"])
        grid_diff_dict = {}
        for driver in fullname_list:
            i = driver_name.index(driver)
            start = self.race.results["GridPosition"][i]
            end = self.race.results["Position"][i]
            if start == 0.0:
                start = 20
            grid_diff_dict[driver] = start - end
        return grid_diff_dict
