# Wisconsin Type Card Sorting Task - Psychopy Edition

![logo](logo.png)

This is a Python project where we have created a computer version of the Wisconsin Card Sorting Task, running with PsychoPy. The end product is a psychological test that can be run locally on any computer.

This project was inspired by the original paper by Esta Berg (1948). It was created for educational purposes as part of a university course at the Arctic University of Norway, UiT.

## Installation

1. **Download the Repository**
   - Navigate to the GitHub repository page.
   - Click on the 'Code' button and select 'Download ZIP'

2. **Install PsychoPy**
   - PsychoPy is required to run the game.
   - Download PsychoPy by following this link: [Download PsychoPy Locally](https://www.psychopy.org/download.html).
   - Install PsychoPy on your machine following the instructions provided on the website.

3. **Run the Game**
   - After installing PsychoPy, open the PsychoPy Coder.
   - In the PsychoPy Coder, open the `WCST.py` game script. This file is located in the `Psychopy` directory of the cloned repository.
   - Execute the script to start the game.


## Folder Overview

### Psychopy
In this directory, you'll find a PsychoPy version of the WCST.

- **game**
  - The game is stored as `WCST.py`.
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

**Sources**:
- Esta A. Berg (1948) A Simple Objective Technique for Measuring Flexibility in Thinking, The Journal of General Psychology, 39:1, 15-22, DOI: 10.1080/00221309.1948.9918159


