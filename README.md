# Wisconsin Type Card Sorting Task - Psychopy Edition

![logo](logo.png)

![GitHub all releases](https://img.shields.io/github/downloads/keijumies/WCST/total) ![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Keijumies/WCST) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Keijumies/WCST) ![GitHub language count](https://img.shields.io/github/languages/count/Keijumies/WCST) ![GitHub License](https://img.shields.io/github/license/Keijumies/WCST)







This project is a Python-based adaptation inspired by the Wisconsin Card Sorting Task (WCST). Utilizing PsychoPy, we have developed an psychological test that captures the essence of cognitive flexibility. Our version is designed to run locally on any computer. This project was inspired by the original paper by Esta Berg (1948). It was created for educational purposes as part of a university course at the Arctic University of Norway, UiT.

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
   - In the PsychoPy Coder, open the `WCST.py` game script. This file is located in GitHub repository folder `Psychopy` and there in the `game` folder.
   - Execute the script to start the game. <span>Press this: <img src="img.png" alt="logo" style="height:30px; vertical-align:middle;"/> image when the file is opened in the PsychopyCoder.</span>



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

### Exam
Here are the docs, further elaboration on the process of making the test.

- **GameLogic**
  - Initial logic of the game.

**Sources**:
- Esta A. Berg (1948) A Simple Objective Technique for Measuring Flexibility in Thinking, The Journal of General Psychology, 39:1, 15-22, DOI: 10.1080/00221309.1948.9918159


