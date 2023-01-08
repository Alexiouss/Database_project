/*Τα ονοματεπώνυμα όσων έχουν κάνει αίτηση για κάποια αγγελία ταξινομημένους με
αλφαβητική σειρά του ονόματος*/
SELECT Onoma,Eponymo
FROM (XRHSTHS as x JOIN PROFIL_AITOUMENOY as pa on x.User_ID=pa.ID_aitoumenou)
WHERE X.User_ID IN(SELECT ID_aitoumenou FROM AITHSH)
ORDER BY Onoma


/*Τον μέσο όρο του μισθού από τις αγγελίες που προσφέρονται στην κατηγορία εργασίας των ηλεκτρολόγων μηχανικών*/
SELECT AVG(Misthos) as mesos_oros_misthou
FROM AGGELIA_ERGASIAS
WHERE ID_kathgorias_ergasias=(SELECT ID_kathgorias FROM KATHGORIA_ERGASIAS WHERE Titlos='μηχανικοί-ηλεκτρολόγοι')

/*Το πλήθος των αιτήσεων μίας αγγελίας του παρόχου 6*/
SELECT COUNT(A.ID_paroxou) as aggelies_paroxou
FROM (AGGELIA_ERGASIAS as A JOIN AITHSH as AIT ON Ait.ID_aggelias=A.ID_aggelias)
WHERE ID_paroxou=6

/*Το πλήθος των ικανοτήτων κάθε αιτουμένου*/
SELECT Username,COUNT(ID_aitoumenou) as plithos_ikanothtwn
FROM KATEXEI_IKANOTHTA JOIN XRHSTHS on User_ID=ID_aitoumenou
GROUP BY(ID_aitoumenou)

/Τους παρόχους που προσφέρουν αγγελία στην τοποθεσία πάτρα
SELECT P.ID_paroxou,P.Eponymia,P.Perigrafh,P.Dieythynsh,P.Bathmologia
FROM PROFIL_PAROXOU AS P JOIN AGGELIA_ERGASIAS AS A ON P.ID_paroxou=A.ID_paroxou 
WHERE A.Topothesia='ΠΑΤΡΑ'