import re
import DB_Project as db

database="DB_project.db"


def Sign_UP():
    email=input("Email : ")
    while(email==''):
        print("Εισάγετε αποδεκτό Email : ")
        email=input("Email : ")
    username=input("Username : ")
    while(username==''):
        print("Εισάγετε αποδεκτό Username : ")
        username=input("Username :")
    password=input("Κωδικός : ")
    while(password=='' or CheckPassword(password)==False):
        print("Ο Κωδικός πρέπει να περιέχει τουλάχιστον έναν αριθμό, έναν ειδικό χαρακτήρα και να είναι από 8 έως 16 χαρακτήρες : ")
        password=input("Password : ")
    eidos_xrhsth=input("Συνδεθείτε ως αιτούμενος ή πάροχος εργασίας\nΠατήστε Α για αιτούμενο και P για πάροχο : ")
    while(eidos_xrhsth=='' or eidos_xrhsth not in ["A","P"]):
        print("Please insert the correct information")
        eidos_xrhsth=input("Συνδεθείτε ως αιτούμενος ή πάροχος εργασίας\nΠατήστε Α για αιτούμενο και P για πάροχο : ")
    Insert_in_Xrhsths(email,username,password,eidos_xrhsth)
    if(eidos_xrhsth=="A"):
        Create_ait_profil()
    else:
        Create_paroxos_profil()
    return None

def Create_ait_profil():
    onoma=input("Όνομα : ")
    while(onoma==''):
        print("Εισάγετε αποδεκτό Όνομα : ")
        onoma=input("Όνομα : ")
    eponymo=input("Επώνυμο : ")
    while(eponymo==''):
        print("Εισάγετε αποδεκτό Επώνυμο : ")
        eponymo=input("Επώνυμο : ")
    hlikia=input("Ηλικία : ")
    while(hlikia==''):
        print("Εισάγετε αποδεκτή Ηλικία : ")
        hlikia=input("Ηλικία : ")
    fylo=input("Φύλο : ")
    Insert_in_Profil_aitoumenou(onoma,eponymo,hlikia,fylo)

    return None

def Create_paroxos_profil():
    eponymia=input("Επωνυμία : ")
    while(eponymia==''):
        print("Εισάγετε αποδεκτή Επωνυμία : ")
        eponymia=input("Επωνυμία : ")
    perigrafh=input("Περιγραφή : ")
    while(perigrafh==''):
        print("Εισάγετε αποδεκτή Περιγραφή : ")
        perigrafh=input("Περιγραφή : ")
    dieythynsh=input("Διεύθυνση : ")
    while(dieythynsh==''):
        print("Εισάγετε αποδεκτή Διεύθυνση : ")
        dieythynsh=input("Διεύθυνση : ")
    thlefono=input("Τηλέφωνο : ")
    while(thlefono==''):
        print("Εισάγετε αποδεκτό Τηλέφωνο : ")
        thlefono=input("Τηλέφωνο : ")
    bathmologia=input("Βαθμολογία : ")
    Insert_in_Profil_paroxou(eponymia,perigrafh,dieythynsh,thlefono,bathmologia)
    return None

def CheckPassword(Password):
    special_characters=re.findall("[!,@,#,$,%,^,&,*,(,)]",Password)
    numbers=re.findall("[1,2,3,4,5,6,7,8,9,0]",Password)
    letters=re.findall("[a-z,A-Z]",Password)
    if(len(Password)>=8 and len(Password)<=16 and len(letters)>=1 and len(numbers)>=1 and len(special_characters)>=1 ):
        return True
    else:
        return False

def Insert_in_Xrhsths(email,username,password,eidos_xrhsth):
    conn1=db.create_connection(database)
    cur=conn1.cursor()
    query = """INSERT INTO XRHSTHS (email,username,password,eidos_xrhsth) VALUES ('%s','%s','%s','%s')""" % (email,username,password,eidos_xrhsth)
    cur.execute(query)
    cur.close()
    conn1.commit()
    conn1.close()
    return None

def Insert_in_Profil_aitoumenou(onoma,eponymo,hlikia,fylo):
    conn2=db.create_connection(database)
    cur=conn2.cursor()
    query = """ INSERT INTO PROFIL_AITOUMENOY (onoma,eponymo,hlikia,fylo) VALUES ('%s','%s','%s','%s')""" % (onoma,eponymo,hlikia,fylo)
    cur.execute(query)
    cur.close()
    conn2.commit()
    conn2.close()
    return None

def Insert_in_Profil_paroxou(eponymia,perigrafh,dieythynsh,thlefono,bathmologia):
    conn3=db.create_connection(database)
    cur=conn3.cursor()
    query = """ INSERT INTO PROFIL_PAROXOU (eponymia,perigrafh,dieythynsh,thlefono,bathmologia) VALUES ('%s','%s','%s','%s','%s')""" % (eponymia,perigrafh,dieythynsh,thlefono,bathmologia)
    cur.execute(query)
    cur.close()
    conn3.commit()
    conn3.close()
    return None

def Check_User_existance_on_Sign_Up(email):
    conn2=db.create_connection(database)
    cur=conn2.cursor()
    query="SELECT x.Email FROM XRHSTHS as x WHERE x.Email"
    return None


def SignIn():
    print(2)
    return None