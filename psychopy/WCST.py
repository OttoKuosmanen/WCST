# IMPORTS
from psychopy import visual, core, event, sound, prefs
import random
import csv
import os

# Output
    # To do, make data file name dependent on the user input.
    # or generate random code for users, or something along theese lines.
results_destination = "results/"
filename = "BLANK"
logger = []

# CLASSES
class Card:
    """
    A card class that creates playing card objects.
    Attributes:
    -----------
    number : int
        The number associated with the card
    shape : str
        The shape of the card (e.g., "circle", "square").
    color : str
        The color of the card

    Methods:
    --------
    get_card_property(prop) -> str:
        Returns the requested property of the card. `prop` can be "number", "shape", or "color".

    get_filename() -> str:
        Returns the filename of the image associated with the card.
        _CAUTION_
        Dependent on correct image_path: Sett inside the class. 
        As of now, only works if you actually have png files at the image_path, that are named following the format: number_shape_color.png
        
    get_psychopy(position) -> obj
        Creates a PsychoPy ImageStim object representing the card.
    """
    
    #The directory path where card images are stored.
    image_path = "cards/"
    
    def __init__(self,number,shape,color):
        self.number = number
        self.shape = shape
        self.color = color
        self.psypy = self.create_psychopy()
        
    def get_card_property(self, prop):
        """
        Function returns one of the properties of the card.
        prop is one of "number", "shape" or "color"
        """
        if prop=="number":
            return self.number
        elif prop=="shape":
            return self.shape
        elif prop=="color":
            return self.color
        else:
            raise AttributeError("Unknown atttribute")
    
    def __repr__(self):
        """
        Returns the string representation of the card object
        str: Card(number,shape,color)
        """
        return "Card({num},{shape},{color})".format(num=self.number,shape=self.shape, color=self.color)
    
    def get_filename(self):
        """Return filename of the image file for that card"""
        fname = os.path.join(self.image_path, "%i_%s_%s.png"%(self.number, self.shape, self.color))
        return fname
    
    def create_psychopy(self, position=(0,0)):
        """
        Creates a PsychoPy ImageStim object representing the card.
    
        Parameters:
        -----------
        position : tuple of int, optional
            The (x, y) coordinates for the position of the image in the window.
            Defaults to (0, 0).
    
        Returns:
        --------
        A PsychoPy ImageStim object with the card's image set at the specified position.
        """
        ppy_repr = visual.ImageStim(win,image=self.get_filename(),size=(card_size),pos=(position))
        return ppy_repr
        

class Stack():
    
    """
    A class that simulates a stack, akin to a deck of cards.
    
    Attributes:
    -----------
    list_of_cards : list[Card1,Card2,Card3]
        A list containing objects of the Card class.
        
    Methods:
    --------
    add(new_card: Card) -> None:
        Adds the given card to the top of the stack.
    
    pop() -> Card:
        Removes and returns the card from the top of the stack.
    
        _CAUTION_
        THe end of the list is conceptualized as the top of the stack
    
    render()
        A function that takes the card at the top of the stack and renders it on screen as psychopy image.
        Also, updates the card with a position argument corresponding to its stack.
    """

    
    def __init__(self,list_of_cards):
        self.list_of_cards = list_of_cards
        
    def __repr__(self):
        return repr(self.list_of_cards)
    
    def __len__(self):
        return len(self.list_of_cards)
    
    def add(self,new_card):
        self.list_of_cards.append(new_card)
    
    def pop(self):
        return self.list_of_cards.pop()
    
    def render(self):
        if self.list_of_cards:
            card = self.list_of_cards[-1]
            card.psypy.pos = (self.xpos,self.ypos)
            card.psypy.draw()

class MainStack(Stack):
    """
    This is the player deck. Its a subclass of the stack class.
    Compiles a a list of card objects and gives it a cordinate position.
    
    Contains data:
        Contains lists of card attributes.
        -numbers-list[int]
        -shapes -list[str]
        -colors -list[str]
        -xpos   -int
        -ypos   -int
    """
    
    xpos = 0
    ypos = -200
    numbers = [1,2,3,4]
    shapes = ["circle","square","triangle","star"]
    colors = ["blue","green","red","yellow"]
    
    def __init__(self):
        self.list_of_cards = []
        for i in self.numbers:
            for y in self.shapes:
                for x in self.colors:
                    card = Card(i,y,x)
                    self.list_of_cards.append(card)
        random.shuffle(self.list_of_cards)
        
    

class DiscardStack(Stack):
    """
    This is a multistack. Its a subclass of the stack class.
    A representation of the stimulus cards and their corresponding discard piles.
    Compiles the stimulus decks and gives them the presett card and a rendering cordinates.
    Contains data:
        -xpos_stimcard   -int
        -ypos_discard   -int
    Method
    ------
    render()
    Contains a custom renderingg method, specific for this multistack.
    It will always draw the stimulus card, and if there are cards present in the discard stack, the top card will be rendered.
    """
    
    ypos_stimcard = 400
    ypos_discard = 200
    def __init__(self, num):
        self.list_of_cards=[]
        self.stimulus_card=None
        
        if num==1:
            self.xpos = -300
            self.stimulus_card=Card(1, "triangle", "red")
        elif num==2:
            self.xpos = -100
            self.stimulus_card=Card(2, "star", "green")
        elif num==3:
            self.xpos =  100
            self.stimulus_card=Card(3, "square", "yellow")
        elif num==4:
            self.xpos =  300
            self.stimulus_card=Card(4, "circle", "blue")

    def __repr__(self):
        if len(self.list_of_cards)>0:
            card=self.list_of_cards[-1]
        else:
            card="<empty>"
        return "DiscardStack(%s, %s)"%(self.stimulus_card, card)
        
    def render(self):
        self.stimulus_card.psypy.pos = (self.xpos, self.ypos_stimcard)
        self.stimulus_card.psypy.draw()
        if self.list_of_cards:
            card=self.list_of_cards[-1]
            card.psypy.pos = (self.xpos, self.ypos_discard)
            card.psypy.draw()


    
# FUNCTIONS


def matched_category(rules,choice,card):
    """" parameters: 
        a function that takes in, a list of matching categories 'aka' rules, and two card objects
        returns: a list of strings that contain the categories on which the cards are matched """
    matched = []
    for rule in rules:
        if card.get_card_property(rule) == chosen_card.get_card_property(rule):
            matched.append(rule)
    return matched
    

def random_key(key_length):
    """A function that makes a random string of letters and numbers
    Parameters: lenght of string as int
    Returns: -> str
    """
    key = []
    alpha = "abcdefghijklmnopqrstuvwxyz"
    num = "123456789"
    for i in range(key_length):
        l = random.choice(alpha)
        n = random.choice(num)
        if int(n) % 2 == 0:
            l = l.capitalize()
        key.append(l + n)
    return ''.join(key)

    
    

def save_results(data, results_destination, filename):
    """A function that saves a datafile
    Parameters: datafile, a folder path, a name for the file
    """
    full_path = os.path.join(results_destination, filename)
    with open(full_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

def results(logger):
    """ A function that calculates the procent of correct answers
       param: [[[active_rule][matched_rule]],[[actice_rule][matched_rule]]]
       returns: percent correct as float
    """
    total_correct = 0
    total_items = len(logger)

    for item in logger:
        active_rule = item[0]
        matched = item[1]

        if active_rule in matched:
            total_correct += 1

    percent = total_correct / total_items * 100
    return percent
    
# initialize
rules = ["shape", "color", "number"]
active_rule = random.choice(rules)
win_streak=0
card_size = (128,176)
win = visual.Window([1800,1200], monitor="testMonitor", units="pix")

# Create stacks of cards
mainstack = MainStack()
dstacks = {i:DiscardStack(i) for i in range(1,5)}



# PSYCHOPY CONSTANTS


# TEXTS

intro = {
    'text': 'Welcome to the Wisconsin Card Sorting Task! \n \n Press any key to start.',
    'font': 'Arial',
    'height': 36,
    'color': 'white',
    'bold': True,
    'italic': False,
    'pos': (0, 0)
}

success = {
    'text': 'Correct!',
    'font': 'Arial',
    'height': 42,
    'color': 'green',
    'bold': True,
    'italic': False,
    'pos': (0, 0)
}

fail = {
    'text': 'Wrong!',
    'font': 'Arial',
    'height': 42,
    'color': 'red',
    'bold': True,
    'italic': False,
    'pos': (0, 0)
}

one = {
    'text': '1',
    'font': 'Arial',
    'height': 42,
    'color': 'white',
    'bold': True,
    'pos': (dstacks[1].xpos, dstacks[1].ypos_stimcard + 110)
}

two = {
    'text': '2',
    'font': 'Arial',
    'height': 42,
    'color': 'white',
    'bold': True,
    'pos': (dstacks[2].xpos, dstacks[2].ypos_stimcard + 110)
}

three = {
    'text': '3',
    'font': 'Arial',
    'height': 42,
    'color': 'white',
    'bold': True,
    'pos': (dstacks[3].xpos, dstacks[3].ypos_stimcard + 110)
}

four = {
    'text': '4',
    'font': 'Arial',
    'height': 42,
    'color': 'white',
    'bold': True,
    'pos': (dstacks[4].xpos, dstacks[4].ypos_stimcard + 110)
}

stim1_text = visual.TextStim(win, **one)
stim2_text = visual.TextStim(win, **two)
stim3_text = visual.TextStim(win, **three)
stim4_text = visual.TextStim(win, **four)

#SOUNDS
# Create a sound object from an audio file
#sound_file = "sounds/win.wav"
#win_music = sound.Sound(sound_file)
#sound.init()


# GAME

# Start screen
intro_txt = visual.TextStim(win, **intro)
intro_txt.draw()
win.flip()
event.waitKeys()
#Main loop
while mainstack.list_of_cards:

    # Render the top card of the stack
    mainstack.render()
    
    # Render top card of discard stack and the corresponding stimcards
    for stack in dstacks.values():
        stack.render()
    
    # Update window
    win.flip()
    
    # Get input from user and record it as a variable
    keys = event.waitKeys(keyList=['1','2','3','4'])
    choice = int(keys[0])
    
    # Pop the top card from the mainstack and put it in the right discard pile
    card = mainstack.pop()
    dstacks[choice].add(card)
    
    
    # Feedback
    chosen_card=dstacks[choice].stimulus_card
    correct = card.get_card_property(active_rule)==chosen_card.get_card_property(active_rule)
    
    if correct:
        #win_music.stop()
        #win_music.play()
        win_streak += 1 
        text = visual.TextStim(win, **success)
        text.draw()
    else:
        win_streak = 0
        text = visual.TextStim(win, **fail)
        text.draw()
        
    # Logg results
    match = matched_category(rules, choice, card)
    trial = [active_rule, match]
    logger.append(trial)    
    
    # Change rule if streak is more than 5   
    if win_streak >= 5:
        active_rule=random.choice(list(set(rules).difference([active_rule])))
        win_streak = 0
    
#End screen
win.flip(clearBuffer=True)
filename = random_key(21)
results(logger)

results = visual.TextStim(win, f"You got a total of: {results(logger)}% correct")
results.draw()
win.flip()
core.wait(3)

# save data
save_results(logger,results_destination,filename)
# close the window
win.close()

# clean up at the end of the experiment.
core.quit()
