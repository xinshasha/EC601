import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image,ImageDraw,ImageFont
import _mysql
import pymongo

def table(db,table_name,n):
	db.query("""DROP TABLE IF EXISTS """+table_name)
	cmd="""CREATE TABLE """
	cmd+=table_name
	cmd+=" ("
	cmd+="NAME CHAR(20)"
	for i in range(n):
		cmd+=",ATR"+str(i)+" CHAR(20)"
	cmd+=",NUM INT"
	cmd+=")"
	db.query(cmd)


def GET_Video(input_path,output_path,out_file,dbway):
	files= os.listdir(input_path)
	print(files)
	files.sort()
	print()
	print(files)
	if dbway == 'mysql':
		db=_mysql.connect(host=server,user=user_name,passwd=password,db=database)
		pic_label={}
		label_pic={}
	else:
		db= pymongo.MongoClient()
		database=db.mini_project_2
		connection = database.chart
		connection.drop()
		pic_label={}
		label_pic={}


	for i in files:
		pic_label[i]=[]
		# Instantiates a client
		client = vision.ImageAnnotatorClient()

		# The name of the image file to annotate
		file_name = os.path.join(
		    os.path.dirname(__file__),
		    input_path+i)
		print("Processing "+i)
		# Loads the image into memory
		with io.open(file_name, 'rb') as image_file:
		    content = image_file.read()

		image = types.Image(content=content)

		# Performs label detection on the image file
		response = client.label_detection(image=image)
		labels = response.label_annotations

		pic = Image.open(input_path+i)
		txt = ImageDraw.Draw(pic)
		font =ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf',40)
		
		w,h = pic.size
		l=0
		pic_label[i]=[]
		for label in labels:
			if label.description in label_pic:
				label_pic[label.description].append(i)
			else:
				label_pic[label.description]=[]
				label_pic[label.description].append(i)
			pic_label[i].append(label.description)
			txt.text((80,0+l*50),label.description,(255,50,50),font=font)
			l=l+1
		pic.save(output_path+i+'.jpg')
	
	if dbway == 'mysql':		
		n=0;
		for i in label_pic:
			if n < len(label_pic[i]):
				n=len(label_pic[i])
		table(db,"label_pic",n)

		flag=0;
		cmd="""INSERT INTO label_pic VALUES """
		for ikey in label_pic:
			if flag ==0:
				cmd+="('"
				flag=1
			else:
				cmd+=",('"
			cmd+=(ikey+"'")
			for i in range(n):
				if i < len(label_pic[ikey]):
					cmd+=",'"+label_pic[ikey][i]+"'"
				else:
					cmd+=",NULL"
			cmd+=","+str(len(label_pic[ikey]))
			cmd+=")"
		db.query(cmd)

		n=0;
		for i in pic_label:
			if n < len(pic_label[i]):
				n=len(pic_label[i])
		table(db,"pic_label",n)
		flag=0;
		cmd="""INSERT INTO pic_label VALUES """
		for ikey in pic_label:
			if flag ==0:
				cmd+="('"
				flag=1
			else:
				cmd+=",('"
			cmd+=ikey+"'"
			for i in range(n):
				if i < len(pic_label[ikey]):
					cmd+=",'"+pic_label[ikey][i]+"'"
				else:
					cmd+=",NULL"
			cmd+=","+str(len(pic_label[ikey]))
			cmd+=")"
		db.query(cmd)
	else:
		for pics in pic_label:
			connection.insert({"Tag":"pic_label","pic": pics,"labels":pic_label[pics]})
		for labels in label_pic:
			connection.insert({"Tag":"label_pic","labels":labels,"pic": label_pic[labels]})


	cc = "ffmpeg -r 0.5 -i "+output_path+"image%03d.jpg "+out_file
	shell = os.popen(cc)
	shell.close()


if __name__ == '__main__':
	GET_Video('./imgs/','./label_images/','Chanel.mp4','Mongo')