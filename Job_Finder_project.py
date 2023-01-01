import re
import DB_Project as db

database="DB_project.db"

"""--------------------------- TAKE DATA VALUES FROM USER INPUT ---------------------------"""

""" ΑΥΤΑ ΤΑ ΕΚΑΝΑ ΓΙΑ ΤΑ ΙΝΠΟΥΤΣ ΠΟΥ ΠΡΕΠΕΙ ΝΑ ΔΙΝΕΙ Ο ΧΡΗΣΤΗΣ ΑΣΧΕΤΑ ΜΕ ΤΑ ΦΟΡΕΙΝ 
ΠΟΥ ΘΑ ΠΡΕΠΕΙ ΝΑ ΠΕΡΑΣΟΥΜΕ ΕΠΙΣΗΣ"""

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
        print("\nΓια να εισάγετε εκπαίδευση πατήστε 'Ε' \nΓια να εισάγετε προυπηρεσία πατήστε 'Π'\nΓια να εισάγετε ικανότητα πατήστε 'Ι'\n")
        eisagwgh_empeirias=input("Επιλογή : \n")
        if(eisagwgh_empeirias=='Ε'):
            Create_ekpaideusi_ypopsifiou()
            print("\nΓια να εισάγετε προυπηρεσία πατήστε 'Π'\nΓια να εισάγετε ικανότητα πατήστε 'Ι'\n")
            eisagwgh_empeirias=input("Επιλογή : \n")
            if(eisagwgh_empeirias=='Π'):
                Create_proyphresia_ypospsifiou()
            elif(eisagwgh_empeirias=='Ι'):
                Create_ikanothta_ypopsifiou()
        elif(eisagwgh_empeirias=='Π'):
            Create_proyphresia_ypospsifiou()
            print("\nΓια να εισάγετε εκπαίδευση πατήστε 'Ε'\nΓια να εισάγετε ικανότητα πατήστε 'Ι'\n")
            eisagwgh_empeirias=input("Επιλογή : \n")
            if(eisagwgh_empeirias=='Ε'):
                Create_ekpaideusi_ypopsifiou()
            elif(eisagwgh_empeirias=='Ι'):
                Create_ikanothta_ypopsifiou()
        elif(eisagwgh_empeirias=='Ι'):
            Create_ikanothta_ypopsifiou()
            print("\nΓια να εισάγετε εκπαίδευση πατήστε 'Ε'\nΓια να εισάγετε προυπηρεσία πατήστε 'Π'\n")
            eisagwgh_empeirias=input("Επιλογή : \n")
            if(eisagwgh_empeirias=='Ε'):
                Create_ekpaideusi_ypopsifiou()
            elif(eisagwgh_empeirias=='Π'):
                Create_proyphresia_ypospsifiou()
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
    Insert_in_Profil_paroxou(eponymia,perigrafh,dieythynsh,thlefono)
    return None

def Create_ekpaideusi_ypopsifiou():
    bathmos=input("Βαθμός : ")
    hmnia_enarksis=input("Ημερομηνία έναρξης : ")
    while(hmnia_enarksis==''):
        print("Εισάγετε αποδεκτή Ημερομηνία έναρξης : ")
        hmnia_enarksis=input("Ημερομηνία έναρξης : ")
    hmnia_liksis=input("Ημερομηνία λήξης : ")
    while(hmnia_liksis==''):
        print("Εισάγετε αποδεκτή Ημερομηνία λήξης : ")
        hmnia_liksis=input("Ημερομηνία λήξης : ")
    bathmida=input("Βαθμίδα : ")
    while(bathmida==''):
        print("Εισάγετε αποδεκτή βαθμίδα : ")
        bathmida=input("Βαθμίδα : ")
    Insert_in_Ekpaideusi_ypopsifiou(bathmos,hmnia_enarksis,hmnia_liksis,bathmida)
    return None

def Create_proyphresia_ypospsifiou():
    titlos=input("Τίτλος : ")
    while(titlos==''):
        print("Εισάγετε αποδεκτό Τίτλο : ")
        titlos=input("Τίτλος : ")
    paroxos=input("Πάροχος : ")
    while(paroxos==''):
        print("Εισάγετε αποδεκτό Πάροχο : ")
        paroxos=input("Πάροχο : ")
    hmnia_enarksis=input("Ημερομηνία έναρξης : ")
    while(hmnia_enarksis==''):
        print("Εισάγετε αποδεκτή Ημερομηνία έναρξης : ")
        hmnia_enarksis=input("Ημερομηνία έναρξης : ")
    hmnia_liksis=input("Ημερομηνία λήξης : ")
    while(hmnia_liksis==''):
        print("Εισάγετε αποδεκτή Ημερομηνία λήξης : ")
        hmnia_liksis=input("Ημερομηνία λήξης : ")
    Insert_in_Proyphresia_ypospsifiou(titlos,paroxos,hmnia_enarksis,hmnia_liksis)
    return None

def Create_ikanothta_ypopsifiou():
    titlos_kathgorias=input("Τίτλος Κατηγορίας : ")
    while(titlos_kathgorias==''):
        print("Εισάγετε αποδεκτό Τίτλο Κατηγορίας : ")
        titlos_kathgorias=input("Τίτλος Κατηγορίας : ")
    titlos_ikanothtas=input("Τίτλος Ικανότητας : ")
    while(titlos_ikanothtas==''):
        print("Εισάγετε αποδεκτό Τίτλο Ικανότητας : ")
        titlos_ikanothtas=input("Τίτλος Ικανότητας : ")
    epipedo=input("Επίπεδο : ")
    while(epipedo==''):
        print("Εισάγετε αποδεκτό Επίπεδο : ")
        epipedo=input("Επίπεδο : ")
    Insert_in_Ikanothta_ypopsifiou(titlos_kathgorias,titlos_ikanothtas,epipedo)
    return None

def Create_aggelia_erg():
    topothesia=input("Τοποθεσία : ")
    while(topothesia==''):
        print("Εισάγετε αποδεκτή Τοποθεσία : ")
        topothesia=input("Τοποθεσία : ")
    wrario=input("Ωράριο : ")
    misthos=input("Μισθός : ")
    perigrafi=input("Περιγραφή : ")
    typos_ergasias=input("Τύπος Εργασίας : ")
    titlos=input("Τίτλος : ")
    Insert_in_Aggelia_erg(topothesia,wrario,misthos,perigrafi,typos_ergasias,titlos)
    return None

def Create_apaitoumeni_ekpaideusi():
    bathmida=input("Βαθμίδα : ")
    bathmos=input("Βαθμός : ")
    Insert_in_Apaitoumeni_ekpaideusi(bathmida,bathmos)
    return None

def Create_apaitoumeni_proyphresia():
    titlos=input("Τίτλος : ")
    while(titlos==''):
        print("Εισάγετε αποδεκτό Τίτλο : ")
        titlos=input("Τίτλος : ")
    diarkeia=input("Διάρκεια : ")
    while(diarkeia==''):
        print("Εισάγετε αποδεκτή Διάρκεια : ")
        diarkeia=input("Διάρκεια : ")
    Insert_in_Apaitoumeni_proyphresia(titlos,diarkeia)
    return None

def Create_apaitoumeni_ikanothta():
    titlos_ikanothtas=input("Τίτλος Ικανότητας : ")
    while(titlos_ikanothtas==''):
        print("Εισάγετε αποδεκτό Τίτλο Ικανότητας : ")
        titlos_ikanothtas=input("Τίτλος Ικανότητας : ")
    epipedo=input("Επίπεδο : ")
    while(epipedo==''):
        print("Εισάγετε αποδεκτό Επίπεδο : ")
        epipedo=input("Επίπεδο : ")
    Insert_in_Apaitoumeni_ikanothta(titlos_ikanothtas,epipedo)
    return None

def Create_aithsh():
    """ΔΕΝ ΕΧΩ ΚΑΤΑΛΑΒΕΙ ΠΩΣ ΘΑ ΤΟ ΚΑΝΟΥΜΕ ΑΥΤΟ. ΘΑ ΕΛΕΓΑ ΟΤΑΝ ΕΜΦΑΝΙΖΕΙ ΑΓΓΕΛΙΑ ΣΤΟ 
    ΧΡΗΣΤΗ ΝΑ ΤΟΥ ΛΕΜΕ ΘΕΛΤΕ ΝΑ ΚΑΝΕΤΕ ΑΙΤΗΣΗ Ν/Ο; ΚΑΙ ΑΝΑΛΟΓΩΣ ΝΑ ΠΕΡΝΑΜΕ ΤΑ ΣΤΟΙΧΕΙΑ ΣΤΟΝ ΠΙΝΑΚΑ"""
    return None

def Create_synenteyksi():
    """ΕΠΙΣΗΣ ΔΕΝ ΕΧΩ ΚΑΤΑΛΑΒΕΙ ΥΠΟΘΕΤΩ ΟΤΙ ΘΑ ΠΡΕΠΕΙ ΠΑΛΙ ΝΑ ΡΩΤΑΜΕ ΤΟΝ ΠΑΡΟΧΟ ?ΚΑΠΟΥ?
    ΑΝ ΔΕΧΕΤΑΙ ΤΗΝ ΑΙΤΗΣΗ ?????"""
    return None

def Create_aksiologhsh():
    bathmologia=input("Βαθμολογία : ")
    while(bathmologia==''):
        print("Εισάγετε αποδεκτή Βαθμολογία : ")
        bathmologia=input("Βαθμολογία : ")
    perilipsi=input("Περίληψη : ")
    while(perilipsi==''):
        print("Εισάγετε αποδεκτή Περίληψη : ")
        perilipsi=input("Περίληψη : ")
    Insert_in_Profil_paroxou(bathmologia,perilipsi)
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

def Insert_in_Profil_paroxou(eponymia,perigrafh,dieythynsh,thlefono):
    conn3=db.create_connection(database)
    cur=conn3.cursor()
    query = """ INSERT INTO PROFIL_PAROXOU (eponymia,perigrafh,dieythynsh,thlefono) VALUES ('%s','%s','%s','%s')""" % (eponymia,perigrafh,dieythynsh,thlefono)
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

def Insert_in_Aggelia_erg(topothesia,wrario,misthos,perigrafi,typos_ergasias,titlos):
    conn7=db.create_connection(database)
    cur=conn7.cursor()
    query = """ INSERT INTO AGGELIA_ERGASIAS (topothesia,wrario,misthos,perigrafi,typos_ergasias,titlos) VALUES ('%s','%s','%s','%s','%s','%s')""" % (topothesia,wrario,misthos,perigrafi,typos_ergasias,titlos)
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

def Insert_in_Apaitoumeni_ikanothta(titlos_ikanothtas,epipedo):
    conn10=db.create_connection(database)
    cur=conn10.cursor()
    query = """ INSERT INTO APAITOUMENI_IKANOTHTA (titlos_ikanothtas,epipedo) VALUES ('%s','%s')""" % (titlos_ikanothtas,epipedo)
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

def Insert_in_Aksiologhsh(bathmologia,perilipsi):
    conn13=db.create_connection(database)
    cur=conn13.cursor()
    query = """ INSERT INTO AKSIOLOGHSH (bathmologia,hmeromhnia_aksiologishs,perilipsi) VALUES ('%s','%s')""" % (bathmologia,perilipsi)
    cur.execute(query)
    cur.close()
    conn13.commit()
    conn13.close()
    return None