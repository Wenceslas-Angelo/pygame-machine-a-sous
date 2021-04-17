import pygame
import numpy
from emplacement import Emplacement

pygame.init()

def lancement():
    global jetons
    fruits = ["ananas", "cerise", "orange", "pasteque", "pomme_dore"]
    proba_fruit= [0.2, 0.25, 0.4, 0.1, 0.05]
    fruits_jetons = {
                        "ananas":50,
                        "cerise":15,
                        "orange":5,
                        "pasteque":150,
                        "pomme_dore":10000
                    }

    hasard = numpy.random.choice(fruits, 3, proba_fruit)
    
    emplacement_gauche.set_image(fruits_dict[hasard[0]])
    emplacement_milieu.set_image(fruits_dict[hasard[1]])
    emplacement_droite.set_image(fruits_dict[hasard[2]])

    if hasard[0] == hasard[1] == hasard[2]:
        jetons_gagnes = fruits_jetons[hasard[0]]
        jetons += jetons_gagnes
        # print("{}: + {} jetons".format(hasard[0], jetons_gagnes))


jetons = 1000
screen_width, screen_height = 800, 460
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Machine a sous")

white = (255, 255, 255)
screen.fill(white)

#Background
fond = pygame.image.load("images/slot.png")

font = pygame.font.SysFont("comicsansms", 40)

fruits_dict = {
                    "cerise":pygame.image.load("images/cerise.png"),
                    "ananas":pygame.image.load("images/ananas.png"),
                    "orange":pygame.image.load("images/orange.png"),
                    "pasteque":pygame.image.load("images/pasteque.png"),
                    "pomme_dore":pygame.image.load("images/pomme_dore.png")
                }

hauteur_emplacement = screen_height / 2 + 30
emplacement_x_milieu = screen_width / 3 + 62

emplacements = pygame.sprite.Group()

emplacement_gauche = Emplacement(emplacement_x_milieu-102, hauteur_emplacement)
emplacement_milieu = Emplacement(emplacement_x_milieu, hauteur_emplacement)
emplacement_droite = Emplacement(emplacement_x_milieu+100, hauteur_emplacement)

emplacements.add(emplacement_gauche)
emplacements.add(emplacement_milieu)
emplacements.add(emplacement_droite)


run = True
while run:
    screen.blit(fond, (0, 0))
    emplacements.draw(screen)
    text = font.render(str(jetons)+" jetons", True, (0, 0, 0))
    screen.blit(text, (10,5))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and jetons>=10:
                lancement()
                jetons -= 10

    #pygame.display.update()

pygame.quit()