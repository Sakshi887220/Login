import  sqlite3
from tkinter import *
conn=sqlite3.connect("student.db")
print("Database created successfully")

conn.execute("""
CREATE TABLE AD(
ADMIN_ID INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL ,
USERNAME TEXT NOT NULL, 
PASSWORD TEXT NOT NULL)
""")
print ("Table ADMIN created successfully")

#Output
#Database Opened successfully
#Table ADMIN created successfully

conn.execute("INSERT INTO AD(USERNAME,PASSWORD) VALUES ('admin', 'admin789')");

conn.execute("INSERT INTO AD(USERNAME,PASSWORD) VALUES ('krazy', 'krazy789')");

conn.commit()
print ("Records inserted successfully")
conn.close()
"""
###Output###
Database Opened successfully
Records inserted successfully
"""

def login():
    #getting form data
    uname=username.get()
    pwd=password.get()
    #applying empty validation
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
      #open database
      conn = sqlite3.connect('student.db')
      #select query
      cursor = conn.execute('SELECT * from AD where USERNAME="%s" and PASSWORD="%s"'%(uname,pwd))
      #fetch data 
      if cursor.fetchone():
       message.set("Login success")
      else:
       message.set("Wrong username or password!!!")
#defining loginform function
def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("Krazyprogrammer.com")
    #setting height and width of screen
    login_screen.geometry("350x250")
    login_screen["bg"]="#1C2833"
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Login From", bg="#0E6655",fg="white",font=("Arial",12,"bold")).pack()
    #Username Label
    Label(login_screen, text="Username * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=40)
    #Username textbox
    Entry(login_screen, textvariable=username,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=42)
    #Password Label
    Label(login_screen, text="Password * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=95,y=120)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, command=login, bg="#0E6655",fg="white",font=("Arial",12,"bold")).place(x=125,y=170)
    login_screen.mainloop()
#calling function Loginform
Loginform()