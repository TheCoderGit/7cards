from enum import Enum
import random

class Card:
    def __init__(self, card_type, card_value):
        self.type = card_type
        self.value = card_value

class CardTypes(Enum):
    SPADE = '♠️'
    HEART = '❤️'
    DIAMOND = '♦️'
    FLOWER = '♣️'

class Engine:

    def __init__(self):
        pass

    full_dice = [
        Card(CardTypes.DIAMOND,1),Card(CardTypes.HEART,1),Card(CardTypes.SPADE,1),Card(CardTypes.FLOWER,1),
        Card(CardTypes.DIAMOND,2),Card(CardTypes.HEART,2),Card(CardTypes.SPADE,2),Card(CardTypes.FLOWER,2),
        Card(CardTypes.DIAMOND,3),Card(CardTypes.HEART,3),Card(CardTypes.SPADE,3),Card(CardTypes.FLOWER,3),
        Card(CardTypes.DIAMOND,4),Card(CardTypes.HEART,4),Card(CardTypes.SPADE,4),Card(CardTypes.FLOWER,4),
        Card(CardTypes.DIAMOND,5),Card(CardTypes.HEART,5),Card(CardTypes.SPADE,5),Card(CardTypes.FLOWER,5),
        Card(CardTypes.DIAMOND,6),Card(CardTypes.HEART,6),Card(CardTypes.SPADE,6),Card(CardTypes.FLOWER,6),
        Card(CardTypes.DIAMOND,7),Card(CardTypes.HEART,7),Card(CardTypes.SPADE,7),Card(CardTypes.FLOWER,7),
        Card(CardTypes.DIAMOND,8),Card(CardTypes.HEART,8),Card(CardTypes.SPADE,8),Card(CardTypes.FLOWER,8),
        Card(CardTypes.DIAMOND,9),Card(CardTypes.HEART,9),Card(CardTypes.SPADE,9),Card(CardTypes.FLOWER,9),
        Card(CardTypes.DIAMOND,10),Card(CardTypes.HEART,10),Card(CardTypes.SPADE,10),Card(CardTypes.FLOWER,10),
        Card(CardTypes.DIAMOND,11),Card(CardTypes.HEART,11),Card(CardTypes.SPADE,11),Card(CardTypes.FLOWER,11),
        Card(CardTypes.DIAMOND,12),Card(CardTypes.HEART,12),Card(CardTypes.SPADE,12),Card(CardTypes.FLOWER,12),
        Card(CardTypes.DIAMOND,13),Card(CardTypes.HEART,13),Card(CardTypes.SPADE,13),Card(CardTypes.FLOWER,13),
    ]

    trials = 0
    
    #take a copy from the original dice and start a new game, returning 21 cards ready for playing
    def start_new_game(self):
        
        dice_copy = self.full_dice.copy()
        random.shuffle(dice_copy)
        playing_cards =[]
        for x in range(21):
            playing_cards.append(dice_copy.pop())
    
        return playing_cards
    
    #shuffle the cards 
    def collect_cards(self,playing_cards: list,selected: str):
        if not len(playing_cards) == 21:
            pass
        self.trials += 1
        if selected == 'top':
            x = playing_cards[7:14]+playing_cards[:7]+playing_cards[14:]
            return x
        if selected == 'middle':
            x = playing_cards
            return x
        if selected == 'bottom':
            x = playing_cards[7:14]+playing_cards[14:]+playing_cards[:7]
            return x
    def redistripute(self,playing_cards: list):
        new_list = []
        
        for i in range(3):
            while (i < 21):
                new_list.append(playing_cards[i])
                i += 3
        return new_list

    def print_card_list(self,playing_card_list):
        for card in playing_card_list:
            print(card.value, card.type.value)

    def card_to_text(self,card:Card):
        num = card.value
        figure = card.type.value
        if num == 1:
            num = "A"
        if num == 11:
            num = "🫅🏻"
        if num == 12:
            num = "👸🏻"
        if num == 13:
            num = "🤴🏻"
        return f"{num}\n{figure}"

    def face_values(self,game_cards):
        res = []
        for card in game_cards:
            x = self.card_to_text(card)
            res.append(x)
        
            
        return dict(
        c1_1=res[0],
        c1_2=res[1],
        c1_3=res[2],
        c1_4=res[3],
        c1_5=res[4],
        c1_6=res[5],
        c1_7=res[6],
        c2_1=res[7],
        c2_2=res[8],
        c2_3=res[9],
        c2_4=res[10],
        c2_5=res[11],
        c2_6=res[12],
        c2_7=res[13],
        c3_1=res[14],
        c3_2=res[15],
        c3_3=res[16],
        c3_4=res[17],
        c3_5=res[18],
        c3_6=res[19],
        c3_7=res[20],)

    def selected_card(self,playing_cards):
        return self.card_to_text(playing_cards[10])
