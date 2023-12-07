with open("q", 'r') as file:
    data = file.readlines()
    file.close()

for i in range(len(data)):
    data[i] = data[i].replace('\n', "")
print(data)
length = len(data[0])

symbol_indices = []
for i in range(0, len(data)):
    elm = data[i]
    symb_ind = []
    for j in range(len(elm)):
        if elm[j].isalnum() == False and elm[j] != '.':
            symb_ind.append(j)
    print(symb_ind)
    symbol_indices.append(symb_ind)

def num_collector(st, ind):
    num_in = '0'
    if ind>0 and st[ind-1].isnumeric() and st[ind].isnumeric():
        
        i = ind-1
        while i >= 0:
            if st[i].isnumeric()==False:
                break
            i-=1
        num_in += st[i+1:ind]
        # print("num_in = ", num_in)
        num_in = int(num_in)
        num_in = str(num_in)
    
    num = '0'

    for i in range(ind, len(st)):
        if st[i].isnumeric()==False:
            # print("nope")
            break
        num+=st[i]
        
    
    if int(num == '0'):
        for i in range(ind+1, len(st)):
            if st[i].isnumeric()==False:
                # print("nope")
                break
            num+=st[i]
        
    return int(num_in+str(int(num)))

def num_collector_rev(st, ind):
    num = '0'
    if st[ind-1].isnumeric() == True and st[ind].isnumeric() == False:
        for i in range(ind-1, -1,-1):
            if st[i].isnumeric() == False:
                break
            num += st[i]
    num = str(int(num))
    return int(num[::-1])

print(symbol_indices)

parts_list = []

for i in range(1, len(symbol_indices)-1):
    symbols = symbol_indices[i]
    ith_line = data[i]
    i_prev_line = data[i-1]
    i_next_line = data[i+1]

    # print(ith_line)
    # print(i_next_line)
    # print(i_prev_line)
    for j in symbols:
        
        parts_list.append(num_collector(ith_line, j))
        parts_list.append(num_collector(i_prev_line, j))
        parts_list.append(num_collector(i_next_line, j))

        parts_list.append(num_collector_rev(ith_line, j))
        parts_list.append(num_collector_rev(i_prev_line, j))
        parts_list.append(num_collector_rev(i_next_line, j))

# print(parts_list)
print(sum(parts_list))     




 