from tkinter import *
from firebase_communication import auth
from firebase_communication.update_db import set_active, set_deactive
import os
def main_menu():
    global main_screen
    main_screen = Tk()    
    main_screen.geometry("350x300") 
    main_screen.title("Account Login")

    Label(text="SISOSIG Client Software", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 

    Button(text="Login", height="2", width="30", command=login_screen).pack() 
    Label(text="").pack() 

    Button(text="Register", height="2", width="30", command=register_screen).pack()
    
    main_screen.mainloop() 

def register_screen():
    global register_screen
    global email
    global password
    global location_name
    global max_people
    global email_entry
    global password_entry
    global location_name_entry
    global people_entry

    register_screen = Toplevel(main_screen) 
    register_screen.title("Register")
    register_screen.geometry("350x300")

    email = StringVar()
    password = StringVar()
    location_name = StringVar()
    max_people = IntVar()

    Label(register_screen, text="Register", ).pack()
    Label(register_screen, text="").pack()
    
    email_label = Label(register_screen, text="Email: ")
    email_label.pack()

    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()
   
    password_label = Label(register_screen, text="Password: ")
    password_label.pack()
    
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    location_name_label = Label(register_screen, text="Location Name: ")
    location_name_label.pack()

    location_name_entry = Entry(register_screen, textvariable=location_name)
    location_name_entry.pack()
   
    people_label = Label(register_screen, text="Person Capacity to Enhance Social Distancing: ")
    people_label.pack()
    
    people_entry = Entry(register_screen, textvariable=max_people)
    people_entry.pack()
    
    Label(register_screen, text="").pack()
    
    Button(register_screen, text="Register", width=10, height=1, command=register_user).pack()

def register_user():
    email_info = email.get()
    password_info = password.get()
    location_name_info = location_name.get()
    max_people_info = max_people.get()
    user_id = auth.create_account(email_info,password_info,location_name_info,max_people_info)
    control_screen(user_id)
    '''
    try:
        user_id = auth.create_account(email_info,password_info,location_name_info,max_people_info)
        control_screen(user_id)
    except:
        Label(register_screen, text="Registration Failed. Please try again.", fg="red", font=("calibri", 11)).pack()
    '''
def login_screen():
    global login_screen
    global login_email
    global login_password
    global login_email_entry
    global login_password_entry

    login_screen = Toplevel(main_screen) 
    login_screen.title("Login")
    login_screen.geometry("300x250")

    login_email = StringVar()
    login_password = StringVar()

    Label(login_screen, text="Login", ).pack()
    Label(login_screen, text="").pack()
    
    email_label = Label(login_screen, text="Email: ")
    email_label.pack()

    login_email_entry = Entry(login_screen, textvariable=login_email)
    login_email_entry.pack()
   
    password_label = Label(login_screen, text="Password: ")
    password_label.pack()
    
    login_password_entry = Entry(login_screen, textvariable=login_password, show='*')
    login_password_entry.pack()
    Label(login_screen, text="").pack()

    Button(login_screen, text="Login", width=10, height=1, command=login_user).pack()

def login_user():
    email_info = login_email.get()
    password_info = login_password.get()

    try:
        user = auth.login_user(email_info,password_info)
    except:
        Label(login_screen, text="Registration Failed. Please try again.", fg="red", font=("calibri", 11)).pack()
    # TODO: USER LOGIN

def control_screen(user):
    global is_active
    register_screen.destroy()
    #main_screen.withdraw()
    is_active = False
    control_screen = Toplevel(main_screen) 
    control_screen.title("Control Screen")
    control_screen.geometry("350x250")

    is_active_label = Label(control_screen, text='Change your camera activity.').pack()
    Button(control_screen, text="Activate", width=10, height=1, command=lambda: change_camera_activity(user)).pack()
    Button(control_screen, text="De-Activate", width=10, height=1).pack() #TODO: Add Camera Deactivation

def change_camera_activity(user):
    global is_active
    if not is_active:
        is_active = True
        os.system(r'python yolov3_deepsort.py demo\test.mp4 '+f'{user[1:]}' ' --display')
main_menu() 