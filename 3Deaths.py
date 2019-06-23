# Modulos
# ----------------------------------------------------------------------------
import pygame
import sys
from pygame.locals import *
import random
#----------------------------------------------------------------------------

# Global
#--------------------------------------------------------------------------
WIDTH = 800    #1300
HEIGHT = 650
# ---------------------------------------------------------------------

# Clases
# ---------------------------------------------------------------------
class Agentes(pygame.sprite.Sprite):

    def __init__(self, i, n, c, vida):
        #pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/grupo.png")
        self.image = pygame.transform.scale(self.image,(100,50))
        self.speed = 4

        self.rect = self.image.get_rect()

        self.i = i
        self.n = n
        self.c = c
        self.vida = vida

        self.equipo = []


    def AgregarPersonajes(self, agentes, equipo, screen):
        for i in range(3):
            #print("personaje ",i," ---->", i+10)
            agentes.equipo.append(Agentes(random.randint(1,10),random.randint(1,10),random.randint(1,10), 800))


    def ActualizarAtributos(self, screen, agentes, nivel):
        #print(nivel, agentes.i, agentes.n, agentes.c, agentes.vida)
        agentes.barras1(screen, agentes.vida)

        for n in agentes.equipo:
            self.ActualizarAtributos(screen, n, nivel + "-")


    def RestartVida(self, screen, agentes, Rvida):
        #print(".....>",nivel,agentes.vida)
        agentes.vida -= Rvida
        #print(agentes.vida)

        for n in agentes.equipo:
            self.RestartVida(screen, n, Rvida)


    def load_image(self, filename, transparent=False):
        image = pygame.image.load(filename)
        image = image.convert()

        return image


    def nivelEnJuego1(self, screen, agentes):

        nivel1 = pygame.image.load('imagenes/barda1.png')
        #nivel1 = pygame.transform.scale(nivel1,(700,70))
        screen.blit(nivel1,(0,50))
        transparent = pygame.Surface((0,0),pygame.SRCALPHA)

        bloque1 = pygame.Rect(260,60,100,50)
        bloque2 = pygame.Rect(630,60,100,50)
        bloque3 = pygame.Rect(1040,60,100,50)

        pygame.draw.rect(screen,(0,0,0), transparent.get_rect())

        if(bloque1.colliderect(agentes)):
            self.RestartVida(screen, agentes, 1)
            print("\n bloque 1 nivel 1")

        elif(bloque2.colliderect(agentes)):
            print("\n bloque 2 nivel 1")

        elif(bloque3.colliderect(agentes)):
            print("\n bloque 3 nivel 1")

    def nivelEnJuego2(self, screen, agentes):

        nivel2 = pygame.image.load('imagenes/barda2.png')
        screen.blit(nivel2,(0,180))
        transparent = pygame.Surface((0,0),pygame.SRCALPHA)

        bloque1 = pygame.Rect(90,190,100,50)
        bloque2 = pygame.Rect(420,190,100,50)
        bloque3 = pygame.Rect(810,190,100,50)
        bloque4 = pygame.Rect(1100,190,100,50)

        pygame.draw.rect(screen,(0,0,0), transparent.get_rect())

        if(bloque1.colliderect(agentes)):
            print("\n bloque 1 nivel 2")

        elif(bloque2.colliderect(agentes)):
            print("\n bloque 2 nivel 2")

        elif(bloque3.colliderect(agentes)):
            print("\n bloque 3 nivel 2")

        elif(bloque4.colliderect(agentes)):
            print("\n bloque 4 nivel 2")

    def nivelEnJuego3(self, screen, agentes):

        nivel3 = pygame.image.load('imagenes/barda3.png')
        screen.blit(nivel3,(0,310))
        transparent = pygame.Surface((0,0),pygame.SRCALPHA)

        bloque1 = pygame.Rect(5,320,75,50)
        bloque2 = pygame.Rect(265,320,75,50)
        bloque3 = pygame.Rect(600,320,90,50)
        bloque4 = pygame.Rect(970,320,80,50)
        bloque5 = pygame.Rect(1230,320,100,50)

        pygame.draw.rect(screen,(0,0,0), transparent.get_rect())

        if(bloque1.colliderect(agentes)):
            print("\n bloque 1 nivel 3")

        elif(bloque2.colliderect(agentes)):
            print("\n bloque 2 nivel 3")

        elif(bloque3.colliderect(agentes)):
            print("\n bloque 3 nivel 3")

        elif(bloque4.colliderect(agentes)):
            print("\n bloque 4 nivel 3")

        elif(bloque5.colliderect(agentes)):
            print("\n bloque 5 nivel 3")

    def barras1(self, screen, vida):

        color1 = (255,0,0,0)
        rect1 = (0 ,560, vida , 20) #el tercer parametro es la vida 100 = 100%
        pygame.draw.rect(screen, color1, rect1, 1)

        #color2 = (40, 210, 250)
        #rect2 = (10,540, e1,10)
        #pygame.draw.rect(screen, color2, rect2, 1)

    '''
    def barras2(screen,agentes):

        color1 = (255,0,0,0)
        rect1 = (10,570,400, 10)
        color2 = (40, 210, 250)
        rect2 = (10,580,400, 10)
        width = 0

        pygame.draw.rect(screen, color1, rect1, width)
        pygame.draw.rect(screen, color2, rect2, width)

    def barras3(screen,agentes):

        color1 = (255,0,0,0)
        rect1 = (10,610, 400, 10)
        color2 = (40, 210, 250)
        rect2 = (10,620, 400, 10)
        width = 0

        pygame.draw.rect(screen, color1, rect1, width)
        pygame.draw.rect(screen, color2, rect2, width)
    '''

    def MovimientoTeclas(self, agentes):
            key = pygame.key.get_pressed()

            if key[K_LEFT]:
                if agentes.rect.left == 0:
                    pass
                else:
                    agentes.rect.left -= agentes.speed
                    if key[K_UP]:
                        if agentes.rect.top == 0:
                            pass
                        else:
                            agentes.rect.top -= agentes.speed

                    elif key[K_DOWN]:
                        if agentes.rect.top == 429:
                            pass
                        else:
                            agentes.rect.top += agentes.speed

            elif key[K_RIGHT]:
                if agentes.rect.left == 1240:
                    pass
                else:
                    agentes.rect.left += agentes.speed
                    if key[K_UP]:
                        if agentes.rect.top == 0:
                            pass
                        else:
                            agentes.rect.top -= agentes.speed

                    elif key[K_DOWN]:
                        if agentes.rect.top == 429:
                            pass
                        else:
                            agentes.rect.top += agentes.speed

            elif key[K_UP]:
                if agentes.rect.top == 0:
                    pass
                else:
                    agentes.rect.top -= agentes.speed

            elif key[K_DOWN]:
                if agentes.rect.top == 432:
                    pass
                else:
                    agentes.rect.top += agentes.speed


    def MouseClick(self, screen, agentes, evento):

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                print("boton izquierdo")

            elif evento.button == 2:
                #agentes.AgregarPersonajes(agentes, screen)
                print("boton enmedio")

            elif evento.button == 3:
                print("boton derecho")


def main():
    pygame.init()
    agentes = Agentes(0,0,0,0)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Proyecto IA - 3Deaths")
    background = agentes.load_image('imagenes/fondo.png')

    agentes.AgregarPersonajes(agentes, agentes.equipo, screen)

    while True:



        screen.blit(background,(0,0))
        screen.blit(agentes.image, agentes.rect)

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
                return 0

            agentes.MouseClick(screen, agentes, evento)

        agentes.ActualizarAtributos(screen, agentes, "-")

        agentes.MovimientoTeclas(agentes)

        agentes.nivelEnJuego1(screen, agentes)
        agentes.nivelEnJuego2(screen, agentes)
        agentes.nivelEnJuego3(screen, agentes)


        pygame.display.update()
        pygame.display.flip()

    #return 0

# ---------------------------------------------------------------------


# Main
#----------------------------------------------------------------------
if __name__ == '__main__':

    main()
