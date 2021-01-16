
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
            #si l'image est binaire
            else:
                if valeur_pixel > 1:
                    img_apres_addition[i][j] = 1
                else:
                    img_apres_addition[i][j] = valeur_pixel

    return img_apres_addition

#Remarque: on n'a pas besoin de spécifier si l'image est binaire ou en niveau de gris
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


def erosion_image_binaire(img):
    x_max = len(img)
    y_max = len(img[0])
    img_apres_erosion = np.zeros((x_max, y_max), dtype=int)
    # parcourir l'image
    for i in range(1, x_max-1):
        for j in range(1, y_max-1):
            s = 0
            # element structurant
            for ligne_elem_struct in range(-1, 2):
                for col_elem_struct in range(-1, 2):
                    s += img[i+ligne_elem_struct][j+col_elem_struct]
            # l'image est initialisée à 0
            if s == 9:
                img_apres_erosion[i][j] = 1
    return img_apres_erosion


def dilatation_image_binaire(img):
    x_max = len(img)
    y_max = len(img[0])
    img_apres_dilatation = np.zeros((x_max, y_max), dtype=int)
    # parcourir l'image
    for i in range(1, x_max-1):
        for j in range(1, y_max-1):
            s = 0
            # element structurant
            for ligne_elem_struct in range(-1, 2):
                for col_elem_struct in range(-1, 2):
                    s += img[i+ligne_elem_struct][j+col_elem_struct]
            # l'image est initialisée à 0
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


def amincissement_img(img, element_structurant):
    x_max = len(img)
    y_max = len(img[0])
    img_apres_amincissement = np.zeros((x_max, y_max), dtype=int)

    return img_apres_amincissement


def epaississement_img(img, element_structurant):
    x_max = len(img)
    y_max = len(img[0])
    img_apres_epaississement = np.zeros((x_max, y_max), dtype=int)

    return img_apres_epaississement

