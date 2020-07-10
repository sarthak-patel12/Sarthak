import cv2
#from PIL import Image
import numpy as np
from keras.models import load_model
img=cv2.imread("5.png",0)
model=load_model('Neural_Net')
def predict(image):
    input = cv2.resize(image,(28,28)).reshape((28 , 28,1)).astype('float32') / 255.0
    return model.predict_classes(np.array([input]))
result=predict(img)
str1=str(result)
str2="Prediction is :"
str_f=str2+str1
canvas = np.ones((500,500), dtype="uint8") * 255
canvas[0:500,0:500] = 0
img1 = canvas[0:500,0:500]
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img1,str(str_f),(130,270),font,1,(255,0,0),2,cv2.LINE_AA)
while(True):
	cv2.imshow("Test Canvas", canvas)
	key = cv2.waitKey(1) & 0xFF
	if key == ord('q'):
		break

