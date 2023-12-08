with open("q", 'r') as file:
    data = file.readlines()
    file.close()

for i in range(len(data)):
    data[i] = data[i].replace('\n', "")
# print(data)
length = len(data[0])
print("len =", length)
symbol_indices = []
for i in range(0, len(data)):
    elm = data[i]
    symb_ind = []
    for j in range(len(elm)):
        if elm[j].isnumeric() == False and elm[j] != '.':
            symb_ind.append(j)
    # print(symb_ind)
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
        print(True)
        for i in range(ind-1, -1,-1):
            if st[i].isnumeric() == False:
                break
            num += st[i]
    try:
        return int(num[::-1])
    except:
        return 0
# print(symbol_indices)

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


def num_checker(data, ind, number = ''):
    if ind <len(data):
        if data[ind].isnumeric():
            return num_checker(data, ind+1, number+data[ind])
        else:
            return number, ind+1
    else:
        return number, ind+1
# print(datu[25])


number_list = []
for line in range(len(data)):
    i=0
    lin = data[line]
    while i < len(lin):
        if lin[i].isnumeric():
            numb, indx = num_checker(lin, i)
            # print(indx, "  ", numb)
            number_list.append(int(numb))
            # print(indx, "  ", numb)
            i = indx 
        else:
            i+=1   
# print(number_list)

parts_list = [i for i in parts_list if i != 0]
print(len(parts_list))
print(len(number_list))

# parts_list.remove(0)

unseen_list = []
for i in number_list:
    if i not in parts_list:
        unseen_list.append(i)
        # print(i)
print((unseen_list))
















# for i in symbol_indices:
#     try:
#         if min(i) <10:
#             print(min(i))
#     except:
#         pass


 