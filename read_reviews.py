data = []
count = 0
with open('reviews.txt', 'r')as f:	
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 10000 == 0:#讀取進度
			print(len(data))
print('總共有', len(data),  '筆資料!')#文章筆數
sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print(len(new))
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print(len(good))
print(good[0])

