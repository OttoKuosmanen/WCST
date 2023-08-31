
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
               
                

deck = construct_deck(number,shape,color)
deck_active = deck.copy()
random.shuffle(deck_active)

rule = ['number','shape','color']
active_rule = random.choice(rule)



def feedback(active_rule,choice):
    return getattr(stimulus_card[choice], active_rule) == getattr(a_card, active_rule)

def streak(winning_streak, win):
     if win:
         winning_streak = winning_streak +1
         print(winning_streak)
         return winning_streak
     else:
         winning_streak = 0
         print(winning_streak)
         return winning_streak


#GameLoop
while deck_active:
    a_card = deck_active.pop()
    print(f'This is the card you have in hand:{a_card.shape},{a_card.number},{a_card.color}')
    print(f'0:{stimulus_card[0].number,stimulus_card[0].shape,stimulus_card[0].color}')
    print(f'1:{stimulus_card[1].number,stimulus_card[1].shape,stimulus_card[1].color}')
    print(f'2:{stimulus_card[2].number,stimulus_card[2].shape,stimulus_card[2].color}')
    print(f'3:{stimulus_card[3].number,stimulus_card[3].shape,stimulus_card[3].color}')
    choice = int(input("Type 0,1,2,3 to choose where to group your card"))
    win = feedback(active_rule,choice)
    winning_streak = streak(winning_streak,win)



 
