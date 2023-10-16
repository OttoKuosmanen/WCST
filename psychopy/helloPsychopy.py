from psychopy import visual, core, event  # import some libraries from PsychoPy
import random
import csv
import os

filename = "../results/data.csv"
logger = []

class Card:
    image_path = "cards/"

    def __init__(self,number,shape,color):
        self.number = number
        self.shape = shape
        self.color = color

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
        return "Card({num},{shape},{color})".format(num=self.number,shape=self.shape, color=self.color)
    
    def get_filename(self):
        """Return filename of the image file for that card"""
        fname = os.path.join(self.image_path, "%i_%s_%s.png"%(self.number, self.shape, self.color))
        return fname
    
    def get_psychopy(self):
        return None
        #ppy_repr = psychopy.visual.ImageStim(self.get_filename())
        #return ppy_repr
            
class Stack():
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
        pass
        #obj = self.list_of_cards[-1].get_psychopy()
        #obj.x_pos = self.xpos
        #print(self.list_of_cards[-1].shape,self.list_of_cards[-1].number,self.list_of_cards[-1].color)

class MainStack(Stack):
    """
    Reprenstation of the main stack, containing the full set in the beginning.
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
        
    def render(self):
        print("Main Stack: %s"%self.list_of_cards[-1])
        # call self.list-of_cards[-1].render()
    

class DiscardStack(Stack):
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
        if len(self.list_of_cards)>0:
            card=self.list_of_cards[-1]
        else:
            card="<empty>"
        print("Stimulus: %s, Last card: %s"%(self.stimulus_card, card))
        # call self.stimcard.render() and place at ypos_stimcard
        # call self.list_of_cards[-1].render()


def user_input():
    while True:
        try:
            c = int(input("Type 1, 2, 3, or 4 to choose where to group your card: "))
            if c in [1, 2, 3, 4]:
                return c
            else:
                print("Please enter a valid choice (1, 2, 3, or 4).")
        except ValueError:
            print("Please enter a valid choice (1, 2, 3, or 4).")

def matched_category(rules,choice,card):
    """" parameters: 
        a function that takes in, a list of matching categories 'aka' rules, and two card objects
        returns: a list of strings that contain the categories on which the cards are matched """
    matched = []
    for rule in rules:
        if card.get_card_property(rule) == chosen_card.get_card_property(rule):
            matched.append(rule)
    return matched

def save_results(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

mainstack = MainStack()
dstacks = {i:DiscardStack(i) for i in range(1,5)}

# initialize

deck_active = True
rules = ["shape", "color", "number"]
active_rule = random.choice(rules)
win_streak=0

# create a window
win = visual.Window([1600,1200], monitor="testMonitor", units="pix")

#Sett card size
card_size = (128,176)

# get filename of stimuli
s1 = dstacks[1].stimulus_card.get_filename()
s2 = dstacks[2].stimulus_card.get_filename()
s3 = dstacks[3].stimulus_card.get_filename()
s4 = dstacks[4].stimulus_card.get_filename()


# create stimuli with positions
stim1 = visual.ImageStim(win, image=s1, size=(card_size), pos = (dstacks[1].xpos, dstacks[1].ypos_stimcard))
stim2 = visual.ImageStim(win, image=s2, size=(card_size), pos = (dstacks[2].xpos, dstacks[2].ypos_stimcard))
stim3 = visual.ImageStim(win, image=s3, size=(card_size), pos = (dstacks[3].xpos, dstacks[3].ypos_stimcard))
stim4 = visual.ImageStim(win, image=s4, size=(card_size), pos = (dstacks[4].xpos, dstacks[4].ypos_stimcard))

# TEXTS
success = {
    'text': 'Correct!',
    'font': 'Arial',
    'height': 42,
    'color': 'green',
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

# GAMELOOP
for card in mainstack.list_of_cards:
    card = mainstack.pop()
    hand_img = card.get_filename()
    hand = visual.ImageStim(win,image=hand_img,size=(card_size),pos=(mainstack.xpos,mainstack.ypos))
    hand.draw()
    
    stim1.draw()
    stim1_text.draw()
    
    stim2.draw()
    stim2_text.draw()
    
    stim3.draw()
    stim3_text.draw()
    
    stim4.draw()
    stim4_text.draw()


    win.flip()
    keys = event.waitKeys(keyList=['1','2','3','4'])
    choice = int(keys[0])
    dstacks[choice].add(card)
    
    for i, value in enumerate(range(1, 5)):
        if len(dstacks[value].list_of_cards) > 0:
            d = visual.ImageStim(win, image=dstacks[value].list_of_cards[-1].get_filename(), size=(card_size), pos = (dstacks[value].xpos, dstacks[value].ypos_discard))
            d.draw()
    
    chosen_card=dstacks[choice].stimulus_card
    correct = card.get_card_property(active_rule)==chosen_card.get_card_property(active_rule)
    
    print(correct)
    if correct:
        win_streak += 1 
        text = visual.TextStim(win, **success)
        text.draw()
    else:
        win_streak = 0
        
    # Logg results
    match = matched_category(rules, choice, card)
    trial = [active_rule, match]
    logger.append(trial)    
    
    # Change rule if streak is more than 5   
    if win_streak >= 5:
        active_rule=random.choice(list(set(rules).difference([active_rule])))
        win_streak = 0
    
# close the window
win.close()

# clean up at the end of the experiment.
core.quit()
