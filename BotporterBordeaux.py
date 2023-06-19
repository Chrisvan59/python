class SuperBot:
    print("BotPoerter")
try :
        ownteam =str(input("Entrer le nom de votre équipe favorite : "))
        print(f"votre équipe favorite est {ownteam}")
        myteam =int(input("Entrer le score de votre équipe: "))
        oppt =int(input("Entrer le score de l'equipe adverse: "))
except ValueError:
    print("Erreur de type-veuillez patientez redemarage du systeme")
    



    print(f"Le score final pour {ownteam} était de {myteam} - {oppt}")
try:
    if myteam> oppt :
        print(f" {ownteam} est la meilleur équipe au monde")
    elif myteam< oppt:
        print("L'arbitre a été acheté")
    
    else:
        print("le match etait nul")
except ValueError:
    print("erreur de type -veuillez patientez le systeme va redemarer Valencienn")

clt =int(input("Entrer le classement de votre équipe: "))

if clt <=2 :
    print(f"{ownteam} est encore dans la course ")
else:
    print(f"{ownteam} ne remontras pas ")


Olivier = SuperBot()
Guillaume = SuperBot()

favoriteTeam = str(input("Entrer votre équipe favorite: ")) 

if favoriteTeam == "Valenciennes":
    print(f" Guillaume Le score de ton equipe {ownteam} est de {myteam } ")
elif favoriteTeam == "Bordeaux":
    print(f"Olivier Le score de ton equipe {ownteam} est de {myteam }")
else :
    print(f"Aucun suporter pour cette équipe")


    
    
    


