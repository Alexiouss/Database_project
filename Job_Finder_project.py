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
        query="""SELECT User_ID,Eidos_xrhsth from XRHSTHS where Email='%s' and Password='%s' """ % (email,password)
        cur.execute(query)
        user=cur.fetchone()
        if(user==None):
            print("Λάθος email ή password\nΠροσπαθήστε ξανά")
            email=input("Email:")
            password=input("password:")
            self.Sign_In(email,password)
        else:
            return user

class Empeiria():
    
    def __init__(self):
        return
    
    def Create_education(self,id_ait):
        print("Επιλέξτε την βαθμίδα της εκπαίδευσης σας")
        bathmida=int(input("1:Τριτοβάθμια 2:Πτυχίο 3:Master 4:Διδακτορικό"))
        if(bathmida==1):
            hmnia_enarksis=input("Έναρξη εκπαίδευσης. Χρησιμοποιήστε το format yyyy-mm-dd")
            hmnia_liksis=input("Λήξη εκπαίδευσης.")
            bathmos=int(input("Βαθμός απολυτηρίου\n"))
            Empeiria().Insert_ekpaideysi(id_ait,bathmos,hmnia_enarksis,hmnia_liksis,bathmida,0)
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
            hmnia_liksis=input("Λήξη εκπαίδευσης:")
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

    def Create_proyphresia(self,id_ait):
        no_work_experience=input("Αν δεν θέλετε να εισάγεται προϋπηρεσία πατήστε 0 αλλίως πατήστε 1:")
        if(no_work_experience==0):
            return None
        Select_kathgories_ergasias()
        kathgoria=int(input("Επιλέξτε μία κατηγορία εργασίας από τις παρακάτω σύμφωνα με το id της"))
        titlos=input("Καταχωρήστε τον τίτλο εργασίας σας:")
        paroxos=input("Πάροχος:")
        Hmnia_enarksis=input("Ημερομηνία έναρξης. Χρησιμοποιήστε το format yyyy-mm-dd:")
        Hmnia_liksis=input("Ημερομηνία λήξης. Χρησιμοποιήστε το format yyyy-mm-dd\nΑν δουλεύεται ακόμα εκεί πιέστε enter")
        if(Hmnia_liksis==''):Hmnia_liksis="now"
        x=input("Αν θέλετε να εισάγεται και άλλη προυπηρεσία πιέστε 1 αλλιώς 2:")
        if(x==1):Empeiria().Create_proyphresia(id_ait)
        else:
            self.Insert_proyphresia(id_ait,kathgoria,titlos,paroxos,Hmnia_enarksis,Hmnia_liksis)
        return None

    def Insert_proyphresia(self,id_ait,kathgoria,titlos,parochos,Hmnia_enarksis,Hmnia_liksis):
        conn=db.create_connection(database)
        cur=conn.cursor()
        query = """ INSERT INTO PROYPHRESIA_YPOPSIFIOY (ID_aitoumenou,ID_kathgorias_ergasias,Titlos,Paroxos,Hmnia_enarksis,Hmnia_liskis) 
                    VALUES ('%d','%d','%s','%s','%s','%s')""" % (id_ait,kathgoria,titlos,parochos,Hmnia_enarksis,Hmnia_liksis)
        cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
        return None

    def Create_Ikanothta_ypopsifiou(self,id_ait):
        x=int(input("Εάν θέλετε να εισάγεται ικανότητες πιέστε 1 αλλίως πιέστε 0:"))
        if(x==0):
            return None
        Kathgoria_skill=int(input("Επιλέξτε Hard skill ή soft skill. Πιέστε 1 για hard 2 για soft:"))
        print("Διαλέξτε 0 ή παραπάνω από τις παρακάτω ικανότητες")
        Select_kathgoria_ikanotitas(Kathgoria_skill)
        ikanotites=[int(ikanotita) for ikanotita in input().split()]
        self.Insert_ikanothta(id_ait,ikanotites)
        self.Create_Ikanothta_ypopsifiou(id_ait)
        return None
    
    def Insert_ikanothta_ypopsifioy(self,id_ait,ikanotites):
        conn=db.create_connection(database)
        cur=conn.cursor()
        for i in range(len(ikanotites)):
            query = """ INSERT INTO KATEXEI_IKANOTHTA (ID_aitoumenou,ID_ikanothtas) 
                        VALUES ('%d','%d')""" % (id_ait,ikanotites[i])
            cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
        return None

class Aggelia():
    def Create_aggelia_erg(self,id_par):
        print("Δημιουργία Αγγελίας \nΕπιλέξτε μία από τις κατηγορίες εργασίας : ")
        Select_kathgories_ergasias()
        id_kathgorias=int(input("Επιλέξτε τον κωδικό της κατηγορίας:"))
        titlos=input("Εισάγετε τίτλο : ")
        topothesia=input("Εισάγετε την πόλη όπου βρίσκεται η θέση εργασίας : ")
        while(topothesia==''):
            print("Εισάγετε αποδεκτή Τοποθεσία : ")
            topothesia=input("Τοποθεσία : ")
        wrario=input("Εισάγετε το ωράριο της θέση εργασίας :" )
        misthos=int(input("Εισάγετε τον μισθό της θέσης εργασίας : "))
        perigrafi=input("Εισάγετε περιγραφή : ")
        proyphresia=int(input("Εισάγετε απαιτούμενα έτη προϋπηρεσίας : "))
        hmnia_dhmosieusis=date.today()
        id=self.Insert_in_Aggelia_erg(id_par,id_kathgorias,titlos,topothesia,wrario,misthos,perigrafi,proyphresia,hmnia_dhmosieusis)
        Apaithsh().Create_Apaitoumeni_ekpaideusi(id,id_par)
        Apaithsh().Create_Apaitoumeni_ikanothta(id,id_par)
        return

    def Insert_in_Aggelia_erg(self,id_par,id_kathgorias,titlos,topothesia,wrario,misthos,perigrafi,proyphresia,hmnia_dhmosieusis):
        id=self.Check_Aggelia_id()
        conn=db.create_connection(database)
        cur=conn.cursor()
        query = """ INSERT INTO AGGELIA_ERGASIAS (ID_aggelias,ID_paroxou,ID_kathgorias_ergasias,Titlos,Topothesia,Wrario,Misthos,Perigrafi,Apaitoumeni_proyphresia,Hmeromhnia_dhmosieusis) 
        VALUES ('%d','%d','%d','%s','%s','%s','%d','%s','%d','%s')""" % (id,id_par,id_kathgorias,titlos,topothesia,wrario,misthos,perigrafi,proyphresia,hmnia_dhmosieusis)
        cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
        return id
    
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

    def Create_Apaitoumeni_ekpaideusi(self,ID_aggelias,id_par):
        print("Eπιλέξτε το επίπεδο εκπαίδευσης του υποψηφίου")
        bathmida=int(input("1:Τριτοβάθμια 2:Πτυχίο 3:Master 4:Διδακτορικό"))
        if(bathmida==1):
            self.Insert_Apaitoumeni_ekpaideusi(int(ID_aggelias),int(id_par),0,bathmida)
            x=int(input("Αν θέλετε να εισάγετε κι άλλη εκπαίδευση πατήστε 1 αλλιώς πατήστε 2:"))
            if(x==1):
                self.Create_Apaitoumeni_ekpaideusi(ID_aggelias,id_par)
            else:
                return None
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
        self.Insert_Apaitoumeni_ekpaideusi(int(ID_aggelias),int(id_par),id_pediou,bathmida)
        x=int(input("Αν θέλετε να εισάγετε κι άλλη εκπαίδευση πατήστε 1 αλλιώς πατήστε 2:"))
        if(x==1):
            self.Create_Apaitoumeni_ekpaideusi(ID_aggelias,id_par)
        else:
            return None

    def Insert_Apaitoumeni_ekpaideusi(self,ID_aggelias,id_par,id_pediou,bathmida):
        conn=db.create_connection(database)
        cur=conn.cursor()
        query = """ INSERT INTO APAITOUMENI_EKPAIDEYSI (ID_aggelias,ID_paroxou,ID_pediou,Elaxisth_bathmida) 
                    VALUES ('%d','%d','%d','%d')""" % (ID_aggelias,id_par,id_pediou,bathmida)
        cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
        return None

    def Create_Apaitoumeni_ikanothta(self,ID_aggelias,id_par):
        x=int(input("Εάν θέλετε να εισάγεται ικανότητες πιέστε 1 αλλίως πιέστε 0:"))
        if(x==0):
            return None
        Kathgoria_skill=int(input("Επιλέξτε Hard skill ή soft skill. Πιέστε 1 για hard 2 για soft:"))
        print("Διαλέξτε 0 ή παραπάνω από τις παρακάτω ικανότητες")
        Select_kathgoria_ikanotitas(Kathgoria_skill)
        ikatonites=[int(ikanotita) for ikanotita in input().split()]
        self.Insert_in_Apaitoumeni_ikanothta(ID_aggelias,id_par,ikatonites)
        self.Create_Apaitoumeni_ikanothta(ID_aggelias,id_par)
        return None


    def Insert_in_Apaitoumeni_ikanothta(self,ID_aggelias,id_par,ikanotites):
        conn=db.create_connection(database)
        cur=conn.cursor()
        for i in range(len(ikanotites)):
            query = """ INSERT INTO APAITEI_IKANOTHTA (ID_aggelias,ID_paroxou,ID_ikanothtas) 
                        VALUES ('%d','%d','%d')""" % (ID_aggelias,id_par,ikanotites[i])
            cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
        return None

class Anazhthsh_aggelion():
    def __init__(self):
        return
    
    def Search_aggelies(self):
        Filters={}
        print("Αναζήτηση αγγελιών\nΦίλτρα αναζήτησης(Κατηγορία εργασίας,Τίτλος θέσης,Ωράριο,Μισθός,Τύπος εργασίας,Απαιτούμενη προϋπηρεσία)")
        print("Αν δεν θέλετε αναζήτηση με κάποιο φίλτρο πατήστε enter")
        Select_kathgories_ergasias()
        try:Filters['ID_kathgorias_ergasias']=int(input("Επιλέξτε μία κατηγορία εργασίας από τις παρακάτω σύμφωνα με το id της"))
        except:Filters.update({'ID_kathgorias_ergasias':''})
        Filters.update({'Titlos':input("Καταχωρήστε τίτλο εργασίας:")})
        titlos=Filters['Titlos']
        if(len(titlos)>5):
            titlos[0].upper()  
            Filters['Titlos'] = titlos[0:5]
        Filters['Topothesia']=input("Καταχωρήστε την τοποθεσία(πόλη):")
        try:Filters['Topothesia'][0].upper()
        except:Filters['Topothesia']=''
        try:Filters['Wrario']=input("Εισάγεται τις ώρες/μέρα εργασίας:")
        except:Filters['Wrario']=''
        try:Filters['Misthos']=int(input("Εισάγεται τον ελάχιστο μισθό:"))
        except:Filters['Misthos']=''
        try:Filters['Apaitoumeni_proyphresia']=int(input("Εισάγεται τον ελάχιστο χρόνο προϋπηρεσίας σε χρόνια:"))
        except:Filters['Apaitoumeni_proyphresia']=''
        not_filters=[]
        for i in Filters.keys():
            if(Filters[i]==''):
                not_filters.append(i)
        for filter in not_filters:
            del Filters[filter]
        self.Select_aggelies_to_show(Filters)
        return None

    def Select_aggelies_to_show(self,Filters):
        conn=db.create_connection(database)
        cur=conn.cursor()
        filters_keys=[]
        filters_values=[]
        for i in Filters.keys():
            filters_keys.append(i)
        for i in Filters.values():
            filters_values.append(i)
        query="""SELECT P.Eponymia,A.ID_aggelias,A.Titlos,A.Topothesia,A.Wrario,A.Misthos,A.Perigrafi,A.Apaitoumeni_proyphresia,
        A.Hmeromhnia_dhmosieusis,E.Titlos as pedio_ergasias
        FROM AGGELIA_ERGASIAS AS A,PROFIL_PAROXOU as P,KATHGORIA_ERGASIAS as E
        WHERE A.ID_paroxou=P.ID_paroxou 
        and A.ID_kathgorias_ergasias=E.ID_kathgorias"""
        if(len(Filters)!=0):
            query+=" and ( "
        
        for i in range(len(filters_keys)):
            if(filters_keys[i]=='Misthos' or filters_keys[i]=="Apaitoumenh_proyphresia"):
                if(i==len(filters_keys)-1):
                    query+=("A."+str(filters_keys[i])+">=%d"%(filters_values[i])+")")
                else:
                    query+=("A."+str(filters_keys[i])+">=%d"%(filters_values[i])+" and ")
            else:
                if(i==len(filters_keys)-1):
                    query+=("A."+str(filters_keys[i])+"='%s'"%(filters_values[i])+")")
                else:
                    query+=("A."+str(filters_keys[i])+"='%s'"%(filters_values[i])+" and ")
        cur.execute(query)
        data=cur.fetchall()
        cur.close()
        list_of_attributes=["Πάροχος","ID_αγγελίας","Τίτλος θέσης εργασίας","Τοποθεσία εργασίας","Ωράριο","Μισθός","Περιγραφή",
                            "Απαιτούμενη προϋπηρεσία","Ημερομηνία δημοσίευσης","Πεδίο εργασίας"]
        ekpaideysi=[]
        cur1=conn.cursor()
        for i in range(len(data)):
            query_1="""SELECT SP.Titlos,AE.Elaxisth_bathmida 
                        FROM PEDIO_SPOUDON as SP,APAITOUMENI_EKPAIDEYSI AS AE,AGGELIA_ERGASIAS AS A
                        WHERE SP.ID_pediou=AE.ID_pediou 
                        and A.ID_aggelias=AE.ID_aggelias and A.ID_aggelias=%d"""%data[i][1]
            cur1.execute(query_1)
            temp_data=cur1.fetchall()
            ekpaideysi.append(temp_data)
        cur1.close()
        ikanotites=[]
        cur2=conn.cursor()
        for i in range(len(data)):
            query_2="""SELECT IK.Onoma,IK.Kathgoria FROM IKANOTHTA AS IK,APAITEI_IKANOTHTA AS AI,AGGELIA_ERGASIAS AS A
                    WHERE A.ID_aggelias=AI.ID_aggelias and AI.ID_ikanothtas=IK.ID_skill and A.ID_aggelias=%d"""%data[i][1]
            cur2.execute(query_2)
            temp_data=cur2.fetchall()
            ikanotites.append(temp_data)
        cur2.close()
        ar_aggelias=1
        for j in range(len(data)):
            print("Αγγελία "+str(ar_aggelias))
            ar_aggelias+=1
            for i in range(len(list_of_attributes)):
                print(list_of_attributes[i]+": "+str(data[j][i]))
            print("Απαιτούμενη εκπαίδευση,Βαθμίδα:",end='')
            for l in range(len(ekpaideysi[j])):
                if(l==len(ekpaideysi[j])-1):print(ekpaideysi[j][l])
                else:print(ekpaideysi[j][l],end=',')
            print("Ικανότητες:",end='')
            for k in range(len(ikanotites[j])):
                if(k==len(ikanotites[j])-1):print(ikanotites[j][k])
                else:print(ikanotites[j][k],end=',')
        return None

class Aithsh():
    def __init__(self):
        return
    def Create_Aithsh(self,id_ait):
        id_aggelias=int(input("Διαλέξτε την αγγελία για την οποία θέλετε να κάνετε αίτηση:"))
        conn=db.create_connection(database)
        cur=conn.cursor()
        query="""SELECT ID_paroxou 
                FROM AGGELIA_ERGASIAS 
                WHERE ID_aggelias=%d"""%(id_aggelias)
        cur.execute(query)
        id_par=cur.fetchone()
        hm_nia=date.today()
        self.Insert_into_aithsh(id_ait,id_par[0],id_aggelias,hm_nia)
        cur.close()
        return None
    
    def Insert_into_aithsh(self,id_ait,id_paroxou,id_aggelias,hm_nia):
        conn=db.create_connection(database)
        cur=conn.cursor()
        query="""INSERT INTO AITHSH (ID_aitoumenou,ID_paroxou,ID_aggelias,Hmeromhnia_aithshs)
                VALUES('%d','%d','%d','%s')"""%(id_ait,id_paroxou,id_aggelias,hm_nia)
        cur.execute(query)
        cur.close()
        conn.commit()
        conn.close()
        return None

class Aksiologhsh():
    def __init__(self):
        return None
    
    def Create_aksiologhsh(self,id_ait):
        print("Αξιολογήστε κάποιον πάροχο.Διαλέξτε σύμφωνα με το ID του παρόχου.")
        conn=db.create_connection(database)
        cur=conn.cursor()
        query="""SELECT ID_paroxou,Eponymia
                FROM PROFIL_PAROXOU"""
        cur.execute(query)
        data=cur.fetchall()
        cur.close()
        conn.close()
        for i in data:print(i)
        id_par=int(input())
        bathmos=int(input("Βαθμολογήστε τον πάροχο με μέγιστο το 5 και ελάχιστο το 1:"))
        hm_nia_aksiiologisis=date.today()
        self.Insert_into_askiologhsh(id_par,id_ait,bathmos,hm_nia_aksiiologisis)

    def Insert_into_askiologhsh(self,ID_par,ID_ait,Bathmologia,Hm_nia):
        conn=db.create_connection(database)
        cur=conn.cursor()
        query="""INSERT INTO AKSIOLOGHSH (ID_paroxou,ID_aitoumenou,Bathmologia,Hmeromhnia_aksiologishs)
                VALUES('%d','%d','%d','%s')"""%(ID_par,ID_ait,Bathmologia,Hm_nia)
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

def Select_kathgories_ergasias():
    search=input("Αναζητήστε την κατηγορία εργασίας για καλύτερα αποτελέσματα: Αν θέλετε να δείτε όλες τις κατηγορίες πατήστε 0:")
    conn=db.create_connection(database)
    cur=conn.cursor()
    if(search=='0'):
        query="""SELECT ID_kathgorias,Titlos from KATHGORIA_ERGASIAS"""
        cur.execute(query)
        titloi=cur.fetchall()
        for i in titloi:print(i)
        cur.close()
        conn.close()
        return None
    else:
        if(len(search)>5):
            search=search[0:5]
        search=search.lower()
        placeholder="'%"+search+"%'"
        query="""SELECT ID_kathgorias,Titlos from KATHGORIA_ERGASIAS WHERE Titlos like %s"""%placeholder
        cur.execute(query)
        titloi=cur.fetchall()
        for i in titloi:print(i)
        cur.close()
        conn.close()
        return None

def Select_kathgoria_ikanotitas(kathgoria_ikanotitas):
    conn=db.create_connection(database)
    cur=conn.cursor()
    if(kathgoria_ikanotitas==1):
        query="""SELECT ID_skill,Onoma from IKANOTHTA WHERE Kathgoria='Hard'"""
    else:
        query="""SELECT ID_skill,Onoma from IKANOTHTA WHERE Kathgoria='Soft'"""
    cur.execute(query)
    data=cur.fetchall()
    for i in data:print(i)
    return None
