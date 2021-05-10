animal=["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster","dog","pig"]
Year = int(input("請輸入年份"))
print(animal[(Year + 8) % 12])