import pygame
import random
from pathlib import Path

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

w = 20
h = 20

homePath = Path.cwd()

sfondoPath = homePath / "games" / "Snake" / "erba.jpg"

imgSfondo = pygame.image.load(sfondoPath) 
imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))

melaPath = homePath / "games" / "Snake" / "mela.png"

imgMela = pygame.image.load(melaPath)
imgMela = pygame.transform.scale(imgMela,(w,h))

# Velocità del serpente
speed = 8

# Creazione del serpente
w = 20
h = 20
serpente = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
direzione = "destra"

# Creazione del cibo
cibo_posizione = (random.randint(1, (SCREEN_WIDTH - w) // w) * w,random.randint(1, (SCREEN_HEIGHT - h) // h) * h)

# Punteggio
punteggio = 0
font = pygame.font.Font(None, 25)

running = True
clock = pygame.time.Clock()


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

        testoIstruzioni1 = font.render("Muovi il serpente usando il joystick",True,"white")
        testoIstruzioni2 = font.render("Mangia più mele possibili e fai crescere il serpente",True, "white")
        testoIstruzioni3 = font.render("Evita i muri e non morderti la coda",True, "white")
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

        # Controllo dei tasti 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direzione != "destra":
                direzione = "sinistra"
            elif event.key == pygame.K_RIGHT and direzione != "sinistra":
                direzione = "destra"
            elif event.key == pygame.K_UP and direzione != "giu":
                direzione = "su"
            elif event.key == pygame.K_DOWN and direzione != "su":
                direzione = "giu"

    # Movimento del serpente
    testa = serpente[0]
    x = testa[0]
    y = testa[1]

    if direzione == "destra":
        x += w
    elif direzione == "sinistra":
        x -= w
    elif direzione == "su":
        y -= h
    elif direzione == "giu":
        y += h

    testa = (x, y)
    serpente.insert(0, testa)

    # Controllo collisione con il cibo
    if testa == cibo_posizione:
        punteggio += 1
        cibo_posizione = (random.randint(1, (SCREEN_WIDTH - w) // w) * w,random.randint(1, (SCREEN_HEIGHT - h) // h) * h)
    else:
        serpente.pop()

    # Controllo collisione con i bordi
    if testa[0] < 0 or testa[0] >= SCREEN_WIDTH or testa[1] < 0 or testa[1] >= SCREEN_HEIGHT:
        running = False
    
    # Lo sfondo
    screen.blit(imgSfondo,(0,0) )
    
   
    # Disegno del serpente
    for blocco in serpente:
        pygame.draw.rect(screen, "orange", (blocco[0], blocco[1], w, h))
        
    

    # Disegno del cibo
    #pygame.draw.rect(screen, "red", (cibo_posizione[0], cibo_posizione[1], w, h))
    screen.blit(imgMela,cibo_posizione)
    
    # Aggiornamento del punteggio
    testo_punteggio = font.render("Punteggio: " + str(punteggio), True, "white")
    screen.blit(testo_punteggio, (10, 10))

    pygame.display.flip()

    clock.tick(speed)

# Uscita dal gioco
pygame.quit()

