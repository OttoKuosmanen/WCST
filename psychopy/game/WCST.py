# IMPORTS
from psychopy import visual, core, event, sound, prefs
import random
import csv
import os
import pandas as pd


# OUTPUT
results_destination = "../results/"   # Data storage. Excel friendly csv.
filename = "BLANK"  # Participant_id

index = ["card","chosen card", "success", "matched on categories", "active rule",  "win streak"]
game_data = [] 


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
        Sett window before initialzing any cards.
        Dependent on correct image_path: Sett inside the class. 
        As of now, only works if you actually have png files at the image_path, that are named following the format: number_shape_color.png
        
    get_psychopy(position) -> obj
        Creates a PsychoPy ImageStim object representing the card.
    """
    
    #The directory path where card images are stored and card_size.
    image_path = "../cards/"
    card_size = (128,176)
    _pos = None
    window = None
    
    @classmethod
    def set_window(cls,window):
        cls.window = window
    
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
        return "{num},{shape},{color}".format(num=self.number,shape=self.shape, color=self.color)
    
    def get_filename(self): # property possibility
        """Return filename of the image file for that card"""
        fname = os.path.join(self.image_path, "%i_%s_%s.png"%(self.number, self.shape, self.color))
        return fname
    
    def create_psychopy(self, position=(0,0), **kwargs):
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
        if not Card.window:
            raise ValueError("The window attribute for Card is not set. Use Card.set_window() and give the class a valid psychopy window configuration.")
        ppy_repr = visual.ImageStim(Card.window,image=self.get_filename(),size=(self.card_size),pos=(position), **kwargs)
        return ppy_repr
        
    @property
    def pos(self):
        return self._pos
    
    @pos.setter
    def pos(self, value):
        self._pos = value
        self.psypy.pos = value

        
    def render(self):
        self.psypy.draw()
        
    @property
    def rect(self):
        """A method that gives the cordinates of the card: Used when looking for mouse clicks"""
        width, height = self.card_size
        xpos, ypos = self.psypy.pos
        left = xpos - width / 2
        right = xpos + width / 2
        top = ypos + height / 2
        bottom = ypos - height / 2

        return [left, top, right, bottom]
        

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
            card.pos = (self.xpos, self.ypos)
            card.render()


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
    Compiles the stimulus decks and gives them the presett card, rendering cordinates and a clickbox.
    Contains data:
        -xpos_stimcard   -int
        -ypos_discard   -int
        -stimdesign    -dict : contains text information for psychoppy textStim object : Can be changed in class for visual customization.
    Method
    ------
    render()
    Contains a custom renderingg method, specific for this multistack.
    It will always draw the stimulus card, and if there are cards present in the discard stack, the top card will be rendered.
    Additionally, it will draw a psychopy text object on top of the stimulus card, indicating keybord input for choosing that stimulus card.
    """
    
    ypos_stimcard = 400
    ypos_discard = 200
    
    stimdesign  = {
    'font': 'Arial',
    'height': 42,
    'color': 'white',
    'bold': True
    }
    
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
            
        self.stimulus_card.pos = (self.xpos, self.ypos_stimcard)
        
    def __repr__(self):
        if len(self.list_of_cards)>0:
            card=self.list_of_cards[-1]
        else:
            card="<empty>"
        return "DiscardStack(%s, %s)"%(self.stimulus_card, card)
        
    def render(self):
        # render the stimulus card
        self.stimulus_card.pos = (self.xpos, self.ypos_stimcard)
        self.stimulus_card.render()
        # if there are cards in the discard stack render the top card
        if self.list_of_cards:
            card=self.list_of_cards[-1]
            card.pos = (self.xpos, self.ypos_discard)
            card.render()
        # render the number on top of the stack
        add = {
        'text': self.stimulus_card.number,
        'pos': (self.xpos, self.ypos_stimcard + 110)
        }
        design = DiscardStack.stimdesign.copy()
        design.update(add)
        stim_text = visual.TextStim(window, **design)
        stim_text.draw()




    
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
            
            
def track(data_point, trial):
    trial.append(data_point)
    return trial
    
    

def results(data):
    holder = "blank"
    preservative_error = 0
    index = ["card","chosen card", "success", "matched on categories", "active rule",  "win streak"]
    # procent_correct
    win_list = [item[2] for item in data]
    total_correct = sum(win_list)
    total_number = len(win_list)
    procent_correct = total_correct /total_number * 100
    
    # Categories completed
    win_streak = [item[5]for item in data]
    completed = [item[5] for item in data if item[5] == 5]
    completed_categories = len(completed)
    
    # Error type
    active_rule = [item[4] for item in data]
    matched_categories = [item[3] for item in data]
    
    for index, (win, rule, matched, streak) in enumerate(zip(win_list, active_rule, matched_categories, win_streak)):  # Figure out how to calculate this
        print(index)
        if streak == 5:
            holder = rule
        if win == False and holder in matched:
            print(f"There was a preservative error at trial:{index + 1}")
            preservative_error += 1
    
    
    
    return procent_correct, completed_categories, preservative_error
    




# initialize
rules = ["shape", "color", "number"]
win_streak=0

# Window settings
window = visual.Window([1800,1200], monitor="testMonitor", units="pix")
Card.set_window(window) # Pass in the window for the card class

# Create stacks of cards
mainstack = MainStack()
dstacks = {i:DiscardStack(i) for i in range(1,5)}


# TEXTS

intro = {
    'text': 'Welcome to the Wisconsin type Card Sorting Task! \n \n Press Space to continue or Esc to quit.',
    'font': 'Arial',
    'height': 36,
    'color': 'white',
    'bold': True,
    'italic': False,
    'pos': (0, -100)
}

instruct = {
    'text': 'Your task is to put the cards into four groups, underneath the ones on top of the screen. You will be informed whether you are right or wrong. \n \n To choose the group you can either click the card or use the corresponding numbers on your keyboard.\n \n Press space when you are ready to start the game!',
    'font': 'Arial',
    'height': 26,
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

text_input = visual.TextBox2(win=window, text='Write your username: ')

#SOUNDS
# Create a sound object from an audio file
#sound_file = "sounds/win.wav"
#win_music = sound.Sound(sound_file)
#sound.init()

#LOGO
logo = visual.ImageStim(window,image="../logo/logo.png",pos=(0,300),size=(400,400))

# GAME

# set active rule
active_rule = random.choice(rules)


# Start screen
intro_txt = visual.TextStim(window, **intro)
start_key = "space"
end_key = "escape"
"""
while True:
    logo.draw()
    intro_txt.draw()
    window.flip()

    # Check for keypresses
    keys = event.getKeys()

    if start_key in keys:
        break
    elif end_key in keys:
        window.close()
        core.quit()
"""


# user_name

username = []
valid_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

while True:
    logo.draw()
    keys = event.getKeys()
    
    if 'return' in keys:
        break
    elif 'backspace' in keys:
        if len(username) > 0:
            text_input.text = text_input.text[:-1]
            username = username[:-1]
    elif 'space' in keys:
        pass
    elif len(keys) == 1 and keys[0] in valid_characters:
        username += keys[0]
        text_input.text += keys[0]
    
    text_input.draw()
    window.flip()

window.flip(clearBuffer=True)
    
if len(username) > 0:
    filename ="".join(username)
else:
    filename = random_key(21)
    
## instructions
instruction = visual.TextStim(window, **instruct)
while True:
    
    instruction.draw()
    window.flip()

    # Check for keypresses
    keys = event.getKeys()

    if start_key in keys:
        break
        
mouse = event.Mouse()
#Main loop
while len(mainstack)>40:
    
    trial = [] # initialize a trial data list

    # Render the top card of the stack
    mainstack.render()
    
    # Render top card of discard stack and the corresponding stimcards
    for stack in dstacks.values():
        stack.render()
          

    # Update window
    window.flip()
    
    choice = None
    while choice is None:
        # Check for mouse click first
        if mouse.getPressed()[0]:  # [0] corresponds to the left mouse button
            mouse_pos = mouse.getPos()
            for i, dstack in dstacks.items():
                rect = dstack.stimulus_card.rect
                if (rect[0] <= mouse_pos[0] <= rect[2] and rect[1] >= mouse_pos[1] >= rect[3]): #left,top,right,bottom
                    choice = i
                    break
        else:
            # If no mouse click, wait for keyboard input
            keys = event.getKeys(keyList=['1','2','3','4'])
            if keys:
                choice = int(keys[0])

    
    # Pop the top card from the mainstack and put it in the right discard pile
    card = mainstack.pop()
    track(card.__repr__(),trial)
    
    dstacks[choice].add(card)
    track(dstacks[choice].stimulus_card.__repr__(),trial)
    

    
    # Feedback
    chosen_card=dstacks[choice].stimulus_card
    correct = card.get_card_property(active_rule)==chosen_card.get_card_property(active_rule)
    track(correct,trial)
    
    if correct:
        #win_music.stop()
        #win_music.play()
        win_streak += 1 
        text = visual.TextStim(window, **success)
        text.draw()
    else:
        win_streak = 0
        text = visual.TextStim(window, **fail)
        text.draw()
        
    # Logg results
    match = matched_category(rules, choice, card)
    track(match,trial)
    track(active_rule,trial)
    track(win_streak,trial)
    # Change rule if streak is more than 5   
    if win_streak >= 5:
        active_rule=random.choice(list(set(rules).difference([active_rule])))
        win_streak = 0
    
    game_data.append(trial)

# results

p, c, e = results(game_data)
pro = int(p)

#End screen
window.flip(clearBuffer=True)
results = visual.TextStim(window, f"You got a total of {pro}% correct  \n You completed a total of {c} categories \n Preservative errors: {e}") # show some score data at the end of the game.
results.draw()
window.flip()
core.wait(3)


# save data
game_data_dicts = []

for trial_data in game_data:
    trial_dict = {}
    
    for i, field in enumerate(index):
        trial_dict[field] = trial_data[i]
    
    game_data_dicts.append(trial_dict)

df = pd.DataFrame(game_data_dicts)

output_filename = f"{filename}_data.csv"
df.to_csv(os.path.join(results_destination, output_filename), index=False)

# close the window
window.close()

# clean up at the end of the experiment.
core.quit()
