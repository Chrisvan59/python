print("Resusltats Scolaires")

def nomEleve():
    nom =str(input("Entrer le nom de l'élève: "))
    prenom =str(input("Entrer le prènom de l'élève: "))

    print(f"Bulletin de m(mlle).{nom} {prenom} ")



def noteEleve():
    Note =float(input("Entrer les notes de l'éléve :"))

    if Note >= 5 and Note <10:
        print("Cette éléve est médiocre.")

    elif Note >= 0 and Note <5:
        print("C'est un cancre.")

    elif Note >=10 and Note<15:
        print("Eleve moyen ,peux mieux faire")

    else :
        print("c'est un petit génie")
    
    
    
        
nomEleve()
noteEleve()