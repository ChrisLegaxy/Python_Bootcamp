player_cards = "AH KH QH JH TH"
player_cards = "TS TH 4H 4S 3H"

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

unique_cards = []
rank = 0
count_pairs = 0

player_cards = covert_player_cards(player_cards)
split_cards = player_cards.split(" ")
unique_cards_without_suits = []

for i in split_cards:
    if i not in unique_cards:
        unique_cards.append(i)

for i in generate_cards_without_suits(player_cards):
    if i not in unique_cards_without_suits:
        unique_cards_without_suits.append(i)

if len(unique_cards) == 5:
    for i in unique_cards_without_suits:
        if generate_cards_without_suits(player_cards).count(i) == 2:
            count_pairs += 1
    if count_pairs == 2:
        rank = 3

print(rank)