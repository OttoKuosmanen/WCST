import random


number = [1,2,3,4]
shape = ["circle","square","triangle","star"]
color = ["blue","green","red","yellow"]
winning_streak = 0


class Card:
    def __init__(self,number,shape,color):
        self.number = number
        self.shape = shape
        self.color = color
        
    def render(self):
        print(self.shape,self.number,self.color)
            
class Stack(Card):
    def __init__(self,list_of_cards,pos):
        self.list_of_cards = list_of_cards
        self.pos = pos
        
    def get(self,new_card):
        self.list_of_cards.append(new_card)
    
    def give(self):
        return self.list_of_cards.pop()
        

def construct_deck(number,shape,color):
    deck = []
    for i in number:
        for y in shape:
            for x in color:
                card = Card(i,y,x)
                deck.append(card)
    return deck
 

stimulus_card = [
    Card(1, "triangle", "red"),
    Card(2, "star", "green"),
    Card(3, "square", "yellow"),
    Card(4, "circle", "blue")
]
               
                
# Deck
deck = construct_deck(number,shape,color)
deck_active = deck.copy()
random.shuffle(deck_active)

#Rules
rule = ['number','shape','color']
active_rule = random.choice(rule)

#Make stacks

stack_hand = Stack(deck_active,1)
stack_1 = Stack(stimulus_card[0],2)
stack_2 = Stack(stimulus_card[1],3)
stack_3 = Stack(stimulus_card[2],4)
stack_4 = Stack(stimulus_card[3],5)
d_stack1= Stack([],6)
d_stack2= Stack([],6)
d_stack3= Stack([],6)
d_stack4= Stack([],6)



def feedback(active_rule,choice):
    return getattr(stimulus_card[choice], active_rule) == getattr(a_card, active_rule)

def update_streak(win):
    global winning_streak
    if win:
         winning_streak += 1
         print(f"Streak:{winning_streak}\n")
         return winning_streak
    else:
         winning_streak = 0
         print(f"Streak:{winning_streak}\n")
         return winning_streak

def change_rule():
    global winning_streak
    global active_rule
    new_rule = []
    if winning_streak >= 5:
        new_rule = random.choice(rule)
        while new_rule == active_rule:
            new_rule = random.choice(rule)
        active_rule = new_rule
        winning_streak = 0
        print(active_rule)

def user_input():
    while True:
        try:
            c = int(input("Type 1, 2, 3, or 4 to choose where to group your card: "))
            if c in [1, 2, 3, 4]:
                return c - 1
            else:
                print("Please enter a valid choice (1, 2, 3, or 4).")
        except ValueError:
            print("Please enter a valid choice (1, 2, 3, or 4).")


#GameLoop
while deck_active:
    a_card = stack_hand.give()
    print("----HAND----")
    a_card.render()
    print("##############")
    stimulus_card[0].render()
    stimulus_card[1].render()
    stimulus_card[2].render()
    stimulus_card[3].render()
    
    choice = user_input()
    win = feedback(active_rule,choice)
    update_streak(win)
    change_rule()
    print("____________________________________________________________________")



 
