cards = [2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K", "A"]
cards_suite = ["S", "H", "D", "C"]
player_one_cards = "AH KH QH JH TH"
player_two_cards = "AS KS TS 2H 3H"
player_one_cards = "AH AS AD AC TH"
player_two_cards = "8S 8H 8D 8C 2H"

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

def royal_flush(player_cards):
    player_cards = covert_player_cards(player_cards)
    royal_flush = [10, 11, 12, 13, 14]
    rank = 0

    if flush(player_cards) == 6:
        if sorted(generate_cards_without_suits(player_cards)) == royal_flush:
            rank = 10
    
    return rank

def straight_flush(player_cards):
    rank = 0

    if flush(player_cards) == 6:
        if straight(player_cards) == 5:
            rank = 9

    return rank

def four_of_a_kind(player_cards):
    unique_cards = []
    rank = 0

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
            if generate_cards_without_suits(player_cards).count(i) == 4:
                rank = 8
                break
    
    return rank

def full_house(player_cards):
    rank = 0

    if three_of_a_kind(player_cards) == 4:
        if one_pair(player_cards) == 2:
            rank = 7
    
    return rank

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

def three_of_a_kind(player_cards):
    unique_cards = []
    rank = 0

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
            if generate_cards_without_suits(player_cards).count(i) == 3:
                rank = 4
                break
    
    return rank

def two_pairs(player_cards):
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
    
    return rank

def one_pair(player_cards):
    unique_cards = []
    rank = 0

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
                rank = 2
                break
    
    return rank

def player_rank(player_cards):
    player_rank = 0
    ranking_system = [
        royal_flush, straight_flush, 
        four_of_a_kind, full_house,
        flush, straight, three_of_a_kind,
        two_pairs, one_pair
        ]

    for i in ranking_system:
        player_rank = i(player_cards)
        if player_rank != 0:
            break
    
    if player_rank == 0:
        player_rank = 1
    
    return player_rank

def poker_hand(player_one_cards, player_two_cards):
    player_one_rank = player_rank(player_one_cards)
    player_two_rank = player_rank(player_two_cards)

    if player_one_rank == player_two_rank:
        return "Tie"
    elif player_one_rank > player_two_rank:
        return "Player One WIN"
    elif player_two_rank > player_one_rank:
        return "Player Two WIN"

print(poker_hand(player_one_cards,player_two_cards))