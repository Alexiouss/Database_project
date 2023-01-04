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
                                Email VARCHAR(50) NOT NULL UNIQUE,
                                Username VARCHAR(20) NOT NULL UNIQUE,
                                Password VARCHAR(20) NOT NULL,
                                Eidos_xrhsth VARCHAR(1) NOT NULL,
                                PRIMARY KEY(User_ID)
                                );"""

    Tables[1]="""CREATE TABLE IF NOT EXISTS PROFIL_AITOUMENOY(
                                ID_aitoumenou INTEGER NOT NULL,
                                Onoma VARCHAR(30) NOT NULL,
                                Eponymo VARCHAR(30) NOT NULL,
                                Hlikia INTEGER NOT NULL,
                                Fylo VARCHAR(5),
                                PRIMARY KEY(ID_aitoumenou),
                                FOREIGN KEY(ID_aitoumenou) REFERENCES XRHSTHS(User_ID)
                                ON UPDATE CASCADE
                                ON DELETE CASCADE
                                );"""

    Tables[2]="""CREATE TABLE IF NOT EXISTS PROFIL_PAROXOU(
                                ID_paroxou INTEGER NOT NULL,
                                Eponymia VARCHAR(20) NOT NULL,
                                Perigrafh TEXT NOT NULL,
                                Dieythynsh VARCHAR(50) NOT NULL,
                                Thlefono VARCHAR(10) NOT NULL,
                                Bathmologia INTEGER,
                                PRIMARY KEY(ID_paroxou),
                                FOREIGN KEY(ID_paroxou) REFERENCES XRHSTHS(User_ID)
                                ON UPDATE CASCADE
                                ON DELETE CASCADE
                                );"""

    Tables[3]="""CREATE TABLE IF NOT EXISTS EKPAIDEYSH_YPOPSIFIOY(
                                ID_aitoumenou INTEGER NOT NULL,
                                Bathmos INTEGER DEFAULT NULL,
                                Hmnia_enarksis DATE NOT NULL DEFAULT '0000-00-00',
                                Hmnia_liksis DATE DEFAULT '0000-00-00',
                                Bathmida INTEGER DEFAULT NULL,
                                ID_pediou INTEGER DEFAULT 0,
                                PRIMARY KEY(ID_aitoumenou,Hmnia_enarksis),
                                FOREIGN KEY(ID_aitoumenou) REFERENCES PROFIL_AITOUMENOY(ID_aitoumenou)
                                ON UPDATE CASCADE
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
                                ID_kathgorias_ergasias INTEGER NOT NULL,
                                Titlos VARCHAR(100) NOT NULL,
                                Paroxos VARCHAR(100) NOT NULL,
                                Hmnia_enarksis DATE NOT NULL DEFAULT '0000-00-00',
                                Hmnia_liskis DATE DEFAULT NULL,
                                PRIMARY KEY(ID_aitoumenou,Hmnia_enarksis),
                                FOREIGN KEY(ID_aitoumenou) REFERENCES PROFIL_AITOUMENOY(ID_aitoumenou)
                                ON UPDATE CASCADE
                                ON DELETE CASCADE,
                                FOREIGN KEY(ID_kathgorias_ergasias) REFERENCES KATHGORIA_ERGASIAS(ID_kathgorias)
                                ON UPDATE CASCADE
                                ON DELETE NO ACTION
                                );"""
    
    Tables[6]="""CREATE TABLE IF NOT EXISTS KATHGORIA_ERGASIAS(
                                    ID_kathgorias INTEGER NOT NULL,
                                    Titlos VARCHAR(100) NOT NULL UNIQUE,
                                    PRIMARY KEY(ID_kathgorias)
                                    );"""

    Tables[7]="""CREATE TABLE IF NOT EXISTS KATEXEI_IKANOTHTA(
                                ID_aitoumenou INTEGER NOT NULL,
                                ID_ikanothtas INTEGER NOT NULL,
                                Epipedo INTEGER DEFAULT NULL,
                                PRIMARY KEY(ID_aitoumenou,ID_ikanothtas),
                                FOREIGN KEY(ID_aitoumenou) REFERENCES PROFIL_AITOUMENOY(ID_aitoumenou)
                                ON UPDATE CASCADE
                                ON DELETE CASCADE,
                                FOREIGN KEY(ID_ikanothtas) REFERENCES IKANOTHTA(ID_skill)
                                ON UPDATE CASCADE
                                ON DELETE NO ACTION
                                );
                                """
    
    Tables[8]="""CREATE TABLE IF NOT EXISTS IKANOTHTA(
                                    ID_skill INTEGER NOT NULL,
                                    Onoma VARCHAR(50) NOT NULL,
                                    Kathgoria VARCHAR(20) NOT NULL,
                                    PRIMARY KEY(ID_skill)
                                    );"""

    Tables[9]="""CREATE TABLE IF NOT EXISTS AGGELIA_ERGASIAS(
                                ID_aggelias INTEGER NOT NULL,
                                ID_paroxou INTEGER NOT NULL,
                                ID_kathgorias_ergasias INTEGER NOT NULL,
                                Titlos VARCHAR(100),
                                Topothesia VARCHAR(50) NOT NULL,
                                Wrario VARCHAR(30),
                                Misthos INTEGER,
                                Perigrafi TEXT,
                                Typos_ergasias VARCHAR(50),
                                Apaitoumeni_proyphresia INTEGER,
                                Hmeromhnia_dhmosieusis DATE NOT NULL,
                                PRIMARY KEY(ID_aggelias,ID_paroxou),
                                FOREIGN KEY(ID_paroxou) REFERENCES PROFIL_PAROXOU(ID_paroxou)
                                ON UPDATE CASCADE
                                ON DELETE CASCADE,
                                FOREIGN KEY(ID_kathgorias_ergasias) REFERENCES KATHGORIA_ERGASIAS(ID_kathgorias)
                                ON UPDATE CASCADE
                                ON DELETE NO ACTION
                                );"""

    Tables[10]="""CREATE TABLE IF NOT EXISTS APAITOUMENI_EKPAIDEYSI(
                                ID_aggelias INTEGER NOT NULL,
                                ID_paroxou INTEGER NOT NULL,
                                ID_pediou INTEGER DEFAULT 0,
                                Elaxisth_bathmida INTEGER,
                                FOREIGN KEY(ID_aggelias) REFERENCES AGGELIA_ERGASIAS(ID_aggelias)
                                ON UPDATE CASCADE
                                ON DELETE CASCADE,
                                FOREIGN KEY(ID_paroxou) REFERENCES AGGELIA_ERGASIAS(ID_paroxou)
                                ON UPDATE CASCADE
                                ON DELETE CASCADE,
                                FOREIGN KEY(ID_pediou) REFERENCES PEDIO_SPOUDON(ID_pediou)
                                ON UPDATE CASCADE
                                ON DELETE NO ACTION
                                );"""
    

    Tables[11]="""CREATE TABLE IF NOT EXISTS APAITEI_IKANOTHTA(
                                ID_aggelias INTEGER NOT NULL,
                                ID_paroxou INTEGER NOT NULL,
                                ID_ikanothtas INTEGER NOT NULL,
                                Epipedo INTEGER DEFAULT NULL,
                                PRIMARY KEY(ID_aggelias,ID_paroxou,ID_ikanothtas),
                                FOREIGN KEY(ID_aggelias) REFERENCES AGGELIA_ERGASIAS(ID_aggelias)
                                ON UPDATE CASCADE
                                ON DELETE CASCADE,
                                FOREIGN KEY(ID_paroxou) REFERENCES AGGELIA_ERGASIAS(ID_paroxou)
                                ON UPDATE CASCADE
                                ON DELETE CASCADE,
                                FOREIGN KEY(ID_ikanothtas) REFERENCES IKANOTHTA(ID_skill)
                                ON UPDATE CASCADE
                                ON DELETE NO ACTION
                                );"""
    
    Tables[12]="""CREATE TABLE IF NOT EXISTS SYNTEYKSI(
                                    ID_aithshs INTEGER NOT NULL,
                                    Hmeromhnia_synenteyksis DATE NOT NULL DEFAULT '0000-00-00',
                                    PRIMARY KEY(ID_aithshs),
                                    FOREIGN KEY(ID_aithshs) REFERENCES AITHSH(ID_aithshs)
                                    ON UPDATE CASCADE
                                    ON DELETE CASCADE
                                    );"""
    
    Tables[13]="""CREATE TABLE IF NOT EXISTS AITHSH(
                                    ID_aitoumenou INTEGER NOT NULL,
                                    ID_aithshs INTEGER NOT NULL,
                                    ID_paroxou INTEGER NOT NULL,
                                    ID_aggelias INTEGER NOT NULL,
                                    Hmeromhnia_aithshs DATE NOT NULL,
                                    PRIMARY KEY(ID_aithshs),
                                    FOREIGN KEY(ID_aitoumenou) REFERENCES PROFIL_AITOUMENOU(ID_aitoumenou)
                                    ON UPDATE CASCADE
                                    ON DELETE SET NULL,
                                    FOREIGN KEY(ID_aggelias) REFERENCES AGGELIA_ERGASIAS(ID_aggelias)
                                    ON UPDATE CASCADE
                                    ON DELETE SET NULL,
                                    FOREIGN KEY(ID_paroxou) REFERENCES AGGELIA_ERGASIAS(ID_paroxou)
                                    ON UPDATE CASCADE
                                    ON DELETE SET NULL
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
                                    ON UPDATE CASCADE
                                    ON DELETE SET NULL,
                                    FOREIGN KEY(ID_aitoumenou) REFERENCES PROFIL_AITOUMENOU(ID_aitoumenou)
                                    ON UPDATE CASCADE
                                    ON DELETE SET NULL
                                    );"""
    
    return Tables

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

def in_kathgoria_ergasias(conn):
    cur=conn.cursor()
    insertion="""INSERT INTO KATHGORIA_ERGASIAS
                    (Titlos)
                    VALUES('τουρισμός / ξενοδοχεία'),
                    ('εστίαση'),
                    ('μηχανικοί-Ηλεκτρολόγοι'),
                    ('μηχανικοί-Αρχιτέκτονες'),
                    ('μηχανικοί-Χημικοί'),
                    ('μηχανικοί-Πολιτικοί'),
                    ('μηχανικοί-Μηχανολόγοι'),
                    ('μηχανικοί-Αεροναυπηγοί'),
                    ('ναυτικοί'),
                    ('εκπαιδευτικοί'),
                    ('εξυπηρέτηση Πελατών / Call Center'),
                    ('λογιστήριο'),
                    ('τομέας Παραγωγής'),
                    ('δημιουργικό Τμήμα / Γραφίστες'),
                    ('διαφήμιση / Promotion'),
                    ('τράπεζες'),
                    ('επιστήμες'),
                    ('ανώτατη Διοίκηση'),
                    ('ασφάλειες'),
                    ('διαχείριση Ποιότητας'),
                    ('αερομεταφορές'),
                    ('μεσιτικά'),
                    ('γραμματειακή Υποστήριξη'),
                    ('υποστηρικτικοί Υπάλληλοι'),
                    ('αποθήκη / Logistics'),
                    ('οδηγοί'),
                    ('υπάλληλοι Γραφείου'),
                    ('μεταφορές'),
                    ('μάρκετινγκ'),
                    ('διοίκηση Επιχειρήσεων'),
                    ('αγροτικά'),
                    ('δημόσιες Σχέσεις'),
                    ('πολιτιστικά / Τέχνες'),
                    ('δημοσιογράφοι / ΜΜΕ'),
                    ('εθελοντικές Εργασίες'),
                    ('αισθητική / Κομμωτήρια'),
                    ('νομικοί'),
                    ('πωλήσεις'),
                    ('καταστήματα Λιανικής'),
                    ('τεχνικοί / Συντηρητές'),
                    ('οικιακοί Βοηθοί'),
                    ('επαγγέλματα Υγείας'),
                    ('πληροφορική'),
                    ('εξωτερικές Εργασίες / Security'),
                    ('χρηματοοικονομικά'),
                    ('αγορές / Προμήθεις'),
                    ('human Resources(HR)'),
                    ('τηλεπικοινωνίες'),
                    ('περιβάλλον'),
                    ('επιχειρηματικότητα'),
                    ('σύμβουλοι Επιχειρήσεων'),
                    ('δίκτυα')"""
    cur.execute(insertion)
    cur.close()
    return None

def in_ikanotita(conn):
    cur= conn.cursor()
    insertion1="""INSERT INTO IKANOTHTA
        (Onoma,Kathgoria)
        VALUES('Συντήρηση αυτοκινήτων','Hard'),
        ('Διαχείριση έργου','Hard'),
        ('Ξυλουργική','Hard'),
        ('Ψηφιακή ασφάλεια','Hard'),
        ('Ξένες γλώσσες','Hard'),
        ('Γραφικό σχέδιο','Hard'),
        ('Οικονομικά','Hard'),
        ('Επεξεργασία φωτογραφίας','Hard'),
        ('Προγραμματισμός','Hard'),
        ('Βελτιστοποίηση μηχανών αναζήτησης','Hard'),
        ('Επεξεργασία βίντεο','Hard'),
        ('Ηθοποιία','Hard'),
        ('Μηχανική μάθηση','Hard'),
        ('Κινηματογραφία','Hard'),
        ('Πολιτικού μηχανικού','Hard'),
        ('Υδραυλικά','Hard'),
        ('Σύνταξη συμβολαίου','Hard'),
        ('Εισαγωγή δεδομένων','Hard'),
        ('Χρηματοοικονομική μοντελοποίηση','Hard'),
        ('Νοσηλευτικής','Hard'),
        ('Κρυπτογράφηση','Hard'),
        ('Απεικόνιση','Hard'),
        ('Εσωτερική διακόσμηση','Hard'),
        ('Διοίκηση υγειονομικής περίθαλψης','Hard'),
        ('Ανάπτυξη διαδικτύου','Hard'),
        ('Microsoft office','Hard'),
        ('Ερμηνεία δεδομένων','Hard'),
        ('Αντιμετώπιση προβλημάτων','Hard'),
        ('Διαχείριση μέσων κοινωνικής δικτύωσης','Hard'),
        ('Τήρηση λογιστικών βιβλίων','Hard'),
        ('Ερευνα','Hard'),
        ('Σχέδιο','Hard'),
        ('Διαχείριση διοχέτευσης πωλήσεων','Hard'),
        ('Δεξιότητες παρουσίασης','Hard'),
        ('Δημιουργία περιεχομένου','Hard'),
        ('Ερευνα αγοράς','Hard'),
        ('Τεχνικό γράψιμο','Hard'),
        ('Έλεγχος','Hard'),
        ('Διαδικτυακή διαφήμιση','Hard'),
        ('Διαχείριση συστημάτων','Hard'),
        ('Στρατηγική πωλήσεων','Hard'),
        ('Σχεδιασμός διεπαφής χρήστη','Hard'),
        ('Βελτιστοποίηση μετατροπής','Hard'),
        ('Επεξεργασία κειμένου','Hard'),
        ('Διαχείριση εξοπλισμού','Hard'),
        ('Κατασκευή','Hard'),
        ('Επιδιόρθωση','Hard'),
        ('Σύνταξη σχεδιαγράμματος','Hard'),
        ('Έλεγχος ποιότητας','Hard'),
        ('Στατιστική ανάλυση','Hard'),
        ('Ανάπτυξη προϊόντων','Hard'),
        ('Δεξιότητες επικοινωνίας','Soft'),
        ('Πειστικότητα','Soft'),
        ('Τυπικότητα','Soft'),
        ('Ηγετικές ικανότητες','Soft'),
        ('Φιλοδοξία','Soft'),
        ('Κίνητρο','Soft'),
        ('Διαπραγμάτευση','Soft'),
        ('Κριτική σκέψη','Soft'),
        ('Δημιουργική σκέψη','Soft'),
        ('Ηθική εργασίας','Soft'),
        ('Συνεργασία','Soft'),
        ('Ενεργητική ακρόαση','Soft'),
        ('Θετική στάση','Soft'),
        ('Ενέργεια','Soft'),
        ('Ενθουσιασμός','Soft'),
        ('Φιλικότητα','Soft'),
        ('Τιμιότητα','Soft'),
        ('Αυτοπεποίθηση','Soft'),
        ('Επίλυση προβλήματος','Soft'),
        ('Ικανότητα προσαρμογής','Soft'),
        ('Επίλυση των συγκρούσεων','Soft'),
        ('Καθοδήγηση','Soft'),
        ('Ενσυναίσθηση','Soft'),
        ('Υπομονή','Soft'),
        ('Συνεργασία','Soft'),
        ('Συναισθηματική νοημοσύνη','Soft'),
        ('Επιρροή','Soft'),
        ('Αυτογνωσία','Soft'),
        ('Δικτύωση','Soft'),
        ('Ανταγωνισμός','Soft'),
        ('Ευγένεια','Soft'),
        ('Ανεξαρτησία','Soft'),
        ('Επιμονή','Soft'),
        ('Αξιοπιστία','Soft'),
        ('Δημόσια ομιλία','Soft'),
        ('Κατανόηση της γλώσσας του σώματος','Soft'),
        ('Εποπτικές ικανότητες','Soft'),
        ('Καλλιτεχνία','Soft'),
        ('Ευθύνη','Soft'),
        ('Αφοσίωση','Soft'),
        ('Αυτοπεποίθηση','Soft'),
        ('Εξυπηρέτηση πελατών','Soft'),
        ('Διαχείριση της ομάδας','Soft'),
        ('Τεκμηρίωση','Soft'),
        ('Ανατροφοδότηση','Soft'),
        ('Καταιγισμός ιδεών','Soft'),
        ('Αξιολόγηση','Soft'),
        ('Χρονοπρογραμματισμός','Soft'),
        ('Εκπαιδευτικές ικανότητες','Soft'),
        ('Διαχείριση κρίσης','Soft'),
        ('Προσαρμοστικότητα','Soft')"""
    cur.execute(insertion1)
    cur.close()
    return None

def main():
    database="DB_project.db"
    sql_create_tables=tables()
    conn=create_connection(database)
    conn.execute("PRAGMA foreign_keys = ON;")
    for i in range(0,NumofTables):
        if conn is not None:
            create_table(conn,sql_create_tables[i])
        else:
            print("ERROR ERROR ERROR")
    try:
        in_ikanotita(conn)
        in_pedio_spoudon(conn)
        in_kathgoria_ergasias(conn)
    except:
        print("Data already inserted")
    conn.commit()
    print("-----Welcome to Job_Finder-----\nPlease create an account if you dont have one\nAlready have an account?\nPress Sign in to continue\n")
    print("Press 1 for Sign up or 2 for Sign in")
    signing=int(input())
    if(signing==1):
        data=jf.SignUP().Sign_UP()
        print("Ας ξεκινήσουμε με την δημιουργία του προφίλ σας")
        id_assignement=jf.User_id_assignement(data["Email"])
        if data["Eidos_xrhsth"]=='A':
           jf.Profile_Creation().Create_ait_profil(data["Email"])

           jf.Empeiria().Create_education(id_assignement)
           
           jf.Empeiria().Create_proyphresia(id_assignement)
        elif data["Eidos_xrhsth"]=='P':
            jf.Profile_Creation().Create_paroxos_profil(data["Email"])
    
    elif(signing==2):
        email=input("Email:")
        password=input("password:")
        user=jf.SignIn().Sign_In(email,password)
    '''-----------Μετά το sign in ή μετά από όλη την διαδικασία δημιουργίας προφίλ αρχίζουμε την αναζήτηση την αίτηση-----------'''
    conn.commit()
    conn.close()

if __name__=="__main__":
    main()



