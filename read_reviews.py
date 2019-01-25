data = []
count = 0
with open('reviews.txt', 'r')as f:	
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 10000 == 0:#讀取進度
			print(len(data))

print(len(data))#文章筆數
print(data[0])
print(data[1])