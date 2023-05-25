import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *

def connection() : #connect Database
    global conn,cursor
    conn = sqlite3.connect("Final Project.db")
    cursor = conn.cursor() #กดcursor

def mainwindow() : #หน้าแรก
    root = Tk()
    root.geometry("1200x800")
    root.config(bg='white')
    root.title("BURangsit")
    root.option_add('*font',"Calibri 16 bold")
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)
    return root

def leftlayout() :
    leftframe.rowconfigure((0,1,2,3,4,5,6),weight=1)
    leftframe.columnconfigure((0),weight=1)
    leftframe.grid(row=0,column=0,rowspan=9,sticky="news")
    Label(leftframe,image=img1,bg='#0194F3').grid(row=0,column=0,sticky="news") 
    Label(leftframe,text="Become a member and enjoy exclusive benefits!",bg='white').grid(row=3,column=0) 
    Label(leftframe,image=img2,bg='white').grid(row=4,column=0,sticky="n") 
    
def loginlayout() :
    global userentry,pwdentry
    regisframe.grid_forget()
    loginframe.rowconfigure((0,1,2,3,4,5,6),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    upframe.grid(row=0,column=1,sticky="news")
    downframe.grid(row=8,column=1,sticky="news")
    loginframe.grid(row=1,column=1,rowspan=7,sticky="news") #ทำให้loginframeเป็นกรอบๆข้างใน
    Label(loginframe,text="Login to your Account",font="Calibri 20 bold",bg='white',padx=20).grid(row=0,columnspan=2,sticky='w')
    Label(loginframe,text="Username: ",bg='white',padx=20).grid(row=1,column=0,sticky='w')
    userentry = Entry(loginframe,bg='white',width=20) #กล่องข้อความ user
    userentry.grid(row=2,column=0,sticky='w',padx=20)
    Label(loginframe,text="Password  : ",bg='white',padx=20).grid(row=3,column=0,sticky='w')    
    pwdentry = Entry(loginframe,bg='white',width=20,show='*') #กล่องข้อความ Password show*
    pwdentry.grid(row=4,column=0,sticky='w',padx=20) 
    Button(loginframe,text="Login",width=10,command=lambda:loginclick(userentry.get(),pwdentry.get())).grid(row=5,column=0,pady=20,ipady=15,sticky='w',padx=40)
    Button(loginframe,text="Register",width=10,command=regislayout).grid(row=5,column=1,pady=20,ipady=15,sticky='w',padx=40)
    Button(loginframe,text="Exit",bg="red",fg="white",width=5,command=root.quit).grid(row=6,column=1,pady=10,ipady=5,sticky='e',padx=40) #ปุ่ม Exit

def loginclick(user,pwd) : #ใช้ตรวจสอบว่า User ใส่ถูกมั้ย
    global result2
    if user == "" or pwd == "" : #ถ้า user เป็นช่องว่าง จะขึ้นแจ้ง
        messagebox.showwarning("Admin : ","Please enter a username or password")
        userentry.focus_force() #focus_force คือ เม้ากระพิบ
    else :
        sql = "select * from User where Username=?;" #ให้ไปเช็ค username ใน students ว่ามีในข้อมูลมั้ย
        cursor.execute(sql,[user])
        result2 = cursor.fetchone() #fetchone กด run ใน database ดุงข้อมูล Username แค่อันเดียว มาตรวจสอบ
        if result2 :
            sql = "select * from User where Username=? and Password=?;" #ถ้า fetch ออกมาได้ result จะเป็น True
            cursor.execute(sql,[user,pwd])
            result2 = cursor.fetchone()
            if result2 : #If true //login success
                messagebox.showinfo("Admin : ","Login Successfully.")
                Nutsearch() #เปิดหน้า welcomepage
            else : #If False // login error
                messagebox.showwarning("Admin : ","Incorrect Password \nPlease try again")
                pwdentry.selection_range(0,END) #ลบข้อมูลตั้งแต่ตัว0ถึงจบ และกระพิบที่เดิม
                pwdentry.focus_force()
        else : # ถ้าเช็ค username แล้วไม่มี จะขึ้นแจ้งเตือน
            messagebox.showwarning("Admin : ","The username not found.")
            userentry.selection_range(0,END)
            userentry.focus_force()
    print(result2[3])
    print(result2[4])

def regislayout() :
    global fname,lname,newuser,newpwd,cfpwd
    loginframe.grid_forget()
    regisframe.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11),weight=1)
    regisframe.columnconfigure((0,1),weight=1)
    regisframe.grid(row=1,column=1,rowspan=7,sticky="news") #ทำให้loginframeเป็นกรอบๆข้างใน
    Label(regisframe,text="Join us as a BURangsit member",font="Calibri 20 bold",bg='white').grid(row=0,column=0,columnspan=2,sticky='news',pady=10)
    Label(regisframe,text='Your data will be kept confidential and secure.',font="Calibri 8",bg='white',fg='#687176').grid(row=8,column=0,columnspan=2,sticky='w',padx=10)    
    Label(regisframe,text='First name : ',bg='white').grid(row=2,column=0,sticky='w',padx=10)
    fname = Entry(regisframe,width=20,bg='white')
    fname.grid(row=3,column=0,sticky='w',padx=10)
    Label(regisframe,text='Last name : ',bg='white').grid(row=2,column=1,sticky='w',padx=10)
    lname = Entry(regisframe,width=20,bg='white')
    lname.grid(row=3,column=1,sticky='w',padx=10)
    Label(regisframe,text="Username : ",bg='white').grid(row=4,column=0,sticky='w',padx=10)
    newuser = Entry(regisframe,width=20,bg='white')
    newuser.grid(row=5,columnspan=2,sticky='w',padx=10)
    Label(regisframe,text="Password : ",bg='white').grid(row=6,column=0,sticky='w',padx=10)
    newpwd = Entry(regisframe,width=20,bg='white',show='*')
    newpwd.grid(row=7,column=0,sticky='w',padx=10)
    Label(regisframe,text="Confirm Password : ",bg='white').grid(row=6,column=1,sticky='w',padx=10)
    cfpwd = Entry(regisframe,width=20,bg='white',show='*')
    cfpwd.grid(row=7,column=1,sticky='w',padx=10)
    regisaction = Button(regisframe,text="Register",bg="#FF5E1F",fg="white",command=registration)
    regisaction.grid(row=12,columnspan=2,ipady=5,ipadx=5,pady=5,sticky='e',padx=10)
    fname.focus_force()
    loginbtn = Button(regisframe,text="Back to Login",command=loginlayout)
    Label(regisframe,text="Already registered? ",bg='white',fg='blue').grid(row=12,column=0,sticky='w',padx=10)
    loginbtn.grid(row=12,columnspan=2,ipady=5,ipadx=5,pady=5,sticky='e',padx=150)
    
def registration() :
    #print("Hello from registration")
    if fname.get() == "" :
        messagebox.showwarning("Admin: ","Please enter a firstname")
        fname.focus_force()
    elif lname.get() == "" :
        messagebox.showwarning("Admin : ","Please enter a lastname")
        lname.focus_force()
    elif newuser.get() == "" :
        messagebox.showwarning("Admin : ","Please enter a username")
        newuser.focus_force()
    elif newpwd.get() == "" :
        messagebox.showwarning("Admin : ","Please enter a password")
        newpwd.focus_force()
    elif cfpwd.get() == "" :
        messagebox.showwarning("Admin : ","Please enter a confirm password")
        cfpwd.focus_force()
    else : # check a username is already exist???
        sql = "select * from User where Username=?; "
        #execute sql query
        cursor.execute(sql,[newuser.get()])
        result = cursor.fetchone() #fetch a result
        if result :
            messagebox.showerror("Admin:","The username is already exists\n Try again")
            newuser.selection_range(0,END)
            newuser.focus_force()
        else :
            if newpwd.get() == cfpwd.get() : #verify a new pwd and confirm pwd are equal
                sql = "insert into User (Username,Password,Fname,Lname) values (?,?,?,?);"
                #execute sql query 
                cursor.execute(sql,[newuser.get(),newpwd.get(),fname.get(),lname.get()])
                conn.commit() #save
                retrivedata()
                messagebox.showinfo("Admin:","Registration Successfully")
                resetdata()                
            else :  #verify a new pwd and confirm pwd are not equal
                messagebox.showwarning("Admin: ","Incorrect a confirm password\n Try again")
                cfpwd.selection_range(0,END)
                cfpwd.focus_force()

def retrivedata() :
    sql = "select * from User"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total row = ",len(result))
    for i,data in enumerate(result) :
        print("Row#",i+1,data)

def resetdata() :
    fname.delete(0,END)
    lname.delete(0,END)
    newuser.delete(0,END)
    newpwd.delete(0,END)
    cfpwd.delete(0,END)
    




###########################################################################################

def search_hostels(root):
    global Frame_search_hostels,Room_ui2,Room_ui1,Room_ui,data_hostel,content
    #ข้อมูลวันที่ check-in , check-out
    global setDate_in,setDate_out,cal_check_in,cal_check_out #ลอง print ดู
    #frame ตัวสีเทา
    Frame_search_hostels = Frame(root,bg=bg_behind)

    Frame_search_hostels.grid(row=0,column=0,sticky='news')
    Frame_search_hostels.rowconfigure((0,2),weight=1)
    Frame_search_hostels.rowconfigure((1),weight=2)

    Frame_search_hostels.columnconfigure((0,1,2),weight=1)

    #frame ตัวสีขาว
    data_hostel = Frame(Frame_search_hostels,bg="white")
    data_hostel.grid(row=1,column=1,sticky="news")

    data_hostel.rowconfigure((0,2),weight=1)
    data_hostel.rowconfigure((1),weight=3)
    
    data_hostel.columnconfigure((0,2),weight=1)
    data_hostel.columnconfigure((1),weight=3)

    # content ตัวหนังสือ,button,input ต่างๆ *************************************************
    content = Frame(data_hostel,bg="#fff")
    content.grid(row=1,column=1,sticky="news")

    content.rowconfigure((0,1,2,3,4,5,6),weight=1)
    content.columnconfigure((1,2,3),weight=1)
    content.columnconfigure((0,4),weight=2)

    #name title
    name_title = Label(content,text="ค้นหาที่พักในรังสิต",bg="white",font='Garamond 24 bold')
    name_title.grid(row=0,columnspan=5,sticky=S)

    #search
    # search_var = StringVar()
    # search_name = Entry(content,width=50,borderwidth=2, relief="groove",textvariable=search_var)
    # search_var.set('รังสิต')
    # search_name.grid(row=1,columnspan=5)

    #check in-out
    #column 0
#----------------------- calendar checkin ----------------------------------
    checkin_title = Label(content,text="Check in",bg="white")
    checkin_title.grid(row=2,column=1,sticky=W,padx=40)

    # checkin_ui = Label(content,text=f"Wed, {22} Mar {2023}",bg=color.white) #ต้องมีแสดง calenda **********************
    # checkin_ui.grid(row=3,column=1,sticky=NW,padx=40)
    cal_check_in = Calendar(content, seLectmode='day', year=2023,month=5,day=10)
    cal_check_in.grid(row=3,column=1,sticky=NW)

    setDateList_in = cal_check_in.get_date().split('/')
    setDate_in = f'{setDateList_in[1]}/{setDateList_in[0]}/{setDateList_in[2]}'

#----------------------- calendar checkin ----------------------------------
#----------------------- calendar checkout ----------------------------------
    checkout_title = Label(content,text="check-out",bg="white")
    checkout_title.grid(row=2,column=2,sticky=W)

    # checkout_ui = Label(content,text=f"Thu, {23} Mar {2023}",bg=color.white)
    # checkout_ui.grid(row=3,column=3,sticky=NW)
    cal_check_out = Calendar(content, seLectmode='day', year=2023,month=5,day=11)
    cal_check_out.grid(row=3,column=2,sticky=NW)
    setDateList_out = cal_check_out.get_date().split('/')
    setDate_out = f'{setDateList_out[1]}/{setDateList_out[0]}/{setDateList_out[2]}'
#----------------------- calendar checkout ----------------------------------

    #เลือกจำนวณคน และ ห้อง
    Room_title = Label(content,text="Guest and Room",bg="white")
    Room_title.grid(row=4,columnspan=2,column=1,sticky=W,padx=40)

    Room_ui = Label(content,width=35,textvariable=Roomtext)
    Roomtext.set(f"ผู้ใหญ่ {1} คน, {1} ห้อง")
    Room_ui.grid(row=5,columnspan=2,column=1,sticky=W,padx=38)

    RoomFrame = Frame(content,bg="white")
    RoomFrame.grid(row=6,columnspan=2,column=1,sticky="news")
    RoomFrame.rowconfigure(0,weight=1)
    RoomFrame.columnconfigure((0,1,2,3,4),weight=1)

    people_title = Label(RoomFrame,text="ผู้ใหญ่ :",bg="white")
    people_title.grid(row=0,column=0,sticky=NE)
    
    Room_ui1 = ttk.Combobox(RoomFrame,values=['1','2','3','4','5'],width=5)
    Room_ui1.set('1')
    Room_ui1.bind("<<ComboboxSelected>>", changeRoom1)
    Room_ui1.grid(row=0,column=1,sticky=N)

    room_title = Label(RoomFrame,text="จำนวณห้อง :",bg="white")
    room_title.grid(row=0,column=2,sticky=N)
    
    
    Room_ui2 = ttk.Combobox(RoomFrame,values=['1','2','3','4','5'],width=5)
    Room_ui2.current(0)
    Room_ui2.bind("<<ComboboxSelected>>", changeRoom2)
    Room_ui2.grid(row=0,column=3,sticky=NW)


    #search button
    search_bt = Button(content,text="Search",bg='#FF5E1F',fg='white',width=15,command=deleteFrame)
    search_bt.grid(row=5,column=3,sticky=NW)

    # content ตัวหนังสือ,button,input ต่างๆ *************************************************

def deleteFrame():
    global result,day,setDate_in,setDate_out
    setDate_in = cal_check_in.get_date().split('/')
    setDate_out = cal_check_out.get_date().split('/')
    setDate_in = f'{setDate_in[1]}/{setDate_in[0]}/{setDate_in[2]}'
    setDate_out = f'{setDate_out[1]}/{setDate_out[0]}/{setDate_out[2]}'
    sql = 'SELECT * from HotelData Where DateIn NOT between ? and ? AND DateOut NOT between ? and ?;'
    cursor.execute(sql,[setDate_in,setDate_out,setDate_in,setDate_out])
    result = cursor.fetchall()
    print(result)
    abc = setDate_in[0]+setDate_in[1]
    cba = setDate_out[0]+setDate_out[1]
    day = int(cba)-int(abc)
    print(setDate_in)
    print(setDate_out)
    print(day)
    Frame_search_hostels.grid_forget()
    data_hostel.grid_forget()
    content.grid_forget()
    Annsearch()
    
def changeRoom2(event):
    # print(Room_ui2.get())
    Roomtext.set(f"ผู้ใหญ่ {Room_ui1.get()} คน, {Room_ui2.get()} ห้อง") 
def changeRoom1(event):
    # print(Room_ui1.get())
    Roomtext.set(f"ผู้ใหญ่ {Room_ui1.get()} คน, {Room_ui2.get()} ห้อง")  
    
#####################################  Review  #####################################

def listhotel():
    # list hostels
    Frame_list_hostel = Frame(Frame_hostel,bg="green")
    Frame_list_hostel.grid(row=1,columnspan=2,column=1,sticky="news")
    Frame_list_hostel.rowconfigure(0,weight=1)
    Frame_list_hostel.columnconfigure(0,weight=1)
#-------------------------------------------------------------------------------------------


    # Create A Main Frame
    main_frame = Frame(Frame_list_hostel)
    main_frame.pack(fill=BOTH, expand=1,)
    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas)
    show_card(second_frame,result)
    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

def show_hostels(root):
    global second_frame,Frame_list_hostel,main_frame,lockout_Frame
    Frame_hostel.grid(row=0,sticky='news')
    Frame_hostel.rowconfigure(0,weight=1)
    Frame_hostel.rowconfigure((1),weight=6)
    Frame_hostel.columnconfigure((1),weight=1)
    Frame_hostel.columnconfigure((2),weight=5)


    #Frame ทั้งหมด 3 ตัว
#-------------------------------------------------------------------------------------------
    #Tab menu ด้านบนสุด 
    Frame_menu = Frame(Frame_hostel,bg=tab_menu)
    Frame_menu.grid(row=0,columnspan=3,sticky='news')

    #Frame คุมด้านซ้ายทั้งหมด
    Frame_left = Frame(Frame_hostel,bg=white)
    Frame_left.grid(row=1,column=0,sticky='news')
    Frame_left.rowconfigure((0),weight=1)
    Frame_left.rowconfigure((1),weight=2)
    Frame_left.columnconfigure(0,weight=1)


    #screening ตัวคัดกรอง ด้านซ้าย 
    Frame_screening = Frame(Frame_left, borderwidth=2, relief="groove",bg=white)
    Frame_screening.grid(row=0,column=0,ipady=20,sticky='n',ipadx=20,pady=10,padx=10)
    # Frame_screening = Frame(Frame_hostel, borderwidth=2, relief="groove")
    # Frame_screening.grid(row=1,column=0,ipady=20,sticky='n',ipadx=20,pady=10,padx=10)
    
    #screening ตัวคัดกรอง ด้านซ้าย ล่าง
    lockout_Frame = Frame(Frame_left, borderwidth=2, relief="groove",bg=white)
    lockout_Frame.grid(row=1,column=0,ipady=20,sticky='n',ipadx=20,padx=10)
    # lockout_Frame = Frame(Frame_hostel, borderwidth=2, relief="groove")
    # lockout_Frame.grid(row=1,column=0,ipady=20,sticky='n',ipadx=20,pady=100,padx=10)

    # list hostels
    Frame_list_hostel = Frame(Frame_hostel,bg=white)
    Frame_list_hostel.grid(row=1,columnspan=2,column=1,sticky="news")
    Frame_list_hostel.rowconfigure(0,weight=1)
    Frame_list_hostel.columnconfigure(0,weight=1)
#-------------------------------------------------------------------------------------------


    # Create A Main Frame
    main_frame = Frame(Frame_list_hostel,bg=white)
    main_frame.pack(fill=BOTH, expand=1,)
    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas)
    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    # Layout of โรงแรม
    show_card(second_frame,result)
    show_setting(Frame_screening)
    showTab_menubar(Frame_menu)
    lockout()
    
def lockout():
    lockout_Frame.columnconfigure(0,weight=1)
    lockout_Frame.rowconfigure((0,1),weight=1)
    Label(lockout_Frame,text=' ยินดีต้อนรับ คุณ \n'+result2[3]+'  '+result2[4],image=user_login_img,compound=TOP,bg=white).grid(row=0,column=0)
    Button(lockout_Frame,text="Log Out",command=logoutclick,bg='red',fg='white').grid(row=1,column=0)

def revrseclick():
    Frame_hostel.grid_forget()
    search_hostels(root)

def logoutclick():
    global leftframe,loginframe,regisframe,upframe,downframe,mainloginFrame
    Frame_hostel.grid_forget()
    mainloginFrame = Frame(root)
    mainloginFrame.grid(row=0,sticky="news")
    mainloginFrame.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
    mainloginFrame.columnconfigure((0),weight=2)
    mainloginFrame.columnconfigure((1),weight=1)

    leftframe = Frame(mainloginFrame,bg='white') #กำหนดสี
    loginframe = Frame(mainloginFrame,bg='white',highlightthickness=10,highlightbackground="#EEEEEE")
    regisframe = Frame(mainloginFrame,bg='white',highlightthickness=10,highlightbackground="#EEEEEE")

    upframe = Frame(mainloginFrame,bg='#0194F3')
    downframe = Frame(mainloginFrame,bg='white')
    Volklogin()


# Layout of โรงแรม
def show_card(second_frame,result2):
    global thing
    for thing in range(len(result2)):
        hostel_content = Frame(second_frame, borderwidth=2, relief="groove",bg=white)
        hostel_content.grid(row=thing,column=0, pady=10, padx=10,ipadx=20,sticky='news')
        hostel_content.columnconfigure((1,2),weight=5)
        hostel_content.columnconfigure((0),weight=1)
        hostel_content.rowconfigure((0,1,2,3,4),weight=1)

        Frame_img = Frame(hostel_content,width=20,bg=white)#, borderwidth=2, relief="groove"
        Frame_img.grid(rowspan=5,column=0)
        Frame_img.rowconfigure(0,weight=0)
        
        #img
        Label(Frame_img,image=piclist[int(result2[thing][6])]).grid(row=0,sticky=SE)
        
        #Name hostel
        Label(hostel_content,text=result2[thing][1],bg=white).grid(row=0,column=1,sticky=W)
        # แสดงคะแนน ดาว ของโรงแรม
        Frame_star = Frame(hostel_content,bg=white)
        Frame_star.grid(row=1,column=1,sticky="w")
        Frame_star.columnconfigure((0,1,2,3,4),weight=1)
        Frame_star.columnconfigure((5),weight=15)
        Frame_star.rowconfigure((0),weight=1)
        for i in range(int(result2[thing][5])):#star
            Label(Frame_star,image=star,bg=white).grid(row=0,column=i,sticky=N)

        # แสดง service ต่างๆ
        input_fac = result2[thing][2]
        list_fac = input_fac.split(',')
        list_service = ['เครื่องปรับอากาศ','สระว่ายน้ำ','ร้านอาหาร','แผนกต้อนรับ 24 ชม.','ที่จอดรถ','ลิฟท์','Wifi']
        
        Frame_service = Frame(hostel_content,bg=white)
        Frame_service.grid(row=2,column=1,padx=5,sticky='w')
        Frame_service.columnconfigure((0,1,2,3,4),weight=1)
        Frame_service.rowconfigure((0,1),weight=1)

        row_service2 = Frame(Frame_service,bg=white)
        row_service2.grid(row=1,column=0,columnspan=4,sticky='news')
        row_service2.columnconfigure((0,1,2,3,4),weight=1)
        row_service2.rowconfigure((0),weight=1)
        for index,item in enumerate(list_fac):
            # ถ้า service มากกว่า 4 ตัว จะใส่ลง row ถัดไป
            if index >= 4:
                row_service2.grid(row=1,columnspan=4,sticky=W)
                row_service2.columnconfigure((0,1,2,3,4),weight=1)
                Label(row_service2,text=list_service[int(item)-1],font=("Arial", 12), borderwidth=2, relief="groove",bg=white).grid(row=0,column=index-4,pady=5,sticky=NW,padx=3,ipadx=5,ipady=5)
            else:
                Label(Frame_service,text=list_service[int(item)-1],font=("Arial", 12), borderwidth=2, relief="groove",bg=white).grid(row=0,column=index,pady=5,sticky=N,padx=3,ipadx=5,ipady=5)


        #Frame review and price
        Frame_3 = Frame(hostel_content,bg=white)#, borderwidth=2, relief="groove"
        Frame_3.grid(rowspan=5,row=0,column=2,sticky="news")
        Frame_3.rowconfigure((0,1),weight=1)
        Frame_3.columnconfigure((0,1),weight=1)

        #review
        # Label(Frame_3,text="ดีมาก 7.7 คะแนน",bg=white).grid(row=0,columnspan=2,sticky=NE,pady=10,padx=30)
        # Label(Frame_3,text="1,000 reviews",font=("Arial", 12),bg=white).grid(row=0,columnspan=2,sticky=NE,pady=40,padx=30)

        Label(Frame_3,bg=white,text=''' 
''').grid(row=0,columnspan=2,sticky=NE,pady=10,padx=30)

        #price
        price = Label(Frame_3,text=f'{result[thing][3]} ฿',bg=white)
        price.grid(row=0,columnspan=2,sticky=SE,padx=30)
        Button(Frame_3,text="เลือกห้องพัก",bg='#FF5E1F',fg="white",command=aaaa[thing]).grid(row=1,columnspan=2,sticky=NE,padx=30,pady=10)
    #ใส่ Label ข้างล่างให้มีพื้นที่ว่าง ตรงบรรทัดสุดท้าย
    if thing == len(result2)-1 :
        Label(second_frame,text='\n\n').grid(row=thing+1,column=0)

def search(a):
    global result
    sql = "select * from HotelData Where SID=?;"
    cursor.execute(sql,[a])
    result = cursor.fetchone()
    print(result)
    Review()

s = []
def a1():
    global result
    search(result[0][8])
def a2():
    global result
    search(result[1][8])
def a3():
    # a=2
    # s[2]
    #search(a)
    global result
    search(result[2][8])
def a4():
    global result
    search(result[3][8])
def a5():
    global result
    search(result[4][8])
def a6():
    global result
    search(result[5][8])
def a7():
    global result
    search(result[6][8])
def a8():
    global result
    search(result[7][8])
def a9():
    global result
    search(result[8][8])
def a10():
    global result
    search(result[9][8])
def a11():
    global result
    search(result[10][8])
def a12():
    global result
    search(result[11][8])
def a13():
    global result
    search(result[12][8])
def a14():
    global result
    search(result[13][8])
def a15():
    global result
    search(result[14][8])
def a16():
    global result
    search(result[15][8])
def a17(a):
    global result
    search(result[16][8])
def a18():
    global result
    search(result[17][8])
def a19():
    global result
    search(result[18][8])
def a20():
    global result
    search(result[19][8])

def show_setting(Frame_screening):
    global minsc,maxsc,ch1,ch2,ch3,ch4,ch5
    #setting Frame
    Frame_screening.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)
    Frame_screening.rowconfigure((10),weight=10)
    Frame_screening.columnconfigure((0,1),weight=1)

    Label(Frame_screening,text="ราคา/ห้อง/คืน",bg=white).grid(row=1,columnspan=2)

    #min
    Entry(Frame_screening,width=10,borderwidth=2, relief="groove",textvariable=mintext).grid(row=4,column=0,sticky=N)
    minsc = Scale(Frame_screening,from_=0,to=1000,orient='horizontal',bg='darkcyan',fg="white",length=100,variable=mintext)
    minsc.grid(row=2,column=0,sticky=S)
    Label(Frame_screening,text="min",bg=white).grid(row=3,column=0,sticky=S)
    #max
    Entry(Frame_screening,width=10,borderwidth=2, relief="groove",textvariable=maxtext).grid(row=4,column=1,sticky=N)
    maxsc = Scale(Frame_screening,from_=0,to=3000,orient='horizontal',bg='#b70994',fg="white",length=100,variable=maxtext)
    maxsc.grid(row=2,column=1,sticky=S)
    Label(Frame_screening,text="max",bg=white).grid(row=3,column=1,sticky=S)

    # เลือก Checkbutton stars
    for i in range(5):
        Frame_star = Frame(Frame_screening,bg=white)
        Frame_star.grid(row=i+6,columnspan=2,sticky=NW,pady=10,padx=60)
        Frame_star.rowconfigure(0,weight=1)
        Frame_star.columnconfigure((0,1,2,3,4,5,6),weight=1)
        for time_star in range(i+1): #start  stop  step 
            Label(Frame_star,image=star,bg=white).grid(row=0,column=time_star)
    Button(Frame_screening,text="Search",command=starSearch).grid(row=11,columnspan=2,sticky=N)
    ch1 = Checkbutton(Frame_screening,variable=spy1,bg=white)
    ch2 = Checkbutton(Frame_screening,variable=spy2,bg=white)
    ch3 = Checkbutton(Frame_screening,variable=spy3,bg=white)
    ch4 = Checkbutton(Frame_screening,variable=spy4,bg=white)
    ch5 = Checkbutton(Frame_screening,variable=spy5,bg=white)
    ch1.grid(row=6,column=0,sticky=NW,padx=20)
    ch2.grid(row=7,column=0,sticky=NW,padx=20)
    ch3.grid(row=8,column=0,sticky=NW,padx=20)
    ch4.grid(row=9,column=0,sticky=NW,padx=20)
    ch5.grid(row=10,column=0,sticky=NW,padx=20)
    Button(Frame_screening,text="Search",command=starSearch,fg="black").grid(row=11,columnspan=2,sticky=N)

####################

def showTab_menubar(Frame_menu):
    global people,room,name
    Frame_menu.rowconfigure(0,weight=1)
    Frame_menu.columnconfigure((0,1,2,3,4,5),weight=1)

    name = Entry(Frame_menu,width=40)
    name.grid(row=0,columnspan=2,column=0,sticky=E)
    Button(Frame_menu,command=revrseclick,image=img3).grid(row=0,column=0,sticky=W,padx=5)

    Button(Frame_menu,image=search_icon,width=60,command=nameSearch).grid(row=0,column=3,sticky=W)

    Label(Frame_menu,text="ผู้ใหญ่ :",bg="#0194F3").grid(row=0,column=3,sticky=E,padx=100)
    people = ttk.Combobox(Frame_menu,values=['1','2','3','4','5'],width=5,justify='center')
    people.set(Room_ui1.get())
    people.grid(row=0,column=3,sticky=E,padx=20)
    
    Label(Frame_menu,text="ห้อง :",bg="#0194F3").grid(row=0,column=4,sticky=W)
    room = ttk.Combobox(Frame_menu,values=['1','2','3','4','5'],width=5,justify='center')
    room.set(Room_ui2.get())
    room.grid(row=0,column=4,sticky=W,padx=60)

    Button(Frame_menu,image=search_icon,width=60,command=peopleSearch).grid(row=0,column=4,sticky=E)

def minMaxSearch():
    global result
    sql = "select * from HotelData where Price between ? and ? And DateIn NOT between ? and ? AND DateOut NOT between ? and ?;"
    cursor.execute(sql,[minsc.get(),maxsc.get(),setDate_in,setDate_out,setDate_in,setDate_out])
    result = cursor.fetchall()
    if result:
        Frame_list_hostel.grid_forget()
        main_frame.grid_forget()
        second_frame.grid_forget()
        listhotel()
    else:
        messagebox.showwarning("ระบบ:","ไม่มีราคาตามที่กำหนดไว้")

def peopleSearch():
    global result
    sql = "select * from HotelData where Guests>=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ?;"
    cursor.execute(sql,[int(people.get())/int(room.get()),setDate_in,setDate_out,setDate_in,setDate_out])
    result = cursor.fetchall()
    if result:
        Frame_list_hostel.grid_forget()
        main_frame.grid_forget()
        second_frame.grid_forget()
        listhotel()
    else:
        messagebox.showwarning("ระบบ:","ไม่มีห้องที่ตรงกับจำนวนคน")

def nameSearch():
    global result
    sql = "select * from HotelData where Name=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ?;"
    cursor.execute(sql,[name.get(),setDate_in,setDate_out,setDate_in,setDate_out])
    result = cursor.fetchall()
    if result:
        Frame_list_hostel.grid_forget()
        main_frame.grid_forget()
        second_frame.grid_forget()
        listhotel()
    elif name.get() == "":
        sql = "select * from HotelData where DateIn NOT between ? and ? AND DateOut NOT between ? and ?;"
        cursor.execute(sql,[setDate_in,setDate_out,setDate_in,setDate_out])
        result = cursor.fetchall()
        listhotel()
    else:
        messagebox.showwarning("ระบบ:","ไม่มีห้องที่ตรงกับชื่อ")
        name.select_range(0,END)
        name.focus_force()

def starSearch():
    global result
    conut = 0
    if spy1.get() == 1:
        conut += 1
    if spy2.get() == 1:
        conut += 1
    if spy3.get() == 1:
        conut += 1
    if spy4.get() == 1:
        conut += 1
    if spy5.get() == 1:
        conut += 1

    if conut == 1:
        if spy1.get():
            # sql = "select * from HotelData where Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            sql = "select * from HotelData where Star=? and Price between ? and ?;"
            cursor.execute(sql,[1,minsc.get(),maxsc.get()])
        elif spy2.get() == 1:
            sql = "select * from HotelData where Star=? And Price between ? and ?;"
            cursor.execute(sql,[2,minsc.get(),maxsc.get()])
        elif spy3.get() == 1:
            sql = "select * from HotelData where Star=? And Price between ? and ?;"
            cursor.execute(sql,[3,minsc.get(),maxsc.get()])
        elif spy4.get() == 1:
            sql = "select * from HotelData where Star=? And Price between ? and ?;"
            cursor.execute(sql,[4,minsc.get(),maxsc.get()])
        elif spy5.get() == 1:
            sql = "select * from HotelData where Star=? And Price between ? and ?;"
            cursor.execute(sql,[5,minsc.get(),maxsc.get()])
    elif conut == 2:
        if spy1.get() == 1 and spy2.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[1,2,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy1.get() == 1 and spy3.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[1,3,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy1.get() == 1 and spy4.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[1,4,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy1.get() == 1 and spy5.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[1,5,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy2.get() == 2 and spy3.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[2,3,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy2.get() == 1 and spy4.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[2,4,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy2.get() == 1 and spy5.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[2,5,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy3.get() == 1 and spy4.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[3,4,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy3.get() == 1 and spy5.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[3,5,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy4.get() == 1 and spy5.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[4,5,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
    elif conut == 3:
        if spy1.get() == 1 and spy2.get() == 1 and spy3.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[1,2,3,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy1.get() == 1 and spy2.get() == 1 and spy4.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[1,2,4,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy1.get() == 1 and spy2.get() == 1 and spy5.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[1,2,5,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy1.get() == 1 and spy3.get() == 1 and spy4.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[1,3,4,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy1.get() == 1 and spy3.get() == 1 and spy5.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[1,3,5,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy1.get() == 1 and spy4.get() == 1 and spy5.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[1,4,5,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy2.get() == 1 and spy3.get() == 1 and spy4.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[2,3,4,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy2.get() == 1 and spy3.get() == 1 and spy5.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[2,3,5,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy2.get() == 1 and spy4.get() == 1 and spy5.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[2,4,5,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy3.get() == 1 and spy4.get() == 1 and spy5.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[3,4,5,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
    elif conut == 4:
        if spy1.get() == 1 and spy2.get() == 1 and spy3.get() == 1 and spy4.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? or Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[1,2,3,4,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy1.get() == 1 and spy2.get() == 1 and spy3.get() == 1 and spy5.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? or Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[1,2,3,5,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy1.get() == 1 and spy3.get() == 1 and spy4.get() == 1 and spy5.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? or Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[1,3,4,5,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
        elif spy2.get() == 1 and spy3.get() == 1 and spy4.get() == 1 and spy5.get() == 1:
            sql = "select * from HotelData where Star=? or Star=? or Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
            cursor.execute(sql,[2,3,4,5,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
    elif conut == 5:
        sql = "select * from HotelData where Star=? or Star=? or Star=? or Star=? or Star=? And DateIn NOT between ? and ? AND DateOut NOT between ? and ? And Price between ? and ?;"
        cursor.execute(sql,[1,2,3,4,5,setDate_in,setDate_out,setDate_in,setDate_out,minsc.get(),maxsc.get()])
    elif conut == 0:
        sql = "select * from HotelData where Price between ? and ? And DateIn NOT between ? and ? AND DateOut NOT between ? and ?;"
        cursor.execute(sql,[minsc.get(),maxsc.get(),setDate_in,setDate_out,setDate_in,setDate_out])
    result = cursor.fetchall()
    if result:
        print(result)
        Frame_list_hostel.grid_forget()
        main_frame.grid_forget()
        second_frame.grid_forget()
        listhotel()
    else:
        messagebox.showwarning("ระบบ:","ไม่มีห้องที่ตรงกับความต้องการ")
        sql = 'SELECT * from HotelData Where DateIn NOT between ? and ? AND DateOut NOT between ? and ?;'
        cursor.execute(sql,[setDate_in,setDate_out,setDate_in,setDate_out])
        result = cursor.fetchall()
        Frame_list_hostel.grid_forget()
        main_frame.grid_forget()
        second_frame.grid_forget()
        listhotel()



def delete_FrameReviews():
    global result,mainFrame_checkout
    #Layout_reviews()
    mainFrame_checkout = Frame(root)
    Review_Frame.grid_forget()
    menu_review_Frame.grid_forget()
    showHostel_review_Frame.grid_forget()
    comment_review_Frame.grid_forget()
    mainFrame_checkout.grid_forget()

    #Layout comment review ขวา-ล่าง
    scrollbar_review.grid_forget()
    second_frame2.grid_forget()
    average.grid_forget()
    comment.grid_forget()

    #Layout Show data of hostel (ด้านซ้าย กลาง)
    Frame_star.grid_forget()
    Frame_service.grid_forget()
    row_service2.grid_forget()
    sql = 'SELECT * from HotelData Where DateIn NOT between ? and ? AND DateOut NOT between ? and ?;'
    cursor.execute(sql,[setDate_in,setDate_out,setDate_in,setDate_out])
    result = cursor.fetchall()
    print(result)
    Frame_list_hostel.grid_forget()
    main_frame.grid_forget()
    second_frame.grid_forget()
    listhotel()

def delete_FrameReviews3():
    global result
    messagebox.showinfo("ระบบ:","การจองเสร็จสิ้น")
    #Layout_reviews()
    Review_Frame.grid_forget()
    menu_review_Frame.grid_forget()
    showHostel_review_Frame.grid_forget()
    comment_review_Frame.grid_forget()
    mainFrame_checkout.grid_forget()

    #Layout comment review ขวา-ล่าง
    scrollbar_review.grid_forget()
    second_frame2.grid_forget()
    average.grid_forget()

    #Layout Show data of hostel (ด้านซ้าย กลาง)
    Frame_star.grid_forget()
    Frame_service.grid_forget()
    row_service2.grid_forget()
    sql = 'insert into History (IDHotel,IDUser,DateIn,DateOut) values (?,?,?,?);'
    cursor.execute(sql,[result[0],result2[0],setDate_in,setDate_out])
    conn.commit()
    sql = 'SELECT * from HotelData Where DateIn NOT between ? and ? AND DateOut NOT between ? and ?;'
    cursor.execute(sql,[setDate_in,setDate_out,setDate_in,setDate_out])
    result = cursor.fetchall()
    Frame_list_hostel.grid_forget()
    main_frame.grid_forget()
    second_frame.grid_forget()
    listhotel()

def delete_FrameReviews2():
    global result
    #Layout_reviews()
    Review_Frame.grid_forget()
    menu_review_Frame.grid_forget()
    showHostel_review_Frame.grid_forget()
    comment_review_Frame.grid_forget()
    mainFrame_checkout.grid_forget()

    #Layout comment review ขวา-ล่าง
    scrollbar_review.grid_forget()
    second_frame2.grid_forget()
    average.grid_forget()
    comment.grid_forget()

    #Layout Show data of hostel (ด้านซ้าย กลาง)
    Frame_star.grid_forget()
    Frame_service.grid_forget()
    row_service2.grid_forget()
    sql = 'SELECT * from HotelData Where DateIn NOT between ? and ? AND DateOut NOT between ? and ?;'
    cursor.execute(sql,[setDate_in,setDate_out,setDate_in,setDate_out])
    result = cursor.fetchall()
    Frame_list_hostel.grid_forget()
    main_frame.grid_forget()
    second_frame.grid_forget()
    listhotel()

def Layout_reviews():
    global Review_Frame, menu_review_Frame, showHostel_review_Frame, comment_review_Frame
    #Layout เต็มหน้าจอ
    Review_Frame = Frame(root)
    Review_Frame.grid(row=0,column=0,sticky='news')
    Review_Frame.rowconfigure(0,weight=1)
    Review_Frame.rowconfigure(1,weight=10)
    Review_Frame.columnconfigure((0),weight=1)
    Review_Frame.columnconfigure((1),weight=3)

    #Layout Menu (บนสุด)
    menu_review_Frame = Frame(Review_Frame,bg="#0194F3")
    menu_review_Frame.grid(row=0,columnspan=2,sticky='news')
    menu_review_Frame.rowconfigure(0,weight=1)
    menu_review_Frame.columnconfigure(0,weight=1)

    #Layout Show data of hostel (ด้านซ้าย กลาง)
    showHostel_review_Frame = Frame(Review_Frame)
    showHostel_review_Frame.grid(row=1,column=0,sticky='nw',pady=10,padx=20,ipady=20)
    showHostel_review_Frame.rowconfigure((0,1,2,3,7),weight=1)
    showHostel_review_Frame.rowconfigure((4,5,6),weight=2)
    #หน้าว่าง
    showHostel_review_Frame.rowconfigure((8),weight=3)
    #column
    showHostel_review_Frame.columnconfigure((0),weight=3)
    showHostel_review_Frame.columnconfigure((1),weight=1)

    #Layout comment
    comment_review_Frame = Frame(Review_Frame)
    comment_review_Frame.grid(row=1,column=1,sticky='news')
    comment_review_Frame.columnconfigure(0,weight=1)
    comment_review_Frame.rowconfigure(0,weight=1)

#Layout Menu (บนสุด)
def menu_review():
    Button(menu_review_Frame,text="กลับไปหน้าหลัก",bg='white',command=delete_FrameReviews).grid(row=0,sticky=W,ipadx=10,padx=20,ipady=5,pady=10)
    #tap login
    Label(menu_review_Frame,text=' ยินดีต้อนรับ คุณ   '+result2[3]+'  '+result2[4],image=user_login_img,compound='left',bg="#0194F3",fg="white").grid(row=0,sticky=E,ipadx=10,padx=160,ipady=3)


#Layout comment review ขวา-ล่าง
def reviews_scrollbar():
    global scrollbar_review,second_frame2,average,comment
    # Create A Main Frame
    scrollbar_review = Frame(comment_review_Frame)
    scrollbar_review.pack(fill=BOTH, expand=1,)
    # Create A Canvas
    my_canvas2 = Canvas(scrollbar_review)
    my_canvas2.pack(side=LEFT, fill=BOTH, expand=1)
    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(scrollbar_review, orient=VERTICAL, command=my_canvas2.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    # Configure The Canvas
    my_canvas2.configure(yscrollcommand=my_scrollbar.set)
    my_canvas2.bind('<Configure>', lambda e: my_canvas2.configure(scrollregion = my_canvas2.bbox("all")))
    # Create ANOTHER Frame INSIDE the Canvas
    second_frame2 = Frame(my_canvas2)
    # Add that New frame To a Window In The Canvas
    my_canvas2.create_window((0,0), window=second_frame2, anchor="nw")

    #หน้าสรุปจำนวนคนรีวิว
    average = Frame(second_frame2, borderwidth=2, relief="groove")
    average.grid(row=0,column=0, pady=5,sticky='news')
    average.rowconfigure((0,1,2,3,4),weight=1)
    average.columnconfigure((0,1,2),weight=1)

###########################################################################################################
    # คะแนนเฉลี่ย 
    Label(average,text=str(sum(total_list_star) / len(total_list_star)),font='areal 64 bold').grid(rowspan=3,column=0)
    # จำนวนคนรีวิว
    Label(average,text='ทั้งหมด '+str(len(total_list_star))+' ความคิดเห็น',font='areal 12').grid(row=3,column=0,padx=20)

    number = ['1','2','3','4','5']
    point = [10,2,1,1,1]
    for i in range(5):
        # number
        Label(average,text=number[i]).grid(row=i,column=1,sticky=E)
        # หลอดพลัง พื้นหลังสีเทา
        Label(average,width=15,bg='gray').grid(row=i,column=2,sticky=W,pady=10,padx=20)
        # คะแนนหลอดพลัง สีเขียว
        Label(average,width=int(find_energy(i+1) // 6.6666),bg='green').grid(row=i,column=2,sticky=W,pady=10,padx=20)
###########################################################################################################



    # รีวิวทั้งหมด
    print(result[0])
    global result3
    sql = 'select * from Review where IDHotel=?;'
    cursor.execute(sql,[result[0]])
    result3 = cursor.fetchall()
    print(result3)
    for thing in range(len(result3)):
        rowComment = thing + 1

        comment = Frame(second_frame2, borderwidth=2, relief="groove")
        comment.grid(row=rowComment,column=0,sticky='news',pady=5)
        comment.rowconfigure((0,1,2,3,4),weight=1)
        comment.columnconfigure(0,weight=3)
        comment.columnconfigure(1,weight=1)

        #day
        Label(comment,text="14 JAN 2023",font='areal 12').grid(row=1,column=1,sticky=E,ipadx=20,pady=10)
        #Name
        sql = 'select * from User where IDUser=?;'
        cursor.execute(sql,[result3[thing][1]])
        result4 = cursor.fetchone()
        Label(comment,text=result4[3]+'  '+result4[4]).grid(row=1,column=0,sticky=W,ipadx=20,pady=10)
        #Point
        Label(comment,text=str(result3[thing][2])+' / 5',font='areal 12',bg='lightgreen').grid(row=2,column=0,sticky=W,ipadx=10,padx=20)
        #comment
        b = ''
        textcom = str(result3[thing][3])
        for i in range(len(textcom)):
            b += textcom[i]
            if i % 50 == 0 and i != 0:
                b += '\n'
            
        Label(comment,text=b,font='areal 12',justify=LEFT).grid(row=3,column=0,sticky=W,ipadx=20,pady=10)

        # พื้นที่หน้าว่างด้านล่าง
        if(thing == 14):
            Label(second_frame2,text='\n\n').grid(row=rowComment+1,column=0, pady=5,sticky=NW)
            

#Layout Show data of hostel (ด้านซ้าย กลาง)
def main_hostel_review():
    global Frame_star,Frame_service,row_service2,find_energy,total_list_star
    #name hostel
    Label(showHostel_review_Frame,text=result[1],font='areal 24 bold').grid(row=1,columnspan=2,sticky=W)
    
    #star
    Frame_star = Frame(showHostel_review_Frame)
    Frame_star.grid(row=2,column=0,sticky="W")
    Frame_star.columnconfigure((0,1,2,3,4),weight=1)
    Frame_star.columnconfigure((5),weight=15)
    Frame_star.rowconfigure((0),weight=1)
    for i in range(5):#star
        Label(Frame_star,image=star).grid(row=0,column=i,sticky=N)
    
    #address
    c = ''
    name_address = result[4]
    for i in range(len(name_address)):
        c += name_address[i]
        if i % 80 == 0 and i != 0:
            c += '\n'

    Label(showHostel_review_Frame,text=f' {c}',font='areal 12',image=placeholder,compound='left',justify=LEFT).grid(row=3,columnspan=2,sticky=W)

    #img
    Label(showHostel_review_Frame,image=piclist[int(result[6])+17], borderwidth=2, relief="groove").grid(row=4,columnspan=2,pady=10)

    #service
    # แสดง service ต่างๆ
    input_fac = result[2]
    list_fac = input_fac.split(',')
    list_service = ['เครื่องปรับอากาศ','สระว่ายน้ำ','ร้านอาหาร','แผนกต้อนรับ 24 ชม.','ที่จอดรถ','ลิฟท์','Wifi']
    
    Frame_service = Frame(showHostel_review_Frame)
    Frame_service.grid(row=5,column=0,padx=5)
    Frame_service.columnconfigure((0,1),weight=1)
    Frame_service.columnconfigure((2,3,4),weight=2)
    Frame_service.rowconfigure((0,1,2),weight=1)

    row_service2 = Frame(Frame_service)
    row_service2.grid(row=1,column=0,columnspan=4)
    row_service2.columnconfigure((0,1,2,3,4),weight=1)
    row_service2.rowconfigure((0),weight=1)
    for index,item in enumerate(list_fac):
        # ถ้า service มากกว่า 4 ตัว จะใส่ลง row ถัดไป
        if index >= 4:
            row_service2.grid(row=1,columnspan=4,sticky=W)
            row_service2.columnconfigure((0,1,2,3,4),weight=1)
            Label(row_service2,text=list_service[int(item)-1],font=("Arial", 12), borderwidth=2, relief="groove").grid(row=1,column=index-4,sticky=NW,padx=3,ipadx=5,ipady=5)
        else:
            Label(Frame_service,text=list_service[int(item)-1],font=("Arial", 12), borderwidth=2, relief="groove").grid(row=0,column=index,pady=5,sticky=N,padx=3,ipadx=5,ipady=5)
    

    #ราคา
    lprice = float(room.get()) * float(result[3])
    momBt = Frame(showHostel_review_Frame)
    momBt.grid(row=7,columnspan=5,sticky='news',pady=18,ipady=5,)
    momBt.rowconfigure(0,weight=1)
    momBt.columnconfigure(0,weight=1)

    childBt = Frame(momBt)
    childBt.grid(row=0,column=0,sticky=E)
    childBt.rowconfigure(0,weight=1)
    childBt.columnconfigure((0,1,2),weight=1)

    Label(childBt,text=str(result[3])+' ฿',font=("Arial 20 bold")).grid(row=0,column=0)
    # Label(Frame_service,text=str(result[3])+' ฿',font=("Arial 20 bold")).grid(row=3,column=3,sticky=E,ipady=5)
    #button ปุ่มเข้าเลือกห้องพัก

    Button(childBt,text='จองห้องพัก',bg='#FF5E1F',fg="white",command=check_outNut).grid(row=0,column=1,padx=15)
    Button(childBt,image=img4,bg='white',command=treeview0).grid(row=0,column=2)


    total_list_star = []

    sql = 'select * from Review where IDHotel=?;'
    cursor.execute(sql,[result[0]])
    result3 = cursor.fetchall()

    print(result3)

    for st in range(len(result3)):
        total_list_star.append(int(result3[st][2]))


    print(f'total_list_star = {sum(total_list_star)}')
    print(f'average_star = {sum(total_list_star) / len(total_list_star)}')
    print(f'ทั้งหมด {len(total_list_star)} ความคิดเห็น')

    star1_list = total_list_star.count(4)

    def find_energy(number):
        return total_list_star.count(number) / len(total_list_star) * 100


    # width max = 15
    print(f'1ดาว = {"%.1f"%(find_energy(1))} %  ; width = {find_energy(1) // 6.6666}')
    print(f'1ดาว = {"%.1f"%(find_energy(2))} %  ; width = {find_energy(2) // 6.6666}')
    print(f'1ดาว = {"%.1f"%(find_energy(3))} %  ; width = {find_energy(3) // 6.6666}')
    print(f'1ดาว = {"%.1f"%(find_energy(4))} %  ; width = {find_energy(4) // 6.6666}')
    print(f'1ดาว = {"%.1f"%(find_energy(5))} %  ; width = {find_energy(5) // 6.6666}')

#########################################  Check Out  ##############################################################

def check_outNut():
    global mainFrame_checkout
    Review_Frame.grid_forget()
    mainFrame_checkout = Frame(root)
    print(result)
    FrameLogoBu = Frame(mainFrame_checkout,bg='#0194f3')
    # กำหนด layout เป็น Frameหลัก คุมทั้งหน้าจอ
    mainFrame_checkout.grid(row=0,column=0,sticky='news')
    mainFrame_checkout.rowconfigure((0),weight=3)
    mainFrame_checkout.rowconfigure((1,2,3,4,5,6,7,8,9,10,11),weight=1)
    mainFrame_checkout.columnconfigure((0,1),weight=1)

    # Fram Logo บนสุด
    FrameLogoBu.grid(row=0,columnspan=2,sticky='news')
    FrameLogoBu.rowconfigure(0,weight=1)
    FrameLogoBu.columnconfigure(0,weight=1)


    # FrameLogoBu_detail = Frame(FrameLogoBu)
    # FrameLogoBu_detail.grid(row=0,columnspan=2)
    # FrameLogoBu_detail.rowconfigure(0,weight=1)
    # FrameLogoBu_detail.columnconfigure(0,weight=1)
    #img
    Label(FrameLogoBu,image=img1,bg='#0194f3').grid(row=0,sticky=W)
    Label(FrameLogoBu,text='BURangsit',bg='#0194f3',font="Calibri 32 bold").grid(row=0,sticky=E,padx=25)

    padX_left = 200
    padX_right = 200
    #infomation 
    Label(mainFrame_checkout,text=f'Thaks {result2[3] } {result2[4]}').grid(row=1,columnspan=2,sticky=SW,padx=padX_left,pady=10)
    Label(mainFrame_checkout,text='Your booking in '+result[1]+ ' is confirmed',font="Calibri 20 bold").grid(row=2,columnspan=2,sticky=W,padx=padX_left)
    Label(mainFrame_checkout,text=result[1],font="Calibri 20 bold",fg='blue').grid(row=3,columnspan=2,sticky=W,padx=padX_left)
    #img
    Label(mainFrame_checkout,image=piclist[int(result[6])]).grid(row=4,columnspan=2,pady=20,sticky=W,padx=padX_left)

    #detel
    Label(mainFrame_checkout,text='Your reservation').grid(row=5,columnspan=2,sticky=W,padx=padX_left)
    Label(mainFrame_checkout,text=f'{day} night, {room.get()} dormitory bed').grid(row=5,column=1,sticky=E,padx=padX_right)
    
    Label(mainFrame_checkout,text='check-in').grid(row=6,columnspan=2,sticky=W,padx=padX_left)
    Label(mainFrame_checkout,text=setDate_in).grid(row=6,columnspan=2,sticky=E,padx=padX_right)
    
    Label(mainFrame_checkout,text='Check out').grid(row=7,columnspan=2,sticky=W,padx=padX_left)
    Label(mainFrame_checkout,text=setDate_out).grid(row=7,columnspan=2,sticky=E,padx=padX_right)
    
    Label(mainFrame_checkout,text='Prepayment').grid(row=8,columnspan=2,sticky=W,padx=padX_left)
    Label(mainFrame_checkout,text='You will charged a prepayment of the total price at any time').grid(row=8,columnspan=2,sticky=E,padx=padX_right)

    Button(mainFrame_checkout,text='Cancel',bg='white',fg='Black',command=delete_FrameReviews2).grid(row=9,column=1,padx=50,pady=20,sticky=SW)
    Button(mainFrame_checkout,text='Confirm your booking',bg='orange',fg='white',command=delete_FrameReviews3).grid(row=9,column=1,pady=20,padx=150,sticky=SW)

    Label(mainFrame_checkout,text='').grid(row=10)
    Label(mainFrame_checkout,text='').grid(row=11)












################################# Tree View ###################################################################################











def treeview0() :
    global result4,result5,comment_entry,star_comment,comment_mainFrame
    Review_Frame.grid_forget()
    Frame_hostel.grid_forget()
    comment_mainFrame = Frame(root,bg='#0194f3')
    comment_mainFrame.grid(row=0,column=0,sticky='news')
    comment_mainFrame.rowconfigure((0),weight=2)
    comment_mainFrame.rowconfigure((1,2,3,4,5),weight=1)
    comment_mainFrame.columnconfigure((0,1,2),weight=1)

    Button(comment_mainFrame,image=img3,command=backtomain).grid(row=0,columnspan=3,sticky=NW,padx=10,pady=20)
    Label(comment_mainFrame,text="เลือกรีวิวห้องพักของคุณ",bg=bg_comment,font="Calibri 24 bold",fg=fg_comment).grid(row=0,columnspan=3,pady=20,padx=20,sticky=N)
    ################ Treeview
    global mytree,comment_entry,name_comment
    mytree= ttk.Treeview(comment_mainFrame,columns= ("col1","col2","col3") )
    mytree.grid(row=0,columnspan=3,pady=20,padx=20,sticky=S)
    mytree.heading("#0",text="Name")
    mytree.heading("col1",text="Username")
    mytree.heading("col2",text="Check-in")
    mytree.heading("col3",text="Ceck-out")

    mytree.column("#0", width=0, minwidth=0)
    mytree.column("col1", width=500, minwidth=200)
    mytree.column("col2", width=150, minwidth=100) 
    mytree.column("col3", width=150, minwidth=100)

    sql = 'select * from History where IDHotel=? and IDUser=?;'
    cursor.execute(sql,[result3[0][0],result2[0]])
    result4 = cursor.fetchall()
    print(result4)
    for i in range(len(result4)):
       sql = 'select * from HotelData where IDHotel=?;'
       cursor.execute(sql,[result4[0][0]])
       result5 = cursor.fetchone()
       data = (result5[1],result4[i][3],result4[i][4])
       mytree.insert('','end',values=data)


    ################

    #name
    #name_comment = Label(comment_mainFrame,bg=bg_comment,font="Calibri 20 bold",fg=fg_comment,text=ntbasic)#,textvariable=ntbasic
    # name_comment.grid(row=1,columnspan=3)

    #ให้คะแนน
    Label(comment_mainFrame,text="ให้คะแนนที่พักของคุณ: ",bg=bg_comment,fg=fg_comment).grid(row=2,column=0,pady=20,padx=20,sticky=E)
    star_comment = ttk.Combobox(comment_mainFrame,values=['1','2','3','4','5'],width=5)
    star_comment.set('1')
    star_comment.grid(row=2,column=1,sticky=W)
    Label(comment_mainFrame,text="ดาว",bg=bg_comment,fg=fg_comment).grid(row=2,column=1,columnspan=2,sticky=W,padx=100)

    #input entry
    Label(comment_mainFrame,text="รีวิวห้องพัก: ",bg=bg_comment,fg=fg_comment).grid(row=3,column=0,sticky=E,padx=10)
    comment_entry = Entry(comment_mainFrame,width=50, borderwidth=2, relief="groove",font="Calibri 16")
    comment_entry.grid(row=3,columnspan=2,column=1,sticky=W)

    Button(comment_mainFrame,width=20,text='Edit',command=updateComment).grid(row=4,column=1)
    Button(comment_mainFrame,width=20,text='Delete',command=deleteComment).grid(row=4,column=2,sticky=W)
    mytree.bind('<Double-1>',treeviewclick)

def treeviewclick(e) :
    global clickdata,ntbasic,name_comment
    selectrow = mytree.selection() #Mytree selection ->  ('I002',)
    print("Mytree selection -> ",selectrow)
    clickdata = mytree.item(mytree.selection(),'values')
    print("Clickdata",clickdata)
    # setEntry = [enAdd,enUpdate,enDelete,enClear]
    ntbasic = clickdata[0]
    name_comment = Label(comment_mainFrame,bg=bg_comment,font="Calibri 20 bold",fg=fg_comment,text=ntbasic)
    name_comment.grid(row=1,columnspan=3)
    name_comment['text'] = clickdata[0]
    sql = 'select * from Review where IDHotel=? and IDUser=?'
    print(result2)
    print(result3)
    cursor.execute(sql,[result3[0][0],result2[0]])
    check = cursor.fetchone()
    if check:
        comment_entry.delete(0,END)
        comment_entry.insert(0,check[3])
    else:
        Button(comment_mainFrame,width=20,text='add comment',command=addComment).grid(row=4,column=0,sticky=E)


def addComment():
    if(comment_entry.get() == ''):
        messagebox.showinfo("ระบบ","กรุณากรอก comment")
    else: 
        sql = '''
        INSERT INTO Review (IDHotel, IDUser, Star, Text)
        VALUES (?,?,?,?);
        '''
        cursor.execute(sql, [result3[0][0],result2[0],star_comment.get(),comment_entry.get()] )
        conn.commit()
        messagebox.showinfo("ระบบ","บันทึกความคิดเห็นเสร็จแล้ว")
        comment_entry.delete(0,END)
    resetTreeview()


    
def updateComment():
    sql = 'update Review set Text=? , Star=? where IDHotel=? and IDUser=?;'
    cursor.execute(sql,[comment_entry.get(),star_comment.get(),result3[0][0],result2[0]])
    conn.commit()
    messagebox.showinfo("ระบบ","อัปเดตความคิดเห็นเสร็จแล้ว")
    comment_entry.delete(0,END)
    resetTreeview()


def deleteComment():
    sql = 'select * from Review where IDHotel=? and IDUser=?'
    cursor.execute(sql,[result3[0][0],result2[0]])
    testresult = cursor.fetchall()
    if testresult:
        sql = 'delete from Review where IDHotel=? and IDUser=?;'
        cursor.execute(sql,[result3[0][0],result2[0]])
        messagebox.askquestion('ระบบ','คุณยืนยันที่จะลบความคิดเห็นทิ้งหรือไม่')
        conn.commit()
        messagebox.showinfo('ระบบ','ลบความคิดเห็นเสร็จสิ้น')
    else:
        messagebox.showwarning('ระบบ','คุณยังไม่ได้แสดงความคิดเห็นกับโรงแรมนี้')
    resetTreeview()


def resetTreeview():
    comment_mainFrame.grid_forget()
    treeview0()

def backtomain():
    global result
    comment_mainFrame.grid_forget()
    sql = 'SELECT * from HotelData Where DateIn NOT between ? and ? AND DateOut NOT between ? and ?;'
    cursor.execute(sql,[setDate_in,setDate_out,setDate_in,setDate_out])
    result = cursor.fetchall()
    show_hostels(root)







###############################################################################################################################################################################################################################################





    
    
# login 
def Volklogin():
    leftlayout()
    loginlayout()

#Framesearch
def Nutsearch():
    mainloginFrame.grid_forget()
    search_hostels(root)
    
def Annsearch():
    Frame_search_hostels.grid_forget()
    show_hostels(root)

def Review():
    Layout_reviews()
    menu_review()
    main_hostel_review()
    reviews_scrollbar()


connection() #สั่งให้มันทำงาน
root = mainwindow() #ใส่ไป
mainloginFrame = Frame(root)
mainloginFrame.grid(row=0,sticky="news")
mainloginFrame.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
mainloginFrame.columnconfigure((0),weight=2)
mainloginFrame.columnconfigure((1),weight=1)

leftframe = Frame(mainloginFrame,bg='white') #กำหนดสี
loginframe = Frame(mainloginFrame,bg='white',highlightthickness=10,highlightbackground="#EEEEEE")
regisframe = Frame(mainloginFrame,bg='white',highlightthickness=10,highlightbackground="#EEEEEE")

upframe = Frame(mainloginFrame,bg='#0194F3')
downframe = Frame(mainloginFrame,bg='white')

img1 = PhotoImage(file='image/logo.png')
img2 = PhotoImage(file='image/discount.png')
img3 = PhotoImage(file='image/back.png').subsample(13,13)
img4 = PhotoImage(file='image/review.png').subsample(13,13)

p1 = PhotoImage(file="image/p1.png").subsample(8,8)
p2 = PhotoImage(file="image/p2.png").subsample(2,2)
p3 = PhotoImage(file="image/p3.png").subsample(8,8)
p4 = PhotoImage(file="image/p4.png").subsample(5,5)
p5 = PhotoImage(file="image/p5.png").subsample(5,5)
p6 = PhotoImage(file="image/p6.png").subsample(8,8)
p7 = PhotoImage(file="image/p7.png").subsample(8,8)
p8 = PhotoImage(file="image/p8.png").subsample(8,8)
p9 = PhotoImage(file="image/p9.png").subsample(8,8)
p10 = PhotoImage(file="image/p10.png").subsample(4,4)
p11 = PhotoImage(file="image/p11.png").subsample(8,8)
p12 = PhotoImage(file="image/p12.png").subsample(8,8)
p13 = PhotoImage(file="image/p13.png").subsample(5,5)
p14 = PhotoImage(file="image/p14.png").subsample(4,4)
p15 = PhotoImage(file="image/p15.png").subsample(8,8)
p16 = PhotoImage(file="image/p16.png").subsample(8,8)
p17 = PhotoImage(file="image/p17.png").subsample(5,5)

p21 = PhotoImage(file="image/p1.png").subsample(4,4)
p22 = PhotoImage(file="image/p2.png").subsample(1,1)
p23 = PhotoImage(file="image/p3.png").subsample(4,4)
p24 = PhotoImage(file="image/p4.png").subsample(2,2)
p25 = PhotoImage(file="image/p5.png").subsample(2,2)
p26 = PhotoImage(file="image/p6.png").subsample(4,4)
p27 = PhotoImage(file="image/p7.png").subsample(4,4)
p28 = PhotoImage(file="image/p8.png").subsample(4,4)
p29 = PhotoImage(file="image/p9.png").subsample(4,4)
p30 = PhotoImage(file="image/p10.png").subsample(2,2)
p31 = PhotoImage(file="image/p11.png").subsample(4,4)
p32 = PhotoImage(file="image/p12.png").subsample(4,4)
p33 = PhotoImage(file="image/p13.png").subsample(2,2)
p34 = PhotoImage(file="image/p14.png").subsample(2,2)
p35 = PhotoImage(file="image/p15.png").subsample(4,4)
p36 = PhotoImage(file="image/p16.png").subsample(4,4)
p37 = PhotoImage(file="image/p17.png").subsample(2,2)

piclist = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p37]
aaaa = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20]

star = PhotoImage(file="image/star.png").subsample(40,40)
search_icon = PhotoImage(file="image/search_bold.png").subsample(20,20)

mintext,maxtext = [IntVar()],[IntVar()]
spy1,spy2,spy3,spy4,spy5 = IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
stars = [IntVar() for i in range(5)]
Acomment = StringVar()

star = PhotoImage(file="image/star.png").subsample(40,40)
user_login_img = PhotoImage(file="image/user_login.png").subsample(20,20)
placeholder = PhotoImage(file="image/placeholder.png").subsample(20,20)

#Framesearch
Roomtext = StringVar()
#Label border-color


comment_mainFrame = Frame(root,bg='#0194f3')

ntbasic = [StringVar()]
bg_comment = '#0194f3'
fg_comment = 'white'




#background
border_gray = '#0000004d'
bg_behind = '#424242' #black 50%
white = "#fff"
green = '#1AE1A5'
tab_menu = '#0194F3'
#font
main_fontBlack = 'black'
#button
green_button = '#1AE1A5'
text_nomal = '16'
Arial = "Arial"

#Annsearch
Frame_hostel = Frame(root)

Volklogin()
root.mainloop() #ใส่
cursor.close() #ใส่
conn.close() #ใส่