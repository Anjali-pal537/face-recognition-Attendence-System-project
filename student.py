from tkinter import*    # it is use for making GUI interface
from tkinter import ttk     #it is use for styleing
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 # libary of MLT


# making a student class
class Student:
  # making a constructor
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Face Recognition System")
        
    # variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_email=StringVar()
        
    # firdob
        img1 = Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\student1.jpg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)


    #Second img
        img2 = Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\student2.jpg")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)


    #third img
        img3 = Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\student7.jpg")
        img3=img3.resize((550,130))
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=550,height=130)

#bg image
        img = Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\black.jpg")
        img=img.resize((1530,710))
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1490,height=610)

    #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=750)

        img_left = Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\student3.jpg")
        img_left=img_left.resize((720,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


    # current course
        current_course=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course Details",font=("times new roman",12,"bold") )
        current_course.place(x=5,y=125,width=715,height=150)

    #Department
        dep_label=Label(current_course,text="Department :",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

    #combobox and its values
        dep_comb=ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_comb["values"]=("Select Department","Computer","IT","Civil","Mechnical")
        dep_comb.current(0)
        dep_comb.grid(row=0,column=1,padx=2,pady=10,sticky=W)

    #Course
        course_label=Label(current_course,text="Course :",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)

    #combobox comboBox values
        course_comb=ttk.Combobox(current_course,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="read only")
        course_comb["values"]=("Select Course","Btech","BCA","MCA","BA","BSA")
        course_comb.current(0)
        course_comb.grid(row=0,column=3,padx=2,pady=10,sticky=W)


    #Year
        year_label=Label(current_course,text="Year :",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)

    #combobox 
        year_comb=ttk.Combobox(current_course,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")

    #comboBox values
        year_comb["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_comb.current(0)
        year_comb.grid(row=1,column=1,padx=2,pady=10,sticky=W)



    #Semester
        semester_label=Label(current_course,text="Semester :",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)

    #combobox 
        semester_comb=ttk.Combobox(current_course,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="read only")

    #comboBox values
        semester_comb["values"]=("Select Semester ","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_comb.current(0)
        semester_comb.grid(row=1,column=3,padx=2,pady=10,sticky=W)

    #Class Student information
        Class_Student_information=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        Class_Student_information.place(x=5,y=275,width=715,height=220)

    #StudentId
        studentId_label=Label(Class_Student_information,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(Class_Student_information,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

    #Student_name
        Student_name_label=Label(Class_Student_information,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        Student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Student_name_entry=ttk.Entry(Class_Student_information,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        Student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


    #class_Division
        class_Division=Label(Class_Student_information,text="class Division:",font=("times new roman",12,"bold"),bg="white")
        class_Division.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_Division_entry=ttk.Entry(Class_Student_information,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        class_Division_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

            #Roll_no
        Roll_no_label=Label(Class_Student_information,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        Roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Roll_no_entry=ttk.Entry(Class_Student_information,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        Roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #Gender
        Gender_label=Label(Class_Student_information,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Gender_entry=ttk.Entry(Class_Student_information,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        Gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        DOB_label=Label(Class_Student_information,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        DOB_entry=ttk.Entry(Class_Student_information,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        Email_label=Label(Class_Student_information,text="Email:",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Email_entry=ttk.Entry(Class_Student_information,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone_no
        Phone_no_label=Label(Class_Student_information,text="Phone_no",font=("times new roman",12,"bold"),bg="white")
        Phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        Phone_no_entry=ttk.Entry(Class_Student_information,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        Phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


   #    Address
        Address_label=Label(Class_Student_information,text="Address:",font=("times new roman",12,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Address_entry=ttk.Entry(Class_Student_information,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

   #    Teacher_name
        Teacher_name_label=Label(Class_Student_information,text="Teacher_name",font=("times new roman",12,"bold"),bg="white")
        Teacher_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        Teacher_name_entry=ttk.Entry(Class_Student_information,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        Teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

# Radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_information,variable=self.var_radio1,text="take photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(Class_Student_information,variable=self.var_radio2,text="take no photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        # buttons frame
        btn_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=495,width=720,height=45)


        # button Save
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",14,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)


        # button update_btn
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",14,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        # button delete_btn
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",14,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        # button reset_btn
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)



        btn_frame1=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=530,width=720,height=50)


#take a photo sample button
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")   
        take_photo_btn.grid(row=1,column=0)


        # update photo sample
        upadate_photo_btn=Button(btn_frame1,text="Update Photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        upadate_photo_btn.grid(row=1,column=2)


        #Right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=710,height=580)
#ima    ge in right side

        img_Right = Image.open(r"C:\Users\Anjali Pal\Desktop\facie recognition project\image\student8.jpg")
        img_Right=img_Right.resize((720,130))
        self.photoimg_Right=ImageTk.PhotoImage(img_Right)
        f_lbR=Label(Right_frame,image=self.photoimg_Right)
        f_lbR.place(x=5,y=0,width=720,height=130)



# ==    ==Search frame
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text=" Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=130,width=695,height=70)

# se    arch label
        Search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="white" ,fg="Blue")
        Search_label.grid(row=0,column=0,)


        search_comb=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=17,state="read only")

        #comboBox values
        search_comb["values"]=("Select ","Roll no","Phone no")
        search_comb.current(0)
        search_comb.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # button delete_btn
        search_btn=Button(Search_frame,text="Search",width=10,font=("times new roman",14,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=4,padx=3)

        # button delete_btn
        show_btn=Button(Search_frame,text="Show All",width=9,font=("times new roman",14,"bold"),bg="blue",fg="white")
        show_btn.grid(row=0,column=5)


# ====Table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=200,width=695,height=350)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

# width
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are requires")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="anjali2005",database="facial_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                
    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="anjali2005",database="facial_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]) ,
        
        
    #update function      
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are requires",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="anjali2005",database="facial_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),  self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()))
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success","Student Details Succesfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

#Delete button function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete >0:
                            conn=mysql.connector.connect(host="localhost",username="root",password="anjali2005",database="facial_recognition")
                            my_cursor=conn.cursor()
                            sql="delete from student where Student_id=%s"
                            val=(self.var_std_id.get(),)
                            my_cursor.execute(sql,val )
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student detail",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

#Reset button function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

# ================== Generate data set or Take photo Sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are requires",parent=self.root)
        else:
            try:
                
                    conn=mysql.connector.connect(host="localhost",username="root",password="anjali2005",database="facial_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from student ")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                        id+=1
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),  self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()==id+1
                                                                                         ))
                    
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

#=================== Load predefined data on face frontals from opencv using haarcascade Algorithm
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        # scaling factor =1.3
                        # minimum Neighbor=5

                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h ,x:x+w]
                            return face_cropped
                    cap=cv2.VideoCapture(0) # web camera
                    img_id=0
                    while True:
                        ret , my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==50:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets completed !!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)





        

        


            
              
                
if __name__ == "__main__":
   root=Tk()
   obj=Student(root)
   root.mainloop()