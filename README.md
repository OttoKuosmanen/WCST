# Wisconsin Card Sorting Task - Python Project

![logo](logo.png)

This is a Python project to create a computer version of the Wisconsin Card Sorting Task, running with PsychoPy. The end product is a game that can be run locally on any computer.

**Sources**:
- Esta A. Berg (1948) A Simple Objective Technique for Measuring Flexibility in Thinking, The Journal of General Psychology, 39:1, 15-22, DOI: 10.1080/00221309.1948.9918159

## DIRECTORIES

### Psychopy
In this directory, you'll find a PsychoPy version of the WCST.

- **game**
  - The game is stored as `WCST.py`. PsychoPy needs to be installed locally to play. [Download PsychoPy](https://www.psychopy.org/download.html)
- **cards**
  - Contains image files of the cards.
- **sounds**
  - Sound files used in the game. Sourced from [Zapsplat](https://www.zapsplat.com/)
- **results**
  - Results of the test are saved here after completion.
- **logo**
  - Logo for the game, generated with DALL-E 3.

### Jupyter
Documentation of the WCST creation for PsychoPy.

- **gamelogic**
  - Basics of game logic. The final code has evolved significantly.
- **imageCreation**
  - Documentation on creating the card images.
- **create_image_script**
  - Final script to create the 64 card images.
- **analysis**
  - Data analysis script (OUT OF DATE).
- **logger**
  - Documentation on creating the logger (OUT OF DATE).

### Script
Find the independent game logic for the WCST as a Python script.

- **GameLogic**
  - Initial logic of the game.

This project was inspired by the original paper by Esta Berg (1948). It was created for educational purposes as part of a university course at the Arctic University of Norway, UiT.

