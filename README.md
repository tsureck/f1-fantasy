# Project to automate a Google Spreadsheet for F1 Fantasy Tipping

This project uses the fastf1 package and google spreadsheet api package, to calculate the metrics
used in a custom f1 fantasy sheet and enter them in the sheet.

This will be modified to only calculate metrics and not interact with the google spreadsheet,
as this is just unnecessary complexity.

# Installation

## Python3.10

[Ubuntu 20 Python3.10](https://gist.github.com/rutcreate/c0041e842f858ceb455b748809763ddb)

## Poetry

Install Poetry with Python:
``` bash
python3.10 -m pip install poetry
```

Install python environment with poetry
```bash
poetry config virtualenvs.in-project true
poetry install
```

# How to run it
(WIP! First you need to set up a mail that serves for the google spreadsheet api to enter and read stuff.) 

Then you can start the script in the following way:
```bash
# Currently for testing purpose
poetry run python main.py

# Later it will be
poetry run python main.py <Race Name> <Session>
```

Here `<Race Name>` stands for the city of the Race

-> Imola, Monaco, Bahrain etc.

and `<Session>` is an optional argument.
If we give `Q` as a argument, the script only enters the qualyfying position.

If we give `R` as a argument, the script enters everything besides the qualyfying positions.

If we don't give `<Session>` something it automatically enters everything.