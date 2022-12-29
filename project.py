import sqlite3
from sqlite3 import Error

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
                                Epipedo INTEGER NOT NULL DEFAULT 0,
                                ID_kathgorias INTEGER NOT NULL,
                                PRIMARY KEY(ID_aitoumenou,ID_kathgorias),
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
                                Titlos VARCHAR(50),
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
    conn=create_connection(database)
    for i in range(0,NumofTables):
        if conn is not None:
            create_table(conn,sql_create_tables[i])
        else:
            print("ERROR ERROR ERROR")
    cursor =conn.cursor()
    conn.close()



if __name__=="__main__":
    main()
