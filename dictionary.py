data = []
count = 0
with open('reviews.txt', 'r')as f:	
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 100000 == 0:#讀取進度
			print(len(data))
print('總共有', len(data),  '筆資料!')#文章筆數


#word_count單字計次
wc = {} 
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

#用for印出字典
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

while True:
	word = input('請輸入欲查尋單字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現次數', wc[word])
	else:
		print('這單字沒出現過喔')
print('感謝使用本功能')