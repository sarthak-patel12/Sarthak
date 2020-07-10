import os
from tkinter import *
def track():
	os.system('python app.py')
def image():
	os.system('python image.py')
def live_image():
	os.system('python image_live.py')
r=Tk()
r.geometry('{}x{}'.format(500,500))
r_frame=Frame(r,bg='slategray',pady=61,padx=200)
r_frame.pack(side=TOP)
l_frame=Frame(r,bg='slategray',pady=61,padx=200)
l_frame.pack(side=TOP)
b_frame=Frame(r,bg='slategray',pady=61,padx=200)
b_frame.pack(side=TOP)
button_track = Button(l_frame,height=2,width=15,text="TrackPad",fg="black",bg="ivory",command=track)
button_track.pack(side=TOP)
button_img = Button(r_frame,height=2,width=15,text="Image",fg="black",bg="ivory",command=image)
button_img.pack(side=TOP)
button_liveimg=Button(b_frame,height=2,width=15,text="Live Image",fg="black",bg="ivory",command=live_image)
button_liveimg.pack(side=TOP)
r.mainloop()