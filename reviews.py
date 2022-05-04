#寫法一:
# with open('reviews.txt','r') as reviews:
	# for review in reviews:
		# print(review.strip())

#寫法二:
data = []
with open('reviews.txt','r') as reviews:
	for review in reviews:
		data.append(review.strip())
print(len(data)) #印出留言有幾筆 
print(data[0]) #印出第一筆資料
print(data[1]) #印出第二筆資料