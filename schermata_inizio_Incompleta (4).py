import pygame
from pathlib import Path
import subprocess # lo utilizzerò solamente per avviare i giochi.py tramite codice
pygame.init()

percorso = Path.cwd()
CG = percorso / "games" # CG sta per cartella giochi / games è la cartella situata su GiThub

# dichiaro tutte le cartelle dei giochi (il loro path per aprirle una volta l'utente ci vorrà giocare)
Reaper = CG / "Escape_The_Reaper"
Gabibbo = CG / "Gabibbo"
Fico = CG / "Ficosecco"
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

#creo la lista con i nomi dei giochi
ListaNomiGiochi = ["Escape the Reaper" , "Gabibbo" , "Fico" , "Jumper" , "Pac-Man" , "Snake" , "Space Something" , "Space wars" , "Sparabolle"]

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


    screen.fill("white") #coloro lo sfondo di bianco
    
    for buttonRect in ListaButton:
        buttonColor = "red" #colore normale: rosso
        if buttonRect.collidepoint(mPos): # se passo sopra il pulsante cambia colore
            buttonColor = "green" #colore se sono sopra con il mouse: verde
        pygame.draw.rect(screen, buttonColor, buttonRect) #disegno il bottone
    # do un nome ai pulsanti dei vari giochi
    NameButton = [] # lista per i nomi dei bottoni
    for x, buttonRect in enumerate(ListaButton):
        textRect = font.render(ListaNomiGiochi[x], True, "white")#abbino gni bottone al nome del corrispettivo gioco
        NameButton.append(x) # aggiungo il nome del pulsante alla lista
        screen.blit(textRect, (buttonRect.x + 10, buttonRect.y + 10))
        
    if event.type == pygame.MOUSEBUTTONDOWN: # se clicco il tasto del mouse...
    # Loop attraverso tutti i pulsanti
        for buttonRect in ListaButton:
            if buttonRect.collidepoint(mPos):
                # per ogni pulsante che clicco mi apre un gioco diverso
                if ListaButton.index(buttonRect) == NameButton[0]:
                   for x in Reaper.glob("*py"):
                       filePath = CG / x
                       file = filePath.open()
                       comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                       subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[1]:
                    for x in Gabibbo.glob("*py"):
                       filePath = CG / x
                       file = filePath.open()
                       comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                       subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[2]:
                    for x in Fico.glob("*py"):
                       filePath = CG / x
                       file = filePath.open()
                       comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                       subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[3]:
                    for x in Jumper.glob("*py"):
                       filePath = CG / x
                       file = filePath.open()
                       comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                       subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[4]:
                    for x in PacMan.glob("*py"):
                       filePath = CG / x
                       file = filePath.open()
                       comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                       subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[5]:
                    for x in Snake.glob("*py"):
                       filePath = CG / x
                       file = filePath.open()
                       comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                       subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[6]:
                    for x in SaceSomething.glob("*py"):
                       filePath = CG / x
                       file = filePath.open()
                       comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                       subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[7]:
                    for x in SpaceWars.glob("*py"):
                       filePath = CG / x
                       file = filePath.open()
                       comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                       subprocess.run(comando)
                if ListaButton.index(buttonRect) == NameButton[8]:
                    for x in Sparabolle.glob("*py"):
                       filePath = CG / x
                       file = filePath.open()
                       comando = ["python", str(filePath)] # mi servirà per avviare i giochi
                       subprocess.run(comando)
                

        
        
    

    pygame.display.flip()

pygame.quit()
