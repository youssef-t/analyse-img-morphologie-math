import numpy as np
import matplotlib.pyplot as plt
from functions import *
import matplotlib.image as mpimg

if __name__ == '__main__':
    img = np.zeros((120, 120), dtype=int)
    img[27][27] = 1
    img[7][8] = 1
    for i in range(0, 20):
        img[i + 10][10] = 1
        img[i + 10][11] = 1
        img[i + 10][12] = 1
        for j in range(0, 6):
            img[i+10][j+14] = 1
    '''
    for j in range(20, len(img[0]) - 20):
        for i in range(40, 100):
            img[i][j] = 1
    '''
    for i in range(40, 60):
        for j in range(30, 90):
            img[i][j] = 1

    for i in range(60, 90):
        for j in range(30, 45):
            img[i][j] = 1
            img[i][j+45] = 1

    img2 = np.zeros((120, 120), dtype=int)
    for i in range(50, 80):
        for j in range(0, 10):
            img2[i][j+50] = 1

    plt.imshow(img, cmap='gray')
    plt.show()

    #img_pieces = mpimg.imread("./resources/frog_binary3.gif")
    #print(img_pieces.shape)

    img_a_traiter = img

    #test addition
    img_addition = addition_2_images(img_a_traiter, img2)

    #test_soustraction
    img_soustraction = soustraction_2_images(img_a_traiter, img2)

    #test erosion
    img_erodee = erosion_image_binaire(img_a_traiter, rayon_element_structurant=1)

    #test dilatation
    img_dilatee = dilatation_image_binaire(img_a_traiter)

    #test_ouverture
    img_ouverture = ouverture_img(img_a_traiter)

    #test_fermeture
    img_fermeture = fermeture_img(img_a_traiter)

    #test amincissement
    img_amincissement = amincissement_img(img_a_traiter)

    #test epaississement
    elem_struct_epaissi = [[2, 0, 2],
                           [1, 0, 2],
                           [2, 2, 2]]
    img_epaississement = epaississement_img(img_a_traiter, elem_struct_epaissi)

    #test
    img_squelette_lantuejoul = squelette_lantuejoul(img_a_traiter, iteration_lantejoul=30)

    #test
    img_squelette_amincissement = squelette_amincissement_homotopique(img_a_traiter)


    #afficher toutes les images
    fig = plt.figure(figsize=(5, 2))
    columns = 4
    rows = 3

    # ax enables access to manipulate each of subplots
    ax = []

    # create subplot and append to ax
    ax.append(fig.add_subplot(rows, columns, 1))
    ax[-1].set_title("Image originale")  # set title
    plt.imshow(img_a_traiter, cmap='gray')

    ax.append(fig.add_subplot(rows, columns, 2))
    ax[-1].set_title("Deuxième image")  # set title
    plt.imshow(img2, cmap='gray')

    ax.append(fig.add_subplot(rows, columns, 3))
    ax[-1].set_title("Addition")  # set title
    plt.imshow(img_addition, cmap='gray')

    ax.append(fig.add_subplot(rows, columns, 4))
    ax[-1].set_title("Soustraction")  # set title
    plt.imshow(img_soustraction, cmap='gray')

    ax.append(fig.add_subplot(rows, columns, 5))
    ax[-1].set_title("Erosion")  # set title
    plt.imshow(img_erodee, cmap='gray')

    ax.append(fig.add_subplot(rows, columns, 6))
    ax[-1].set_title("Dilatation")  # set title
    plt.imshow(img_dilatee, cmap='gray')

    ax.append(fig.add_subplot(rows, columns, 7))
    ax[-1].set_title("Ouverture")  # set title
    plt.imshow(img_ouverture, cmap='gray')

    ax.append(fig.add_subplot(rows, columns, 8))
    ax[-1].set_title("Fermeture")  # set title
    plt.imshow(img_fermeture, cmap='gray')

    ax.append(fig.add_subplot(rows, columns, 9))
    ax[-1].set_title("Epaississement")  # set title
    plt.imshow(img_epaississement, cmap='gray')

    ax.append(fig.add_subplot(rows, columns, 10))
    ax[-1].set_title("Amincissement")  # set title
    plt.imshow(img_amincissement, cmap='gray')

    ax.append(fig.add_subplot(rows, columns, 11))
    ax[-1].set_title("Squelette Lantuejoul")  # set title
    plt.imshow(img_squelette_lantuejoul, cmap='gray')

    ax.append(fig.add_subplot(rows, columns, 12))
    ax[-1].set_title("Squelette amincissement homotopique")  # set title
    plt.imshow(img_squelette_amincissement, cmap='gray')

    plt.show()  # finally, render the plot
