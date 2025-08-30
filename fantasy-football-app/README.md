# Fantasy Football Player Tracker

A web application for tracking and analyzing fantasy football players, their projections, and draft strategies.

## Features

- Displays comprehensive player list with positions, teams, and projected points
- Risk assessment indicators (🚩) for high-risk players
- Undervalued player flags (💎) for potential steals
- Interactive player selection and filtering
- Sortable columns by various metrics
- Player search and filtering capabilities
- Draft strategy tools

## Setup

1. Install Python 3.x
2. Install required packages:
   ```bash
   pip3 install -r requirements.txt
   ```

## Usage

1. Start the web server:
   ```bash
   python3 src/app.py
   ```

2. Open your browser to `http://localhost:5000`

## Data Source

Player data is sourced from your master list with:
- Player names and positions
- Team affiliations
- Projected fantasy points
- Risk indicators
- Undervalued player flags

## Project Structure

- `src/`: Source code
- `data/`: Data files and player lists
- `tests/`: Test files
- `docs/`: Documentation
