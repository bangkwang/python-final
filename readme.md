# NBA Player Data Retrieval and Visualization

This program allows you to retrieve NBA player data or create a graph of player stats over the seasons.
The csv I used was found on Kaggle.com and is updated till the 2022-23 Nba seasons. It contains the demographics of every player since 1996 to 2023. 
Link to csv: https://www.kaggle.com/datasets/justinas/nba-players-data
## Requirements

- Python 3
- pandas
- matplotlib
- argparse
- all_seasons.csv
## Usage

To use this program, you need to provide two command-line arguments: the player's name and the option number.

The player's name should be a string containing the player's first and last name. For example, "Michael Jordan".

The option number should be either 1 or 2. Enter 1 to retrieve player data, or 2 to create a graph of player stats over the seasons.

Here's an example of how to run the program:

py PythonProjectIT3038.py -n "Michael Jordan" -o 1
Displays the raw stats of the player

py PythonProjectIT3038.py -n "Michael Jordan" -o 2
Displays a graph of the stats over the seasons.
