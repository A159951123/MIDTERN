N=int(input("測試的資料量:"))
for i in range(0,N):
    f,m,c=input("父、母、子的血型:").split()
    if f=='O' or m=='O':
        if (m == 'A' or f =='A') and (c=='A' or c=='O'):
            print("YES")
        elif (m =='B' or f=='B') and (c=='B' or c=='O'):
            print("YES")
        elif (m =='O' or f =='O') and c=='O':
            print("YES")
        else:
             print("IMPOSSIBLE")
    elif f =='A' or m =='A':
       if (m == 'A' or f == 'A') and (c=='A' or c=='O'):
           print("YES")
       elif (m == 'B' or f == 'B') and (c=='A' or c=='B' or c=='O' or c=='AB'):
           print("YES")
       else:
           print("IMPOSSIBLE")
    elif f == 'B' or m =='B':
        if (m=='B' or f=='B') and (c=='B' or c=='O'):
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif f == 'AB':
        if(m=='AB') and (c=='O'):
            print("IMPOSSIBLE")
        elif (m == 'A' )and (c=='O'):
            print("IMPOSSIBLE")
        elif (m=='B') and(c=='O'):
            print("IMPOSSIBLE")
        elif m=='O' and (c=='O'or c=='AB'):
            print("IMPOSSIBLE")
        else:
            print("YES")
    elif m == 'AB':
        if(f=='AB') and (c=='O'):
            print("IMPOSSIBLE")
        elif (f=='A')and (c=='O'):
            print("IMPOSSIBLE")
        elif (f=='B') and(c=='O'):
            print("IMPOSSIBLE")
        elif f=='O' and (c=='O'or c=='AB'):
            print("IMPOSSIBLE")
        else:
            print("YES")
    