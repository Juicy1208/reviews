#因逐筆print很慢，所以改成只print每次地1000筆
data = []
count = 0
with open('reviews.txt','r') as reviews:
	for review in reviews:
		data.append(review.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))