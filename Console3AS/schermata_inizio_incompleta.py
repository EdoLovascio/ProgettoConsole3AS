import pygame
from pathlib import Path
import subprocess # lo utilizzerò solamente per avviare i giochi.py tramite codice
pygame.init()
CurentPath = Path.cwd()
CG = CurentPath / "games" # CG sta per cartella giochi

# dichiaro tutte le cartelle dei giochi (il loro path per aprirle una volta l'utente ci vorrà giocare)
Reaper = CG / "Escape_The_Reaper"
Gabibbo = CG / "Gabibbo"
Ficosecco = CG / "Ficosecco"
Jumper = CG / "Jumper"
PacMan = CG / "Pac-Man"
Snake = CG / "Snake"
SpaceSomething = CG / "Space_Something"
SpaceWars = CG / "Space_Wars"
Sparabolle = CG / "Sparabolle"

#-------------------------------------#
# variabili

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #creo la finestra

font = pygame.font.SysFont('Arial', 30)

# Crea una lista di 9 rettangoli per i pulsanti
ListaButton = []
 #misure pulsanti
buttonWidth = 200
buttonHeight = 100
buttonMargin = 50

#----------------------------------#
# creo i pulsanti
for x in range(3):
    for y in range(3):
        buttonRect = pygame.Rect(
            (buttonWidth + buttonMargin) * y + SCREEN_WIDTH // 10,
            (buttonHeight + buttonMargin) * x + SCREEN_HEIGHT // 10,
            buttonWidth,
            buttonHeight
        )
        ListaButton.append(buttonRect)

#---------------------------------#

running = True

while running:

    mPos = pygame.mouse.get_pos()

    # se devo uscire dal gioco...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False


    screen.fill("white")
    
    for buttonRect in ListaButton:
        buttonColor = "red"
        if buttonRect.collidepoint(mPos): # se passo sopra il pulsante cambia colore
            buttonColor = "green"
        pygame.draw.rect(screen, buttonColor, buttonRect)
    # do un nome ai pulsanti dei vari giochi
    NameButton = [] # lista per i nomi dei bottoni
    for x, buttonRect in enumerate(ListaButton):
        textRect = font.render(f'Pulsante {x + 1}', True, "white")
        NameButton.append(x) # aggiungo il nome del pulsante alla lista
        screen.blit(textRect, (buttonRect.x + 10, buttonRect.y + 10))
        
    if event.type == pygame.MOUSEBUTTONDOWN:
    # Loop attraverso tutti i pulsanti
        for buttonRect in ListaButton:
            if buttonRect.collidepoint(mPos):
                # per ogni pulsante che clicco mi apre un gioco diverso
                if ListaButton.index(buttonRect) == NameButton[0]:
                   filePath = Reaper / "escapethereaperv2.py"
                   file = filePath.open()
                   comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                   subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[1]:
                   filePath = Gabibbo / "GabibboFly.py"
                   file = filePath.open()
                   comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                   subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[2]:
                   filePath = Ficosecco / "Gioco.py"
                   file = filePath.open()
                   comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                   subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[3]:
                   filePath = Jumper / "JUMPER.py"
                   file = filePath.open()
                   comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                   subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[4]:
                   filePath = PacMan / "Pac-Man.py"
                   file = filePath.open()
                   comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                   subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[5]:
                   filePath = Snake / "Snake.py"
                   file = filePath.open()
                   comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                   subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[6]:
                   filePath = SpaceSomething / "SPACE_SOMETHING.py"
                   file = filePath.open()
                   comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                   subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[7]:
                   filePath = SpaceWars / "GuerreSpaziali.py"
                   file = filePath.open()
                   comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                   subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[8]:
                   filePath = Sparabolle / "Sparabolle.py"
                   file = filePath.open()
                   comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                   subprocess.run(comando)
                

        
        
    

    pygame.display.flip()

pygame.quit()
