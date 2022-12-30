import re
import DB_Project as db

database="DB_project.db"

"""--------------------------- TAKE DATA VALUES FROM USER INPUT ---------------------------"""

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

"""--------------------------- CHECK FOR REQUIREMENTS ---------------------------"""

def CheckPassword(Password):
    special_characters=re.findall("[!,@,#,$,%,^,&,*,(,)]",Password)
    numbers=re.findall("[1,2,3,4,5,6,7,8,9,0]",Password)
    letters=re.findall("[a-z,A-Z]",Password)
    if(len(Password)>=8 and len(Password)<=16 and len(letters)>=1 and len(numbers)>=1 and len(special_characters)>=1 ):
        return True
    else:
        return False

"""--------------------------- CHECK IN DATABASE ---------------------------"""

def Check_User_existance_on_Sign_Up(email):
    conn2=db.create_connection(database)
    cur=conn2.cursor()
    query="SELECT x.Email FROM XRHSTHS as x WHERE x.Email"
    return None

def SignIn():
    print(2)
    return None

"""--------------------------- INSERT INPUT DATA VALUES INTO TABLES ---------------------------"""

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

def Insert_in_Ekpaideusi_ypopsifiou(bathmos,hmnia_enarksis,hmnia_liksis,bathmida):
    conn4=db.create_connection(database)
    cur=conn4.cursor()
    query = """ INSERT INTO EKPAIDEYSH_YPOPSIFIOY (bathmos,hmnia_enarksis,hmnia_liksis,bathmida) VALUES ('%s','%s','%s','%s')""" % (bathmos,hmnia_enarksis,hmnia_liksis,bathmida)
    cur.execute(query)
    cur.close()
    conn4.commit()
    conn4.close()
    return None

def Insert_in_Proyphresia_ypospsifiou(titlos,paroxos,hmnia_enarksis,hmnia_liksis):
    conn5=db.create_connection(database)
    cur=conn5.cursor()
    query = """ INSERT INTO PROYPHRESIA_YPOPSIFIOY (titlos,paroxos,hmnia_enarksis,hmnia_liksis) VALUES ('%s','%s','%s','%s')""" % (titlos,paroxos,hmnia_enarksis,hmnia_liksis)
    cur.execute(query)
    cur.close()
    conn5.commit()
    conn5.close()
    return None

def Insert_in_Ikanothta_ypopsifiou(titlos_kathgorias,titlos_ikanothtas,epipedo):
    conn6=db.create_connection(database)
    cur=conn6.cursor()
    query = """ INSERT INTO IKANOTITA_YPOPSIFIOY (titlos_kathgorias,titlos_ikanothtas,epipedo) VALUES ('%s','%s','%s')""" % (titlos_kathgorias,titlos_ikanothtas,epipedo)
    cur.execute(query)
    cur.close()
    conn6.commit()
    conn6.close()
    return None

def Insert_in_Aggelia_erg(topothesia,wrario,misthos,perigrafh,typos_ergasia,titlos,hmeromhnia_dhmosieusis):
    conn7=db.create_connection(database)
    cur=conn7.cursor()
    query = """ INSERT INTO AGGELIA_ERGASIAS (topothesia,wrario,misthos,perigrafh,typos_ergasia,titlos,hmeromhnia_dhmosieusis) VALUES ('%s','%s','%s','%s','%s','%s','%s')""" % (topothesia,wrario,misthos,perigrafh,typos_ergasia,titlos,hmeromhnia_dhmosieusis)
    cur.execute(query)
    cur.close()
    conn7.commit()
    conn7.close()
    return None

def Insert_in_Apaitoumeni_ekpaideusi(bathmida,bathmos):
    conn8=db.create_connection(database)
    cur=conn8.cursor()
    query = """ INSERT INTO APAITOUMENI_EKPAIDEYSI (bathmida,bathmos) VALUES ('%s','%s')""" % (bathmida,bathmos)
    cur.execute(query)
    cur.close()
    conn8.commit()
    conn8.close()
    return None

def Insert_in_Apaitoumeni_proyphresia(titlos,diarkeia):
    conn9=db.create_connection(database)
    cur=conn9.cursor()
    query = """ INSERT INTO APAITOUMENI_PROYPHRESIA (titlos,diarkeia) VALUES ('%s','%s')""" % (titlos,diarkeia)
    cur.execute(query)
    cur.close()
    conn9.commit()
    conn9.close()
    return None

def Insert_in_Apaitoumeni_ikanothta(epipedo):
    conn10=db.create_connection(database)
    cur=conn10.cursor()
    query = """ INSERT INTO APAITOUMENI_IKANOTHTA (titlos,diarkeia) VALUES ('%s')""" % (epipedo)
    cur.execute(query)
    cur.close()
    conn10.commit()
    conn10.close()
    return None

def Insert_in_Aithsh(hmeromhnia_aithshs):
    conn11=db.create_connection(database)
    cur=conn11.cursor()
    query = """ INSERT INTO AITHSH (hmeromhnia_aithshs) VALUES ('%s')""" % (hmeromhnia_aithshs)
    cur.execute(query)
    cur.close()
    conn11.commit()
    conn11.close()
    return None

def Insert_in_Synenteyksi(heromhnia_synenteyksis):
    conn12=db.create_connection(database)
    cur=conn12.cursor()
    query = """ INSERT INTO SYNTEYKSI (heromhnia_synenteyksis) VALUES ('%s')""" % (heromhnia_synenteyksis)
    cur.execute(query)
    cur.close()
    conn12.commit()
    conn12.close()
    return None

def Insert_in_Aksiologhsh(bathmologia,hmeromhnia_aksiologishs,perilipsi):
    conn13=db.create_connection(database)
    cur=conn13.cursor()
    query = """ INSERT INTO AKSIOLOGHSH (bathmologia,hmeromhnia_aksiologishs,perilipsi) VALUES ('%s','%s','%s')""" % (bathmologia,hmeromhnia_aksiologishs,perilipsi)
    cur.execute(query)
    cur.close()
    conn13.commit()
    conn13.close()
    return None