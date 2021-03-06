player_cards = "AH KH QH JH TH"
player_cards = "2H 3H 4H 5H 6H"
rank = 0

def covert_player_cards(player_cards):
    player_cards_split = str(player_cards).split(" ")
    player_cards_without_suits = []
    player_cards_suits_only = []
    players_cards_coverted = ""

    for i in player_cards_split:
        player_cards_without_suits.append(i[0])

    for i in player_cards_split:
        player_cards_suits_only.append(i[1])
    # Convert Cards From T J K Q A to Numerical Values
    for i in range(len(player_cards_without_suits)):
        if str(player_cards_without_suits[i]) == "T":
            player_cards_without_suits[i] = 10
        elif str(player_cards_without_suits[i]) == "J":
            player_cards_without_suits[i] = 11
        elif str(player_cards_without_suits[i]) == "Q":
            player_cards_without_suits[i] = 12
        elif str(player_cards_without_suits[i]) == "K":
            player_cards_without_suits[i] = 13
        elif str(player_cards_without_suits[i]) == "A":
            player_cards_without_suits[i] = 14
        else: 
            player_cards_without_suits[i] = int(player_cards_without_suits[i])

    for i in range(len(player_cards_without_suits)):
        if i == len(player_cards_split)-1:
            players_cards_coverted += str(player_cards_without_suits[i])+str(player_cards_suits_only[i])
        else:
            players_cards_coverted += str(player_cards_without_suits[i])+str(player_cards_suits_only[i])+" "

    return players_cards_coverted

def generate_cards_without_suits(player_cards):
    player_cards_split = str(player_cards).split(" ")
    player_cards_without_suits = []

    for i in player_cards_split:
        if len(i) != 3:
            player_cards_without_suits.append(int(i[0]))
        else:
            player_cards_without_suits.append(int(str(i[0])+str(i[1])))


    return player_cards_without_suits

def flush(player_cards):
    # player_cards = covert_player_cards(player_cards)
    player_cards_split = str(player_cards).split(" ")
    unique_suit = []
    rank = 0

    for i in player_cards_split:
        if len(i) == 3:
            if i[2] not in unique_suit:
                unique_suit.append(i[2])
        elif i[1] not in unique_suit:
            unique_suit.append(i[1])
    
    if len(unique_suit) == 1:
        rank = 6
    
    return rank

def straight(player_cards):
    straight = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    straight_check = []
    start = 0
    stop = 5
    rank = 0

    player_cards = covert_player_cards(player_cards)
    
    for i in range(len(straight)):
        start = i 
        straight_check = straight[start:stop]
        if sorted(generate_cards_without_suits(player_cards)) == straight_check:
            rank = 5
            break
        stop += 1
    
    return rank

if flush(player_cards) == 6:
    if straight(player_cards) == 5:
        rank = 9

print(rank)


