s1 = input("輸入一整數序列為: ").split()
set1 = set(s1)
if len(set1) > (len(s1)+1)//2:
    print("過半元素為:NO")
else:
    while len(s1) > 1:
        for i in list(set(s1)):
            s1.remove(i)
    print("過半元素為:",s1[0])