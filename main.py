"""
This script is developed for a f1 fantasy league in a google spreadsheet
to automaticaly enter the results for a given session.
"""

from distutils.log import error

from f1data import RaceSession

def main():
    """
    Main function
    """ 
    session_name = 'Japan'
    if session_name in ('Q', 'R'):
        error("Session Name must be a race track not Q or R")

    fantasy = RaceSession(2024, session_name)
    # https://theoehrly.github.io/Fast-F1-Pre-Release-Documentation/api.html#fastf1.api.track_status_data
    num_yellow = sum([1 for x in fantasy.session.race.track_status['Message'].values if x == 'Yellow'])


def getTrackLimitStat():
    seasons = {}

    for year in (2021,2022,2023):
        seasons[year] = {}
        for i in range(1,24):
            try:
                fantasy = RaceSession(year, i)
                track_limit_messages = [x for x in fantasy.session.sprint.race_control_messages['Message'] if 'TRACK LIMIT' in x and 'DELETED' in x and not 'NEXT LAP' in x and not 'UDNDER INVESTIGATION' in x]
                seasons[year][fantasy.session.sprint.event.Country + '_' + fantasy.session.sprint.event.Location] = len(track_limit_messages)
            except IndexError:
                # If the nth session does not exist, then got further
                break

if __name__ == '__main__':
    main()
