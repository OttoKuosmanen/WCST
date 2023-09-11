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
        
            
class Stack():
    def __init__(self,list_of_cards,pos):
        self.list_of_cards = list_of_cards
        self.pos = pos
        
    def get(self,new_card):
        self.list_of_cards.append(new_card)
    
    def give(self):
        return self.list_of_cards.pop()
    
    def render(self):
        print(self.list_of_cards[-1].shape,self.list_of_cards[-1].number,self.list_of_cards[-1].color)
        

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
stack_1 = Stack([stimulus_card[0]], 2)
stack_2 = Stack([stimulus_card[1]], 3)
stack_3 = Stack([stimulus_card[2]], 4)
stack_4 = Stack([stimulus_card[3]], 5)
d_stack1= Stack([],6)
d_stack2= Stack([],7)
d_stack3= Stack([],8)
d_stack4= Stack([],9)



def feedback(active_rule,choice):
    return getattr(stimulus_card[choice], active_rule) == getattr(stack_hand.list_of_cards[-1], active_rule)

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
 
# Change destination of card to discard pile, when visual adding visuals.            
def place_card(choice):
    if choice == 0:
        stack_1.get(stack_hand.give())
    elif choice == 1:
        stack_2.get(stack_hand.give())
    elif choice == 2:
        stack_3.get(stack_hand.give())
    elif choice == 3:
        stack_4.get(stack_hand.give())


#GameLoop
while deck_active:
    print("----HAND----")
    stack_hand.render()
    print("##############")
    stack_1.render()
    stack_2.render()
    stack_3.render()
    stack_4.render()
    choice = user_input()
    win = feedback(active_rule,choice)
    place_card(choice)
    update_streak(win)
    change_rule()
    print("____________________________________________________________________")

print("Game Over")


 
