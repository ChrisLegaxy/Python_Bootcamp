player_cards = "AH KH QH JH TH"

def generate_cards_without_suits(player_cards):
    player_cards_split = str(player_cards).split(" ")
    player_cards_without_suits = []

    for i in player_cards_split:
        if len(i) != 3:
            player_cards_without_suits.append(i[0])
        else:
            player_cards_without_suits.append(int(str(i[0])+str(i[1])))


    return player_cards_without_suits

print(generate_cards_without_suits(player_cards))