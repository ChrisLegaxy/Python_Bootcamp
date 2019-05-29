# # player_cards = "AH KH QH JH TH"

# # player_cards_split = str(player_cards).split(" ")
# # royal_flush = ["T", "J", "Q", "K", "A"]


# # player_cards_without_suits = []
# # cards_suite = ["S", "H", "D", "C"]
# # unique_suit = []
# # rank = 0

# # for i in player_cards_split:
# #     player_cards_without_suits.append(i[0])

# # if sorted(player_cards) == sorted(royal_flush):
# #     for i in player_cards_split:
# #         if i[1] not in unique_suit:
# #             unique_suit.append(i)
# #     if len(unique_suit) != 1:
# #         rank = 0
# #     else:
# #         rank = 10

# # print(unique_suit)
# # print(rank) 




# # print(player_cards_without_suits)
# # print(sorted(royal_flush))
# # print(player_cards)
# # print(player_cards_split)
# # player_cards = "AH KH QH JH TH"

# # start = 0
# # stop = 5
# # straight = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# # list_of_straght = [
# #     straight[0:5], straight[1:6], straight[2:7], 
# #     straight[3:8], straight[4:9], straight[5:10], 
# #     straight[6:11], straight[7:12], straight[8:13]
# #     ]
# # straight_check = []
# # player_cards_split = str(player_cards).split(" ")
# # player_cards_without_suits = []
# # unique_suit = []
# # rank = 0

# # print(list_of_straght)

# # for i in player_cards_split:
# #     if i[1] not in unique_suit:
# #         unique_suit.append(i[1])

# # if len(unique_suit) != 1:
# #     rank = 0

# # for i in player_cards_split:
# #     player_cards_without_suits.append(i[0])
# # # Convert Cards From T J K Q A to Numerical Values
# # for i in range(len(player_cards_without_suits)):
# #     if str(player_cards_without_suits[i]) == "T":
# #         player_cards_without_suits[i] = 10
# #     elif str(player_cards_without_suits[i]) == "J":
# #         player_cards_without_suits[i] = 11
# #     elif str(player_cards_without_suits[i]) == "Q":
# #         player_cards_without_suits[i] = 12
# #     elif str(player_cards_without_suits[i]) == "K":
# #         player_cards_without_suits[i] = 13
# #     elif str(player_cards_without_suits[i]) == "A":
# #         player_cards_without_suits[i] = 14
# #     else: 
# #         player_cards_without_suits[i] = int(player_cards_without_suits[i])

# # for i in range(len(straight)):
# #     straight_check = straight[start:stop]
# #     if sorted(player_cards_without_suits) == straight_check:
# #         rank = 10
# #         break
# #     start += 1
# #     stop += 1

# # def convert_cards(player_cards):


# print(player_cards)
# print(players_cards_coverted)
# print(player_cards_suits_only)
# print(player_cards_without_suits)

        