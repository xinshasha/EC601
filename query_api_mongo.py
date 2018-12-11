import pymongo
def most_popular_description():
	db= pymongo.MongoClient()
	database=db.mini_project_2
	connection = database.chart
	results = connection.find({"Tag":"label_pic"})
	n=0;
	for log in results:
		if len(log["pic"]) > n:
			n=len(log["pic"])
			des = []
			des.append(log['labels'])
		elif len(log["pic"]) == n:
			des.append(log['labels'])
	return [des,n]

def Pic_with_most_description():
	db= pymongo.MongoClient()
	database=db.mini_project_2
	connection = database.chart
	results = connection.find({"Tag":"pic_label"})
	n=0;
	for log in results:
		if len(log["labels"]) > n:
			n=len(log["labels"])
			des = []
			des.append(log['pic'])
		elif len(log["labels"]) == n:
			des.append(log['pic'])
	return [des,n]

def users_work_on_word(word):
	db= pymongo.MongoClient()
	database=db.mini_project_2
	connection = database.chart
	results = connection.find({"Tag":"pic_label","labels":word})
	result = []
	for user in results:
		result.append(user['pic'])
	return result
