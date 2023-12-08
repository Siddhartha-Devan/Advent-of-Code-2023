a = '....690*....'
b = '....0*....'

def num_collector_rev(st, ind):
    num = ''
    if st[ind-1].isnumeric() == True and st[ind].isnumeric() == False:
        print(True)
        for i in range(ind-1, -1,-1):
            if st[i].isnumeric() == False:
                break
            num += st[i]
    try:
        returner = int(num[::-1])
        return returner
    except ValueError:
        return 0
print(num_collector_rev(b,5))

def num_collector(st, ind):
    num_in = '0'
    if ind>0 and st[ind-1].isnumeric() and st[ind].isnumeric():
        i = ind-1
        while i >= 0:
            if st[i].isnumeric()==False:
                break
            i-=1
        num_in += st[i+1:ind]
        print(num_in)
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

print(num_collector(b, 7))
