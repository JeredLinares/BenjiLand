# Benji's Conway's The Game of Life  
By: JD Linares  
2024 12 22

## Hardware
- Raspberry Pi Zero W 
- LED lights
- Portable Battery Pack
- Key Switches - Red

## Software
- Startup script
-- Add line in crontab -e
```
@reboot python /scripts/benji_game_of_life.py
```
- Main Program
* Rule 1: Any live cell with fewer than 2 live neighbours dies, as if by under-population
* Rule 2: Any live cell with 2 or 3 live neighbours lives on to the next generation
* Rule 3: Any live cell with more than 3 live neighbours dies, as if by over-population
* Rule 4: Any dead cell with exactly 3 live neighbours becomes a live cell, as if by reproduction

## Data
- Inital Conditions File

