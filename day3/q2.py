with open("q", 'r') as file:
    data = file.readlines()
    file.close()

for i in range(len(data)):
    data[i] = data[i].replace('\n', "")
# print(data)
length = len(data[0])
print("len =", length)

star_indices = []
for i in range(0, len(data)):
    elm = data[i]
    star_ind = []
    for j in range(len(elm)):
        if elm[j].isnumeric() == False and elm[j] != '.' and elm[j] == '*':
            star_ind.append(j)
    # print(symb_ind)
    star_indices.append(star_ind)

print(star_indices)

def num_collector(st, ind):
    num_in = '0'
    if ind>0 and st[ind-1].isnumeric() and st[ind].isnumeric():
        i = ind-1
        while i >= 0:
            if st[i].isnumeric()==False:
                break
            i-=1
        num_in += st[i+1:ind]
        # print(num_in)
        # print("num_in = ", num_in)
        num_in = int(num_in)
        num_in = str(num_in)
    
    num = ''

    for i in range(ind, len(st)):
        if st[i].isnumeric()==False:
            # print("nope")
            break
        num+=st[i]
        
    
    if int(num == ''):
        for i in range(ind+1, len(st)):
            if st[i].isnumeric()==False:
                # print("nope")
                break
            num+=st[i]
        
    return int(num_in+num)

def num_collector_rev(st, ind):
    num = ''
    if st[ind-1].isnumeric() == True and st[ind].isnumeric() == False:
        # print(True)
        for i in range(ind-1, -1,-1):
            if st[i].isnumeric() == False:
                break
            num += st[i]
    try:
        return int(num[::-1])
    except:
        return 0
# print(symbol_indices)

new_parts_list = []

for i in range(1, len(star_indices)-1):
    symbols = star_indices[i]
    ith_line = data[i]
    i_prev_line = data[i-1]
    i_next_line = data[i+1]

    # print(ith_line)
    # print(i_next_line)
    # print(i_prev_line)
    for j in symbols:
        adj_list = []
        adj_list.append(num_collector(ith_line, j))
        adj_list.append(num_collector(i_prev_line, j))
        adj_list.append(num_collector(i_next_line, j))

        adj_list.append(num_collector_rev(ith_line, j))
        adj_list.append(num_collector_rev(i_prev_line, j))
        adj_list.append(num_collector_rev(i_next_line, j))

        adj_list = [i for i in adj_list if i>0]
        if len(adj_list) == 2:
            new_parts_list.append(adj_list[0]*adj_list[1])



print(sum(new_parts_list))


