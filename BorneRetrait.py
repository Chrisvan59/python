class retrait:
    print("Machine de retrait")


    print("1==50$")
    print("2==100$")

    NbRetrait =int(input("Veuillez entrer votre nombre corespondant au montant souhaite: "))
    try:
        if NbRetrait == 1 :
            print("Vous avez retirez 50$")
        elif NbRetrait ==2: 
            print("Vous avez retirez 100$")
        else:
            print("Vous avez appuyer sur la mauvais numéro")
    except :
        print("Vous n'avez pas tapez un chiffre")
        
    
    

choixBq = str(input("Faite votre choix "))
if choixBq == "Retrait":
    print(retrait)
C =['retrait','depot','liquide']
for choix in C:
    print(choix)
else:
    print("Passer à votre retrait")


