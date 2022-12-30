import re
import DB_Project as db

database="DB_project.db"


def Sign_UP():
    email=input("Email:")
    while(email==''):
        print("Εισάγετε αποδεκτό Email")
        email=input("Email:")
    data_email=Check_Email_existance(email)
    while(len(data_email)>0):
        print("Φαίνεται πως υπάρχει ήδη λογαριασμός με αυτό το email\nΠαρακαλώ εισάγεται αποδεκτό email")
        email=input("Email:")
        data_email=Check_Email_existance(email)
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



def Check_Email_existance(email):
    conn_for_email=db.create_connection(database)
    cur=conn_for_email.cursor()
    query="""SELECT Email from XRHSTHS WHERE Email='%s'""" % email
    cur.execute(query)
    data=cur.fetchall()
    return data

def Insert_in_Xrhsths(email,username,password,eidos_xrhsth):
    conn1=db.create_connection(database)
    cur=conn1.cursor()
    query = """INSERT INTO XRHSTHS (Email,Username,Password,Eidos_xrhsth) VALUES ('%s','%s','%s','%s')""" % (email,username,password,eidos_xrhsth)
    cur.execute(query)
    cur.close()
    conn1.commit()
    conn1.close()
    return None



def SignIn():
    print(2)
    return None