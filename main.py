from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from Train import Train
from face_recognition import Face_recognition
from Developer import Developer
from Help import Help 
import tkinter  
from attendance import Attendance



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")
        
        #First Image
        img=Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\AI2.jpg")
        img=img.resize((510,200))
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0)
        
        #Second Image
        img2=Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\AI1.jpg")
        img2=img2.resize((510,200))
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=510,y=0)
        
        #Third Image
        img3=Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\AI3.jpg")
        img3=img3.resize((510,200))
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1020,y=0)
        
        #Background image
        img4=Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\bg.jpg")
        img4=img4.resize((1530,710))
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=200)
        
        #title button
        title_lbl=Label(bg_img,text="STUDENT  FACE  RECOGNITION  ATTENDANCE  SYSTEM",font=("Times New Roman",30,"italic","bold"),fg="blue",bg="white")
        title_lbl.place(x=0,y=0,width=1530,height=40)
        
        #student button
        img5=Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\student_detail.jpg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=80,width=220,height=220)
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b1_1.place(x=200,y=270,width=220,height=40)
        
         #face detection button
        img6=Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\men.jpg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)
        b2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.Face_recognition)
        b2.place(x=500,y=80,width=220,height=220)
        b2_1=Button(bg_img,text="Face Recognition",command=self.Face_recognition,cursor="hand2",font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b2_1.place(x=500,y=270,width=220,height=40)

        #Attendance button
        img7=Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\attendence.jpg")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)
        b3=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.Attendance)
        b3.place(x=800,y=80,width=220,height=220)
        b3_1=Button(bg_img,text="Attendance",command=self.Attendance,cursor="hand2",font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b3_1.place(x=800,y=270,width=220,height=40)

        #Help desk button
        img8=Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\helpdesk.jpg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)
        b4=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.Help)
        b4.place(x=1100,y=80,width=220,height=220)
        b4_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.Help,font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b4_1.place(x=1100,y=270,width=220,height=40)


        # photo
        
        img11=Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\photoalbum.jpeg")
        img11=img11.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)
        b11=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.open_img)
        b11.place(x=500,y=350,width=220,height=220)
        b11_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b11_1.place(x=500,y=540,width=220,height=40)
        
         #Train data button
        img9=Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\train data.jpg")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)
        b5=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=350,width=220,height=220)
        b5_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b5_1.place(x=200,y=540,width=220,height=40)

         #Developer button
        img12=Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\developer.png")
        img12=img12.resize((220,220))
        self.photoimg12=ImageTk.PhotoImage(img12)
        b12=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.Developer)
        b12.place(x=800,y=350,width=220,height=220)
        b12_1=Button(bg_img,text="Developer",command=self.Developer,cursor="hand2",font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b12_1.place(x=800,y=540,width=220,height=40)
        
         #Exit button
        img10=Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\exit.jpg")
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)
        b6=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.iExit)
        b6.place(x=1100,y=350,width=220,height=220)
        b6_1=Button(bg_img,text="Exit Button",cursor="hand2",command=self.iExit,font=("Arial",15,"italic"),bg="lightpink",fg="black")
        b6_1.place(x=1100,y=540,width=220,height=40)


    def open_img(self):
        os.startfile("data")




        # FUNCTIONS BUTTONS
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def Face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def Developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)


    def Help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project")
        if self.iExit>0:
            self.root.destroy()
        else:
            return
        
    def Attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

        

 
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

    