lis = [2, 4, 1, 0, 2, -1]
min_lis = []
max_lis = []


for i in lis:
    if len(min_lis) > 0:
        if i > min_lis[0]:
            min_lis[0] = i
    else:
        min_lis.append(i)