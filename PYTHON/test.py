blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
di = dict()
for t in blood_types:
    if di.get(t) == None:
        di[t] = 1
    else:
        di[t] += 1
print(di)