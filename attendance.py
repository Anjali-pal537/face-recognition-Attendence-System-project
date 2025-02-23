from tkinter import*    # it is use for making GUI interface
from tkinter import ttk     #it is use for styleing
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 # libary of MLT
import os
import csv
from tkinter import filedialog

mydata=[]
# making a student class
class Attendance:
  # making a constructor
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")

    #variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


    # firdob
        img1 = Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\student1.jpg")
        img1=img1.resize((800,200))
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=800,height=200)


    #Second img
        img2 = Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\student2.jpg")
        img2=img2.resize((800,200))
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=800,height=200)

#bg image
        img = Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\black.jpg")
        img=img.resize((1530,710))
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE   MANAGMENT   SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)   

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1490,height=535)     

    #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=510)


        img_left = Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\att2.png")
        img_left=img_left.resize((720,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=8,y=135,width=710,height=340)


      # Entry  and Labels
     #StudentId
        Attendance_label=Label(left_inside_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        Attendance_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Attendance_label=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",13,"bold"))
        Attendance_label.grid(row=0,column=1,padx=10,pady=5,sticky=W)  


    #Roll no
        Roll_label=Label(left_inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        Roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        
        Roll_label=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",13,"bold"))
        
        Roll_label.grid(row=0,column=3,padx=10,pady=5,sticky=W)     

             #Name
        Name_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        
        Name_label=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",13,"bold"))
        
        Name_label.grid(row=1,column=1,padx=10,pady=5,sticky=W)     

             #Department
        Department_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        Department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        
        Department_label=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",13,"bold"))
        
        Department_label.grid(row=1,column=3,padx=10,pady=5,sticky=W)     


             #Time
        Time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        Time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        
        Time_label=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",13,"bold"))
        
        Time_label.grid(row=2,column=1,padx=10,pady=5,sticky=W)     

# Date Status

        Date_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        Date_label=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",13,"bold"))
        Date_label.grid(row=2,column=3,padx=10,pady=5,sticky=W)  

        Attendance_label=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        Attendance_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
    
        Attendance_comb=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),width=17,state="read only")
        Attendance_comb["values"]=("Status","Present","Absent")
        Attendance_comb.current(0)
        Attendance_comb.grid(row=3,column=1,padx=2,pady=10,sticky=W)
   

        # buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=270,width=720,height=50)


        # button Save
        Import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=15,font=("times new roman",14,"bold"),bg="blue",fg="white")
        Import_btn.grid(row=0,column=0)


        # button update_btn
        Export_btn=Button(btn_frame,command=self.exportCsv,text="Export CSV",width=15,font=("times new roman",14,"bold"),bg="blue",fg="white")
        Export_btn.grid(row=0,column=1)

        # button delete_btn
        Delete_btn=Button(btn_frame,text="Delete",width=15,font=("times new roman",14,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2)

        # button reset_btn
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        # btn_frame1=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        # btn_frame1.place(x=0,y=530,width=730,height=50)


    # Right Label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student  Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=710,height=510)


# ====Table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=695,height=470)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendancereportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendancereportTable.xview)
        scroll_y.config(command=self.AttendancereportTable.yview)

        self.AttendancereportTable.heading("id",text="Attendance ID")
        self.AttendancereportTable.heading("roll",text="Roll")
        self.AttendancereportTable.heading("name",text="Name")
        self.AttendancereportTable.heading("department",text="Department")
        self.AttendancereportTable.heading("time",text="Time")
        self.AttendancereportTable.heading("date",text="Date")
        self.AttendancereportTable.heading("attendance",text="Attendance")
 
        self.AttendancereportTable["show"]="headings"
        self.AttendancereportTable.column("id",width=100)
        self.AttendancereportTable.column("roll",width=100)
        self.AttendancereportTable.column("name",width=100)
        self.AttendancereportTable.column("department",width=100)
        self.AttendancereportTable.column("time",width=100)
        self.AttendancereportTable.column("attendance",width=100)


        self.AttendancereportTable.pack(fill=BOTH,expand=1)
        self.AttendancereportTable.bind("<ButtonRelease>",self.get_cursor)
        
#============Fetch Data============
    def fetchData(self,rows):
        self.AttendancereportTable.delete(*self.AttendancereportTable.get_children())
        for i in rows:
            self.AttendancereportTable.insert("",END,values=i)
            
#============import csv============           
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("All File",".*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
#============export csv============          
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root) 
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("All File",".*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Dta export","Your data exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendancereportTable.focus()
        content=self.AttendancereportTable.item(cursor_row)
        rows=content['values']  
        self.var_atten_id.set(rows[0]) 
        self.var_atten_roll.set(rows[1]) 
        self.var_atten_name.set(rows[2]) 
        self.var_atten_dep.set(rows[3]) 
        self.var_atten_time.set(rows[4]) 
        self.var_atten_date.set(rows[5]) 
        self.var_atten_attendance.set(rows[6]) 
    
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("") 
        self.var_atten_name.set("") 
        self.var_atten_dep.set("")
        self.var_atten_time.set("") 
        self.var_atten_date.set("") 
        self.var_atten_attendance.set("")

if __name__ == "__main__":
   root=Tk()
   obj=Attendance(root)
   root.mainloop()