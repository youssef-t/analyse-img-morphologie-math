import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from functions import *

if __name__ == '__main__':
    # Generate picture
    img = np.zeros((120, 120), dtype=int)
    img[27][27] = 1
    img[7][8] = 1
    for i in range(0, 20):
        img[i + 10][10] = 1
        img[i + 10][11] = 1
        img[i + 10][12] = 1
        for j in range(0, 6):
            img[i + 10][j + 14] = 1
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
            img[i][j + 45] = 1

    img2 = np.zeros((120, 120), dtype=int)
    for i in range(50, 80):
        for j in range(0, 10):
            img2[i][j + 50] = 1

    # Display generate picture
    plt.imshow(img, cmap='gray')
    plt.title("Generated picture")
    plt.show()

    # Record picture
    # img_pieces = mpimg.imread("./resources/frog_binary3.gif")
    # print("img_pieces.shape: '{}'".format(img_pieces.shape))

    #image to test "seuil"
    chemin_img_DC = "./resources/Fig1204(WashingtonDC ).tif"
    img_DC = mpimg.imread(chemin_img_DC)
    #show initial image
    plt.imshow(img_DC, cmap=plt.cm.gray)
    plt.title("Image to test 'seuil'")
    plt.show()
    # threshold test
    img_DC = seuil_image(img_DC, 100)
    plt.imshow(img_DC, cmap=plt.cm.gray)
    plt.title("'seuil' test'")
    plt.show()

    # Save image to be processed
    img_a_traiter = img

    # Create figure for global result display
    fig = plt.figure(figsize=(5, 2))
    columns = 4
    rows = 3

    # ax enables access to manipulate each of subplots
    ax = []

    # create subplot and append to ax
    ax.append(fig.add_subplot(rows, columns, 1))
    ax[-1].set_title("Image originale")
    plt.imshow(img_a_traiter, cmap='gray')

    # Display img2 for subtraction and addition
    ax.append(fig.add_subplot(rows, columns, 2))
    ax[-1].set_title("Deuxième image")
    plt.imshow(img2, cmap='gray')

    # Calculate and display img_addition
    img_addition = addition_2_images(img_a_traiter, img2)
    ax.append(fig.add_subplot(rows, columns, 3))
    ax[-1].set_title("Addition")
    plt.imshow(img_addition, cmap='gray')

    # Calculate and display img_soustraction
    img_soustraction = soustraction_2_images(img_a_traiter, img2)
    ax.append(fig.add_subplot(rows, columns, 4))
    ax[-1].set_title("Soustraction")
    plt.imshow(img_soustraction, cmap='gray')

    # Calculate and display img_erodee
    img_erodee = erosion_image_binaire(img_a_traiter, rayon_element_structurant=1)
    ax.append(fig.add_subplot(rows, columns, 5))
    ax[-1].set_title("Erosion")
    plt.imshow(img_erodee, cmap='gray')

    # Calculate and display img_dilatee
    img_dilatee = dilatation_image_binaire(img_a_traiter)
    ax.append(fig.add_subplot(rows, columns, 6))
    ax[-1].set_title("Dilatation")
    plt.imshow(img_dilatee, cmap='gray')

    # Calculate and display img_ouverture
    img_ouverture = ouverture_img(img_a_traiter)
    ax.append(fig.add_subplot(rows, columns, 7))
    ax[-1].set_title("Ouverture")
    plt.imshow(img_ouverture, cmap='gray')

    # Calculate and display img_fermeture
    img_fermeture = fermeture_img(img_a_traiter)
    ax.append(fig.add_subplot(rows, columns, 8))
    ax[-1].set_title("Fermeture")
    plt.imshow(img_fermeture, cmap='gray')

    # Calculate and display img_epaississement
    elem_struct_epaissi = [[2, 0, 2], [1, 0, 2], [2, 2, 2]]
    img_epaississement = epaississement_img(img_a_traiter, elem_struct_epaissi)
    ax.append(fig.add_subplot(rows, columns, 9))
    ax[-1].set_title("Epaississement")
    plt.imshow(img_epaississement, cmap='gray')

    # Calculate and display img_amincissement
    img_amincissement = amincissement_img(img_a_traiter)
    ax.append(fig.add_subplot(rows, columns, 10))
    ax[-1].set_title("Amincissement")
    plt.imshow(img_amincissement, cmap='gray')

    # Calculate and display img_squelette_lantuejoul
    img_squelette_lantuejoul = squelette_lantuejoul(img_a_traiter, iteration_lantejoul=30)
    ax.append(fig.add_subplot(rows, columns, 11))
    ax[-1].set_title("Squelette Lantuejoul")
    plt.imshow(img_squelette_lantuejoul, cmap='gray')

    # Calculate and display img_squelette_amincissement
    img_squelette_amincissement = squelette_amincissement_homotopique(img_a_traiter)
    ax.append(fig.add_subplot(rows, columns, 12))
    ax[-1].set_title("Squelette amincissement homotopique")
    plt.imshow(img_squelette_amincissement, cmap='gray')

    plt.show()  # finally, render the plot
