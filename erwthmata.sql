/*Τα ονοματεπώνυμα όσων έχουν κάνει αίτηση για κάποια αγγελία ταξινομημένους με
αλφαβητική σειρά του ονόματος*/
SELECT Onoma,Eponymo
FROM (XRHSTHS as x JOIN PROFIL_AITOUMENOY as pa on x.User_ID=pa.ID_aitoumenou)
JOIN AITHSH as ait on x.User_ID=ait.ID_aitoumenou
ORDER BY Onoma

/*Τον μέσο όρο των μισθών που ανήκουν στην κατηγορία 3*/
SELECT AVG(Misthos) as mesos_oros_misthwn
FROM AGGELIA_ERGASIAS
WHERE ID_kathgorias_ergasias=3

/*Το άθροισμα των αιτήσεων μίας αγγελίας ενός παρόχου*/
SELECT COUNT(A.ID_paroxou) as aggelies_paroxou
FROM (AGGELIA_ERGASIAS as A JOIN AITHSH as AIT ON Ait.ID_aggelias=A.ID_aggelias)
WHERE ID_paroxou=6

/*Το πλήθος των ικανοτήτων κάθε αιτουμένου*/
SELECT Username,COUNT(ID_aitoumenou) as plithos_ikanothtwn
FROM KATEXEI_IKANOTHTA JOIN XRHSTHS on User_ID=ID_aitoumenou
GROUP BY(ID_aitoumenou)
