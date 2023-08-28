# Creating card variables
number = [1,2,3,4]
shape = ["circle","square","triange","star"]
color = ["blue","green","red","yellow"]


# Setting class and function
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
                
 
# Running sequence
deck = construct_deck(number,shape,color)



# Visualization
for card in deck:
    print(card.number,card.shape,card.color)
