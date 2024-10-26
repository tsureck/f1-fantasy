"""
This script is developed for a f1 fantasy league in a google spreadsheet
to automaticaly enter the results for a given session.
"""

from distutils.log import error
import sys

from f1_fantasy import F1Fantasy

def main():
    """
    Main function
    """ 
    session_name = 'Japan'
    if session_name in ('Q', 'R'):
        error("Session Name must be a race track not Q or R")

    fantasy = F1Fantasy(2024, session_name)
    count= 0
    # https://theoehrly.github.io/Fast-F1-Pre-Release-Documentation/api.html#fastf1.api.track_status_data
    num_yellow = sum([1 for x in fantasy.session.race.track_status['Message'].values if x == 'Yellow'])
    # fantasy.enter_qualy()
    pass
    """
    try:
        sys.argv[2]
    except IndexError:
        fantasy.enter_qualy()
        fantasy.enter_race()
        fantasy.enter_constructor_battle()
        fantasy.enter_fastest_lap()
        fantasy.enter_ots_done()
    except TypeError as err:
        print(err)
        break
    else:
        if sys.argv[2] == 'Q':
            fantasy.enter_qualy()
        elif sys.argv[2] == 'R':
            fantasy.enter_race()
            fantasy.enter_constructor_battle()
            fantasy.enter_fastest_lap()
            fantasy.enter_ots_done()
        else:
            error("Give either 'Q' or 'R' as input.. not " + str(sys.argv[2]))
    """

def getTrackLimitStat():
    event_ident = 5 # for race
    seasons = {}

    for year in (2021,2022,2023):
        seasons[year] = {}
        for i in range(1,24):
            try:
                fantasy = F1Fantasy(year, i)
                track_limit_messages = [x for x in fantasy.session.sprint.race_control_messages['Message'] if 'TRACK LIMIT' in x and 'DELETED' in x and not 'NEXT LAP' in x and not 'UDNDER INVESTIGATION' in x]
                seasons[year][fantasy.session.sprint.event.Country + '_' + fantasy.session.sprint.event.Location] = len(track_limit_messages)
            except:
                # If the nth session does not exist, then got further
                break
            pass
        
    pass

if __name__ == '__main__':
    main()
