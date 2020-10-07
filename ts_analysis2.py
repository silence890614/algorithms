year = list()
for i in range(2000,2041):
    a = i%4
    if a == 0:
        a = i%100
        if a == 0:
            a = i%400
            if a == 0:
                year.append(int(i))
b = input("輸入2000到2040其中一年:")
b = int(b)
if b in year:
    print("1")
if b not in year:
    print("0")
