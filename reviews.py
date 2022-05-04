#計算留言平均長度 #方法一
total_rlen = []
data = []
with open('reviews.txt','r') as reviews:
	for review in reviews:
		total_rlen.append(len(review)) #每筆留言長度加進total_rlen資料集
		data.append(review)
sum1=sum(total_rlen) #每筆留言長度加總
sum2=len(data) #計算有幾筆留言
average = sum1/sum2
print(average)

#方法二:
#total_rlen=0
#for d in data: ## d為data裡其中一個字串。
  #total_rlen = total_rlen + len(d)