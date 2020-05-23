import serial, time
from tkinter import *
from tkinter.ttk import * 
from PIL import ImageTk, Image
import os

circle = './circle.png'
conveyer = './banda.png'

windowWidht = 1500
windowHeight = 500

s1_status = False
# s1_stop = False
s1_x1 = 1020
s1_x2 = 1000

s2_status = False
s2_stop = False
s2_x1 = 820
s2_x2 = 800

s3_status = False
s3_stop = False
s3_x1 = 620
s3_x2 = 600

s4_status = False
# s4_stop = False
s4_x1 = 435
s4_x2 = 415

arduino = serial.Serial("COM5",9600)
arduino.write(str.encode("Arduino conectado \r"))


class GFG: 
    s1_status = False
    s1_x1 = 196
    s1_x2 = 193

    def __init__(self, master = None): 
        self.master = master 
          
        self.x = 0
        self.y = 0
  
        self.canvas = Canvas(master,width = windowWidht, height = windowHeight)

        img = Image.open(conveyer)
        self.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(windowWidht/4, windowHeight/3,anchor="nw",image = self.image)

        self.rectangle = self.canvas.create_oval(1000, 170, 1045, 215, fill = "yellow")

        self.pointS1 = self.canvas.create_oval(1020, 270, 1000, 290, fill = "cyan")
        self.pointS2 = self.canvas.create_oval(800, 270, 820, 290, fill = "cyan")
        self.pointS3 = self.canvas.create_oval(600, 270, 620, 290, fill = "cyan")
        self.pointS4 = self.canvas.create_oval(435, 270, 415, 290, fill = "cyan")


        self.canvas.pack(fill=BOTH) 
  
        self.movement() 

    def movement(self): 
        self.canvas.move(self.rectangle, self.x, self.y)
        self.canvas.after(100, self.movement)
        self.checkStatus()
        self.checkSerial()

    def checkSerial(self):
        x1,y1,x2,y2 = self.canvas.coords(self.rectangle)
        global s2_stop, s3_stop

        while arduino.in_waiting:
            p = arduino.read(1)
            if p == b'B':
                self.left(self)
            if p == b'S':
                self.stop(self)
            if p == b'1':
                self.right(self)
            if p == b'2':
                s2_stop = True
                s3_stop = False
                # Calculate coords to move left or right
                if x1 > s2_x1:
                    self.left(self)
                if x1 < s2_x1:
                    self.right(self)
            if p == b'3':
                s3_stop = True
                s2_stop = False
                # Calculate coords to move left or right
                if x1 > s3_x1:
                    self.left(self)
                if x1 < s3_x1:
                    self.right(self)
            if p == b'4':
                self.left(self)

    def checkStatus(self):
        x1,y1,x2,y2 = self.canvas.coords(self.rectangle)
        global s1_status, s2_status, s3_status, s4_status
        global s2_stop, s3_stop


        if x1 > s1_x1:
            if s1_status ==  False:
                s1_status = True
                s2_status = s3_status = s4_status = False
                arduino.write(str.encode('Passing by S1 \r'))
            self.x = 0


        if x1 < s2_x1 and x2 > s2_x2:
            if s2_stop:
                self.stop(self)
            if s2_status ==  False:
                s2_status = s1_status = s3_status = s4_status = False
                arduino.write(str.encode('Passing by S2 \r'))


        if x1 < s3_x1 and x2 > s3_x2:
            if s3_stop:
                self.stop(self)
            if s3_status ==  False:
                s3_status = True
                s2_status = s1_status = s4_status = False
                arduino.write(str.encode('Passing by S3 \r'))


        if x1 == s4_x2:
            if s4_status ==  False:
                s4_status = True
                s2_status = s3_status = s1_status = False
                arduino.write(str.encode('Passing by S4 & ending \r'))
            self.stop(self)


    def left(self,event): 
        self.x = -5

    def right(self, event): 
        self.x = 5

    def stop(self, event):
        self.x = 0

    # def motion(self, event):
    #     x, y = event.x, event.y
    #     print('{}, {}'.format(x, y))

  
if __name__ == "__main__":
    master = Tk() 
    gfg = GFG(master) 
  
    master.title('Banda transportadora con Arduino')
    master.geometry("%dx%d" % (windowWidht,windowHeight))
    # master.resizable(width=False,height=False)

    # master.bind('<Motion>', gfg.motion)
    # master.bind("<KeyPress-Left>", lambda e: gfg.left(e))
    # master.bind("<KeyPress-Right>", lambda e: gfg.right(e))
    mainloop()
