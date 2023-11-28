import random
import csv
import os


# Classes
class Card:
    image_path = "/..jupyter/cards/"

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
    ypos = -0.5
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
    ypos_stimcard = 0.8
    ypos_discard = -0.2
    def __init__(self, num):
        self.list_of_cards=[]
        self.stimulus_card=None
        
        if num==1:
            self.xpos = -0.6
            self.stimulus_card=Card(1, "triangle", "red")
        elif num==2:
            self.xpos = -0.3
            self.stimulus_card=Card(2, "star", "green")
        elif num==3:
            self.xpos =  0.3
            self.stimulus_card=Card(3, "square", "yellow")
        elif num==4:
            self.xpos =  0.6
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

# Functions
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

# Make stacks
mainstack = MainStack()
dstacks = {i:DiscardStack(i) for i in range(1,5)}

# initialize
rules = ["shape", "color", "number"]
active_rule = random.choice(rules)
win_streak=0
filename = "../results/data.csv"
logger = []

# Game Loop
while len(mainstack)>0:
    # render current stacks
    mainstack.render()
    for stack in dstacks.values():
        stack.render()
        
    # take card from main stack
    card = mainstack.pop()
    # let user choose one of the cards
    choice = user_input()
    chosen_card=dstacks[choice].stimulus_card
    dstacks[choice].add(card)
    
    # assess correctness
    correct = card.get_card_property(active_rule)==chosen_card.get_card_property(active_rule)
    
    print(correct)
    
    # Update winstreak
    if correct:
        win_streak += 1    
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
        
#save_results(logger,filename)
      
    
    