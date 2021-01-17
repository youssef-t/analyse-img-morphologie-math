import numpy as np
import matplotlib.pyplot as plt
from functions import *
import matplotlib.image as mpimg

if __name__ == '__main__':
    img = np.zeros((120, 120), dtype=int)
    img[27][27] = 1
    img[7][8] = 1
    for i in range(0, 20):
        img[i + 7][5] = 1
        img[i + 7][6] = 1
        img[i + 7][7] = 1
        for j in range(0, 6):
            img[i+3][j+10] = 1

    for j in range(20, len(img[0]) - 20):
        for i in range(40, 100):
            img[i][j] = 1

    img2 = np.zeros((120, 120), dtype=int)
    for i in range(30, 100):
        for j in range(0, 10):
            img2[i][j+50] = 1

    plt.imshow(img, cmap=plt.cm.gray)
    plt.show()

    #img_pieces = mpimg.imread("./resources/frog_binary3.gif")
    #print(img_pieces.shape)

    img_a_traiter = img

    #test addition
    img_addition = addition_2_images(img_a_traiter, img2)

    #test_soustraction
    img_soustraction = soustraction_2_images(img_a_traiter, img2)

    #test erosion
    img_erodee = erosion_image_binaire(img_a_traiter)

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
    img_squelette_lantuejoul = squelette_lantuejoul(img_a_traiter, iteration_lantejoul=25)

    #test
    img_squelette_amincissement = squelette_amincissement_homotopique(img_a_traiter)

    '''
    # subplot(r,c) provide the no. of rows and columns
    f, axarr = plt.subplots(5, 2)

    # use the created array to output your multiple images. In this case I have stacked 4 images vertically
    axarr[0][0].imshow(img)
    axarr[0][1].imshow(img_erodee)
    axarr[1][0].imshow(img_dilatee)
    axarr[1][1].imshow(img_ouverture)
    axarr[2][0].imshow(img_fermeture)
    axarr[2][1].imshow(img_epaississement)
    axarr[3][0].imshow(img_amincissement)
    axarr[3][1].imshow(img_squelette_lantuejoul)
    axarr[4][0].imshow(img_squelette_amincissement)
    f.show()
    '''


    #afficher toutes les images
    fig = plt.figure(figsize=(5, 2))
    columns = 4
    rows = 3

    # ax enables access to manipulate each of subplots
    ax = []

    # create subplot and append to ax
    ax.append(fig.add_subplot(rows, columns, 1))
    ax[-1].set_title("Image originale")  # set title
    plt.imshow(img_a_traiter, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 2))
    ax[-1].set_title("Deuxième image")  # set title
    plt.imshow(img2, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 3))
    ax[-1].set_title("Addition")  # set title
    plt.imshow(img_addition, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 4))
    ax[-1].set_title("Soustraction")  # set title
    plt.imshow(img_soustraction, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 5))
    ax[-1].set_title("Erosion")  # set title
    plt.imshow(img_erodee, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 6))
    ax[-1].set_title("Dilatation")  # set title
    plt.imshow(img_dilatee, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 7))
    ax[-1].set_title("Ouverture")  # set title
    plt.imshow(img_ouverture, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 8))
    ax[-1].set_title("Fermeture")  # set title
    plt.imshow(img_fermeture, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 9))
    ax[-1].set_title("Epaississement")  # set title
    plt.imshow(img_epaississement, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 10))
    ax[-1].set_title("Amancissement")  # set title
    plt.imshow(img_amincissement, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 11))
    ax[-1].set_title("Squelette Lantuejoul")  # set title
    plt.imshow(img_squelette_lantuejoul, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 12))
    ax[-1].set_title("Squelette emancissement homotopique")  # set title
    plt.imshow(img_squelette_amincissement, cmap=plt.cm.gray)

    plt.show()  # finally, render the plot

