N = int(input("組數為:"))
t = list()
for i in range(N):
    v = list(map(int, input(F"第 {i+1} 組:").split()))
    t.append(250 * v[0] + 175 * v[1])
for i in range(N):
    print(F"第 {i+1} 組應收費用:", t[i])