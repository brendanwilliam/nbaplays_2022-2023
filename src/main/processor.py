# Date: April 17, 2023
# Author: Brendan Keane
# Description: This program will work through the play by play data and convert
# it into a more readable format. It will also create a new file with all the
# data contained in the folder 'data/raw' and save it in the folder 'data/processed'

import os
import pandas as pd



# Function loops over every file in the list and converts it into a dataframe
# and adds the game id to the dataframe as a column titled 'game_id'
def load_game(files):

    games = []

    # # Testing with a single file
    # df = pd.read_json('../../data/raw/' + files[0])
    # df['game_id'] = files[0].split('.')[0]

    # # Cleaning the values within the dataframe
    # df = clean_df(df)

    # Looping over every file in the list
    for file in files:
        print("Processing file: " + file)

        # Reading the file as a dataframe
        temp_df = pd.read_json('../../data/raw/' + file)

        # Adding the game id as a column
        temp_df['game_id'] = file.split('.')[0]

        # Cleaning the values within the dataframe
        temp_df = clean_df(temp_df)

        # Appending the dataframe to the main dataframe
        games.append(temp_df)

    # Combining all the dataframes into one dataframe
    df = pd.concat(games)

    return df

# Function is the list of all data cleaning functions used on the dataframe
def clean_df(df):

    # List of columns to keep
    export_columns = ['game_id', 'period', 'clock', 'home', 'scoreHome', 'away', 'scoreAway',\
        'playerNameI', 'teamTricode', 'description', 'actionType', 'subType',\
        'xLegacy', 'yLegacy', 'shotDistance', 'isFieldGoal', 'shotVal', 'scoreVal',\
        'location']

    # Adds 'home' and 'away' columns with the team tricode
    df = create_teams(df)

    # Creates 'shotVal' and 'scoreVal' columns. These columns represent the
    # point value and points scored from a field goal or freethrow
    df = create_shotval(df)
    df = create_scoreval(df)

    # Converting the 'clock' from a string to a time format
    df = convert_clock(df)

    return df[export_columns].reset_index(drop=True)

# Function adds home and away team names to the dataframe
def create_teams(df):

    # Get home team names
    home_df = df[df['location'] == 'h']
    home = home_df['teamTricode'].unique()[0]

    # Get away team names
    away_df = df[df['location'] == 'v']
    away = away_df['teamTricode'].unique()[0]

    # Add home and away team names to the dataframe
    df['home'] = home
    df['away'] = away

    return df

# Function creates the 'shotval' column which measures the point
# value of a field goal
def create_shotval(df):

    # Sets all non-field goal rows to 0
    df.loc[df['isFieldGoal'] == 0, 'shotVal'] = ''

    # Sets all field goal rows to 2 or 3 depending on if it is a 2 or 3 pointer
    df.loc[(df['isFieldGoal'] == 1) & (df['description'].str.contains('3PT')), 'shotVal'] = 3
    df.loc[(df['isFieldGoal'] == 1) & (~df['description'].str.contains('3PT')), 'shotVal'] = 2

    # Sets all free throw rows to 1
    df.loc[df['actionType'] == 'Free Throw', 'shotVal'] = 1

    return df

# Function creates the 'scoreval' column which measures the points scored from a field goal attempt
def create_scoreval(df):

    # Sets all non-field goal rows to 0
    df.loc[df['isFieldGoal'] == 0, 'scoreVal'] = ''

    # Sets all field goal rows to their shot value if they are made shots and 0 if they are missed shots
    df.loc[df['actionType'] == 'Made Shot', 'scoreVal'] = df['shotVal']
    df.loc[df['actionType'] == 'Missed Shot', 'scoreVal'] = 0

    # Sets all free throw rows to 1 if they are made shots and 0 if they are missed shots
    df.loc[(df['actionType'] == 'Free Throw') & (df['description'].str.contains('MISS')), 'scoreVal'] = 0
    df.loc[(df['actionType'] == 'Free Throw') & (~df['description'].str.contains('MISS')), 'scoreVal'] = 1

    return df

# Function converts the 'clock' column from a string to a time format
def convert_clock(df):

    # Cleaning the string to create a time format value
    df['clock'] = df['clock'].str.strip('PT')
    df['clock'] = df['clock'].str.replace('M', ':')
    df['clock'] = df['clock'].str.replace('S', '')
    df['clock'] = pd.to_datetime(df['clock'], format='%M:%S.%f').dt.time

    # Extracting the minutes and seconds from the time format
    df['clock'] = df['clock'].astype(str).str.slice(start=3)

    return df

if __name__ == '__main__':
    # Create a list of all the files in the folder 'data/raw'
    fp = '../data/raw/'
    files = os.listdir(fp)
    df = load_game(files)

    # Save the dataframe as a csv file in the folder 'data/processed'
    df.to_csv('../data/processed/all_data.csv', index=False)