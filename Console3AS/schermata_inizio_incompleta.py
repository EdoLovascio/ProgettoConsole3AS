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
PacMan = CG / "PacMan"
Snake = CG / "Snake"
SpaceSomething = CG / "Space_Something"
SpaceWars = CG / "Space_Wars"
Sparabolle = CG / "Sparabolle"

#-------------------------------------#
# variabili

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

button = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #creo la finestra
pygame.display.set_caption("Console giochi 3AS")

font = pygame.font.SysFont('Arial', 30)

#creo la lista con i nomi dei giochi
ListaNomiGiochi = ["Escape the Reaper" , "Gabibbo" , "Fico" , "Jumper" , "PacMan" , "Snake" , "Space Something" , "Space wars" , "Sparabolle"]

# Crea una lista di 9 rettangoli per i pulsanti
ListaButton = []
# misure pulsanti
buttonWidth = 230
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

#----------------------------------#

# Aggiungi descrizioni per ciascun gioco
ListaDescrizioniGiochi = [
    "Fuggi dalla Morte e recupera lo xanax ",
    "Aiuta Gabibbo a superare gli ostacoli e raggiungere la vittoria.",
    "Esplora il mondo di Ficosecco e aiutalo ad essere promosso.",
    "Salta, schiva i draghi, salva la principessa",
    "Un classico...",
    "Un classico...",
    "Divertiti a sparare al tuo amico (si scherza)",
    "Elimina gli alieni e fatti strada",
    "Un classico...",
]

#---------------------------------#

running = True

while running:
    pygame.time.delay(65)


    # se devo uscire dal gioco...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False


    screen.fill("peachpuff") #coloro lo sfondo di bianco
    
    for idx, buttonRect in enumerate(ListaButton):
        buttonColor = "navy" #colore normale: rosso
        if  idx == button: # se passo sopra il pulsante cambia colore
            buttonColor = "maroon" #colore se sono sopra con il mouse: verde
            descrizioneRect = pygame.Rect(10, SCREEN_HEIGHT - 100, SCREEN_WIDTH - 20, 80)
            pygame.draw.rect(screen, "maroon", descrizioneRect)
            descrizioneText = font.render(ListaDescrizioniGiochi[idx], True, "peachpuff")
            screen.blit(descrizioneText, (descrizioneRect.x + 10, descrizioneRect.y + 10))
            
        pygame.draw.rect(screen, buttonColor, buttonRect) #disegno il bottone
    # do un nome ai pulsanti dei vari giochi
    NameButton = [] # lista per i nomi dei bottoni
    for x, buttonRect in enumerate(ListaButton):
        textRect = font.render(ListaNomiGiochi[x], True, "peachpuff")#abbino gni bottone al nome del corrispettivo gioco
        NameButton.append(x) # aggiungo il nome del pulsante alla lista
        screen.blit(textRect, (buttonRect.x + 10, buttonRect.y + 10))
        
        
    if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
        
                if button != 8 :
                    button += 1
                else :
                    button = 0
        
            if event.key == pygame.K_LEFT: 
                if button != 0 :
                    button -= 1
                else :
                    button = 8
            
            if event.key == pygame.K_UP: 
                if button >= 3 :
                    button -= 3
                else :
                    if button == 0 :
                        button = 6
                    if button == 1 :
                        button = 7
                    if button == 2 :
                        button = 8
                        
            if event.key == pygame.K_DOWN: 
                if button <= 5 :
                    button += 3
                else :
                    if button == 6 :
                        button = 0
                    if button == 7 :
                        button = 1
                    if button == 8 :
                        button = 2
                    
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN : # se clicco il tasto del mouse...
    # Loop attraverso tutti i pulsanti
        for idx, buttonRect in enumerate(ListaButton) :
            if idx == button :
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
                    for x in SpaceSomething.glob("*py"):
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

