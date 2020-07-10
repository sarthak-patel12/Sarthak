import cv2
import numpy as np
from keras.models import load_model
#from PIL import Image
model=load_model('Neural_Net')
def predict(image):
    input = cv2.resize(image, (28 , 28)).reshape((28 , 28,1)).astype('float32') / 255
    return model.predict_classes(np.array([input]))
canvas = np.ones((600,600), dtype="uint8") * 255

canvas[100:500,100:500] = 0

start_point = None
end_point = None
is_drawing = False
start_draw=False

def draw_line(img,start_at,end_at):
    cv2.line(img,start_at,end_at,255,15)

def on_mouse_events(event,x,y,flags,params):
    global start_point
    global end_point
    global canvas
    global is_drawing
    global start_draw
    if event == cv2.EVENT_LBUTTONDOWN:
        if start_draw:
            is_drawing = True
            start_point = (x,y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if is_drawing:
            end_point = (x,y)
            draw_line(canvas,start_point,end_point)
            start_point = end_point
    elif event == cv2.EVENT_LBUTTONUP:
        is_drawing = False


cv2.namedWindow("Test Canvas")
cv2.setMouseCallback("Test Canvas", on_mouse_events)


while(True):
    cv2.imshow("Test Canvas", canvas)
    key = cv2.waitKey(1) & 0xFF 
    if key==ord('q'):
        break
    elif key == ord('s'):
        start_draw = True
    elif key == ord('c'):
        canvas[100:500,100:500] = 0
    elif key == ord('p'):
        image = canvas[100:500,100:500]
        result = predict(image)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image,str(result),(10,100),font,2,(255,0,0),2,cv2.LINE_AA)
        print("PREDICTION : ",result)

cv2.destroyAllWindows()

