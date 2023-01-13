grille= {
    'a': [7,8,9],
    'b': [4,5,6],
    'c': [1,2,3]
}



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




def grille_gagnante(tab):                                                                                              #verif si grille est gagnante
    """_summary_

    Args:prend grille morpion paramétre
        tab (_type_): grille
        renvoi booléen(true: E  grille gagnante,false: pas de grille de gagnante)
    """
    if grille['a'][0]==grille['a'][1]==grille['a'][2]:
        return False
    elif grille['b'][0]==grille['b'][1]==grille['b'][2]:
        return False
    elif grille['c'][0]==grille['c'][1]==grille['c'][2]:
        return False
    elif grille['a'][0]==grille['b'][0]==grille['c'][0]:
        return False
    elif grille['a'][1]==grille['b'][1]==grille['c'][1]:
        return False
    elif grille['a'][2]==grille['b'][2]==grille['c'][2]:
        return False
    elif grille['a'][0]==grille['b'][1]==grille['c'][2]:
        return False
    elif grille['a'][2]==grille['b'][1]==grille['c'][0]:
        return False
    else:
        return True
    


def nul(tab):                                                                                                          #verif si match nul // renvoi False si pas de place libre
    """_summary_

    Args:
        tab (_type_): grille (actualisée)

    Returns:
        _type_: renvoie booléen pr savoir s'il y a match nul (aucune position dispo)
    """
    a=[]
    for i in range (1,10):
        if i in [1,4,7]:
            pos=0
        elif i in [2,5,8]:
            pos=1
        elif i in [3,6,9]:
            pos=2
            
        if place_libre(tab,i,pos):       
            a.append(1)
        else:
            pass
        
    if 1 in a:
        return True
    else:
        return False
def choix_po():                                                                                                        #à quelle place le joueur joue
    choix_pos=32#choix position
    
    while int(choix_pos) not in range (1,10):
        choix_pos=input("sur quelle case tu veux jouer?(1-9!!!)")
    return choix_pos

def placer_signe(tabl,signe,choix_pos,pos):                                                                             #placer signe (choix jr sur grille)
    """_summary_

    Args:
        tabl (_type_): grille
        signe (_type_): _X ou O
        choix_pos (_type_): position jr choisie pr jouer
        pos (_type_): translation choix_pos>pos pr compréhension dico
    """
    choix_pos=int(choix_pos)
    if choix_pos in [7,8,9]:
        tabl['a'][pos]=signe
    elif choix_pos in [4,5,6]:
        tabl['b'][pos]=signe
    elif choix_pos in [1,2,3]:
        tabl['c'][pos]=signe    
        
        
def reafection_value(choix_pos):                                                                                     #reaffecte valeur
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

def place_libre(tab, choix_pos, pos):                                                                             #verif place libre // renvoie True si la place est libre
    """_summary_

    Args:grille morpion, choix de la position par le joueur
        tabl (_type_): dic
        choix_pos (_type_): int[1-9]
    """
    
         
    if choix_pos in [7,8,9]:
        a=tab['a'][pos]
        if isinstance(a,int):
            return True
        else:
            return False
            
    elif choix_pos in [4,5,6]:
        a=tab['b'][pos]
        if isinstance(a, int):
            return True
        else:
            return False
        
        
    elif choix_pos in [1,2,3]:
        a=tab['c'][pos]
        if isinstance(a, int):
            return True
        else:
            return False    

def a_qui(tour):
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
    
# if a_qui(9):
#     signe="X"
    
# else:
#     signe="O"  
    
# def place_libre(tabl, choix_pos, pos):      #verif place libre
#     """_summary_

#     Args:grille morpion, choix de la position par le joueur
#         tabl (_type_): dic
#         choix_pos (_type_): int[1-9]
#     """
    
         
#     if choix_pos in [7,8,9]:
#         a=tabl['a'][pos]
#         if isinstance(a,int):
#             return True
            
#     elif choix_pos in [4,5,6]:
#         a=tabl['b'][pos]
#         if isinstance(a, int):
#             return True
        
#     elif choix_pos in [1,2,3]:
#         a=tabl['c'][pos]
#         if isinstance(a, int):
#             return True    
        
tour=0
grille= {
    'a': [7,8,9],
    'b': [4,5,6],
    'c': [1,2,3]
}

choix_pos=1
signe="X"

while nul(grille) or grille_gagnante(grille):
        if a_qui(tour):
            signe="X" 
        else:
            signe="O"  

        if signe=='X':
            joueur_actu="joueur_1"
            print("au joueur 1 de jouer, allez!")
        elif signe=='O':
            joueur_actu="joueur_2"
            print("au joueur 2 de jouer, allez!")
    
        afficher_grille(grille)
        choix_pos=choix_po()                                                                         #retourne choix de position entre 1 et 10
        pos=reafection_value(choix_pos)                                                              #reaffection de la valeur

        placer_signe(grille,signe,choix_pos,pos)                                                      #place le signe du joueur à la position X voulue
        afficher_grille(grille)
        
        while place_libre(grille,choix_pos,pos)==False:
              print("place déjà prise!")                                                           #renvoie booleeen: true si place libre
        else: 
             pass

        
        
        
        if grille_gagnante(grille):                                                                #verif si une grille est gagnante
            print(f"le {joueur_actu}a gagné")
        else:
            pass

   
        if nul(grille) ==False:                                                                            #verifie si la grille est nulle(aucune position libre)                                                  
            print("la partie est en ... match nul !")
        tour+=1   
          
print("bonne partie!!")