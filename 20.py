data = [["123", "Tom", "DTGD"], ["456", "Cat", "CSIE"], ["789", "Nana", "ASIE"], ["321", "Lim", "DBA"], ["654", "Won", "FDD"]]
find = lambda array, i, value:sorted(array, key=lambda x: x[i] != value)[0]
print("學生資料為: " + " ".join(find(data, 0, input("輸入查詢學號為: "))))
