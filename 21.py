N = int(input("輸入查詢組數N為:"))
DATA = [['123','456','9000'],
        ['456','789','5000'],
        ['789','888','6000'],
        ['336','558','10000'],
        ['775','666','12000'],
        ['566','221','7000']]
for i in range(0,N):
    A,P=input("").split()
    if A==DATA[0][0] and P==DATA[0][1]:
        print(DATA[0][2])
    elif A==DATA[1][0] and P==DATA[1][1]:
        print(DATA[1][2])
    elif A==DATA[2][0] and P==DATA[2][1]:
        print(DATA[2][2])
    elif A==DATA[3][0] and P==DATA[3][1]:
        print(DATA[3][2])
    elif A==DATA[4][0] and P==DATA[4][1]:
        print(DATA[4][2])    
    elif A==DATA[5][0] and P==DATA[5][1]:
        print(DATA[5][2])
    else:
        print("error")