from tkinter import*    # it is use for making GUI interface
from tkinter import ttk     #it is use for styleing
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
from time import strftime
from datetime import datetime
# libary of MLT
import os
import numpy as np



# making a student class
class Face_recognition:
  # making a constructor
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text=" FACE RECOGNITION",font=("times new roman",40,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=50)

# first iamge
        img_top = Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\face1.png")
        img_top=img_top.resize((720,750))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=720,height=750)  



      # second image 
        img_bottom = Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\face3.png")
        img_bottom=img_bottom.resize((950,750))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=720,y=55,width=950,height=750)  

        b1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",28,"bold"),fg="green",bg="white")
        b1.place(x=312,y=50,width=300,height=48)


# =======   Attendance ==============
    def mark_attendance(self,i,r,n,d):
       with open ("Anjali.csv","r+",newline="\n") as f:
          myDataList=f.readlines()
          name_list=[]
          for line in myDataList:
            entry = line.split((","))
            name_list.append(entry[0])
          
          if((i not in name_list)) and (r not in name_list) and (n not in name_list) and ((d not in name_list)):
              now=datetime.now()
              d1=now.strftime("%d/%m/%Y")
              dtString=now.strftime("%H:%M:%S")
              f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

             

          


  #===============  face recognition ==========

    def face_recog(self):
        def draw_boundray(img,classifier,scalefactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scalefactor,minNeighbors)
            coord=[]
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int(100*(1-predict/300))

                conn=mysql.connector.connect(host="localhost",username="root",password="anjali2005",database="facial_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll  from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Department from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if confidence >77:
                  cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) 

                  cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)   

                  cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                  cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)  

                  self.mark_attendance(i,r,n,d)              
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord   
        def recognize(img,clf,faceCascade):
          coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)  
          return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
          ret,img=video_cap.read()
          img=recognize(img,clf,faceCascade)
          cv2.imshow("Welcome to face recognition",img)

          if cv2.waitKey(1)==13:
             break
        video_cap.release()
        cv2.destroyAllWindows()
                

if __name__ == "__main__":
   root=Tk()
   obj=Face_recognition(root)
   root.mainloop() 