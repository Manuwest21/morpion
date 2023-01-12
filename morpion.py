grille= {
    'a': [7,8,9],
    'b': [4,5,6],
    'c': [1,2,3]
}

signe={
    
    'a':'O',
    'b':'X'
}

#trouver à l'afficher
def afficher_grille(tabl):
    """_summary_: permet d'afficher la grille morpion

    Args:
        tabl (dic): a besoin d'un dico à 3 clés "a,b et c">> contenant chacune une liste de 3 valeurs 
    En retour: affichage de la grille morpion
    """
    print ("{}|{}|{}".format(tabl['a'][0],tabl['a'][1],tabl['a'][2]))   
    print ("{}|{}|{}".format(tabl['b'][0],tabl['b'][1],tabl['b'][2])) 
    print ("{}|{}|{}".format(tabl['c'][0],tabl['c'][1],tabl['c'][2])) 

afficher_grille(grille)