# Shot Mesh
### Created by Brendan Keane
**Email:** brendanwillkeane@gmail.com
**Website:** [brendankeane.design](https://www.brendankeane.design)

## About
This project's data comes from play-by-play JSONs from the official [NBA website](https://www.nba.com/). All data can be found within the [processed data folder inside src](./src/data/processed/). The contents of this folder are as follows:
- [all_data.csv](./src/data/processed/all_data.csv): All play-by-play data from the 2022-2023 NBA season
- [players](./src/data/processed/players/): Play-by-play data by player name (ex. *Jason Tatum* = `J-Tatum.csv`)
- [teams](./src/data/processed/teams/): Play-by-play data by team name (ex. *Boston Celtics* = `BOS.csv`)

## Column values
(TODO: Write data definitions for each column)

## Data cleaning
All data cleaning was performed with [processor.py](./src/main/processor.py). The operations performed on these data were to eliminate redundant columns, simplify column values, or add context for plays. *None of the data has been modified outside of this specified script.*



