
class Calculateur:
    print("Caluclateur de moyenne")

    Nom =str(input("Veuillez entrer le nom de l'eleve: "))
    Prenom = str(input("Veuillez entrer le prenom de l'eleve: "))
    print(f"Relever de note de m.{Nom} {Prenom}")



    NotePC  = float(input("Entrer la note de physique-chimie "))
    NoteHG  = float(input("Entrer la note de histoire-geo "))
    NoteFra = float(input("Entrer la note de français "))
    NoteMat = float(input("Entrer la note de mathematique "))
    NoteAN  = float(input("Entrer la note de anglais "))

    print(f"note de fraçais : {NoteFra}")
    print(f"note d'anglais : {NoteAN}")
    print(f"note d'hsitoire : {NoteHG}")
    print(f"note de mathematique: {NoteMat}")
    print(f"note de phisique-chimie: {NotePC}")




    noteMoyenne = ((NotePC + NoteHG + NoteFra + NoteMat + NoteAN)/5)

    print(f"voici la moyenne de m (mll).{Nom} {Prenom} : {noteMoyenne}")
    
print("Liste des professeurs")
M_Sheepard = "Mathematique"
M_Myster = "Anglais"
M_Pipette = "Physique-Chimie"
Mme_Borddeseine ="Histoire-Geo"
Mme_Peinardplou = "français"

M_Sheepard = Calculateur()
M_Myster = Calculateur()
Mme_Peinardplou= Calculateur()
M_Pipette = Calculateur()
Mme_Borddeseine =Calculateur()

Matens =str(input("Entrer votre matiere d'enseignement "))

if Matens == "français":
    print("affciher la note de français : ",Mme_Peinardplou.NoteFra)
elif Matens == "Anglais":
    print("affciher la note d'anglais: ",M_Sheepard.NoteAN)
elif Matens == "Mathematique":
    print("afficher la note d'anglais " ,M_Myster.NoteMat)
elif Matens == "Physique-Chimie":
    print("Afficher la note de phisique Chimie", M_Pipette.NotePC )
elif Matens == "Histoire-Geo":
    print("Afficher les note d'histoire geographie", Mme_Borddeseine.NoteHG)
else:
    print("Vous n'avez pas entrer la bonne matiere")
    
    


