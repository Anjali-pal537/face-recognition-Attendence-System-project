from tkinter import*    # it is use for making GUI interface
from tkinter import ttk     #it is use for styleing
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

# making a student class
class Help:
  # making a constructor
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top = Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\help.jpg")
        img_top=img_top.resize((1530,800))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1530,height=800)  
        
        dev_label=Label(f_lbl,text="CONTACT US: ",font=("times new roman",25,"bold"),bg="lightgrey",fg="black")
        dev_label.place(x=975,y=600)
        dev_label1=Label(f_lbl,text="anjalipal2005.pal@gmail.com",font=("times new roman",15,"bold"),fg="green")
        dev_label1.place(x=1200,y=645)
          
if __name__ == "__main__":
  root=Tk()
  obj=Help(root)
  root.mainloop()