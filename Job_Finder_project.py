import re
import DB_Project as db
from datetime import date

database="DB_project.db"

"""--------------------------- TAKE DATA VALUES FROM USER INPUT ---------------------------"""

""" ΑΥΤΑ ΤΑ ΕΚΑΝΑ ΓΙΑ ΤΑ ΙΝΠΟΥΤΣ ΠΟΥ ΠΡΕΠΕΙ ΝΑ ΔΙΝΕΙ Ο ΧΡΗΣΤΗΣ ΑΣΧΕΤΑ ΜΕ ΤΑ ΦΟΡΕΙΝ 
ΠΟΥ ΘΑ ΠΡΕΠΕΙ ΝΑ ΠΕΡΑΣΟΥΜΕ ΕΠΙΣΗΣ"""

class SignUP():
    def __init__(self):
        return
    
    def Sign_UP(self):
        email=input("Email : ")
        while(email==''):
            print("Εισάγετε αποδεκτό Email : ")
            email=input("Email : ")
        """Check email existance"""
        data_email=self.Check_Email_existance(email)
        while(len(data_email)>0):
            print("Φαίνεται πως υπάρχει ήδη λογαριασμός με αυτό το email\nΘέλετε να κάνετε Sign in;")
            signin=int(input("Πατήστε 1 για να εισάγετε άλλο mail ή 2 για να συνεχίσετε με Sign In:"))
            if(signin==1):
                email=input("Email:")
                data_email=self.Check_Email_existance(email)
            elif(signin==2):
                SignIn()
        """username"""
        username=input("Username : ")
        while(username==''):
            print("Εισάγετε αποδεκτό Username : ")
            username=input("Username :")
        """Check username existance"""
        data_username=self.Check_Username_existance(username)
        while(len(data_username)>0):
            print("Υπάρχει ήδη λογαριασμός με αυτό το όνομα χρήστη\nΠαρακαλώ εισάγετε νέο όνομα χρήστη")
            username=input("Username:")
            data_username=self.Check_Username_existance(username)
        """password"""
        password=input("Κωδικός : ")
        while(password=='' or self.CheckPassword(password)==False):
            print("Ο Κωδικός πρέπει να περιέχει τουλάχιστον έναν αριθμό, έναν ειδικό χαρακτήρα και να είναι από 8 έως 16 χαρακτήρες : ")
            password=input("Password : ")
        """eidos xrhsth"""
        eidos_xrhsth=input("Συνδεθείτε ως αιτούμενος ή πάροχος εργασίας\nΠατήστε Α για αιτούμενο και P για πάροχο : ")
        while(eidos_xrhsth=='' or eidos_xrhsth not in ["A","P"]):
            print("Please insert the correct information")
            eidos_xrhsth=input("Συνδεθείτε ως αιτούμενος ή πάροχος εργασίας\nΠατήστε Α για αιτούμενο και P για πάροχο : ")
        """insert input values"""
        self.Insert_in_Xrhsths(email,username,password,eidos_xrhsth)
        return {"Email":email,"Username":username,"Eidos_xrhsth":eidos_xrhsth}

    """--------------------------- CHECK FOR REQUIREMENTS ---------------------------"""
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
        return {"Onoma":onoma,"Eponymo":eponymo,"Hlikia":hlikia,"Fylo":fylo,"Email":email}

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
        return 

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

class Empeiria():

    def __init__(self):
        return

    def Create_education(self,id_ait):
        print("Επιλέξτε την βαθμίδα της εκπαίδευσης σας")
        bathmida=int(input("1:Τριτοβάθμια 2:Πτυχίο 3:Master 4:Διδακτορικό"))
        if(bathmida==1):
            hmnia_enarksis=input("Έναρξη εκπαίδευσης. Χρησιμοποιήστε το format yyyy-mm-dd")
            hmnia_liksis=input("Λήξη εκπαίδευσης. Χρησιμοποιήστε το format yyyy-mm-dd")
            bathmos=int(input("Βαθμός απολυτηρίου: "))
            Empeiria().Insert_ekpaideysi(id_ait,bathmos,hmnia_enarksis,hmnia_liksis,bathmida,0)
        else:
            print("Επιλέξτε ένα από τα παρακάτω πεδία σπουδών")
            search=input("Αναζητήστε το πεδίο σπουδών σας για καλύτερα αποτελέσματα : ")
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
            Empeiria().Insert_ekpaideysi(id_ait,bathmos,hmnia_enarksis,hmnia_liksis,bathmida,id_pediou)
        x=int(input("Αν θέλετε να εισάγετε κι άλλη εκπαίδευση πατήστε 1 αλλιώς πατήστε 2:"))
        if(x==1):
            Empeiria().Create_education(id_ait)
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

    def Create_proyphresia_ypospsifiou(self,id_ait):
        no_work_experience=input("Αν δεν θέλετε να εισάγεται προϋπηρεσία πατήστε 0 αλλίως πατήστε 1")
        if(not no_work_experience):
            return None
        print("Εισάγεται προϋπηρεσία")
        titlos=input("Τίτλος θέσης εργασίας: ")
        while(titlos==''):
            print("Εισάγετε αποδεκτό Τίτλο : ")
            titlos=input("Τίτλος : ")
        paroxos=input("Πάροχος:")
        while(paroxos==''):
            print("Εισάγετε αποδεκτό Πάροχο : ")
            paroxos=input("Πάροχο : ")
        hmnia_enarksis=input("Ημερομηνία έναρξης. Χρησιμοποιήστε το format yyyy-mm-dd:")
        while(hmnia_enarksis==''):
            print("Εισάγετε αποδεκτή Ημερομηνία έναρξης : ")
            hmnia_enarksis=input("Ημερομηνία έναρξης : ")
        hmnia_liksis=input("Ημερομηνία λήξης. Χρησιμοποιήστε το format yyyy-mm-dd\nΑν δουλεύεται ακόα εκεί πιέστε enter")
        if(hmnia_liksis==''):hmnia_liksis="now"
        x=input("Αν θέλετε να εισάγεται και άλλη προυπηρεσία πιέστε 1 αλλιώς 2:")
        if(x==1):Empeiria().Create_proyphresia_ypospsifiou(id_ait)
        else:
            self.Insert_proyphresia(titlos,id_ait,paroxos,hmnia_enarksis,hmnia_liksis)
        return None

    def Insert_proyphresia(self,id_ait,titlos,parochos,hmnia_enarksis,hmnia_liksis):
        conn=db.create_connection(database)
        cur=conn.cursor()
        query = """ INSERT INTO PROYPHRESIA_YPOPSIFIOY (ID_aitoumenou,Titlos,Paroxos,Hmnia_enarksis,Hmnia_liskis) 
                    VALUES ('%d','%d','%s','%s','%d','%d')""" % (id_ait,titlos,parochos,hmnia_enarksis,hmnia_liksis)
        cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
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

class Aggelia():
    def Create_aggelia_erg(self,id_par):
        print("Δημιουργία Αγγελίας \nΕπιλέξτε μία από τις κατηγορίες εργασίας : ")
        search=input("Αναζητήστε την κατηγορία εργασίας για καλύτερα αποτελέσματα : ")
        if(len(search)>5):
            search=search[0:5]
        search=search.lower()
        conn=db.create_connection(database)
        cur=conn.cursor()
        placeholder="'%"+search+"%'"
        query="""SELECT ID_kathgorias,Titlos from KATHGORIA_ERGASIAS WHERE Titlos like %s"""%placeholder
        cur.execute(query)
        titloi=cur.fetchall()
        for i in titloi:print(i)
        id_kathgorias=int(input("Επιλέξτε τον κωδικό της κατηγορίας:"))
        titlos=input("Εισάγετε τίτλο : ")
        topothesia=input("Εισάγετε την πόλη όπου βρίσκεται η θέση εργασίας : ")
        while(topothesia==''):
            print("Εισάγετε αποδεκτή Τοποθεσία : ")
            topothesia=input("Τοποθεσία : ")
        wrario=input("Εισάγετε το ωράριο της θέση εργασίας :" )
        misthos=int(input("Εισάγετε τον μισθό της θέσης εργασίας : "))
        perigrafi=input("Εισάγετε περιγραφή : ")
        typos_ergasias=input("Εισάγετε τον τύπο εργασίας : ")
        proyphresia=input("Εισάγετε απαιτούμενα έτη προϋπηρεσίας : ")
        hmnia_dhmosieusis=date.today()
        self.Insert_in_Aggelia_erg(id_par,id_kathgorias,titlos,topothesia,wrario,misthos,perigrafi,typos_ergasias,proyphresia,hmnia_dhmosieusis)
        return
    
    def Insert_in_Aggelia_erg(self,id_par,id_kathgorias,titlos,topothesia,wrario,misthos,perigrafi,typos_ergasias,proyphresia,hmnia_dhmosieusis):
        id=self.Check_Aggelia_id()
        conn=db.create_connection(database)
        cur=conn.cursor()
        query = """ INSERT INTO AGGELIA_ERGASIAS (ID_aggelias,ID_paroxou,ID_kathgorias_ergasias,Titlos,Topothesia,Wrario,Misthos,Perigrafi,Typos_ergasias,Apaitoumeni_proyphresia,Hmeromhnia_dhmosieusis) 
        VALUES ('%d','%d','%d','%s','%s','%s','%d','%s','%s','%s','%s')""" % (id,id_par,id_kathgorias,titlos,topothesia,wrario,misthos,perigrafi,typos_ergasias,proyphresia,hmnia_dhmosieusis)
        cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
        return
    
    def Check_Aggelia_id(self):
        conn=db.create_connection(database)
        cur=conn.cursor()
        query=""" SELECT ID_aggelias FROM AGGELIA_ERGASIAS ORDER BY ID_aggelias DESC"""
        cur.execute(query)
        id=cur.fetchone()
        cur.close()
        conn.commit()
        conn.close()
        if(id==None):
            return 1
        else:
            print(id[0])
            return id[0]+1

class Apaithsh():
    
    def __init__(self):
        return

    def Create_Apaitoumeni_ekpaideusi(self,id_pediou,bathmos):
        print("Επιλέξτε ένα από τα παρακάτω πεδία σπουδών")
        search=input("Αναζητήστε το πεδίο σπουδών που επιθυμείτε για καλύτερα αποτελέσματα:")
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
            bathmos=input("Βαθμός: \n")
            if(bathmos==''):bathmos=None
            else:bathmos=int(bathmos)
            self.Insert_Apaitoumeni_ekpaideusi(id_pediou,bathmos)
        x=int(input("Αν θέλετε να εισάγετε κι άλλη εκπαίδευση πατήστε 1 αλλιώς πατήστε 2:"))
        if(x==1):
            self.Create_Apaitoumeni_ekpaideusi(self,id_pediou,bathmos)
        else:
            return None

    def Insert_Apaitoumeni_ekpaideusi(id_pediou,bathmos):
        conn=db.create_connection(database)
        cur=conn.cursor()
        query = """ INSERT INTO APAITOUMENI_EKPAIDEYSI (ID_aggelias,ID_paroxou,ID_pediou,bathmos) VALUES ('%d','%d','%d','%s')""" % (id_agg,id_par,id_ped,bathmos)
        cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
        return None

    def Create_Apaitoumeni_proyphresia():
        titlos=input("Τίτλος : ")
        while(titlos==''):
            print("Εισάγετε αποδεκτό Τίτλο : ")
            titlos=input("Τίτλος : ")
        diarkeia=input("Διάρκεια : ")
        while(diarkeia==''):
            print("Εισάγετε αποδεκτή Διάρκεια : ")
            diarkeia=input("Διάρκεια : ")
        Insert_in_Apaitoumeni_proyphresia(titlos,diarkeia)
        return

    def Insert_in_Apaitoumeni_proyphresia(titlos,diarkeia):
        conn9=db.create_connection(database)
        cur=conn9.cursor()
        query = """ INSERT INTO APAITOUMENI_PROYPHRESIA (titlos,diarkeia) VALUES ('%s','%s')""" % (titlos,diarkeia)
        cur.execute(query)
        cur.close()
        conn9.commit()
        conn9.close()
        return None

    def Create_Apaitoumeni_ikanothta():
        titlos_ikanothtas=input("Τίτλος Ικανότητας : ")
        while(titlos_ikanothtas==''):
            print("Εισάγετε αποδεκτό Τίτλο Ικανότητας : ")
            titlos_ikanothtas=input("Τίτλος Ικανότητας : ")
        epipedo=input("Επίπεδο : ")
        while(epipedo==''):
            print("Εισάγετε αποδεκτό Επίπεδο : ")
            epipedo=input("Επίπεδο : ")
        Insert_in_Apaitoumeni_ikanothta(titlos_ikanothtas,epipedo)
        return

    def Insert_in_Apaitoumeni_ikanothta(titlos_ikanothtas,epipedo):
        conn10=db.create_connection(database)
        cur=conn10.cursor()
        query = """ INSERT INTO APAITOUMENI_IKANOTHTA (titlos_ikanothtas,epipedo) VALUES ('%s','%s')""" % (titlos_ikanothtas,epipedo)
        cur.execute(query)
        cur.close()
        conn10.commit()
        conn10.close()
        return None

def User_id_assignement(email):
    conn=db.create_connection(database)
    cur=conn.cursor()
    query="""SELECT User_ID from XRHSTHS WHERE Email='%s'""" % email
    cur.execute(query)
    id=cur.fetchone()
    return id[0]

"""-------------------------------------------"""

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


"""--------------------------- INSERT INPUT DATA VALUES INTO TABLES ---------------------------"""

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
