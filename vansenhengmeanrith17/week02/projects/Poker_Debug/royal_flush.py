player_cards = "AH KH QH JH TH"

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

def flush(player_cards):
    player_cards = covert_player_cards(player_cards)
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
    else:
        rank = 0
    
    return rank

def generate_cards_without_suits(player_cards):
    player_cards_split = str(player_cards).split(" ")
    player_cards_without_suits = []

    for i in player_cards_split:
        if len(i) != 3:
            player_cards_without_suits.append(int(i[0]))
        else:
            player_cards_without_suits.append(int(str(i[0])+str(i[1])))

    return player_cards_without_suits

player_cards = covert_player_cards(player_cards)
royal_flush = [10, 11, 12, 13, 14]
rank = 0

if flush(player_cards) == 6:
    if sorted(generate_cards_without_suits(player_cards)) == royal_flush:
        rank = 10

print(covert_player_cards(player_cards))
print(flush(player_cards))
print(rank)
print(sorted(generate_cards_without_suits(player_cards)))
print(royal_flush)

# print(rank)

# def royal_flush(player_cards):
#     player_cards_split = str(player_cards).split(" ")
#     royal_flush = ["T", "J", "Q", "K", "A"]
#     player_cards_without_suits = []
#     unique_suit = []
#     rank = None
    
#     for i in player_cards_split:
#         player_cards_without_suits.append(i[0])

#     if sorted(player_cards_without_suits) == sorted(royal_flush):
#         for i in player_cards_split:
#             if i[1] not in unique_suit:
#                 unique_suit.append(i[1])
#         if len(unique_suit) != 1:
#             rank = 0
#         else:
#             rank = 10
#     else: 
#         rank = 0

#    # return rank