import sqlite3
from sqlite3 import Error
import Job_Finder_project as jf

NumofTables=15

def create_connection(db_file):
    conn=None
    try:
        conn=sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn,create_table_sql):
    try:
        c=conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def tables():

    Tables=[None]*NumofTables

    Tables[0]="""CREATE TABLE IF NOT EXISTS XRHSTHS(
                                User_ID INTEGER NOT NULL,
                                email VARCHAR(50) NOT NULL UNIQUE,
                                username VARCHAR(20) NOT NULL UNIQUE,
                                password VARCHAR(20) NOT NULL,
                                eidos_xrhsth VARCHAR(1) NOT NULL,
                                PRIMARY KEY(User_ID)
                                );"""

    Tables[1]="""CREATE TABLE IF NOT EXISTS PROFIL_AITOUMENOY(
                                ID_aitoumenou INTEGER NOT NULL,
                                onoma VARCHAR(30) NOT NULL,
                                eponymo VARCHAR(30) NOT NULL,
                                hlikia INTEGER NOT NULL,
                                fylo VARCHAR(5),
                                PRIMARY KEY(ID_aitoumenou),
                                FOREIGN KEY(ID_aitoumenou) REFERENCES XRHSTHS(User_ID)
                                ON UPDATE CASCADE
                                ON DELETE CASCADE
                                );"""

    Tables[2]="""CREATE TABLE IF NOT EXISTS PROFIL_PAROXOU(
                                ID_paroxou INTEGER NOT NULL,
                                eponymia VARCHAR(20) NOT NULL,
                                perigrafh TEXT NOT NULL,
                                dieythynsh VARCHAR(50) NOT NULL,
                                thlefono VARCHAR(10) NOT NULL,
                                bathmologia INTEGER,
                                PRIMARY KEY(ID_paroxou),
                                FOREIGN KEY(ID_paroxou) REFERENCES XRHSTHS(User_ID)
                                ON UPDATE CASCADE
                                ON DELETE CASCADE
                                );"""

    Tables[3]="""CREATE TABLE IF NOT EXISTS EKPAIDEYSH_YPOPSIFIOY(
                                ID_aitoumenou INTEGER NOT NULL,
                                Bathmos INTEGER,
                                Hmnia_enarksis DATE NOT NULL DEFAULT '0000-00-00',
                                Hmnia_liksis DATE NOT NULL DEFAULT '0000-00-00',
                                Bathmida INTEGER,
                                ID_pediou INTEGER DEFAULT NULL,
                                PRIMARY KEY(ID_aitoumenou),
                                FOREIGN KEY(ID_aitoumenou) REFERENCES PROFIL_AITOUMENOY(ID_aitoumenou)
                                ON UPDATE NO ACTION
                                ON DELETE CASCADE,
                                FOREIGN KEY(ID_pediou) REFERENCES PEDIO_SPOUDON(Id_pediou)
                                ON UPDATE CASCADE
                                ON DELETE NO ACTION
                                );"""

    Tables[4]="""CREATE TABLE IF NOT EXISTS PEDIO_SPOUDON(
                                ID_pediou INTEGER NOT NULL,
                                Titlos VARCHAR(50) NOT NULL UNIQUE,
                                PRIMARY KEY(ID_pediou)
                                );"""

    Tables[5]="""CREATE TABLE IF NOT EXISTS PROYPHRESIA_YPOPSIFIOY(
                                ID_aitoumenou INTEGER NOT NULL,
                                Titlos VARCHAR(100) NOT NULL,
                                Paroxos VARCHAR(100) NOT NULL,
                                Hmnia_enarksis DATE NOT NULL DEFAULT '0000-00-00',
                                Hmnia_liskis DATE DEFAULT NULL,
                                PRIMARY KEY(ID_aitoumenou,Hmnia_enarksis),
                                FOREIGN KEY(ID_aitoumenou) REFERENCES PROFIL_AITOUMENOY(ID_aitoumenou)
                                ON UPDATE NO ACTION
                                ON DELETE CASCADE
                                );"""

    Tables[6]="""CREATE TABLE IF NOT EXISTS IKANOTITA_YPOPSIFIOY(
                                ID_aitoumenou INTEGER NOT NULL,
                                Titlos_kathgorias VARCHAR(50) NOT NULL,
                                Titlos_ikanothtas VARCHAR(50) NOT NULL,
                                Epipedo INTEGER NOT NULL DEFAULT 0,
                                ID_kathgorias INTEGER NOT NULL,
                                PRIMARY KEY(ID_aitoumenou,ID_kathgorias,Titlos_ikanothtas),
                                FOREIGN KEY(ID_aitoumenou) REFERENCES PROFIL_AITOUMENOY(ID_aitoumenou)
                                ON UPDATE NO ACTION
                                ON DELETE CASCADE,
                                FOREIGN KEY(ID_kathgorias) REFERENCES KATHGORIA_IKANOTITAS(ID_kathgorias)
                                ON UPDATE CASCADE
                                ON DELETE NO ACTION
                                );
                                """

    Tables[7]="""CREATE TABLE IF NOT EXISTS KATHGORIA_IKANOTITAS(
                                ID_kathgorias INTEGER NOT NULL,
                                Titlos VARCHAR(50) UNIQUE,
                                PRIMARY KEY(ID_kathgorias)
                                );"""

    Tables[8]="""CREATE TABLE IF NOT EXISTS AGGELIA_ERGASIAS(
                                ID_aggelias INTEGER NOT NULL,
                                ID_paroxou INTEGER NOT NULL,
                                Topothesia VARCHAR(50) NOT NULL,
                                Wrario VARCHAR(30),
                                Misthos INTEGER,
                                Perigrafi TEXT,
                                Typos_ergasias VARCHAR(50),
                                Titlos VARCHAR(100),
                                Hmeromhnia_dhmosieusis DATE NOT NULL,
                                PRIMARY KEY(ID_aggelias,ID_paroxou),
                                FOREIGN KEY(ID_paroxou) REFERENCES PROFIL_PAROXOU(ID_paroxou)
                                ON UPDATE NO ACTION
                                ON DELETE CASCADE
                                );"""

    Tables[9]="""CREATE TABLE IF NOT EXISTS APAITOUMENI_EKPAIDEYSI(
                                ID_aggelias INTEGER NOT NULL,
                                ID_paroxou INTEGER NOT NULL,
                                ID_pediou INTEGER,
                                Bathmos VARCHAR(20),
                                PRIMARY KEY(ID_aggelias,ID_paroxou),
                                FOREIGN KEY(ID_aggelias) REFERENCES AGGELIA_ERGASIAS(ID_aggelias)
                                ON UPDATE CASCADE
                                ON DELETE CASCADE,
                                FOREIGN KEY(ID_paroxou) REFERENCES AGGELIA_ERGASIAS(ID_paroxou)
                                ON UPDATE NO ACTION
                                ON DELETE CASCADE,
                                FOREIGN KEY(ID_pediou) REFERENCES PEDIO_SPOUDON(ID_pediou)
                                ON UPDATE CASCADE
                                ON DELETE NO ACTION
                                );"""

    Tables[10]="""CREATE TABLE IF NOT EXISTS APAITOUMENI_PROYPHRESIA(
                                ID_aggelias INTEGER NOT NULL,
                                ID_paroxou INTEGER NOT NULL,
                                Titlos VARCHAR(50) NOT NULL,
                                Diarkeia INTEGER DEFAULT NULL,
                                PRIMARY KEY(ID_aggelias,ID_paroxou),
                                FOREIGN KEY(ID_aggelias) REFERENCES AGGELIA_ERGASIAS(ID_aggelias)
                                ON UPDATE CASCADE
                                ON DELETE CASCADE,
                                FOREIGN KEY(ID_paroxou) REFERENCES AGGELIA_ERGASIAS(ID_paroxou)
                                ON UPDATE NO ACTION
                                ON DELETE CASCADE
                                );"""

    Tables[11]="""CREATE TABLE IF NOT EXISTS APAITOUMENI_IKANOTHTA(
                                ID_aggelias INTEGER NOT NULL,
                                ID_paroxou INTEGER NOT NULL,
                                Epipedo VARCHAR(20) NOT NULL,
                                ID_kathgorias INTEGER NOT NULL,
                                PRIMARY KEY(ID_aggelias,ID_paroxou),
                                FOREIGN KEY(ID_aggelias) REFERENCES AGGELIA_ERGASIAS(ID_aggelias)
                                ON UPDATE CASCADE
                                ON DELETE CASCADE,
                                FOREIGN KEY(ID_paroxou) REFERENCES AGGELIA_ERGASIAS(ID_paroxou)
                                ON UPDATE NO ACTION
                                ON DELETE CASCADE,
                                FOREIGN KEY(ID_kathgorias) REFERENCES KATHGORIA(ID_kathgorias)
                                ON UPDATE CASCADE
                                ON DELETE NO ACTION
                                );"""

    Tables[12]="""CREATE TABLE IF NOT EXISTS AITHSH(
                                    ID_aitoumenou INTEGER NOT NULL,
                                    ID_aithshs INTEGER NOT NULL,
                                    ID_paroxou INTEGER NOT NULL,
                                    ID_aggelias INTEGER NOT NULL,
                                    Hmeromhnia_aithshs DATE NOT NULL,
                                    PRIMARY KEY(ID_aithshs),
                                    FOREIGN KEY(ID_aitoumenou) REFERENCES PROFIL_AITOUMENOU(ID_aitoumenou)
                                    ON UPDATE NO ACTION
                                    ON DELETE NO ACTION,
                                    FOREIGN KEY(ID_aggelias) REFERENCES AGGELIA_ERGASIAS(ID_aggelias)
                                    ON UPDATE NO ACTION
                                    ON DELETE NO ACTION,
                                    FOREIGN KEY(ID_paroxou) REFERENCES AGGELIA_ERGASIAS(ID_paroxou)
                                    ON UPDATE NO ACTION
                                    ON DELETE NO ACTION
                                    );"""

    Tables[13]="""CREATE TABLE IF NOT EXISTS SYNTEYKSI(
                                    ID_aithshs INTEGER NOT NULL,
                                    Hmeromhnia_synenteyksis DATE NOT NULL DEFAULT '0000-00-00',
                                    PRIMARY KEY(ID_aithshs),
                                    FOREIGN KEY(ID_aithshs) REFERENCES AITHSH(ID_aithshs)
                                    ON UPDATE NO ACTION
                                    ON DELETE NO ACTION
                                    );"""

    Tables[14]="""CREATE TABLE IF NOT EXISTS AKSIOLOGHSH(
                                    ID_aksiologhshs INTEGER NOT NULL,
                                    ID_paroxou INTEGER NOT NULL,
                                    ID_aitoumenou INTEGER NOT NULL,
                                    Bathmologia INTEGER NOT NULL,
                                    Hmeromhnia_aksiologishs DATE NOT NULL DEFAULT '0000-00-00',
                                    Perilipsi text,
                                    PRIMARY KEY(ID_aksiologhshs),
                                    FOREIGN KEY(ID_paroxou) REFERENCES PROFIL_PAROXOU(ID_paroxou)
                                    ON UPDATE NO ACTION
                                    ON DELETE NO ACTION,
                                    FOREIGN KEY(ID_aitoumenou) REFERENCES PROFIL_AITOUMENOU(ID_aitoumenou)
                                    ON UPDATE NO ACTION
                                    ON DELETE NO ACTION
                                    );"""
    
    return Tables

def main():
    database="DB_project.db"
    sql_create_tables=tables()
    """conn"""
    conn=create_connection(database)
    for i in range(0,NumofTables):
        if conn is not None:
            create_table(conn,sql_create_tables[i])
        else:
            print("ERROR ERROR ERROR")
    in_pedio_spoudon(conn)
    in_kathgoria(conn)
    conn.commit()
    conn.close()
    
    """conn1"""
    print("-----Welcome to Job_Finder-----Please create account if you dont have one\nAlready have an account?\nPress Sign in to continue\n")
    neos_xrhsths=input("Νέος χρήσητης; Ν/Ο : ")
    while (neos_xrhsths=='N'):
        print("Press 1 for Sign up or 2 for Sign in")
        signing=int(input())
        if(signing==1):
            jf.Sign_UP()
            neos_xrhsths=input("Νέος χρήσητης; Ν/Ο : ")
        elif(signing==2):
            jf.SignIn()

def in_pedio_spoudon(conn):
    cur= conn.cursor()
    insertion1="""INSERT INTO PEDIO_SPOUDON
            (Titlos)
            VALUES('ΑΓΡΟΝΟΜΟΣ - ΤΟΠΟΓΡΑΦΟΣ ΜΗΧΑΝΙΚΟΣ'),
            ('ΑΓΡΟΤΟΟΙΚΟΝΟΜΟΛΟΓΟΣ'),
            ('ΑΙΣΘΗΤΙΚΟΣ'),
            ('ΑΝΘΡΩΠΟΛΟΓΟΣ'),
            ('ΑΝΘΥΠΟΠΥΡΑΓΟΣ'),
            ('ΑΞΙΩΜΑΤΙΚΟΣ ΑΕΡΟΠΟΡΙΑΣ'),
            ('ΑΞΙΩΜΑΤΙΚΟΣ ΝΑΥΤΙΚΟΥ'),
            ('ΑΞΙΩΜΑΤΙΚΟΣ ΣΤΡΑΤΟΥ'),
            ('ΑΡΧΕΙΟΝΟΜΟΣ - ΒΙΒΛΙΟΘΗΚΟΝΟΜΟΣ'),
            ('ΑΡΧΙΤΕΚΤΟΝΑΣ ΜΗΧΑΝΙΚΟΣ'),
            ('ΑΣΤΥΝΟΜΙΚΟΣ - ΥΠΑΣΤΥΝΟΜΟΣ'),
            ('ΑΣΤΥΦΥΛΑΚΑΣ - ΑΡΧΙΦΥΛΑΚΑΣ'),
            ('ΒΑΛΚΑΝΙΟΛΟΓΟΣ'),
            ('ΒΑΣΕΙΣ ΚΥΠΡΟΥ'),
            ('ΒΙΒΛΙΟΘΗΚΟΝΟΜΟΣ'),
            ('ΒΙΟΛΟΓΟΣ'),
            ('ΒΙΟΛΟΓΟΣ - ΓΕΝΕΤΙΣΤΗΣ'),
            ('ΒΙΟΛΟΓΟΣ ΕΦΑΡΜΟΓΩΝ & ΤΕΧΝΟΛΟΓΙΩΝ'),
            ('ΒΙΟΤΕΧΝΙΚΟΣ'),
            ('ΒΙΟΧΗΜΙΚΟΣ - ΒΙΟΤΕΧΝΙΚΟΣ'),
            ('ΒΡΕΦΟΝΗΠΙΟΚΟΜΟΣ'),
            ('ΒΥΖΑΝΤΙΝΟΣ ΜΟΥΣΕΙΟΛΟΓΟΣ'),
            ('ΓΕΩΓΡΑΦΟΣ'),
            ('ΓΕΩΛΟΓΟΣ'),
            ('ΓΕΩΠΟΝΟΣ'),
            ('ΓΕΩΠΟΝΟΣ - ΒΙΟΤΕΧΝΙΚΟΣ'),
            ('ΓΕΩΠΟΝΟΣ - ΜΗΧΑΝΟΛΟΓΟΣ'),
            ('ΓΕΩΠΟΝΟΣ - ΜΗΧΑΝΟΛΟΓΟΣ ΤΡΟΦΙΜΩΝ'),
            ('ΓΕΩΠΟΝΟΣ ΖΩΙΚΗΣ ΠΑΡΑΓΩΓΗΣ'),
            ('ΓΕΩΠΟΝΟΣ ΦΥΤΙΚΗΣ ΠΑΡΑΓΩΓΗΣ'),
            ('ΓΕΩΤΕΧΝΙΚΟΣ - ΠΕΡΙΒΑΛΛΟΝΤΟΛΟΓΟΣ'),
            ('ΓΙΑΤΡΟΣ'),
            ('ΓΙΑΤΡΟΣ ΣΤΡΑΤΙΩΤΙΚΟΣ'),
            ('ΓΡΑΦΙΣΤΑΣ'),
            ('ΓΥΜΝΑΣΤΗΣ'),
            ('ΔΑΣΚΑΛΟΣ'),
            ('ΔΑΣΟΛΟΓΟΣ - ΠΕΡΙΒΑΛΛΟΝΤΟΛΟΓΟΣ'),
            ('ΔΗΜΟΣΙΟΓΡΑΦΟΣ'),
            ('ΔΗΜΟΣΙΟΓΡΑΦΟΣ - ΕΠΙΚΟΙΝΩΝΙΟΛΟΓΟΣ'),
            ('ΔΙΑΙΤΟΛΟΓΟΣ'),
            ('ΔΙΑΚΟΣΜΗΤΗΣ'),
            ('ΔΙΑΤΡΟΦΟΛΟΓΟΣ'),
            ('ΔΙΑΦΗΜΙΣΤΗΣ'),
            ('ΔΙΕΘΝΟΛΟΓΟΣ'),
            ('ΔΙΕΘΝΟΛΟΓΟΣ - ΟΙΚΟΝΟΜΟΛΟΓΟΣ'),
            ('ΔΙΕΘΝΟΛΟΓΟΣ ΜΕΣΟΓΕΙΑΚΩΝ ΣΠΟΥΔΩΝ'),
            ('ΔΙΟΙΚΗΤΙΚΟΣ ΞΕΝΩΝ ΓΛΩΣΣΩΝ'),
            ('ΕΙΚΑΣΤΙΚΟΣ'),
            ('ΕΚΠΑΙΔΕΥΤΙΚΟΣ - ΚΟΙΝΩΝΙΟΛΟΓΟΣ'),
            ('ΕΛΕΓΚΤΗΣ - ΑΣΦΑΛΙΣΤΗΣ'),
            ('ΕΜΠΟΡΟΠΛΟΙΑΡΧΟΣ - ΜΗΧΑΝΙΚΟΣ ΕΜΠΟΡΙΚΟΥ ΝΑΥΤΙΚΟΥ'),
            ('ΕΠΙΚΟΙΝΩΝΙΟΛΟΓΟΣ'),
            ('ΕΠΙΚΟΙΝΩΝΙΟΛΟΓΟΣ - ΤΕΧΝΙΚΟΣ ΠΟΛΙΤΙΣΜΟΥ'),
            ('ΕΡΓΟΘΕΡΑΠΕΥΤΗΣ'),
            ('ΗΛΕΚΤΡΟΛΟΓΟΣ ΜΗΧΑΝΙΚΟΣ - ΠΛΗΡΟΦΟΡΙΚΟΣ'),
            ('ΘΑΛΑΣΣΟΛΟΓΟΣ'),
            ('ΘΕΑΤΡΟΛΟΓΟΣ'),
            ('ΘΕΑΤΡΟΛΟΓΟΣ - ΣΚΗΝΟΘΕΤΗΣ - ΗΘΟΠΟΙΟΣ'),
            ('ΘΕΟΛΟΓΟΣ'),
            ('ΘΕΩΡΗΤΙΚΟΣ ΤΩΝ ΕΠΙΣΤΗΜΩΝ - ΙΣΤΟΡΙΚΟΣ'),
            ('ΙΕΡΕΑΣ'),
            ('ΙΣΤΟΡΙΚΟΣ'),
            ('ΙΣΤΟΡΙΚΟΣ - ΑΡΧΑΙΟΛΟΓΟΣ'),
            ('ΙΣΤΟΡΙΚΟΣ - ΑΡΧΑΙΟΛΟΓΟΣ - ΛΑΟΓΡΑΦΟΣ'),
            ('ΙΣΤΟΡΙΚΟΣ - ΕΘΝΟΛΟΓΟΣ'),
            ('ΙΧΘΥΟΚΟΜΟΣ'),
            ('ΚΑΛΙΤΕΧΝΗΣ'),
            ('ΚΙΝΗΜΑΤΟΓΡΑΦΙΣΤΗΣ'),
            ('ΚΛΩΣΤΟΫΦΑΝΤΟΥΡΓΟΣ'),
            ('ΚΟΙΝΩΝΙΚΟΣ ΛΕΙΤΟΥΡΓΟΣ'),
            ('ΚΟΙΝΩΝΙΟΛΟΓΟΣ'),
            ('ΚΟΙΝΩΝΙΟΛΟΓΟΣ - ΑΝΘΡΩΠΟΛΟΓΟΣ'),
            ('ΚΟΙΝΩΝΙΟΛΟΓΟΣ- ΕΚΠΑΙΔΕΥΤΙΚΟΣ'),
            ('ΚΟΙΝΩΝΙΟΛΟΓΟΣ- ΠΟΛΙΤΙΚΟΣ ΕΠΙΣΤΗΜΟΝΑΣ'),
            ('ΚΤΗΝΙΑΤΡΟΣ'),
            ('ΚΤΗΝΙΑΤΡΟΣ ΣΤΡΑΤΙΩΤΙΚΟΣ'),
            ('ΛΟΓΙΣΤΗΣ'),
            ('ΛΟΓΟΘΕΡΑΠΕΥΤΗΣ'),
            ('ΜΑΘΗΜΑΤΙΚΟΣ'),
            ('ΜΑΘΗΜΑΤΙΚΟΣ - ΦΥΣΙΚΟΣ'),
            ('ΜΑΘΗΜΑΤΙΚΟΣ -ΣΤΑΤΙΣΤΙΚΟΛΟΓΟΣ'),
            ('ΜΑΙΕΥΤΗΣ - ΜΑΙΑ'),
            ('ΜΗΧΑΝΙΚΟΣ ΕΝΕΡΓΕΙΑΚΩΝ ΠΟΡΩΝ'),
            ('ΜΗΧΑΝΙΚΟΣ ΜΕΤΑΛΛΕΙΩΝ'),
            ('ΜΗΧΑΝΙΚΟΣ ΟΙΚΟΝΟΜΙΑΣ'),
            ('ΜΗΧΑΝΙΚΟΣ ΟΡΥΚΤΩΝ ΠΟΡΩΝ'),
            ('ΜΗΧΑΝΙΚΟΣ ΠΑΡΑΓΩΓΗΣ & ΔΙΟΙΚΗΣΗΣ'),
            ('ΜΗΧΑΝΙΚΟΣ ΠΕΡΙΒΑΛΛΟΝΤΟΣ'),
            ('ΜΗΧΑΝΙΚΟΣ ΠΛΗΡΟΦΟΡΙΚΟΣ'),
            ('ΜΗΧΑΝΙΚΟΣ ΠΛΗΡΟΦΟΡΙΚΟΣ ΔΙΚΤΥΩΝ'),
            ('ΜΗΧΑΝΙΚΟΣ ΣΧΕΔΙΑΣΗΣ'),
            ('ΜΗΧΑΝΙΚΟΣ ΤΕΧΝΟΛΟΓΙΑΣ ΥΛΙΚΩΝ'),
            ('ΜΗΧΑΝΙΚΟΣ ΧΩΡΟΤΑΞΙΑΣ - ΠΕΡΙΒΑΛΛΟΝΤΟΣ & ΑΝΑΠΤΥΞΗΣ'),
            ('ΜΗΧΑΝΟΛΟΓΟΣ - ΑΕΡΟΝΑΥΠΗΓΟΣ'),
            ('ΜΗΧΑΝΟΛΟΓΟΣ - ΜΗΧΑΝΙΚΟΣ'),
            ('ΜΗΧΑΝΟΛΟΓΟΣ - ΜΗΧΑΝΙΚΟΣ ΒΙΟΜΗΧΑΝΙΑΣ'),
            ('ΜΗΧΑΝΟΛΟΓΟΣ ΠΑΡΑΓΩΓΗΣ'),
            ('ΜΗΧΑΝΟΛΟΓΟΣ ΤΕΧΝΩΝ ΚΑΙ ΗΧΟΥ -ΑΕΙ'),
            ('ΜΟΥΣΙΚΟΛΟΓΟΣ'),
            ('ΜΟΥΣΙΚΟΛΟΓΟΣ - ΕΙΚΑΣΤΙΚΟΣ'),
            ('ΜΟΥΣΙΚΟΣ'),
            ('ΜΟΥΣΙΚΟΣ ΒΥΖΑΝΤΙΝΗΣ'),
            ('ΝΑΥΠΗΓΟΣ ΜΗΧΑΝΟΛΟΓΟΣ ΜΗΧΑΝΙΚΟΣ'),
            ('ΝΗΠΙΑΓΩΓΟΣ'),
            ('ΝΟΜΙΚΟΣ -ΔΙΚΗΓΟΡΟΣ - ΔΙΚΑΣΤΙΚΟΣ'),
            ('ΝΟΣΗΛΕΥΤΗΣ'),
            ('ΝΟΣΗΛΕΥΤΙΚΟΣ ΑΞΙΩΜΑΤΙΚΟΣ'),
            ('ΝΟΣΟΚΟΜΟΣ'),
            ('ΟΔΟΝΤΙΑΤΡΟΣ'),
            ('ΟΔΟΝΤΙΑΤΡΟΣ ΣΤΡΑΤΙΩΤΙΚΟΣ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ - ΜΗΧΑΝΟΛΟΓΟΣ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ - ΣΥΣΤ. ΕΦΟΔΙΑΣΜΟΥ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ ΑΘΛΗΤΙΣΜΟΥ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ ΒΙΟΜΗΧΑΝΙΚΟΥ ΣΧΕΔΙΑΣΜΟΥ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ ΔΗΜΟΣΙΟΥ ΤΟΜΕΑ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ -ΔΙΑΧΕΙΡΙΣΤΗΣ ΕΡΓΩΝ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ ΔΙΕΘΝΟΥΣ ΕΜΠΟΡΙΟΥ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ ΕΜΠΟΡΙΟΥ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ ΕΠΙΧΕΙΡΗΜΑΤΙΚΗΣ ΕΡΕΥΝΑΣ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ ΜΟΝΑΔΩΝ ΥΓΕΙΑΣ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ ΝΑΥΤΙΛΙΑΣ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ ΤΟΠΙΚΗΣ ΑΥΤΟΔΙΟΙΚΗΣΗΣ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ ΤΟΥΡΙΣΤΙΚΩΝ ΕΠΑΓΓΕΛΜΑΤΩΝ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ ΤΟΥΡΙΣΤΙΚΩΝ ΕΠΙΧΕΙΡΗΣΕΩΝ'),
            ('ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ-ΠΛΗΡΟΦΟΡΙΚΟΣ'),
            ('ΟΙΚΟΝΟΜΟΛΟΓΟΣ'),
            ('ΟΙΚΟΝΟΜΟΛΟΓΟΣ - ΠΕΡΙΦΕΡΕΙΟΛΟΓΟΣ'),
            ('ΟΙΚΟΝΟΜΟΛΟΓΟΣ ΔΙΟΙΚΗΣΗΣ ΚΑΙ ΤΕΧΝΟΛΟΓΙΑΣ'),
            ('ΟΙΚΟΝΟΜΟΛΟΓΟΣ ΟΙΚΙΑΚΗΣ ΟΙΚΟΝΟΜΙΑΣ & ΟΙΚΟΛΟΓΙΑΣ'),
            ('ΟΙΚΟΝΟΜΟΛΟΓΟΣ ΣΤΡΑΤΙΩΤΙΚΟΣ'),
            ('ΟΙΚΟΝΟΜΟΤΕΧΝΙΚΟΣ ΑΓΡΟΤΙΚΩΝ ΕΚΜΕΤΑΛΛΕΥΣΕΩΝ'),
            ('ΠΑΙΔΑΓΩΓΟΣ ΕΙΔΙΚΗΣ ΑΓΩΓΗΣ'),
            ('ΠΕΡΙΒΑΛΛΟΝΤΟΛΟΓΟΣ'),
            ('ΠΙΛΟΤΟΣ'),
            ('ΠΛΗΡΟΦΟΡΙΚΟΣ'),
            ('ΠΛΗΡΟΦΟΡΙΚΟΣ ΒΙΟΪΑΤΡΙΚΟΣ'),
            ('ΠΛΗΡΟΦΟΡΙΚΟΣ ΕΚΠΑΙΔΕΥΤΙΚΟΣ'),
            ('ΠΛΗΡΟΦΟΡΙΚΟΣ- ΕΠΙΚΟΙΝΩΝΙΟΛΟΓΟΣ'),
            ('ΠΛΗΡΟΦΟΡΙΚΟΣ ΕΠΙΚΟΙΝΩΝΙΩΝ'),
            ('ΠΛΗΡΟΦΟΡΙΚΟΣ-ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ ΕΠΙΧ/ΚΩΝ ΣΥΣΤ/ΤΩΝ'),
            ('ΠΟΛΙΤΙΚΟΣ ΕΠΙΣΤΗΜΟΝΑΣ'),
            ('ΠΟΛΙΤΙΚΟΣ ΕΠΙΣΤΗΜΟΝΑΣ-ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ ΔΗΜΟΣΙΟΥ'),
            ('ΠΟΛΙΤΙΚΟΣ ΜΗΧΑΝΙΚΟΣ'),
            ('ΠΟΛΙΤΙΚΟΣ ΜΗΧΑΝΙΚΟΣ- ΠΕΡΙΒΑΛΛΟΝΤΟΛΟΓΟΣ'),
            ('ΡΑΔΙΟΝΑΥΤΙΛΟΣ - ΑΞΙΩΜΑΤΙΚΟΣ ΑΕΡΟΠΟΡΙΑΣ'),
            ('ΣΤΑΤΙΣΤΙΚΟΛΟΓΟΣ'),
            ('ΣΤΑΤΙΣΤΙΚΟΛΟΓΟΣ - ΑΝΑΛΟΓΙΣΤΗΣ'),
            ('ΣΤΑΤΙΣΤΙΚΟΛΟΓΟΣ - ΑΣΦΑΛΙΣΤΗΣ'),
            ('ΣΤΡΑΤΟΛΟΓΟΣ'),
            ('ΣΧΕΔΙΑΣΗΣ ΕΝΔΥΜΑΤΩΝ'),
            ('ΤΕΧΝΙΚΟΣ ΑΓΡΟΤΙΚΩΝ ΠΡΟΙΟΝΤΩΝ- ΕΛΕΓΚΤΗΣ ΠΟΙΟΤΗΤΑΣ'),
            ('ΤΕΧΝΙΚΟΣ ΑΕΡΟΣΚΑΦΩΝ'),
            ('ΤΕΧΝΙΚΟΣ ΑΡΧΙΤΕΚΤΟΝΑΣ'),
            ('ΤΕΧΝΙΚΟΣ ΑΡΧΙΤΕΚΤΟΝΙΚΗΣ ΤΟΠΙΟΥ & ΑΝΘΟΚΟΜΙΑΣ'),
            ('ΤΕΧΝΙΚΟΣ ΑΥΤΟΜΑΤΙΣΜΟΥ'),
            ('ΤΕΧΝΙΚΟΣ ΒΙΟΜΗΧΑΝΙΚΗΣ ΠΛΗΡΟΦΟΡΙΚΗΣ'),
            ('ΤΕΧΝΙΚΟΣ ΓΕΩΠΛΗΡΟΦΟΡΙΚΟΣ -ΤΟΠΟΓΡΑΦΟΣ'),
            ('ΤΕΧΝΙΚΟΣ ΓΕΩΠΟΝΟΣ ΖΩΙΚΗΣ ΠΑΡΑΓΩΓΗΣ'),
            ('ΤΕΧΝΙΚΟΣ ΓΕΩΠΟΝΟΣ ΦΥΤΙΚΗΣ ΠΑΡΑΓΩΓΗΣ'),
            ('ΤΕΧΝΙΚΟΣ ΓΕΩΡΓΙΑΣ'),
            ('ΤΕΧΝΙΚΟΣ ΔΑΣΟΠΟΝΟΣ'),
            ('ΤΕΧΝΙΚΟΣ ΔΙΑΤΡΟΦΗΣ & ΔΙΑΙΤΟΛΟΓΙΑΣ'),
            ('ΤΕΧΝΙΚΟΣ ΔΙΑΧΕΙΡΙΣΗΣ ΦΥΣΙΚΩΝ ΠΟΡΩΝ'),
            ('ΤΕΧΝΙΚΟΣ ΔΟΜΙΚΩΝ ΕΡΓΩΝ'),
            ('ΤΕΧΝΙΚΟΣ ΕΚΠΑΙΔΕΥΤΙΚΟΣ'),
            ('ΤΕΧΝΙΚΟΣ ΕΝΕΡΓΕΙΑΣ'),
            ('ΤΕΧΝΙΚΟΣ ΕΡΓΩΝ ΥΠΟΔΟΜΗΣ'),
            ('ΤΕΧΝΙΚΟΣ ΗΛΕΚΤΡΟΛΟΓΟΣ'),
            ('ΤΕΧΝΙΚΟΣ ΗΛΕΚΤΡΟΝΙΚΟΣ'),
            ('ΤΕΧΝΙΚΟΣ ΗΛΕΚΤΡΟΝΙΚΟΣ Η/Υ'),
            ('ΤΕΧΝΙΚΟΣ ΘΕΡΜΟΚΗΠΙΩΝ - ΑΝΘΟΚΟΜΙΑΣ'),
            ('ΤΕΧΝΙΚΟΣ ΙΑΤΡΙΚΩΝ ΕΡΓΑΣΤΗΡΙΩΝ'),
            ('ΤΕΧΝΙΚΟΣ ΙΑΤΡΙΚΩΝ ΟΡΓΑΝΩΝ'),
            ('ΤΕΧΝΙΚΟΣ ΜΗΧΑΝΟΛΟΓΟΣ'),
            ('ΤΕΧΝΙΚΟΣ ΜΟΥΣΙΚΗΣ & ΑΚΟΥΣΤΙΚΗΣ'),
            ('ΤΕΧΝΙΚΟΣ ΜΟΥΣΙΚΩΝ ΟΡΓΑΝΩΝ'),
            ('ΤΕΧΝΙΚΟΣ ΝΑΥΠΗΓΟΣ'),
            ('ΤΕΧΝΙΚΟΣ ΟΔΟΝΤΟΤΕΧΝΙΤΗΣ'),
            ('ΤΕΧΝΙΚΟΣ ΟΙΝΟΛΟΓΟΣ'),
            ('ΤΕΧΝΙΚΟΣ ΟΠΤΙΚΟΣ'),
            ('ΤΕΧΝΙΚΟΣ ΟΧΗΜΑΤΩΝ'),
            ('ΤΕΧΝΙΚΟΣ ΠΕΡΙΒΑΛΛΟΝΤΟΣ'),
            ('ΤΕΧΝΙΚΟΣ ΠΕΤΡΕΛΑΙΟΥ KAI ΦΥΣΙΚΟΥ ΑΕΡΙΟΥ'),
            ('ΤΕΧΝΙΚΟΣ ΠΛΗΡΟΦΟΡΙΚΗΣ ΚΑΙ ΔΙΚΤΥΩΝ'),
            ('ΤΕΧΝΙΚΟΣ ΠΛΗΡΟΦΟΡΙΚΗΣ ΚΑΙ ΠΟΛΥΜΕΣΩΝ'),
            ('ΤΕΧΝΙΚΟΣ ΠΛΗΡΟΦΟΡΙΚΟΣ'),
            ('ΤΕΧΝΙΚΟΣ ΡΑΔΙΟΛΟΓΙΑΣ & ΑΚΤΙΝΟΛΟΓΙΑΣ'),
            ('ΤΕΧΝΙΚΟΣ ΣΥΝΤΗΡΗΣΗΣ ΑΡΧΑΙΟΤΗΤΩΝ & ΕΡΓΩΝ ΤΕΧΝΗΣ'),
            ('ΤΕΧΝΙΚΟΣ ΣΧΕΔΙΑΣΗΣ ΞΥΛΟΥ ΚΑΙ ΕΠΙΠΛΟΥ'),
            ('ΤΕΧΝΙΚΟΣ ΤΡΟΦΙΜΩΝ'),
            ('ΤΗΛΕΠΛΗΡΟΦΟΡΙΚΟΣ - ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ'),
            ('ΤΟΥΡΚΟΛΟΓΟΣ - ΑΣΙΑΤΟΛΟΓΟΣ'),
            ('ΥΓΕΙΟΝΟΛΟΓΟΣ ΔΗΜΟΣΙΑΣ ΥΓΙΕΙΝΗΣ'),
            ('ΥΠΑΞΙΩΜΑΤΙΚΟΣ ΑΕΡΟΠΟΡΙΑΣ - ΤΕΧΝΙΚΟΣ'),
            ('ΥΠΑΞΙΩΜΑΤΙΚΟΣ ΝΑΥΤΙΚΟΥ'),
            ('ΥΠΑΞΙΩΜΑΤΙΚΟΣ ΟΙΚΟΝΟΜΟΔΙΟΙΚΗΤΙΚΟΣ ΑΕΡΟΠΟΡΙΑΣ'),
            ('ΥΠΑΞΙΩΜΑΤΙΚΟΣ ΣΤΡΑΤΟΥ - ΔΙΟΙΚΗΤΙΚΟΣ'),
            ('ΥΠΑΞΙΩΜΑΤΙΚΟΣ ΣΤΡΑΤΟΥ - ΤΕΧΝΙΚΟΣ'),
            ('ΦΑΡΜΑΚΟΠΟΙΟΣ'),
            ('ΦΑΡΜΑΚΟΠΟΙΟΣ ΣΤΡΑΤΙΩΤΙΚΟΣ'),
            ('ΦΙΛΟΛΟΓΟΣ'),
            ('ΦΙΛΟΛΟΓΟΣ - ΠΑΙΔΑΓΩΓΟΣ'),
            ('ΦΙΛΟΛΟΓΟΣ ΑΓΓΛΙΚΗΣ ΓΛΩΣΣΑΣ'),
            ('ΦΙΛΟΛΟΓΟΣ ΒΥΖΑΝΤΙΝΩΝ & ΝΕΟΕΛΛΗΝΙΚΩΝ ΣΠΟΥΔΩΝ'),
            ('ΦΙΛΟΛΟΓΟΣ ΓΑΛΛΙΚΗΣ ΓΛΩΣΣΑΣ'),
            ('ΦΙΛΟΛΟΓΟΣ ΓΕΡΜΑΝΙΚΗΣ ΓΛΩΣΣΑΣ'),
            ('ΦΙΛΟΛΟΓΟΣ ΙΤΑΛΙΚΗΣ ΓΛΩΣΣΑΣ'),
            ('ΦΙΛΟΛΟΓΟΣ ΙΤΑΛΙΚΗΣ & ΙΣΠΑΝΙΚΗΣ ΓΛΩΣΣΑΣ'),
            ('ΦΙΛΟΛΟΓΟΣ ΞΕΝΩΝ ΓΛΩΣΣΩΝ - ΜΕΤΑΦΡΑΣΤΗΣ - ΔΙΕΡΜΗΝΕΑΣ'),
            ('ΦΙΛΟΛΟΓΟΣ- ΠΑΙΔΑΓΩΓΟΣ'),
            ('ΦΙΛΟΛΟΓΟΣ-ΞΕΝΩΝ - ΓΛΩΣΣΩΝ'),
            ('ΦΙΛΟΣΟΦΟΣ'),
            ('ΦΟΡΟΤΕΧΝΙΚΟΣ - ΧΡΗΜΑΤΟΟΙΚΟΝΟΜΟΛΟΓΟΣ'),
            ('ΦΥΣΙΚΟΘΕΡΑΠΕΥΤΗΣ'),
            ('ΦΥΣΙΚΟΣ'),
            ('ΦΩΤΟΓΡΑΦΟΣ'),
            ('ΧΗΜΙΚΟΣ'),
            ('ΧΗΜΙΚΟΣ - ΜΗΧΑΝΙΚΟΣ'),
            ('ΧΡΗΜΑΤΟΟΙΚΟΝΟΜΟΛΟΓΟΣ - ΤΡΑΠΕΖΟΔΙΟΙΚΗΤΙΚΟΣ'),
            ('ΨΥΧΟΛΟΓΟΣ')"""
    cur.execute(insertion1)
    cur.close()
    return None

def in_kathgoria(conn):
    cur= conn.cursor()
    insertion2="""INSERT INTO KATHGORIA_IKANOTITAS
            (Titlos)
            VALUES ('ΔΗΜΙΟΥΡΓΙΚΟΤΗΤΑ'),
            ('ΔΙΔΑΣΚΑΛΙΑ'),
            ('ΕΠΙΚΟΙΝΩΝΙΑΝΚΕΣ ΔΕΞΙΟΤΗΤΕΣ'),
            ('ΕΠΙΧΕΙΡΗΜΑΤΙΚΟΤΗΤΑ'),
            ('ΞΕΝΕΣ ΓΛΩΣΣΕΣ'),
            ('ΟΜΑΔΙΚΗ ΕΡΓΑΣΙΑ'),
            ('ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ'),
            ('ΣΧΕΔΙΟ')"""
    cur.execute(insertion2)
    cur.close()
    return None

if __name__=="__main__":
    main()

