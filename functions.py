import numpy as np

'''
Remarque: toutes les fonctions n'acceptent que des images avec des niveaux de gris ou binaires
'''


def seuil_image(img, seuil):
    x_max = len(img)
    y_max = len(img[0])
    img_apres_seuillage = np.zeros((x_max, y_max), dtype=int)
    for i in range(0, x_max):
        for j in range(0, y_max):
            if img[i][j] > seuil:
                img_apres_seuillage[i][j] = 1
            else:
                img_apres_seuillage[i][j] = 0
    return img_apres_seuillage


def addition_2_images(img1, img2, is_binaire=True):
    x_max = len(img1)
    y_max = len(img2)
    img_apres_addition = np.zeros((x_max, y_max), dtype=int)
    for i in range(0, x_max):
        for j in range(0, y_max):
            valeur_pixel = img1[i][j] + img2[i][j]
            # si l'image n'est pas binaire
            if not is_binaire:
                if valeur_pixel > 255:
                    img_apres_addition[i][j] = 255
                else:
                    img_apres_addition[i][j] = valeur_pixel
            # si l'image est binaire
            else:
                if valeur_pixel > 1:
                    img_apres_addition[i][j] = 1
                else:
                    img_apres_addition[i][j] = valeur_pixel

    return img_apres_addition


# Remarque: on n'a pas besoin de spécifier si l'image est binaire ou en niveau de gris
def soustraction_2_images(img1, img2):
    x_max = len(img1)
    y_max = len(img1[0])
    img_apres_soustraction = np.zeros((x_max, y_max), dtype=int)
    for i in range(0, x_max):
        for j in range(0, y_max):
            valeur_pixel = img1[i][j] - img2[i][j]
            if valeur_pixel < 0:
                img_apres_soustraction[i][j] = 0
            else:
                img_apres_soustraction[i][j] = valeur_pixel
    return img_apres_soustraction


'''
L'érosion et la dilatation se font avec l'élément structurant par défaut (de taille 1)suivant:
[[1 1 1]
 [1 1 1]
 [1 1 1]]
'''


def erosion_image_binaire(img, taille_element_structurant = 1):
    x_max = len(img)
    y_max = len(img[0])
    img_apres_erosion = np.zeros((x_max, y_max), dtype=int)
    # copier l'image dans une variable locale
    for i in range(0, x_max):
        for j in range(0, y_max):
            img_apres_erosion[i][j] = img[i][j]

    if taille_element_structurant == 0:
        return img_apres_erosion

    # parcourir l'image en prenant en compte la taille de l'élément structurant
    for i in range(taille_element_structurant, x_max - taille_element_structurant):
        for j in range(taille_element_structurant, y_max - taille_element_structurant):
            #pour ne pas faire les calculs pour les pixels de valeur 0
            if img[i][j] == 1:
                s = 0
                # element structurant
                for ligne_elem_struct in range(-taille_element_structurant, taille_element_structurant + 1):
                    for col_elem_struct in range(-taille_element_structurant, taille_element_structurant + 1):
                        s += img[i + ligne_elem_struct][j + col_elem_struct]
                if s != 9:
                    img_apres_erosion[i][j] = 0
    return img_apres_erosion


def dilatation_image_binaire(img, taille_element_structurant=1):
    x_max = len(img)
    y_max = len(img[0])
    img_apres_dilatation = np.zeros((x_max, y_max), dtype=int)

    # copier l'image dans une variable locale
    for i in range(0, x_max):
        for j in range(0, y_max):
            img_apres_dilatation[i][j] = img[i][j]

    if taille_element_structurant == 0:
        return img_apres_dilatation

    # parcourir l'image en prenant en compte la taille de l'élément structurant
    for i in range(taille_element_structurant, x_max - taille_element_structurant):
        for j in range(taille_element_structurant, y_max - taille_element_structurant):
            # pour ne pas faire les calculs pour les pixels de valeur 1
            if img[i][j] == 0:
                s = 0
                # element structurant
                for ligne_elem_struct in range(-taille_element_structurant, taille_element_structurant + 1):
                    for col_elem_struct in range(-taille_element_structurant, taille_element_structurant + 1):
                        s += img[i + ligne_elem_struct][j + col_elem_struct]
                if s > 1:
                    img_apres_dilatation[i][j] = 0
    return img_apres_dilatation


# ouverture: érosion suivie d'une dilatation
def ouverture_img(img):
    img_apres_ouverture = dilatation_image_binaire(erosion_image_binaire(img))
    return img_apres_ouverture


# fermeture: dilatation suivie d'une érosion
def fermeture_img(img):
    img_apres_ouverture = erosion_image_binaire(dilatation_image_binaire(img))
    return img_apres_ouverture


'''
on réalise l'amincissement et l'epaississement avec une configuration qu'on donne dans les paramètres
la configuration correspond à un élément structurant
la valeur 2 correspond à une valeur quelconque 
Example d'élément structant:
    element_structurant = [[0 1 0]
                           [2 1 2]
                           [0 1 0]]
'''
ELEMENT_STRUCTURANT_PAR_DEFAUT = [[1, 1, 1],
                                  [1, 1, 1],
                                  [1, 1, 1]]

def amincissement_img(img, element_structurant=ELEMENT_STRUCTURANT_PAR_DEFAUT):
    x_max = len(img)
    y_max = len(img[0])
    img_apres_amincissement = np.zeros((x_max, y_max), dtype=int)
    # parcourir l'image : appliquer l'amincissement et copier le bon résultat dans img_apres_amincissement
    for i in range(1, x_max - 1):
        for j in range(1, y_max - 1):
            # on n'applique l'amincissement qu'aux pixels mis à 1
            # car le but est de voir si on doit en mettre à 0
            if img[i][j] == 1:
                # parcourir les pixels contenus dans l'élément structurant
                nbr_pixels_identiques = 0
                # break_boucle sert à arrêter la boucle lorsque la configuration n'est pas satisfaite
                # on l'ajoute juste pour des raisons de performance
                # break_boucle = False
                for ligne_elem_struct in range(-1, 2):
                    for col_elem_struct in range(-1, 2):
                        if element_structurant[ligne_elem_struct][col_elem_struct] == 2:
                            nbr_pixels_identiques += nbr_pixels_identiques
                        else:
                            differance = img[i + ligne_elem_struct][j + col_elem_struct] \
                                         - element_structurant[ligne_elem_struct][col_elem_struct]
                            if differance == 0:
                                nbr_pixels_identiques += nbr_pixels_identiques
                                '''
                            else:
                                #sortir de la quatrième boucle
                                break_boucle = True
                                break
                        #sortir de la troisième boucle
                        if break_boucle:
                            break
                            '''
                # vérifier si la configuration est satisfaite
                if nbr_pixels_identiques == 9:
                    img_apres_amincissement[i][j] = 0
                else:
                    # ici img[i][j] est égale à 1
                    img_apres_amincissement[i][j] = img[i][j]
            else:
                # img[i][j] est égale à 0
                img_apres_amincissement[i][j] = img[i][j]

    return img_apres_amincissement


def epaississement_img(img, element_structurant=ELEMENT_STRUCTURANT_PAR_DEFAUT):
    x_max = len(img)
    y_max = len(img[0])
    img_apres_epaississement = np.zeros((x_max, y_max), dtype=int)
    # parcourir l'image : appliquer l'epaississement et copier le bon résultat dans img_apres_epaississement
    for i in range(1, x_max - 1):
        for j in range(1, y_max - 1):
            # on n'applique l'amincissement qu'aux pixels mis à 0
            # car le but est de voir si on doit en mettre à 1
            if img[i][j] == 0:
                # parcourir les pixels contenus dans l'élément structurant
                nbr_pixels_identiques = 0
                # break_boucle sert à arrêter la boucle lorsque la configuration n'est pas satisfaite
                # on l'ajoute juste pour des raisons de performance
                # break_boucle = False
                for ligne_elem_struct in range(-1, 2):
                    for col_elem_struct in range(-1, 2):
                        if element_structurant[ligne_elem_struct][col_elem_struct] == 2:
                            nbr_pixels_identiques += nbr_pixels_identiques
                        else:
                            differance = img[i + ligne_elem_struct][j + col_elem_struct] \
                                         - element_structurant[ligne_elem_struct][col_elem_struct]
                            if differance == 0:
                                nbr_pixels_identiques += nbr_pixels_identiques
                                '''
                            else:
                                #sortir de la quatrième boucle
                                break_boucle = True
                                break
                        #sortir de la troisième boucle
                        if break_boucle:
                            break
                            '''
                # vérifier si la configuration est satisfaite
                if nbr_pixels_identiques == 9:
                    img_apres_epaississement[i][j] = 1
                else:
                    # ici img[i][j] est égale à 0
                    img_apres_epaississement[i][j] = img[i][j]
            else:
                # img[i][j] est égale à 1
                img_apres_epaississement[i][j] = img[i][j]

    return img_apres_epaississement


def squelette_lantuejoul(img, iteration_lantejoul=20):
    x_max = len(img)
    y_max = len(img[0])
    img_squelette_lantuejoul = np.zeros((x_max, y_max), dtype=int)

    for n in range(0, iteration_lantejoul):
        img_erodee_rayon_n = erosion_image_binaire(img, n)
        img_ouverte_img_erodee_rayon_n = ouverture_img(img)
        img_diff = img_diff(img_erodee_rayon_n, img_ouverte_img_erodee_rayon_n)
        img_squelette_lantuejoul = addition_2_images(img_squelette_lantuejoul, img_diff)

    return img_squelette_lantuejoul


def squelette_amincissement_homothopique(img):
    return img
