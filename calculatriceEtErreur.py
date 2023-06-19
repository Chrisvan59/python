print("Calculatrice et les erreurs")

def divison():
    try:
        nombre1 = int(input("Entrer le premiere nombre: "))
        nombre2 = int(input("Entrer le second nombre: "))
        total = nombre1/nombre2
    except ValueError:
        print("Erreur : la valeur entrée n'est pas un entier valide")
    except ZeroDivisionError:
        print("Erreur: impossible de diviser par zéro")
    else: 
        print("Resultat de la divison :",total)
    finally:
        print("Ce message est toujour affiché ")
        
divison()

        

    
    