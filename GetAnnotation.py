import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image,ImageDraw,ImageFont

def GET_Video(input_path,output_path,out_file):



	files= os.listdir(input_path)
	print(files)
	files.sort()
	print()
	print(files)

	for i in files:

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
		for label in labels:
			txt.text((80,0+l*50),label.description,(255,50,50),font=font)
			l=l+1
		pic.save(output_path+i+'.jpg')
		

	cc = "ffmpeg -r 0.5 -i "+output_path+"image%03d.jpg "+out_file
	shell = os.popen(cc)
	shell.close()


if __name__ == '__main__':
	GET_Video('./imgs/','./label_images/','Chanel.mp4')