
import numpy as np

'''
Remarque: toutes les fonctions n'acceptent que des images binaires 
'''
def seuil_image(img, seuil):
    x_max = len(img)
    y_max = len(img[0])
    img_apres_seuillage = np.zeros((x_max, y_max))
    for i in range(0, x_max):
        for j in range(0, y_max):
            if img[i][j] > seuil:
                img_apres_seuillage[i][j] = 1
            else:
                img_apres_seuillage[i][j] = 0
    return img_apres_seuillage


def addition_2_images(img1, img2):
    x_max = len(img1)
    y_max = len(img2)
    img_apres_addition = np.zeros((x_max, y_max))
    for i in range(0, x_max):
        for j in range(0, y_max):
            img_apres_addition[i][j] = img1[i][j] + img2[i][j]
    return img_apres_addition


def soustraction_2_images(img1, img2):
    x_max = len(img1)
    y_max = len(img1[0])
    img_apres_soustraction = np.zeros((x_max, y_max))
    for i in range(0, x_max):
        for j in range(0, y_max):
            img_apres_soustraction[i][j] = img1[i][j] - img2[i][j]
    return img_apres_soustraction


def erosion_image_binaire(img):
    x_max = len(img)
    y_max = len(img[0])
    img_apres_erosion = np.zeros((x_max, y_max))
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
    img_apres_dilatation = np.zeros((x_max, y_max))
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


def amincissement_img(img):
    '''
    :param img:
    :return:
    '''


def epaississement_img(img):
    '''

    :param img:
    :return:
    '''


