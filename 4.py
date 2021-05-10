X = float(input("X軸座標:"))
Y = float(input("Y軸座標:"))
U = (X**2+Y**2)
if X > 0:
    if Y > 0:
        print("該點位於第一象限,離原點距離為根號"+'%.0f'%U)
    elif Y < 0:
        print("該點位於第四象限,離原點距離為根號"+'%.0f'%U)
    else:
        print("該點位於右半平面X軸上,離原點距離為根號"+'%.0f'%U)
if X < 0:
    if Y > 0:
        print("該點位於第二象限,離原點距離為根號"+'%.0f'%U)
    elif Y < 0:
        print("該點位於第三象限,離原點距離為根號"+'%.0f'%U)
    else:
        print("該點位於左半平面X軸上,離原點距離為根號"+'%.0f'%U)
else:
    if Y > 0:
        print("該點位於上半平面Y軸上,離原點距離為根號"+'%.0f'%U)
    elif Y < 0:
        print("該點位於下半平面Y軸上,離原點距離為根號"+'%.0f'%U)
    else:
        print("該點位於原點")