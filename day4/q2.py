with open("q", 'r') as file:
    data = file.readlines()
    file.close()

for i in range(len(data)):
    data[i] = data[i].replace('\n', "")

print(len(data))

for i in range(len(data)):
    data[i] = data[i][9:]

data_new = [i.split('|') for i in data]

win_nums = []
list_nums = []
cards = []
for i in range(len(data_new)):
    # print(data_new[i])
    wins = data_new[i][0]
    lists = data_new[i][1]

    wins = wins.split(" ")
    lists = lists.split(" ")

    win_n = []
    for i in wins:
        try:
            win_n.append(int(i))
        except:
            pass

    list_n = []
    for i in lists:
        try:
            list_n.append(int(i))
        except:
            pass

    win_nums.append(win_n)
    list_nums.append(list_n)
    cards.append([win_n, list_n])
# print(win_nums)
# print(list_nums)


winnings = []
for wins,lists in zip(win_nums, list_nums):
    n_matches = 0
    for i in lists:
        if i in wins:
            n_matches+=1
    # print(n_matches)
    winnings.append(n_matches)


print(winnings)

print(len(cards))
cards_doup = [i for i in cards]
# print(cards_doup)

for i in cards:
    print(i)

win_tup = [(i,j) for i,j in zip(range(1, len(winnings)+1), winnings)]
print(win_tup)


# total_cards = 6

# def card_finder (win_tup, ind = 0):
#     global total_cards; 
#     if win_tup[ind][1] == 0:
#         return 0
#     else:
#         try:
#             print("hi")
#             total_cards+=win_tup[ind][1]

#             return card_finder(win_tup, ind+1)
#         except:
#             return 0
        
# print(card_finder(win_tup))
# print(total_cards)

total_cards = 6

def card_counter(win_tup, ind):
    if win_tup[ind][1] == 0:
        return 0
    else:
        # print(win_tup[ind][1] + card_counter(win_tup, ind+1))
        return win_tup[ind][1] + card_counter(win_tup, ind+1)

print(card_counter(win_tup, 0))
sum = 0
for i in range(len(win_tup)):
    print(card_counter(win_tup, i))
    sum += card_counter(win_tup, i)

print(sum)