with open("q", 'r') as file:
    data = file.readlines()
    file.close()

print(data)

colors  = ['red', 'green', 'blue']
new_q = [i.split(':')[1] for i in data ]

for i in range(len(new_q)):
    new_q[i] = new_q[i].replace("\n", "")
# print(new_q)

new_q = [i.split(";") for i in new_q]
print(new_q)

power_list = []
for i in new_q:
    color_dict = {'red':1, 'green':1, 'blue':1}
    for j in i:
        elm = j[1:]
        elm = elm.split(',')
        for k in elm:
            text = k
            for clr in color_dict:
                if clr in text:
                    num = '0'
                    for dig in text:
                        if dig.isnumeric():
                            num+=dig
                    # print(num)
                    if int(num) >= color_dict[clr]:
                        color_dict[clr] = int(num)
    print(color_dict)
    power = 1
    for ii in color_dict:
        power *= color_dict[ii]
    power_list.append(power)
print(power_list)
print(sum(power_list))

        