

def place_libre(tabl, choix_pos, pos):                                                                             #verif place libre // renvoie True si la place est libre
    """_summary_

    Args:grille morpion, choix de la position par le joueur
        tabl (_type_): dic
        choix_pos (_type_): int[1-9]
    """
    
         
    if choix_pos in [7,8,9]:
        a=tabl['a'][pos]
        if isinstance(a,int):
            return True
        else:
            return False
            
    elif choix_pos in [4,5,6]:
        a=tabl['b'][pos]
        if isinstance(a, int):
            return True
        else:
            return False
        
        
    elif choix_pos in [1,2,3]:
        a=tabl['c'][pos]
        if isinstance(a, int):
            return True
        else:
            return False    

#trouver à l'afficher
def afficher_grille(tabl):                                                                                           #afficher grille
    """_summary_: permet d'afficher la grille morpion

    Args:
        tabl (dic): a besoin d'un dico à 3 clés "a,b et c">> contenant chacune une liste de 3 valeurs 
    En retour: affichage de la grille morpion
    """
    print ("{}|{}|{}".format(tabl['a'][0],tabl['a'][1],tabl['a'][2]))   
    print ("{}|{}|{}".format(tabl['b'][0],tabl['b'][1],tabl['b'][2])) 
    print ("{}|{}|{}".format(tabl['c'][0],tabl['c'][1],tabl['c'][2])) 




def grille_gagnante(grille):                                                                     #verif si grille est gagnante // Renvoi False si pas de grille gagnante
    """_summary_                                                                                                       

    Args:prend grille morpion paramétre
        tab (_type_): grille
        renvoi booléen(true: E  grille gagnante,false: pas de grille de gagnante)
    """
    if grille['a'][0]==grille['a'][1]==grille['a'][2]:
        return True
    elif grille['b'][0]==grille['b'][1]==grille['b'][2]:
        return True
    elif grille['c'][0]==grille['c'][1]==grille['c'][2]:
        return True
    elif grille['a'][0]==grille['b'][0]==grille['c'][0]:
        return True
    elif grille['a'][1]==grille['b'][1]==grille['c'][1]:
        return True
    elif grille['a'][2]==grille['b'][2]==grille['c'][2]:
        return True
    elif grille['a'][0]==grille['b'][1]==grille['c'][2]:
        return "1"
    elif grille['a'][2]==grille['b'][1]==grille['c'][0]:
        return "1"
    else:
        return "0"
    


def nul(tab):                                                                                                          #verif si match nul // renvoi False si pas de place libre
    """_summary_

    Args:
        tab (_type_): grille actualisée

    Returns:
        _type_: renvoie booléen pr savoir s'il y a match nul (aucune position dispo)
    """
    pos=0
    for i in range (1,10):
        if i in [1,4,7]:
            pos=0
        elif i in [2,5,8]:
            pos=1
        elif i in [3,6,9]:
            pos=2
            
        if place_libre(tab,i,pos):
        
            return True
            break
        else:
            return False
        
        
def choix_po():                                                                                        #à quelle place le joueur joue [1-9]
    """choix joueur position de jeu
    retour de la place [1-9] de la grille
    Returns:
        _type_: int
    """
    choix_pos_user=0
    
    while choix_pos_user not in [1,2,3,4,5,6,7,8,9]:
        choix_pos_user=int(input("sur quelle case libre tu veux jouer?(1-9!!!)"))
        pos=reafection_value(choix_pos_user) 
        if place_libre(grille,choix_pos_user,pos):
            pass
        else:
            choix_pos_user=0
    return choix_pos_user



def place_signe(tabl,signe,choix_pos,pos):                                                                             #placer signe X ou O (position voulue)
    """_summary_

    Args:
        tabl (_type_): grille
        signe (_type_): _X ou O
        choix_pos (_type_): position jr choisie pr jouer
        pos (_type_): translation choix_pos>pos pr compréhension dico
    """
    # if pos==3:
    #     pass
    
    if choix_pos in [7,8,9]:
        tabl['a'][pos]=signe
    elif choix_pos in [4,5,6]:
        tabl['b'][pos]=signe
    elif choix_pos in [1,2,3]:
        tabl['c'][pos]=signe    
    
    return tabl
        
        
def reafection_value(choix_pos):                                                                                     #reaffecte valeur // pr raccorder place chiffre à valeur indice du dico
    """_
    reaffecte le choix de position à une valeur utilisable pour placer dans la grille via dictionnaire
    Args:le choix de la position du joueur [1-9]
        choix (_type_): _de
    """
    
    
    if choix_pos in [1,4,7]:
        pos=0
    elif choix_pos in [2,5,8]:
        pos=1
    elif choix_pos in [3,6,9]:
        pos=2
    else:
        pos=2
    return pos
   
def a_qui(tour):                                                                                                      # alternance des tours
    """_summary_

    Args:
        tour (_type_): numéro du tour

    Returns:
        _type_: renvoi booléen: permet ensuitre de savoir quel signe et quel joueur joue
    """
    if tour%2==0:
        return True
    else:
        return False
    


tour=0
grille= {
    'a': [7,8,9],
    'b': [4,5,6],
    'c': [1,2,3]
}

def morpion(grille,tour):
    while nul(grille) or grille_gagnante(grille):
        if a_qui(tour):                                                                                #alternance de tour
            signe="X" 
        else:
            signe="O"  

        if signe=='X':
            joueur_actu="joueur_1"
            print("au joueur 1 de jouer")
        elif signe=='O':
            joueur_actu="joueur_2"
            print("au joueur 2 de jouer")
    
        afficher_grille(grille)
        
        choix_pos=choix_po()                                                                          #retourne choix de position entre 1 et 10
                
        pos=reafection_value(choix_pos)                                                              #reaffection de la valeur

        place_signe(grille,signe,choix_pos,pos)                                                      #place le signe du joueur à la position X voulue
        grille=place_signe(grille,signe,choix_pos,pos)
        # afficher_grille(grille)
        
        if grille_gagnante(grille)==1:                                                               #verif si une grille est gagnante
            print(f"le {joueur_actu}a gagné")
            break
        else:
            pass

        if nul(grille):                                                                             #verifie si la grille est nulle(aucune position libre) 
            pass
        else:                                                 
            print("la partie est en match nul !")
        tour+=1   
          
    # print("bonne partie!")
morpion(grille,tour)