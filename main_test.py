import numpy as np
import matplotlib.pyplot as plt
from functions import *

if __name__ == '__main__':
    img = np.zeros((20, 20), dtype=int)
    img[17][17] = 1
    img[7][8] = 1
    for i in range(0, 5):
        for j in range(0, 5):
            img[i+3][j+10] = 1
            img[i+7][5] = 1
            img[i+7][6] = 1
            img[i+7][7] = 1
    print(img)
    plt.imshow(img, cmap=plt.cm.gray)
    plt.show()

    img_a_traiter = img
    #test erosion
    img_erodee = erosion_image_binaire(img_a_traiter)
    print(img_erodee)
    plt.imshow(img_erodee, cmap=plt.cm.gray)
    plt.title('erosion')
    plt.show()

    #test dilatation
    img_dilatee = dilatation_image_binaire(img_a_traiter)
    plt.imshow(img_dilatee, cmap=plt.cm.gray)
    plt.title('dilatation')
    plt.show()

    #test_ouverture
    img_ouverture = ouverture_img(img_a_traiter)
    plt.imshow(img_ouverture, cmap=plt.cm.gray)
    plt.title('ouverture')
    plt.show()

    #test_fermeture
    img_fermeture = fermeture_img(img_a_traiter)
    plt.imshow(img_fermeture, cmap=plt.cm.gray)
    plt.title('fermeture')
    plt.show()

    #test
    img_amincissement = amincissement_img(img_a_traiter)
    plt.imshow(img_dilatee, cmap=plt.cm.gray)
    plt.title('amincissement')
    plt.show()

    #test
    elem_struct_epaissi = [[2, 0, 2],
                           [1, 2, 2],
                           [2, 2, 2]]
    img_epaississement = epaississement_img(img_a_traiter, elem_struct_epaissi)
    plt.imshow(img_epaississement, cmap=plt.cm.gray)
    plt.title('epaississemnt')
    plt.show()

    #test
    img_squelette_lantuejoul = squelette_lantuejoul(img_a_traiter, 10)
    plt.imshow(img_squelette_lantuejoul, cmap=plt.cm.gray)
    plt.title('lantuejoul')
    plt.show()

    #test
    img_squelette_amincissement = squelette_amincissement_homotopique(img_a_traiter)
    plt.imshow(img_squelette_amincissement, cmap=plt.cm.gray)
    plt.title('squelette amincissement')
    plt.show()
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
    ax[-1].set_title("Erosion")  # set title
    plt.imshow(img_erodee, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 3))
    ax[-1].set_title("Dilatation")  # set title
    plt.imshow(img_dilatee, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 4))
    ax[-1].set_title("Ouverture")  # set title
    plt.imshow(img_ouverture, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 5))
    ax[-1].set_title("Fermeture")  # set title
    plt.imshow(img_fermeture, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 6))
    ax[-1].set_title("Epaississement")  # set title
    plt.imshow(img_epaississement, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 7))
    ax[-1].set_title("Amancissement")  # set title
    plt.imshow(img_amincissement, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 8))
    ax[-1].set_title("Squelette Lantuejoul")  # set title
    plt.imshow(img_squelette_lantuejoul, cmap=plt.cm.gray)

    ax.append(fig.add_subplot(rows, columns, 9))
    ax[-1].set_title("Squelette emancissement homotopique")  # set title
    plt.imshow(img_squelette_amincissement, cmap=plt.cm.gray)

    plt.show()  # finally, render the plot

