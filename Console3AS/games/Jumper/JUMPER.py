# JUMPER
# Matteo Domestico
# Vincenzo Ricci
# 2AS

import pygame
import random
import time
from pathlib import Path

if "Jumper" in str(Path.cwd()) :
    path_cartella_gioco = Path.cwd()
else :
    path_currente = Path.cwd()
    path_cartella_gioco = path_currente / "games" / "Jumper"


pygame.init()

# ---------------------------------------------------------------
# Variabili

screen_x = 1000
screen_y = 750

SCREEN_WIDTH = screen_x
SCREEN_HEIGHT = screen_y

x = screen_x // 2
y = screen_y

x2 = x
y2 = y

x3 = x
y3 = y

x4 = x
y4 = y

x5 = x
y5 = y

xD = 1000
xD2 = xD
xD3 = xD
xD4 = xD
xDD2 = xD2
xDD3 = xD3
xDD4 = xD4

yD = screen_y - 150
yD2 = yD
yD3 = yD
yDD = yD - 100
yDD2 = yD - 100
yDD3 = yD - 100

width = 80
height = 80

speed = 2

jump = False
salto = 10

livello = 0

# ------------------------------------------------------------------------
# immagini
path_HermanoD = path_cartella_gioco / "Hermano.png"
HermanoD = pygame.image.load(path_HermanoD)
HermanoD = pygame.transform.scale(HermanoD, (80, 80))

path_HermanoS = path_cartella_gioco / "HermanoS.png"
HermanoS = pygame.image.load(path_HermanoS)
HermanoS = pygame.transform.scale(HermanoS, (80, 80))

Hermano = HermanoD

path_flying_dragon = path_cartella_gioco / "flying dragon.gif"
Drago = pygame.image.load(path_flying_dragon)
Drago = pygame.transform.scale(Drago, (150, 50))

path_prato = path_cartella_gioco / "prato.png"
prato = pygame.image.load(path_prato)
prato = pygame.transform.scale(prato, (500, 250))

path_nuvolaChiara = path_cartella_gioco / "nuvola chiara.png"
nuvolaChiara = pygame.image.load(path_nuvolaChiara)
nuvolaChiara = pygame.transform.scale(nuvolaChiara,(110,110))

path_nuvolaScura = path_cartella_gioco /"nuvola scura.png"
nuvolaScura = pygame.image.load(path_nuvolaScura)
nuvolaScura = pygame.transform.scale(nuvolaScura,(110,110))

path_nuvolaScurissima = path_cartella_gioco /"nuvola ancora più scura.png"
nuvolaScurissima = pygame.image.load(path_nuvolaScurissima)
nuvolaScurissima = pygame.transform.scale(nuvolaScurissima,(110,110))

path_nuvolaGrande = path_cartella_gioco /"nuvola grande.png"
nuvolaGrande = pygame.image.load(path_nuvolaGrande)
nuvolaGrande = pygame.transform.scale(nuvolaGrande,(500,500))

path_castello = path_cartella_gioco /"Castello Bello.png"
castello = pygame.image.load(path_castello)
castello = pygame.transform.scale(castello,(600,600))

# --------------------------------------------------------------------------
# Suoni
path_suonoSalto = path_cartella_gioco /"suonoSalto.mp3"
pygame.mixer.init()
pygame.mixer.music.load(path_suonoSalto)
pygame.mixer.music.set_volume(0.5)

# ----------------------------------------------------------------------------
# Scritte

Titlefont = pygame.font.SysFont('Impact', 100)

close_tip = Titlefont.render("HAI VINTO!!!", True, "blue")

# -----------------------------------------------------------------------------
# Schermo

screen = pygame.display.set_mode( (screen_x , screen_y) )
pygame.display.set_caption("JUMPER")

# ------------------------------------------------------------------------------

clock = pygame.time.Clock()

# ---------------------------------------------------------------------------
# Ciclo while


running = True

# Carichiamo il font per il testo del menu
font = pygame.font.SysFont('Arial', 30)
fontTitolo = pygame.font.SysFont('Arial', 60)

schermata = "istruzioni"

while schermata == "istruzioni":
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Se viene premuto il tasto Esc, ritorna al menù principale    
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            schermata = "menu"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            
        screen.fill("black")
        
        scrittaRect = font.render("ISTRUZIONI", True, "white")
        titoloRect = scrittaRect.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8))

        testoIstruzioni1 = font.render("Muovi il cavagliere usando il joystick",True,"white")
        testoIstruzioni2 = font.render("Evita i draghi mentre salti sulle nuvole",True, "white")
        testoIstruzioni3 = font.render("Supera tutti i livelli per salvare la principessa",True, "white")
        testoIstruzioni4 = font.render("Premi ESC per uscire dalle istruzioni",True, "white")
        testoIstruzioni6 = font.render("Premi Invio per inziare a giocare",True, "white")
        testoIstruzioni5 = font.render("Buona fortuna!",True, "white")

        screen.blit(scrittaRect, titoloRect)
        screen.blit(testoIstruzioni1,(SCREEN_WIDTH // 2 - testoIstruzioni1.get_width() // 2, SCREEN_HEIGHT // 3 - testoIstruzioni1.get_height() // 2))
        screen.blit(testoIstruzioni2,(SCREEN_WIDTH // 2 - testoIstruzioni2.get_width() // 2, SCREEN_HEIGHT // 3 - testoIstruzioni2.get_height() // 2 + 45))
        screen.blit(testoIstruzioni3,(SCREEN_WIDTH // 2 - testoIstruzioni3.get_width() // 2, SCREEN_HEIGHT // 3 - testoIstruzioni3.get_height() // 2 + 90))
        screen.blit(testoIstruzioni4,(SCREEN_WIDTH // 2 - testoIstruzioni4.get_width() // 2, SCREEN_HEIGHT // 2 + testoIstruzioni4.get_height() // 2 + 45))
        screen.blit(testoIstruzioni6,(SCREEN_WIDTH // 2 - testoIstruzioni6.get_width() // 2, SCREEN_HEIGHT // 2 + testoIstruzioni6.get_height() // 2 + 90))
        screen.blit(testoIstruzioni5,(SCREEN_WIDTH // 2 - testoIstruzioni5.get_width() // 2, SCREEN_HEIGHT - testoIstruzioni5.get_height() - 50))
        pygame.display.update()


while running:  

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    
    
    
    screen.fill("light blue")

# -------------------------------------------------------------------
# livello 1
    
    if livello == 0:

        # Comandi livello 1
        
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT] and x > 40: 
            x -= speed * 6
            Hermano = HermanoS
        if keys[pygame.K_RIGHT] and x < screen_x - width // 2:
            x += speed * 6
            Hermano = HermanoD

        if keys[pygame.K_UP] and y - 95 > 0:
            pygame.mixer.music.play()
            jump = True
            
        
        
        if jump:
            if salto >= 0:
                y -= (salto * abs(salto)) * 0.5
                salto -= 0.5
            else:
                jump = False
        
        # Gravità
        
        if y < 750:
            y += 10
        
        # Condizione per salire di livello
        
        if y - 95 < 0:
            livello = 1
        
        
        
        # -------------------------------------------------------------------------------
        # Sprite
        
        hermano = pygame.draw.rect(screen, "light blue", (x - 36, y - 80, 54, 45))
        
        screen.blit(nuvolaGrande,(-50, -440))
        screen.blit(nuvolaGrande,(350, -440))
        screen.blit(nuvolaGrande,(750, -440))
        
        
        prato_rect = pygame.draw.rect(screen, "light blue", (0, screen_y - 36, 1000, 100))
        
        screen.blit(prato,(0,500))
        screen.blit(prato,(500,500))
        
        nuvola1 = pygame.draw.rect(screen, "light blue", (150, 535, 85, 1))
        nuvola2 = pygame.draw.rect(screen, "light blue", (500, 435, 85, 1))
        nuvola3 = pygame.draw.rect(screen, "light blue", (710, 335, 85, 1))
        nuvola4 = pygame.draw.rect(screen, "light blue", (400, 215, 85, 1))
        
        drago = pygame.draw.rect(screen, "light blue", (xD + 15, screen_y // 2 + 82, 120, 36))
        
        
        screen.blit(Hermano,(x - 50, y - 115))
        
        screen.blit(Drago,(xD, screen_y // 2 + 70))
        
        # Movimento drago
        xD -= speed * 5
        
        screen.blit(nuvolaChiara, (140, 510))
        screen.blit(nuvolaChiara, (490, 410))
        screen.blit(nuvolaChiara, (700, 310))
        screen.blit(nuvolaChiara, (390, 195))
        
        # -----------------------------------------------------------------------------------------
        # Collisioni

        if hermano.colliderect(drago):
            running = False
            print("HAI PERSO")
        
        if hermano.colliderect(nuvola1):
            jump = False
            y = 565
            salto = 10
        
        if hermano.colliderect(nuvola2):
            jump = False
            y = 465
            salto = 10
        
        if hermano.colliderect(nuvola3):
            jump = False
            y = 365
            salto = 10
        
        if hermano.colliderect(nuvola4):
            jump = False
            y = 265
            salto = 10
        
        if hermano.colliderect(prato_rect):
            salto = 10
                      
            
        
# ----------------------------------------------------------------
# livello 2    
    
    if livello == 1:
        
        jump = False
        
        # Comandi livello 2
        
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT] and x2 > 40: 
            x2 -= speed * 6
            Hermano = HermanoS
        if keys[pygame.K_RIGHT] and x2 < screen_x - width // 2:
            x2 += speed * 6
            Hermano = HermanoD

        if keys[pygame.K_UP] and y2 - 95 > 0:
            pygame.mixer.music.play()
            jump = True
            
        
        
        if jump:
            if salto >= 0:
                y2 -= (salto * abs(salto)) * 0.5
                salto -= 0.5
            else:
                jump = False
        
        # Gravità
        
        if y2 < 750:
            y2 += 10
        
        # Condizione per salire di livello
        
        if y2 - 95 < 0:
            livello = 2
        
        # Posizione casuale del drago
        
        if xD2 < 0:
            xD2 = screen_x
            yD = y2 - 80
        if xDD2 < 0:
            xDD2 = screen_x
            yDD = y2 - 180
        
        
        # ----------------------------------------------------------------------------
        # Sprite
        
        hermano = pygame.draw.rect(screen, "light blue", (x2 - 36, y2 - 80, 54, 45))
        
        
        prato_rect = pygame.draw.rect(screen, "light blue", (0, screen_y - 36, 1000, 100))
        
        
        nuvola1 = pygame.draw.rect(screen, "light blue", (800, 520, 85, 1))
        nuvola2 = pygame.draw.rect(screen, "light blue", (270, 370, 85, 1))
        nuvola3 = pygame.draw.rect(screen, "light blue", (710, 320, 85, 1))
        nuvola4 = pygame.draw.rect(screen, "light blue", (180, 220, 85, 1))
        
        
        drago1 = pygame.draw.rect(screen, "light blue", (xD2 - 35, yD + 12, 120, 36))
        drago2 = pygame.draw.rect(screen, "light blue", (xDD2 - 35, yDD + 12, 120, 36))
        
        
        screen.blit(nuvolaGrande,(-50, -440))
        screen.blit(nuvolaGrande,(350, -440))
        screen.blit(nuvolaGrande,(750, -440))
        
        screen.blit(nuvolaGrande,(-50, 280))
        screen.blit(nuvolaGrande,(350, 280))
        screen.blit(nuvolaGrande,(750, 280))
        
        
        screen.blit(Hermano,(x2 - 50, y2 - 115))
        
        screen.blit(Drago,(xD2 - 50, yD))
        screen.blit(Drago,(xDD2 - 50, yDD))
        
        # Movimento del drago
        xD2 -= speed * 5
        xDD2 -= speed * 3
        
        screen.blit(nuvolaScura, (790, 500))
        screen.blit(nuvolaScura, (260, 350))
        screen.blit(nuvolaScura, (700, 300))
        screen.blit(nuvolaScura, (170, 200))
        
        # -----------------------------------------------------------------------------------------
        # Collisioni
        
        if hermano.colliderect(drago1) or hermano.colliderect(drago2):
            running = False
            print("HAI PERSO")
            
        
        if hermano.colliderect(nuvola1):
            jump = False
            y2 = 565
            salto = 10
        
        if hermano.colliderect(nuvola2):
            jump = False
            y2 = 415
            salto = 10
        
        if hermano.colliderect(nuvola3):
            jump = False
            y2 = 365
            salto = 10
        
        if hermano.colliderect(nuvola4):
            jump = False
            y2 = 265
            salto = 10
        
        if hermano.colliderect(prato_rect):
            salto = 10

# --------------------------------------------------------
# livello 3

    if livello == 2:
        
        jump = False
        
        # Comandi livello 3
        
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT] and x3 > 40: 
            x3 -= speed * 6
            Hermano = HermanoS
        if keys[pygame.K_RIGHT] and x3 < screen_x - width // 2:
            x3 += speed * 6
            Hermano = HermanoD

        if keys[pygame.K_UP] and y3 - 95 > 0:
            pygame.mixer.music.play()
            jump = True
            
        
        
        if jump:
            if salto >= 0:
                y3 -= (salto * abs(salto)) * 0.5
                salto -= 0.5
            else:
                jump = False
        
        # Gravità
        
        if y3 < 750:
            y3 += 10
        
        # Condizione per salire di livello
        
        if y3 - 95 < 0:
            livello = 3
        
        # Posizione casuale del drago
        
        if xD3 < 0:
            xD3 = screen_x
            yD2 = y3 - 80
        
        if xDD3 < 0:
            xDD3 = screen_x
            yDD2 = y3 - 180
        
        # ------------------------------------------------------------------------------
        # Drago più grande
        
        Drago = pygame.transform.scale(Drago, (210, 70))
        
        # ------------------------------------------------------------------------------
        # Sprite
        
        hermano = pygame.draw.rect(screen, "light blue", (x3 - 36, y3 - 80, 54, 45))
        
        
        prato_rect = pygame.draw.rect(screen, "light blue", (0, screen_y - 36, 1000, 100))
        
        
        drago1 = pygame.draw.rect(screen, "light blue", (xD3 - 95, yD2 + 12, 180, 56))
        drago2 = pygame.draw.rect(screen, "light blue", (xDD3 - 95, yDD2 + 12, 180, 56))
        
        
        nuvola1 = pygame.draw.rect(screen, "light blue", (screen_x // 2, 520, 85, 1))
        nuvola2 = pygame.draw.rect(screen, "light blue", (180, 370, 85, 1))
        nuvola3 = pygame.draw.rect(screen, "light blue", (710, 320, 85, 1))
        nuvola4 = pygame.draw.rect(screen, "light blue", (380, 220, 85, 1))
        
        
        screen.blit(nuvolaGrande,(-50, 280))
        screen.blit(nuvolaGrande,(350, 280))
        screen.blit(nuvolaGrande,(750, 280))
        
        screen.blit(nuvolaGrande,(-50, -440))
        screen.blit(nuvolaGrande,(350, -440))
        screen.blit(nuvolaGrande,(750, -440))
        
        
        
        screen.blit(Hermano,(x3 - 50, y3 - 115))
        
        screen.blit(Drago,(xD3 - 110, yD2))
        screen.blit(Drago,(xDD3 - 110, yDD2))
        
        # Velocità del drago
        xD3 -= speed * 5
        xDD3 -= speed * 3
        
        screen.blit(nuvolaScura, (screen_x // 2 - 10, 500))
        screen.blit(nuvolaScura, (170, 350))
        screen.blit(nuvolaScura, (700, 300))
        screen.blit(nuvolaScura, (370, 200))
        
        # -----------------------------------------------------------------------------------------
        # Collisioni
        
        if hermano.colliderect(drago1) or hermano.colliderect(drago2):
            running = False
            print("HAI PERSO")
            
        
        if hermano.colliderect(nuvola1):
            jump = False
            y3 = 565
            salto = 10
        
        if hermano.colliderect(nuvola2):
            jump = False
            y3 = 415
            salto = 10
        
        if hermano.colliderect(nuvola3):
            jump = False
            y3 = 365
            salto = 10
        
        if hermano.colliderect(nuvola4):
            jump = False
            y3 = 265
            salto = 10
        
        if hermano.colliderect(prato_rect):
            salto = 10

# -----------------------------------------------------------
# livello 4
    
    if livello == 3:
        
        jump = False
        
        # Comandi livello 4
        
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT] and x4 > 40: 
            x4 -= speed * 6
            Hermano = HermanoS
        if keys[pygame.K_RIGHT] and x4 < screen_x - width // 2:
            x4 += speed * 6
            Hermano = HermanoD

        if keys[pygame.K_UP] and y4 - 95 > 0:
            pygame.mixer.music.play()
            jump = True
            
        
        
        if jump:
            if salto >= 0:
                y4 -= (salto * abs(salto)) * 0.5
                salto -= 0.5
            else:
                jump = False
        
        # Gravità
        
        if y4 < 750:
            y4 += 10
        
        # Condizione per salire di livello
        
        if y4 - 95 < 0:
            livello = 4
        
        # Posizione casuale del drago
        
        if xD4 < 0:
            xD4 = screen_x
            yD3 = y4 - 180
        
        # -------------------------------------------------------------------------------
        # Drago ancora più grande
        
        Drago = pygame.transform.scale(Drago, (480, 160))
        
        # -------------------------------------------------------------------------------
        # Sprite
        
        hermano = pygame.draw.rect(screen, "light blue", (x4 - 36, y4 - 80, 54, 45))
        
         
        prato_rect = pygame.draw.rect(screen, "light blue", (0, screen_y - 36, 1000, 100))
        
        
        drago = pygame.draw.rect(screen, "light blue", (xD4 + 35, yD3 + 20, 410, 120))
        
        
        nuvola1 = pygame.draw.rect(screen, "light blue", (150, 520, 85, 1))
        nuvola2 = pygame.draw.rect(screen, "light blue", (500, 370, 85, 1))
        nuvola3 = pygame.draw.rect(screen, "light blue", (710, 320, 85, 1))
        nuvola4 = pygame.draw.rect(screen, "light blue", (330, 200, 85, 1))
        
        screen.blit(nuvolaGrande,(-50, 280))
        screen.blit(nuvolaGrande,(350, 280))
        screen.blit(nuvolaGrande,(750, 280))
        
        screen.blit(nuvolaGrande,(-50, -440))
        screen.blit(nuvolaGrande,(350, -440))
        screen.blit(nuvolaGrande,(750, -440))
        
        
        
        screen.blit(Hermano,(x4 - 50, y4 - 115))
        
        screen.blit(Drago,(xD4, yD3))
        
        # Velocità del drago
        xD4 -= speed * 5
        
        screen.blit(nuvolaScurissima, (140, 500))
        screen.blit(nuvolaScurissima, (490, 350))
        screen.blit(nuvolaScurissima, (700, 300))
        screen.blit(nuvolaScurissima, (320, 180))
        
        # -----------------------------------------------------------------------------------------
        # Collisioni
        
        if hermano.colliderect(drago):
            running = False
            print("HAI PERSO")
            
        
        if hermano.colliderect(nuvola1):
            jump = False
            y4 = 565
            salto = 10
        
        if hermano.colliderect(nuvola2):
            jump = False
            y4 = 415
            salto = 10
        
        if hermano.colliderect(nuvola3):
            jump = False
            y4 = 365
            salto = 10
        
        if hermano.colliderect(nuvola4):
            jump = False
            y4 = 245
            salto = 10
        
        if hermano.colliderect(prato_rect):
            salto = 10
        
# -----------------------------------------------------------
# livello 5 (finale)

    if livello == 4:
        
        Hermano = HermanoD
        
        # Movimento del drago
        
        if x5 - 450 < screen_x // 2 - 50:
            x5 += 5
        else:
            screen.fill("white")
        
        # -----------------------------------------------------------
        # Sprite
        
        screen.blit(castello,(220, 110))
        
        
        screen.blit(nuvolaGrande,(-50, 200))
        screen.blit(nuvolaGrande,(350, 200))
        screen.blit(nuvolaGrande,(750, 200))
        
        screen.blit(Hermano,(x5 - 450, y5 - 220))
        
        # ----------------------------------------------------------
        
        if x5 - 450 < screen_x // 2 - 50:
            x5 += 5
            
        # Condizione per vincere il gioco    
        else:
            screen.fill("white")
            screen.blit(close_tip, (screen_x // 2 - 200, screen_y // 2 - 50))
        
# ------------------------------------------------------------

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()



