from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting

class RaceSession:
    def __init__(self, session_name) -> None:
        fastf1.Cache.enable_cache('cache/')
        self.qualy = fastf1.get_session(2022, session_name, 'Q')
        self.qualy.load()
        self.race = fastf1.get_session(2022, session_name, 'R')
        self.race.load()

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
