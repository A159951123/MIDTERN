du = int(input("請輸入電費"))
summer=0
nosummer=0
if du >700:
    temp = du-700
    du=700
    summer += temp *5.63
    nosummer += temp*4.5
if du >500:
    temp = du-500
    du=500
    summer += temp *4.97
    nosummer += temp*4.01
if du >330:
    temp = du-330
    du=330
    summer += temp *4.39
    nosummer += temp*3.61
if du >120:
    temp = du-120
    du=120
    summer += temp *3.02
    nosummer += temp*2.68
if du >0:
    temp = du-0
    du=0
    summer += temp *2.10
    nosummer += temp*2.10
print("Summer months:",'%.2f'%summer)
print("No Summer months",'%.2f'%nosummer)