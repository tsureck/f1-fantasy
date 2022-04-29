from distutils.log import error
import sys

from requests import session

from f1_fantasy import F1Fantasy

def main():
    session_name = sys.argv[1]
    fantasy = F1Fantasy(session_name)
    try:
        sys.argv[2]
    except:
        fantasy.enter_Qualy()    
        fantasy.enter_Race()
    else:
        if sys.argv[2] == 'Q':
            fantasy.enter_Qualy()
        elif sys.argv[2] == 'R':
            fantasy.enter_Race()
        else:
            error("Give either 'Q' or 'R' as input.. not " + str(sys.argv[2]))


if __name__ == '__main__':
    main()