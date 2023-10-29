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
            return playing_cards[7:15]+playing_cards[:7]+playing_cards[15:]
        if selected == 'middle':
            return playing_cards
        if selected == 'bottom':
            return playing_cards[7:15]+playing_cards[15:]+playing_cards[:7]

    def redistripute(self,playing_cards: list):
        new_list = []
        
        for i in range(3):
            while (i < 21):
                print(i)
                new_list.append(playing_cards[i])
                i += 3
        print('new list ==> ', len(new_list))
        return new_list

    def print_card_list(self,playing_card_list):
        for card in playing_card_list:
            print(card.value, card.type.value)

    def face_values(self,game_cards):
        return dict(
        c1_1=f"{game_cards[0].value}\n{game_cards[0].type.value}",
        c1_2=f"{game_cards[1].value}\n{game_cards[1].type.value}",
        c1_3=f"{game_cards[2].value}\n{game_cards[2].type.value}",
        c1_4=f"{game_cards[3].value}\n{game_cards[3].type.value}",
        c1_5=f"{game_cards[4].value}\n{game_cards[4].type.value}",
        c1_6=f"{game_cards[5].value}\n{game_cards[5].type.value}",
        c1_7=f"{game_cards[6].value}\n{game_cards[6].type.value}",
        c2_1=f"{game_cards[7].value}\n{game_cards[7].type.value}",
        c2_2=f"{game_cards[8].value}\n{game_cards[8].type.value}",
        c2_3=f"{game_cards[9].value}\n{game_cards[9].type.value}",
        c2_4=f"{game_cards[10].value}\n{game_cards[10].type.value}",
        c2_5=f"{game_cards[11].value}\n{game_cards[11].type.value}",
        c2_6=f"{game_cards[12].value}\n{game_cards[12].type.value}",
        c2_7=f"{game_cards[13].value}\n{game_cards[13].type.value}",
        c3_1=f"{game_cards[14].value}\n{game_cards[14].type.value}",
        c3_2=f"{game_cards[15].value}\n{game_cards[15].type.value}",
        c3_3=f"{game_cards[16].value}\n{game_cards[16].type.value}",
        c3_4=f"{game_cards[17].value}\n{game_cards[17].type.value}",
        c3_5=f"{game_cards[18].value}\n{game_cards[18].type.value}",
        c3_6=f"{game_cards[19].value}\n{game_cards[19].type.value}",
        c3_7=f"{game_cards[20].value}\n{game_cards[20].type.value}",)

    def selected_card(self,playing_cards):
        return playing_cards[11]
