import GetAnnotation
import tweetAPI

def Assign1(tweet,tweet_path,in_path,ou_path,ou_file):
	tweetAPI.get_all_tweets(tweet,tweet_path)
	GetAnnotation.GET_Video(in_path,ou_path,ou_file)

if __name__ == '__main__':
	Assign1("@CHANEL",'./imgs/','./imgs/','./label_images/','Chanel.mp4')