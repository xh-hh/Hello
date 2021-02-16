lst = list()
for i in range(10):
    temp = [1]
    for j in range(1,i):
        data = lst[i-1][j-1]+lst[i-1][j]
        temp.append(data)
    if i != 0:
        temp.append(1)
    # print(temp)
    lst.append(temp)

for i in lst:
    print(i)