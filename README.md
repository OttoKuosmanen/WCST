# Wisconsin Card Sorting Task type psychological test. (WCST)

INTRO

This is a Python project to create a computer version of the Wisconsin Card Sorting Task, that runs with Psychopy.
In this project, we used the original paper (Esta Berg, 1948) as a source of inspiration.
The purpose of this project is learning, as this project was done for a university course at the Artic University of Norway, UiT.

The end product is a Wisconsin Card Sorting Task-type game that can be run locally on any computer.

Sources: 
Esta A. Berg (1948) A Simple Objective Technique for Measuring Flexibility in Thinking, The Journal of General Psychology, 39:1, 15-22, DOI: 10.1080/00221309.1948.9918159

DIRECTORIES

Psychopy
In this directory, you will find a Psychopy version of the WCST.

  -game
  The game is stored as WCST.py. You need to have PsychoPy installed locally to play, specifically the standalone version    	(https://www.psychopy.org/download.html). 
  -cards
  Here are the image files of the cards
  -sounds
  Here are the sound files that are used in the game
  sounds sourced from: https://www.zapsplat.com/
  -results
  Here the results of the test will be saved after the completion
  -logo
  Here is the logo for the game: generated with dalle-3
  
Jupyter
This is a directory where the creation of the WCST for Psychopy is documented.

- gamelogic
  here I go through the basics of game logic. The code has changed much in the final file.
- imageCreation
  here I go through the creation of the card images
- create_image_script
  this is the final script to make the 64 card images
- analysis
  This is a data analysis script: OUT OF DATE
- logger
  this is some documentation on how to create the logger: OUT OF DATE


Script
Here you will find the game logic for the WCST as a Python script.
This is the logic of the game that works independently from PsychoPy

-GameLogic
This is the innitial logic of the game that.

-GameLogicV2
