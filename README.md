# Irish Number Plate Generator

A historically accurate Irish vehicle registration plate 
generator built with Python.

## Features
- Handles both pre-2013 and post-2013 Irish plate formats
- Full county code lookup across all 26 Irish counties
- JSON-based persistent sequence tracking ensuring every 
  generated plate is unique across sessions and follows a sequence
- Real-time year validation via Python's datetime library 
  preventing future-dated or historically invalid registrations
- Robust input validation and error handling throughout

## How it works
Irish plates follow the format YY[half]-CO-NNNNNN:
- YY — last two digits of registration year
- half — 1 (January–June) or 2 (July–December)
- CO — county code (e.g. D for Dublin, C for Cork)
- NNNNNN — unique sequential number

Pre-2013 plates follow the older YY-CO-NNNNNN format 
without the half-year identifier.

## Usage
Run the script and enter:
- Registration year (1987 or later)
- Registration month (1-12)
- County name

## Built with
Python — datetime, json, os, random
