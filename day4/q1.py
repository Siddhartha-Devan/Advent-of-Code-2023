with open("q", 'r') as file:
    data = file.readlines()
    file.close()

for i in range(len(data)):
    data[i] = data[i].replace('\n', "")

print(len(data))

for i in range(len(data)):
    data[i] = data[i][9:]

data_new = [i.split('|') for i in data]
print(data_new[:10])

# data_new = data_new[:10]
win_nums = []
list_nums = []
for i in range(len(data_new)):
    print(data_new[i])
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

print(win_nums)
print(list_nums)
total = 0
for wins,lists in zip(win_nums, list_nums):
    n_matches = -1
    for i in lists:
        if i in wins:
            n_matches+=1
    # print(n_matches)
    if n_matches >=0:
        total+= 2**n_matches

print(total)
