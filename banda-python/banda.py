import serial, time
from tkinter import *
from tkinter.ttk import * 
from PIL import ImageTk, Image
import os

circle = './circle.png'
conveyer = './banda.png'

windowWidht = 300
windowHeight = 200

s1_status = False
s1_x1 = 196
s1_x2 = 193

s2_status = False
s2_x1 = 153
s2_x2 = 150

s3_status = False
s3_x1 = 105
s3_x2 = 102

s4_status = False
s4_x1 = 60
s4_x2 = 57

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
  
        self.canvas = Canvas(master)

        img = Image.open(conveyer)
        self.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(windowWidht/2, windowHeight/2, anchor=CENTER,image = self.image)

        self.rectangle = self.canvas.create_oval(220, 100, 245, 125, fill = "black")

        self.canvas.pack() 
  
        self.movement() 
      
    def movement(self): 
        self.canvas.move(self.rectangle, self.x, self.y)
        self.canvas.after(100, self.movement)
        self.checkStatus()
        self.checkSerial()

    def checkSerial(self):
        while arduino.in_waiting:  
            p = arduino.read(1)
            if p == b'e':
                self.left(self)


    def checkStatus(self):
        x1,y1,x2,y2 = self.canvas.coords(self.rectangle)
        global s1_status, s2_status, s3_status, s4_status
        if x2 > s1_x1:
            if s1_status ==  False:
                s1_status = True
                s2_status = s3_status = s4_status = False
                arduino.write(str.encode('Passing by S1 \r'))
                #print('Starting by S1')
                #print('Passing by S1')
            self.x = 0
        if x1 < s2_x1 and x2 > s2_x2 :
            # Send serial status for S1
            if s2_status ==  False:
                s2_status = True
                s1_status = False
                s3_status = False
                s4_status = False
                arduino.write(str.encode('Passing by S2 \r'))
                #print('Passing by S2')
        if x1 < s3_x1 and x2 > s3_x2:
            # Send serial status for S3
            if s3_status ==  False:
                s3_status = True
                s2_status = False
                s1_status = False
                s4_status = False
                arduino.write(str.encode('Passing by S3 \r'))
                #print('Passing by S3')
        if x1 == s4_x1:
            if s4_status ==  False:
                s4_status = True
                s2_status = False
                s3_status = False
                s1_status = False
                arduino.write(str.encode('Passing by S4 & ending \r'))
                #print('Passing by S4')
                #print('Ended in S4')
            # Send serial status for S4
            self.x = 0


    def left(self,event): 
        # print(event.keysym) # Also print in arduino Serial
        self.x = -5
        self.y = 0


    def right(self, event): 
        # print(event.keysym) # Also print in arduino Serial
        self.x = 5
        self.y = 0

    # def motion(self, event):
    #     x, y = event.x, event.y
    #     # print('{}, {}'.format(x, y))

  
if __name__ == "__main__":



    master = Tk() 
    gfg = GFG(master) 
  
    master.title('Banda transportadora con Arduino')
    # master.resizable(width=False,height=False)
    master.geometry("%dx%d" % (windowWidht,windowHeight))

    # master.bind('<Motion>', gfg.motion)
    #master.bind("<KeyPress-Left>", lambda e: gfg.left(e))
    #master.bind("<KeyPress-Right>", lambda e: gfg.right(e))
    mainloop()
