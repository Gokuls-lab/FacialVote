import eel
import sys
import time
from db import add_data,get_id
from vote import vote
# adding Folder_2 to the system path
sys.path.insert(0, 'face-attendance-system-master/')
sys.path.insert(0, 'face-attendance-system-master/Silent-Face-Anti-Spoofing-master/')


from main import App
#app.start()
eel.init("web")

@eel.expose
def login():
    app=App()
    res=app.login()
    app.stop()
    file=open("voted.txt",'r')
    f=file.read()
    if(str(res) in f):
        return "Already Voted"
    return res
@eel.expose
def register(fname,lname,num,place):
    app = App()
    app.register_new_user()
    g=app.accept_register_new_user(fname)
    app.stop()
    add_data([(get_id(),fname,place)])
    return "Register Succesfull"
@eel.expose
def add_vote(can,user):
    #print(f"hi... {user}")
    file=open(r"C:\Users\Dell\gk-face\voted.txt","a")
    file.write(f"{user}\n")
    if(can=="ADMK "):
        vote("ADMK")
    elif(can=="DMK "):
        vote("DMK")
    elif(can=="BJP "):
        vote("BJP")
    elif(can=="CONGRESS "):
        vote("CONGRESS")
    else:
        pass
eel.start("index.html")