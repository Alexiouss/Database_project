import re
import DB_Project as db

database="DB_project.db"


def Sign_UP():
    email=input("Email:")
    while(email==''):
        print("Εισάγετε αποδεκτό Email")
        email=input("Email:")
    username=input("Username:")
    while(username==''):
        print("Εισάγετε αποδεκτό Username")
        username=input("Username:")
    password=input("Κωδικός:")
    while(password=='' or CheckPassword(password)==False):
        print("Ο Κωδικός πρέπει να περιέχει τουλάχιστον έναν αριθμό, έναν ειδικό χαρακτήρα και να είναι από 8 έως 16 χαρακτήρες")
        password=input("Password:")
    eidos_xrhsth=input("Συνδεθείτε ως αιτούμενος ή πάροχος εργασίας\nΠατήστε Α για αιτούμενο και P για πάροχο")
    while(eidos_xrhsth=='' or eidos_xrhsth not in ["A","P"]):
        print("Please insert the correct information")
        eidos_xrhsth=input("Συνδεθείτε ως αιτούμενος ή πάροχος εργασίας\nΠατήστε Α για αιτούμενο και P για πάροχο")
    dicts={"Email":email,"Username":username,"Password":password,"Eidos_xrhsth":eidos_xrhsth}
    Insert_in_Xrhsths(email,username,password,eidos_xrhsth)
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
    #columns = ', '.join(dicts.keys())
    #placeholders = ','.join(dicts.values())
    #placeholders = ','.join(dicts.values())
    query = """INSERT INTO XRHSTHS (Email,Username,Password,Eidos_xrhsth) VALUES ('%s','%s','%s','%s')""" % (email,username,password,eidos_xrhsth)
    #sql = """INSERT INTO XRHSTHS ({}) VALUES ({})""".format(columns, placeholders)
    cur.execute(query)
    cur.close()
    conn1.commit()
    conn1.close()
    return None

def Check_User_existance_on_Sign_Up(Email):
    conn=db.create_connection(database)
    cur=conn.cursor()
    query="SELECT x.Email FROM XRHSTHS as x WHERE x.Email"
    return None


def SignIn():
    print(2)
    return None