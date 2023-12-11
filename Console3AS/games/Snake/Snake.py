import pygame
import random

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

w = 20
h = 20

imgSfondo = pygame.image.load("erba.jpg") 
imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))

imgMela = pygame.image.load("mela.png")
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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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

