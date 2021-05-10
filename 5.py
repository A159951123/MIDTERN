M = int(input("請輸入階層值:"))
N = 0
A = 1
while A < M:
    N += 1
    A *= N
print("超過M為",M,"的最小階層N值為",N)
