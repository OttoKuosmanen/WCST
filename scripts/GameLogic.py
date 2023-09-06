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
        

#GameLoop
while deck_active:
    a_card = deck_active.pop()
    print(f'This is the card you have in hand:{a_card.shape},{a_card.number},{a_card.color}')
    print(f'0:{stimulus_card[0].number,stimulus_card[0].shape,stimulus_card[0].color}')
    print(f'1:{stimulus_card[1].number,stimulus_card[1].shape,stimulus_card[1].color}')
    print(f'2:{stimulus_card[2].number,stimulus_card[2].shape,stimulus_card[2].color}')
    print(f'3:{stimulus_card[3].number,stimulus_card[3].shape,stimulus_card[3].color}')
    choice = int(input("Type 0,1,2,3 to choose where to group your card: "))
    win = feedback(active_rule,choice)
    update_streak(win)
    change_rule()
    print("____________________________________________________________________________________")



 
