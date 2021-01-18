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
    y_max = len(img2)
    img_apres_addition = np.zeros((x_max, y_max), dtype=int)

    if is_binaire:
        for i in range(0, x_max):
            for j in range(0, y_max):
                valeur_pixel = int(img1[i][j]) + int(img2[i][j])
                if valeur_pixel > 1:
                    img_apres_addition[i][j] = 1
                else:
                    img_apres_addition[i][j] = valeur_pixel

    else:
        for i in range(0, x_max):
            for j in range(0, y_max):
                valeur_pixel = int(img1[i][j]) + int(img2[i][j])
                if valeur_pixel > 255:
                    img_apres_addition[i][j] = 255
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
            valeur_pixel = int(img1[i][j]) - int(img2[i][j])
            if valeur_pixel <= 0:
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


def erosion_image_binaire(img, rayon_element_structurant=1):
    x_max = len(img)
    y_max = len(img[0])
    # copier l'image dans une variable locale
    img_apres_erosion = np.array(img, dtype=int)

    if rayon_element_structurant == 0:
        return img_apres_erosion

    # parcourir l'image en prenant en compte la taille de l'élément structurant
    for i in range(rayon_element_structurant, x_max - rayon_element_structurant):
        for j in range(rayon_element_structurant, y_max - rayon_element_structurant):
            # pour ne pas faire les calculs pour les pixels de valeur 0
            if img[i][j] == 1:
                s = 0
                # element structurant
                for ligne_elem_struct in range(-rayon_element_structurant, rayon_element_structurant + 1):
                    for col_elem_struct in range(-rayon_element_structurant, rayon_element_structurant + 1):
                        s += img[i + ligne_elem_struct][j + col_elem_struct]
                # rayon 1 => 3*3 = (2*1 +1)^2; rayon 2 => 5*5 = (2*2 +1)^2; rayon 3 => (2*3+1)^2
                # rayon n => (2*n +1)^2 éléments dans la matrice
                if s != (2 * rayon_element_structurant + 1) ** 2:
                    img_apres_erosion[i][j] = 0

    # on met les pixels non parcourus à 0
    # bords de l'image
    for i in range(0, x_max):
        for j in range(0, rayon_element_structurant):
            img_apres_erosion[i][j] = 0
            img_apres_erosion[i][y_max - j - 1] = 0
    for j in range(0, y_max):
        for i in range(0, rayon_element_structurant):
            img_apres_erosion[i][j] = 0
            img_apres_erosion[x_max - i - 1][j] = 0

    return img_apres_erosion


def dilatation_image_binaire(img, rayon_element_structurant=1):
    x_max = len(img)
    y_max = len(img[0])
    # copier l'image dans une variable locale
    img_apres_dilatation = np.array(img, dtype=int)

    if rayon_element_structurant == 0:
        return img_apres_dilatation

    # parcourir l'image en prenant en compte la taille de l'élément structurant
    for i in range(rayon_element_structurant, x_max - rayon_element_structurant):
        for j in range(rayon_element_structurant, y_max - rayon_element_structurant):
            # pour ne pas faire les calculs pour les pixels de valeur 1
            if img[i][j] == 0:
                s = 0
                # element structurant
                for ligne_elem_struct in range(-rayon_element_structurant, rayon_element_structurant + 1):
                    for col_elem_struct in range(-rayon_element_structurant, rayon_element_structurant + 1):
                        s += img[i + ligne_elem_struct][j + col_elem_struct]
                if s > 0:
                    img_apres_dilatation[i][j] = 1
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
    img_apres_amincissement = np.array(img, dtype=int)
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
                        if element_structurant[ligne_elem_struct + 1][col_elem_struct + 1] == 2:
                            nbr_pixels_identiques += 1
                        else:
                            differance = img[i + ligne_elem_struct][j + col_elem_struct] \
                                         - element_structurant[ligne_elem_struct + 1][col_elem_struct + 1]
                            if differance == 0:
                                nbr_pixels_identiques += 1
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

    return img_apres_amincissement


# Remarque: avec l'élément structurant par défaut, aucune modification sera faite
def epaississement_img(img, element_structurant=ELEMENT_STRUCTURANT_PAR_DEFAUT):
    x_max = len(img)
    y_max = len(img[0])
    img_apres_epaississement = np.array(img, dtype=int)
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
                        if element_structurant[ligne_elem_struct + 1][col_elem_struct + 1] == 2:
                            nbr_pixels_identiques += 1
                        else:
                            differance = img[i + ligne_elem_struct][j + col_elem_struct] \
                                         - element_structurant[ligne_elem_struct + 1][col_elem_struct + 1]
                            if differance == 0:
                                nbr_pixels_identiques += 1
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

    return img_apres_epaississement


def squelette_lantuejoul(img, iteration_lantejoul=30):
    x_max = len(img)
    y_max = len(img[0])
    img_squelette_lantuejoul = np.zeros((x_max, y_max), dtype=int)

    img_full_zeros = np.zeros((x_max, y_max), dtype=int)
    # formule simplifiée du théorème de Lantuejoul: on commence de 1
    for n in range(1, iteration_lantejoul + 1):
        img_erodee_rayon_n = erosion_image_binaire(img, n)
        if (img_erodee_rayon_n == img_full_zeros).all():
            break
        img_ouverte_img_erodee_rayon_n = ouverture_img(img_erodee_rayon_n)
        print(f"LANTUEJOUL - boucle : {n}")
        img_diff = soustraction_2_images(img_erodee_rayon_n, img_ouverte_img_erodee_rayon_n)
        img_squelette_lantuejoul = addition_2_images(img_squelette_lantuejoul, img_diff)

    return img_squelette_lantuejoul


def squelette_amincissement_homotopique(img):
    # copier l'image dans des variables locales
    img_squelette_amincissement_homotopique_post = np.array(img, dtype=int)
    img_squelette_amincissement_homotopique_pre = np.array(img, dtype=int)
    # la valeur 2 correspond à une valeur quelconque
    element_structurant = [[2, 0, 2],
                           [1, 1, 0],
                           [1, 1, 2]]

    # calculer le squelette jusqu'à l'idempotance
    # la boucle "do...while(condition)" n'existe pas en Python
    # on utilise alors la syntaxe suivante: while True ... if(condition): break
    compteur = 0
    while True:
        img_squelette_amincissement_homotopique_post = amincissement_img(img_squelette_amincissement_homotopique_post,
                                                                         element_structurant)

        compteur += 1
        print(f'Amincissement homotopique - boucle: {compteur}')

        # vérifier l'idempotance
        if (img_squelette_amincissement_homotopique_pre == img_squelette_amincissement_homotopique_post).all() or \
                compteur > 500:
            break

        # copie par valeur
        img_squelette_amincissement_homotopique_pre = np.copy(img_squelette_amincissement_homotopique_post)

    return img_squelette_amincissement_homotopique_post
