with open("q", 'r') as file:
    data = file.readlines()
    file.close()

# print(data)
# print((type(data)))
# print(len(data))
new_list = []

for i in data:
    elm = i.split(":")
    # print(elm)
    elm[1] = elm[1].replace("\n", "")
    ind_grps = elm[1].split(';')
    # print(ind_grps)
    for j in range(len(ind_grps)):
        ind_grps[j] = ind_grps[j].split(",")
    new_list.append([elm[0], ind_grps])


given = {'red': 12, 'green' :13, 'blue': 14}
ans = []
for i in new_list:
    for j in i[1]:
        for k in j:
            txt = k
            txt = txt.replace(" ", "")
            for color in given:
                if color in txt:
                    num = ""
                    for dig in txt:
                        if dig.isnumeric():
                            num+=dig
                    if int(num)>given[color]:
                        ans.append(i[0])
                        break
# print(ans)
ans = set(ans)

ans = list(ans)
# print(ans)
sum_ans = []
for i in range(len(ans)):
    elm = ans[i]
    num = ''
    for j in elm:
        if j.isnumeric():
            num+=j
    sum_ans.append(int(num))

# print(sum_ans)
# print(sum(sum_ans))
sum_ = 0
for i in range(1, 101):
    if i not in sum_ans:
        sum_+=i
print(sum_)


        

