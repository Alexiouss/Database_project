import re
import DB_Project as db

database="DB_project.db"


def Sign_UP():
    Email=input("Email:")
    while(Email==''):
        print("Εισάγετε αποδεκτό Email")
        Email=input("Email:")
    Username=input("Username:")
    while(Username==''):
        print("Εισάγετε αποδεκτό Username")
        Username=input("Username:")
    Password=input("Κωδικός:")
    while(Password=='' or CheckPassword(Password)==False):
        print("Ο Κωδικός πρέπει να περιέχει τουλάχιστον έναν αριθμό, έναν ειδικό χαρακτήρα και να είναι από 8 έως 16 χαρακτήρες")
        Password=input("Password:")
    Eidos_xrhsth=input("Συνδεθείτε ως αιτούμενος ή πάροχος εργασίας\nΠατήστε Α για αιτούμενο και P για πάροχο")
    while(Eidos_xrhsth=='' or Eidos_xrhsth not in ["A","P"]):
        print("Please insert the correct information")
        Eidos_xrhsth=input("Συνδεθείτε ως αιτούμενος ή πάροχος εργασίας\nΠατήστε Α για αιτούμενο και P για πάροχο")
    dicts={'Email':Email,'Username':Username,'Password':Password,'Eidos_xrhsth':Eidos_xrhsth}
    Insert_in_Xrhsths(dicts)
    return None

def CheckPassword(Password):
    special_characters=re.findall("[!,@,#,$,%,^,&,*,(,)]",Password)
    numbers=re.findall("[1,2,3,4,5,6,7,8,9,0]",Password)
    letters=re.findall("[a-z,A-Z]",Password)
    if(len(Password)>=8 and len(Password)<=16 and len(letters)>=1 and len(numbers)>=1 and len(special_characters)>=1 ):
        return True
    else:
        return False

def Insert_in_Xrhsths(dicts):
    conn=db.create_connection(database)
    cur=conn.cursor()
    columns = ', '.join(dicts.keys())
    placeholders = ','.join(dicts.values())
    sql = 'INSERT INTO XRHSTHS ({}) VALUES ({})'.format(columns, placeholders)
    #values = [int(x) if isinstance(x, bool) else x for x in dicts.values()]
    cur.execute(sql)
    cur.close()

def Check_User_existance_on_Sign_Up(Email):
    conn=db.create_connection(database)
    cur=conn.cursor()
    query="SELECT x.Email FROM XRHSTHS as x WHERE x.Email"
    return None


def SignIn():
    print(2)
    return None