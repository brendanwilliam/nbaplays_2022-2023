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
| Column Name | Description | Example value | Example description |
| --- | --- | --- | --- |
| game_id | Game Id | S2223-G0812 | The 812th game of the 2022-2023 NBA season |
| period | Period of play | 3 | The 3rd quarter of the game |
| clock | Game-clock at time of play | 06:13 | 6 minutes and 13 seconds remain in the quarter |
| home | Home team | BOS | The Boston Celtics as the home team |
| scoreHome | Home team points at time of play | 80 | The home team has 80 points |
| away | Away team | DEN | The Denver Nuggets as the away team |
| scoreAway | Away team points at time of play | 78 | The away team has 78 points |
| playerNameI | Player making the play | J. Tatum | Jason Tatum |
| teamTricode | Team of the player making the play | BOS | Boston Celtics |
| description | The description of the play | Tatum 3' Driving Layup (4 PTS) (Horford 4 AST) | Horford gets his 4th assist and Tatum gets his 4th point from a 3-foot driving layup |
| actionType | What kind of play | Rebound | A rebound |
| subType | A more detailed description of a actionType | Driving Floating Bank Jump Shot | A driving, floating, bank jump shot |
| xLegacy | The horizontal position of a player's shot | -99 | 9.9 feet to the left of the basket |
| yLegacy | The vertical position of a player's shot | 40 | 4 feet from the baseline |
| shotDistance | The distance from the basket of a field goal | 11 | An 11-foot shot |
| isFieldGoal | Whether the play is or isn't a field goal | 1 | The play is a field goal |
| shotVal | The number of points that could be scored from a play | 3 | The play was a 3-point shot |
| scoreVal | The number of points that were score on a play | 2 | 2 points were scored |
| location | Which side of the court the play occurred | v | The visiting team's side |

## Data cleaning
All data cleaning was performed with [processor.py](./src/main/processor.py). The operations performed on these data were to eliminate redundant columns, simplify column values, or add context for plays. *None of the data has been modified outside of this specified script.*



