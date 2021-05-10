s1 = list(input("請輸入一組四位數字為:"))
for i in range(4):s1[i]=str((int(s1[i])+7)%10)
s1[0],s1[2] = s1[2],s1[0]
s1[1],s1[3] = s1[3],s1[1]
print("".join(s1))
