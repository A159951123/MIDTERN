N,M=list(map(int,input("輸入 N 及 M 值為: ").split()))
arr = list()
for i in range(N):
    arr.append(input(f"輸入矩陣數值第 {i+1} 列為").split())
for i in range(M):
    print(F"輸出矩陣數值為第 {i+1} 列為:{arr[0][i]} {arr[1][i]}") 