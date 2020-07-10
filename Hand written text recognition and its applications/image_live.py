import cv2
import requests
import numpy as np
from keras.models import load_model

url="http://ipaddress//photo.jpg"
model=load_model('Neural_Net')
def predict(image):
    input = cv2.resize(image,(28,28)).reshape((28 , 28,1)).astype('float32') / 255.0
    return model.predict_classes(np.array([input]))
canvas = np.ones((200,200), dtype="uint8") * 255
canvas[0:200,0:200] = 0
while True:
	cv2.imshow("Test Canvas", canvas)
	img_resp=requests.get(url)
	img_arr=np.array(bytearray(img_resp.content),dtype=np.uint8)
	img9=cv2.imdecode(img_arr,-1)
	cv2.imshow("cam",img9)
	key=cv2.waitKey(1) &0xFF
	if key==ord('p'):
		cv2.imwrite("files3.jpg",img9)
		img=cv2.imread("files3.jpg",0)
		result=predict(img)
		str1=str(result)
		canvas[0:200,0:200] = 0
		img1 = canvas[0:200,0:200]
		font=cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img1,str(str1),(55,110),font,1,(255,0,0),2,cv2.LINE_AA)
	if key == ord('q'):
		break
