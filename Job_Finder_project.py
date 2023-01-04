import re
import DB_Project as db
from datetime import date

database="DB_project.db"

class SignUP():
    def __init__(self) :
        return
    def Sign_UP(self):
        email=input("Email:")
        while(email==''):
            print("Εισάγετε αποδεκτό Email")
            email=input("Email:")
        data_email=self.Check_Email_existance(email)
        while(len(data_email)>0):
            print("Φαίνεται πως υπάρχει ήδη λογαριασμός με αυτό το email\nΘέλετε να κάνετε Sign in;")
            signin=int(input("Πατήστε 1 για να εισάγετε άλλο mail ή 2 για να συνεχίσετε με Sign In:"))
            if(signin==1):
                email=input("Email:")
                data_email=self.Check_Email_existance(email)
            elif(signin==2):
                SignIn()
        username=input("Username:")
        while(username==''):
            print("Εισάγετε αποδεκτό Username")
            username=input("Username:")
        data_username=self.Check_Username_existance(username)
        while(len(data_username)>0):
            print("Υπάρχει ήδη λογαριασμός με αυτό το όνομα χρήστη\nΠαρακαλώ εισάγετε νέο όνομα χρήστη")
            username=input("Username:")
            data_username=self.Check_Username_existance(username)
        password=input("Κωδικός:")
        while(password=='' or self.CheckPassword(password)==False):
            print("Ο Κωδικός πρέπει να περιέχει τουλάχιστον έναν αριθμό, έναν ειδικό χαρακτήρα και να είναι από 8 έως 16 χαρακτήρες")
            password=input("Password:")
        eidos_xrhsth=input("Συνδεθείτε ως αιτούμενος ή πάροχος εργασίας\nΠατήστε Α για αιτούμενο και P για πάροχο")
        while(eidos_xrhsth=='' or eidos_xrhsth not in ["A","P"]):
            print("Please insert the correct information")
            eidos_xrhsth=input("Συνδεθείτε ως αιτούμενος ή πάροχος εργασίας\nΠατήστε Α για αιτούμενο και P για πάροχο")
        self.Insert_in_Xrhsths(email,username,password,eidos_xrhsth)
        return {"Email":email,"Username":username,"Eidos_xrhsth":eidos_xrhsth}

    def CheckPassword(self,Password):
        special_characters=re.findall("[!,@,#,$,%,^,&,*,(,)]",Password)
        numbers=re.findall("[1,2,3,4,5,6,7,8,9,0]",Password)
        letters=re.findall("[a-z,A-Z]",Password)
        if(len(Password)>=8 and len(Password)<=16 and len(letters)>=1 and len(numbers)>=1 and len(special_characters)>=1 ):
            return True
        else:
            return False


    def Check_Email_existance(self,email):
        conn_for_email=db.create_connection(database)
        cur=conn_for_email.cursor()
        query="""SELECT Email from XRHSTHS WHERE Email='%s'""" % email
        cur.execute(query)
        data=cur.fetchall()
        return data

    def Check_Username_existance(self,Username):
        conn_for_email=db.create_connection(database)
        cur=conn_for_email.cursor()
        query="""SELECT Username from XRHSTHS WHERE Username='%s'""" % Username
        cur.execute(query)
        data=cur.fetchall()
        return data

    def Insert_in_Xrhsths(self,email,username,password,eidos_xrhsth):
        conn=db.create_connection(database)
        cur=conn.cursor()
        query = """INSERT INTO XRHSTHS (Email,Username,Password,Eidos_xrhsth) VALUES ('%s','%s','%s','%s')""" % (email,username,password,eidos_xrhsth)
        cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
        return None

class Profile_Creation():
    def __init__(self):
        return

    def Create_ait_profil(self,email):
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
        fylo=input("Φύλο : (A: Άντρας, Γ: Γυναίκα, Ο:Άλλο,Enter: Αν δεν θέλετε να δηλώσετε το φύλο σας ")
        if(fylo==''):fylo=None
        self.Insert_in_Profil_aitoumenou(onoma,eponymo,hlikia,fylo,email)

        return None

    def Insert_in_Profil_aitoumenou(self,onoma,eponymo,hlikia,fylo,email):
        conn=db.create_connection(database)
        cur=conn.cursor()
        id_ait=User_id_assignement(email)
        query = """ INSERT INTO PROFIL_AITOUMENOY (ID_aitoumenou,onoma,eponymo,hlikia,fylo) VALUES ('%d','%s','%s','%s','%s')""" % (id_ait,onoma,eponymo,hlikia,fylo)
        cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
        return None

    def Create_paroxos_profil(self,email):
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
        self.Insert_in_Profil_paroxou(eponymia,perigrafh,dieythynsh,thlefono,email)
        return None
    
    def Insert_in_Profil_paroxou(self,eponymia,perigrafh,dieythynsh,thlefono,email):
        conn=db.create_connection(database)
        cur=conn.cursor()
        id_par=User_id_assignement(email)
        query = """ INSERT INTO PROFIL_PAROXOU (ID_paroxou,eponymia,perigrafh,dieythynsh,thlefono) VALUES ('%d','%s','%s','%s','%s')""" % (id_par,eponymia,perigrafh,dieythynsh,thlefono)
        cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
        return None

class SignIn():
    
    def __init__(self):
        return

    def Sign_In(self,email,password):
        conn=db.create_connection(database)
        cur=conn.cursor()
        query="""SELECT User_ID,Email,Password from XRHSTHS where Email='%s' and Password='%s' """ % (email,password)
        cur.execute(query)
        user=cur.fetchone()
        return user

class User_skills_insertion():
    
    def __init__(self):
        return
    
    def Create_education(self,id_ait):
        print("Επιλέξτε την βαθμίδα της εκπαίδευσης σας")
        bathmida=int(input("1:Τριτοβάθμια 2:Πτυχίο 3:Master 4:Διδακτορικό"))
        if(bathmida==1):
            hmnia_enarksis=input("Έναρξη εκπαίδευσης. Χρησιμοποιήστε το format yyyy-mm-dd")
            hmnia_liksis=input("Λήξη εκπαίδευσης.")
            bathmos=int(input("Βαθμός απολυτηρίου\n"))
            User_skills_insertion().Insert_ekpaideysi(id_ait,bathmos,hmnia_enarksis,hmnia_liksis,bathmida,0)
        else:
            print("Επιλέξτε ένα από τα παρακάτω πεδία σπουδών")
            search=input("Αναζητήστε το πεδίο σπουδών σας για καλύτερα αποτελέσματα:")
            if(len(search)>5):
                search=search[0:5]
            search=search.upper()
            conn=db.create_connection(database)
            cur=conn.cursor()
            placeholder="'%"+search+"%'"
            query="""SELECT Id_pediou,Titlos from PEDIO_SPOUDON WHERE Titlos like %s"""%placeholder
            cur.execute(query)
            titloi=cur.fetchall()
            for i in titloi:print(i)
            id_pediou=int(input("Επιλέξτε τον κωδικό του πεδίου:"))
            hmnia_enarksis=input("Έναρξη εκπαίδευσης. Χρησιμοποιήστε το format yyyy-mm-dd")
            print("Αν σπουδάζετε αυτήν την στιγμή πατήστε enter")
            hmnia_liksis=input("Λήξη εκπαίδευσης.")
            if(hmnia_liksis==''):hmnia_liksis=date.today()
            bathmos=input("Βαθμός: \n")
            if(bathmos==''):bathmos=None
            else:bathmos=int(bathmos)
            User_skills_insertion().Insert_ekpaideysi(id_ait,bathmos,hmnia_enarksis,hmnia_liksis,bathmida,id_pediou)
        x=int(input("Αν θέλετε να εισάγετε κι άλλη εκπαίδευση πατήστε 1 αλλιώς πατήστε 2:"))
        if(x==1):
            User_skills_insertion().Create_education(id_ait)
        else:
            return None
    
    def Insert_ekpaideysi(self,id_ait,bathmos,hmnia_enarksis,hmnia_liksis,bathmida,id_pediou):
        conn=db.create_connection(database)
        cur=conn.cursor()
        if(bathmos!=None):
            query = """ INSERT INTO EKPAIDEYSH_YPOPSIFIOY (ID_aitoumenou,Bathmos,Hmnia_enarksis,Hmnia_liksis,Bathmida,ID_pediou) 
                        VALUES ('%d','%d','%s','%s','%d','%d')""" % (id_ait,bathmos,hmnia_enarksis,hmnia_liksis,bathmida,id_pediou)
        else:
            query = """ INSERT INTO EKPAIDEYSH_YPOPSIFIOY (ID_aitoumenou,Hmnia_enarksis,Hmnia_liksis,Bathmida,ID_pediou) 
                        VALUES ('%d','%s','%s','%d','%d')""" % (id_ait,hmnia_enarksis,hmnia_liksis,bathmida,id_pediou)
        cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
        return None

    def Create_proyphresia(self,id_ait):
        no_work_experience=input("Αν δεν θέλετε να εισάγεται προϋπηρεσία πατήστε 0 αλλίως πατήστε 1")
        if(not no_work_experience):
            return None
        print("Εισάγεται προϋπηρεσία")
        titlos=input("Τίτλος θέσης εργασίας: ")
        parochos=input("Πάροχος:")
        Hmnia_enarksis=input("Ημερομηνία έναρξης. Χρησιμοποιήστε το format yyyy-mm-dd:")
        Hmnia_liksis=input("Ημερομηνία λήξης. Χρησιμοποιήστε το format yyyy-mm-dd\nΑν δουλεύεται ακόα εκεί πιέστε enter")
        if(Hmnia_liksis==''):Hmnia_liksis="now"
        x=input("Αν θέλετε να εισάγεται και άλλη προυπηρεσία πιέστε 1 αλλιώς 2:")
        if(x==1):User_skills_insertion().Create_proyphresia(id_ait)
        else:
            self.Insert_proyphresia(titlos,id_ait,parochos,Hmnia_enarksis,Hmnia_liksis)
        return None

    def Insert_proyphresia(self,id_ait,titlos,parochos,Hmnia_enarksis,Hmnia_liksis):
        conn=db.create_connection(database)
        cur=conn.cursor()
        query = """ INSERT INTO PROYPHRESIA_YPOPSIFIOY (ID_aitoumenou,Titlos,Paroxos,Hmnia_enarksis,Hmnia_liskis) 
                    VALUES ('%d','%d','%s','%s','%d','%d')""" % (id_ait,titlos,parochos,Hmnia_enarksis,Hmnia_liksis)
        cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
        return None

def User_id_assignement(email):
    conn=db.create_connection(database)
    cur=conn.cursor()
    query="""SELECT User_ID from XRHSTHS WHERE Email='%s'""" % email
    cur.execute(query)
    id=cur.fetchone()
    return id[0]