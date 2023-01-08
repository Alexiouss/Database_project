import Job_Finder_project as jf
import DB_Project as db

database="DB_project.db"

def main():
    db.Create_db()
    print("-----Welcome to Job_Finder-----\nPlease create an account if you dont have one\nAlready have an account?\nPress Sign in to continue\n")
    print("Press 1 for Sign up or 2 for Sign in")
    signing=int(input())
    if(signing==1):
        data=jf.SignUP().Sign_UP()
        print("\nΑς ξεκινήσουμε με την δημιουργία του προφίλ σας.\n")
        id_assignement=jf.User_id_assignement(data["Email"])
        if data["Eidos_xrhsth"]=='A':
           jf.Profile_Creation().Create_ait_profil(data["Email"])

           jf.Empeiria().Create_education(id_assignement)
           
           jf.Empeiria().Create_proyphresia(id_assignement)

           jf.Empeiria().Create_Ikanothta_ypopsifiou(id_assignement)

        elif data["Eidos_xrhsth"]=='P':
            jf.Profile_Creation().Create_paroxos_profil(data["Email"])
            jf.Aggelia().Create_aggelia_erg(id_assignement)
    
    elif(signing==2):
        user=jf.SignIn().Sign_In()
        if(user[1]=='A'):
            while True:
                x=int(input("Διαλέξτε μία λειτουργία:\n0:Sign out\n1:Αναζήτηση και αίτηση αγγελιών\n2:Αξιολόγηση παρόχου\n"))
                if(x==0):
                    break
                while True:
                    if(x==1):
                        jf.Anazhthsh_aggelion().Search_aggelies()
                        n=int(input("Αν θέλετε να κάνετε αίτηση σε κάποια αγγελία πατήστε 1 αλλιώς πατήστε 0:"))
                        if(n==1):
                            jf.Aithsh().Create_Aithsh(user[0])
                            break
                        else:
                            break
                    elif(x==2):
                        jf.Aksiologhsh().Create_aksiologhsh(user[0])
                        break
        elif(user[1]=='P'):
            while True:
                x=int(input("Διαλέξτε μία λειτουργία:\n0:Sign out\n1:Αναζήτηση των αιτήσεων σας\n2:Εμφάνιση αξιολόγησης\n3:Δημιουργία αγγελίας\n"))
                if(x==0):
                    break
                while True:
                    if(x==1):
                        jf.Show_aitisis().show_aggelies(user[0])
                        break
                    elif(x==2):
                        jf.Show_aitisis().show_aksiologhsh(user[0])
                        break
                    elif(x==3):
                        jf.Aggelia().Create_aggelia_erg(user[0])
                        break
    return None

if __name__=="__main__":
    main()