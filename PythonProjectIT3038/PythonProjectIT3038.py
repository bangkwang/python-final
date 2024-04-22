#Name: Aniketh Kallam
#Date: 4/17/2024

import pandas as pd
import re
import matplotlib.pyplot as plt
import argparse

#Setting the display options for pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('all_seasons.csv')

# Define the command line arguments
parser = argparse.ArgumentParser(description='NBA Player Data Retrieval and Visualization')
parser.add_argument('-n', '--name', type=str, required=True, help='The name of the player')
parser.add_argument('-o', '--option', type=int, choices=[1, 2], required=True, help='1 to retrieve player data, 2 to create a graph of player stats over the seasons')
args = parser.parse_args()


    
if args.name and args.option:
    player_name = args.name.lower()

    # Check if the player's name is valid using a regex
    if not re.fullmatch('[a-z ]*', player_name):
        print("Invalid player name. Please only use alphabetic characters and spaces.")
    else:
        if args.option == 1:  #Check if option is equal to '1'
            player_data = df[df['player_name'].str.lower() == player_name][['pts', 'reb', 'ast', 'net_rating','season']]  #Retreive the player data
            if player_data.empty:  #Check if player_data is empty
                print(f"No data found for player: {player_name}")
            else:
                print(player_data)  
        elif args.option == 2:  #Check if option is equal to '2'
            # Create a graph of player stats over the seasons
            player_data = df[df['player_name'].str.lower() == player_name][['pts', 'reb', 'ast', 'net_rating','season']] #Retreive the player data
            if player_data.empty:  #Check if player_data is empty
                print(f"No data found for player: {player_name}")  # Output error
            else:
                player_data.set_index('season', inplace=True)  #Set 'season' column as index
                player_data[['pts', 'reb', 'ast', 'net_rating']].plot(kind='line')  #Create a line graph
                plt.title(f'{player_name.title()} Stats Over the Seasons')  #Set the title of the graph
                plt.ylabel('Stats')  # Set the label for the y-axis
                plt.show()  # Display the graph