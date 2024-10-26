"""Script for extracting data for formula one races."""

from distutils.log import error

from f1data import RaceSession

def main():
    """Extract data from fastf1."""
    session_name = 'United State'
    if session_name in ('Q', 'R'):
        error("Session Name must be a race track not Q or R")

    fantasy = RaceSession(2024, session_name)

    # Number of yellow flags
    fantasy.get_num_yellow_flags()

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
