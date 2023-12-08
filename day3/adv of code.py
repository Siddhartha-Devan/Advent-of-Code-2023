# st = '...355456..'

# def num_collector(st, ind):
#     num_in = '0'
#     if ind>0 and st[ind-1].isnumeric() and st[ind].isnumeric():
        
#         i = ind-1
#         while i >= 0:
#             if st[i].isnumeric()==False:
#                 break
#             i-=1
#         num_in += st[i+1:ind]
#         # print("num_in = ", num_in)
#         num_in = int(num_in)
#         num_in = str(num_in)
    
#     num = '0'

#     for i in range(ind, len(st)):
#         if st[i].isnumeric()==False:
#             # print("nope")
#             break
#         num+=st[i]
        
    
#     if int(num == '0'):
#         for i in range(ind+1, len(st)):
#             if st[i].isnumeric()==False:
#                 # print("nope")
#                 break
#             num+=st[i]
        
#     return int(num_in+str(int(num)))

# print(num_collector(st, 1))

# st = '..234...'

# def num_collector_rev(st, ind):
#     num = '0'
#     if st[ind-1].isnumeric() == True and st[ind].isnumeric() == False:
#         for i in range(ind-1, -1,-1):
#             if st[i].isnumeric() == False:
#                 break
#             num += st[i]
#     num = str(int(num))
#     return int(num[::-1])

# print(num_collector_rev(st, 6))

with open("q", 'r') as file:
    data = file.readlines()
    file.close()

for i in range(len(data)):
    data[i] = data[i].replace('\n', "")
# print(data)
length = len(data[0])

print(data[:4])

datu = data[0]

# act = 0
# symbol_indices = []
# for i in range(0, len(data)):
#     elm = data[i]
#     symb_ind = []
#     for j in range(len(elm)):
#         if elm[j].isnumeric() == False and elm[j] != '.':
#             act+=1
#             symb_ind.append(j)
#     print(symb_ind)
#     symbol_indices.append(symb_ind)

# sum = 0
# for i in symbol_indices:
#     sum+=len(i)

# def num_printer(data):
#     ind=0
#     num_list = []
#     while ind< len(data):
        
#         for i in range(ind, len(data)):
#             if data[i].isnumeric():
                

# def num_checker(digit, ind, max_ind):
#     number = ''
#     while ind<=max_ind:
#         if digit[i].isnumeric():
#             number += digit
#             ind+=1
#         else:
#             break
#     return number, ind
    

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
            number_list.append(numb)
            # print(indx, "  ", numb)
            i = indx 
        else:
            i+=1   
print(number_list)

