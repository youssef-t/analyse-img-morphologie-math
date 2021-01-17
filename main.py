import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from functions import *
# chemin des images
chemin_img_apple_1 = "./resources/apple-1.gif"
chemin_img_apple_2 = "./resources/apple-2.gif"
chemin_img_apple_3 = "./resources/apple-4.gif"
chemin_img_DC = "./resources/Fig1204(WashingtonDC ).tif"
chemin_img_frog_1 = "./resources/frog_binary1.gif"
chemin_img_frog_2 = "./resources/frog_binary2.gif"
chemin_img_frog_3 = "./resources/frog_binary3.gif"

#charger les images
img_apple_1 = mpimg.imread(chemin_img_apple_1)
img_apple_2 = mpimg.imread(chemin_img_apple_2)
img_apple_3 = mpimg.imread(chemin_img_apple_3)
img_DC = mpimg.imread(chemin_img_DC)
img_frog_1 = mpimg.imread(chemin_img_frog_1)
img_frog_2 = mpimg.imread(chemin_img_frog_2)
img_frog_3 = mpimg.imread(chemin_img_frog_3)
print(img_frog_3.shape)
#test du seuil
img_DC = seuil_image(img_DC, 100)

plt.imshow(img_DC, cmap=plt.cm.gray)
plt.show()
print(img_DC)

#appeler les fonctions définies
img_a_traiter = img_frog_3
img_added = addition_2_images(img_apple_1, img_apple_3)
img_soustraction = soustraction_2_images(img_apple_2, img_apple_3)
img_erodee = erosion_image_binaire(img_a_traiter)
img_dilatee = dilatation_image_binaire(img_a_traiter)
img_ouverture = ouverture_img(img_a_traiter)
img_fermeture = fermeture_img(img_a_traiter)
img_amincissement = amincissement_img(img_a_traiter)
img_epaississement = epaississement_img(img_a_traiter)
img_squelette_lantuejoul = squelette_lantuejoul(img_a_traiter, 10)
print(img_squelette_lantuejoul)
img_squelette_amincissement_homotopique = squelette_amincissement_homotopique(img_a_traiter)


# Output Images
#plt.imshow(img1, cmap=plt.cm.gray)
plt.imshow(img_added, cmap=plt.cm.gray)
plt.show()

plt.imshow(img_soustraction, cmap=plt.cm.gray)
plt.show()

plt.imshow(img_erodee, cmap=plt.cm.gray)
plt.show()

plt.imshow(img_dilatee, cmap=plt.cm.gray)
plt.show()

plt.imshow(img_ouverture, cmap=plt.cm.gray)
plt.show()

plt.imshow(img_fermeture, cmap=plt.cm.gray)
plt.show()

plt.imshow(img_dilatee, cmap=plt.cm.gray)
plt.show()

plt.imshow(img_amincissement, cmap=plt.cm.gray)
plt.show()

plt.imshow(img_epaississement, cmap=plt.cm.gray)
plt.show()
plt.imshow(img_squelette_lantuejoul, cmap=plt.cm.gray)
plt.show()
plt.imshow(img_squelette_amincissement_homotopique, cmap=plt.cm.gray)
plt.show()



'''
plt.figure()

#subplot(r,c) provide the no. of rows and columns
f, axarr = plt.subplots(4,1)

# use the created array to output your multiple images. In this case I have stacked 4 images vertically
axarr[0].imshow(img_added)
axarr[1].imshow(img_soustraction)
axarr[2].imshow(img_erodee)
axarr[3].imshow(img_)
'''