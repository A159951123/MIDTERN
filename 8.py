N = int(input("輸入第一行正整數為:"))
V = input("第二行中數列中的數字為:").split()
if len(set(V)) == N:
    print("每個數字剛好只出現1次")
else:
    i = 1
    while True:
        for J in list(set(V)):V.remove(J)
        i += 1
        if len(V) == 1:
            print("最大出現次數的數字為:",V[0])
            print("出現次數為:",str(i))
            break
        