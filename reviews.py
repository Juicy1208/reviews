#計算留言平均長度
total_rlen = []
data = []
with open('reviews.txt','r') as reviews:
	for review in reviews:
		total_rlen.append(len(review))
		data.append(review)
sum1=sum(total_rlen)
sum2=len(data)
average = sum1/sum2
print(average)