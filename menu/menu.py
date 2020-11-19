import os
from PIL import Image
from nightsight import nightsight
from nightsight_color import nightsight_color
from random_pixelator import random_pixelator


def lister(*foo):
    print("""Liste des commandes:
    - quitter
    Quitte le menu sans enregistrer les modifications.

    - importer-image {nom}
    Importe l'image de nom {nom} dans le menu pour être modifiée. L'image
    doit être dans le même dossier que le fichier menu.py.

    - lister-images
    Liste les images déjà importées et celles pouvant l'être.

    - de-nuit {image}
    Applique le filtre nightsight à {image}. L'image sera alors modifiée comme
    si elle avait été prise de nuit.

    - de-nuit-couleurs {image}
    Applique le filtre nightsight à {image}. L'image sera alors modifiée comme
    si elle avait été prise de nuit, mais avec des couleurs.

    - dégrader {image} {taille_block} {pourcentage}
    Pixélise des blocs de longueur et largeur {taille_block} pixels, totalisant
    une surface totale de {pourcentage}% de l'image. La position de chaque
    bloc pixelisé est déterminée aléatoirement.

    - afficher {image}
    Afficher {image}. Peut ne pas fonctionner si ImageMagick n'est pas installé
    sur l'ordinateur.

    - sauvegarder {image} {fichier}
    Sauvegarde l'image {image} dans un fichier {fichier} et la supprime de la
    liste d'images.

    Exemple de commandes :
    importer_image lena.png
    de-nuit lena.png
    afficher lena.png
    sauvegarder lena.png lena-modifie.png
    """)

imported_images = dict()

def import_image(*args):
    filename = args[0][0]
    try:
        image = Image.open(filename)
        imported_images[filename] = image
    except:
        print("ERREUR: image introuvable.")

def list_images(*args):
    i_m = list(imported_images.keys())

    try:
        files = [f for f in os.listdir() if os.path.isfile(os.path.join(f))]
        available = [f for f in files if not f in i_m and f.split(".")[-1].lower() in ["jpg", "png", "jpeg"]]
    except:
        pass

    print("Images importées :\n{}\nImages disponibles :\n{}".format(i_m, available))

def ns(*args):
    args = args[0]
    image = args[0]
    if image in imported_images.keys():
        imported_images[image] = nightsight(imported_images[image])
    else:
        print("ERREUR: L'image {} n'est pas importée.".format(image))

def ns_c(*args):
    print("AVERTISSEMENT: ce filtre peut prendre un certain temps à être exécuté.")
    args = args[0]
    image = args[0]
    if image in imported_images.keys():
        imported_images[image] = nightsight_color(imported_images[image])
    else:
        print("ERREUR: L'image {} n'est pas importée.".format(image))

def r_p(*args):
    args = args[0]
    if len(args) < 3:
        print("ERREUR: pas assez d'arguments ont été passés à ce filtre. Pour plus d'informations, tapez 'lister'.")
    else:
        image = args[0]
        block_size = int(args[1])
        coverage_percentage = int(args[2])
        if image in imported_images.keys():
            imported_images[image] = random_pixelator(imported_images[image], block_size, coverage_percentage)
        else:
            print("ERREUR: L'image {} n'est pas importée.".format(image))

def display(*args):
    image = args[0][0]

    if image in imported_images.keys():
        try:
            imported_images[image].show()
        except:
            print("ERREUR: Impossible d'afficher l'image.")
    else:
        print("ERREUR: L'image {} n'est pas importée.".format(image))

def save(*args):
    args = args[0]
    image = args[0]
    name = args[1]
    if image in imported_images.keys():
        if image.split(".")[-1].lower() == "jpg":
            imported_images[image].save(name, "JPEG", quality=100)
        else:
            imported_images[image].save(name, "PNG")
        del(imported_images[image])
    else:
        print("ERREUR: L'image {} n'est pas importée.".format(image))

print("Bonjour,\nBienvenue dans le menu de CORNE Maxime.\nPour lister les\
 commandes disponibles, tapez 'lister'.")

commands = {
        "lister": lister, 
        "importer-image": import_image,
        "lister-images": list_images,
        "de-nuit": ns,
        "de-nuit-couleurs": ns_c,
        "dégrader": r_p,
        "afficher": display,
        "sauvegarder": save,
}
while True:
    command = input("> ")
    if command.split()[0] == "quitter":
        break
    if command.split()[0] in commands:
        try:
            commands[command.split()[0]](command.split()[1:])
        except:
            print("ERREUR: cela a échoué, veuillez recommencer.")
    else:
        print("Commande inconnue. Veuillez réessayer.")
