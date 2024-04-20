import os 
import sys
import cv2
from PIL import Image

# Ascii characters used HERE 
ASCII_CHARS = [".", ",", "-", ";", "+", "*", "?", "%", "S", "#", "@"]
              #Darker side                               Lighter side

def resized_gray_image(image ,new_width=70):
	width,height = image.size
	aspect_ratio = height/width
	new_height = int(aspect_ratio * new_width)#resizing to desired view comfort
	resized_gray_image = image.resize((new_width,new_height)).convert('L') #if you have an L mode image, that means it is a single channel image - normally interpreted as greyscale.
	return resized_gray_image

def pix_mapping(image):
	pixels = image.getdata()
	characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
	return characters

def create_frame(image,new_width=70):
	new_image_data = pix_mapping(resized_gray_image(image))

	total_pixels = len(new_image_data)

	ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, total_pixels, new_width)])

	sys.stdout.write(ascii_image)
	os.system('cls' if os.name == 'nt' else 'clear')




vid = cv2.VideoCapture("video.mp4")

while True:

	ret,frame = vid.read()  #ret is a boolean regarding whether or not there was a return at all, at the frame is each frame that is returned.
	cv2.imshow("ASCII-FUN ;)",frame)
	create_frame(Image.fromarray(frame))
	cv2.waitKey(1)
