A = input("輸入值為:").split(",")
B = int("".join(sorted(A)))
C = int("".join(sorted(A,reverse=True)))
print("最大值數列與最小值數列差值為:",str(C-B))