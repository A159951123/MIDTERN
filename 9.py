s1 = input("輸入 s1 為:")
s2 = input("輸入 s2 為:")
if len(s2.replace(s1,""))!=len(s2):
    print("YES")
else:
    print("NO")