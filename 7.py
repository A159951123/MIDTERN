mt=input("輸入月租費型式及通話時間為:").split(",")
m=int(mt[0])
t=int(mt[1])
if m == 186:
    if t*0.09*2>m:
        print("通話費為:","%.0f"%(t*0.09*0.8))
    elif t*0.09*2<=m:
        print("通話費為:","%.0f"%(t*0.09*0.9))
elif m == 386:
    if t*0.08*2>m:
        print("通話費為:","%.0f"%(t*0.08*0.7))
    elif t*0.08*2<=m:
        print("通話費為:","%.0f"%(t*0.08*0.8))
elif m == 586:
    if t*0.07*2>m:
        print("通話費為:","%.0f"%(t*0.07*0.6))
    elif t*0.07*2<=m:
        print("通話費為:","%.0f"%(t*0.07*0.7))
elif m == 986:
    if t*0.06*2>m:
        print("通話費為:","%.0f"%(t*0.06*0.5))
    elif t*0.06*2<=m:
        print("通話費為:","%.0f"%(t*0.06*0.6))
else:
    print("月租費型式錯誤")