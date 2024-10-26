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
    session_name = 'United State'
    if session_name in ('Q', 'R'):
        error("Session Name must be a race track not Q or R")

    fantasy = RaceSession(2024, session_name)
    num_yellow = sum([1 for x in fantasy.race.track_status['Message'].values if x == 'Yellow'])

    ### Working Methods
    # Qualy Results
    fantasy.get_qualy_results()

    # Race Results
    fantasy.get_race_results()

    # Grid to Checkered Flag Position Difference
    drivers = ['George Russell', 'Lewis Hamilton']
    fantasy.get_grid_diff_list(drivers)

if __name__ == '__main__':
    main()
