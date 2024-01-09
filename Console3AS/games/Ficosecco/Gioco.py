#Lo scopo del gioco è spostare il player"Fico" in modo che schivi le insufficenze(ps le sufficenze valgono doppio) e prenda solo le sufficenze che si aggiungeranno al suo punteggio finale

import pygame
import random
import time
from pathlib import Path

#dopo aver importato le due funzioni "random " e "pygame" iniziamo la creazione del gioco definendo le dimensioni larghezza e lunghezza dello schermo
pygame.init()

homePath = Path.cwd()
captatoPath = homePath / "games" / "Ficosecco" / "CAPTATO.mp3"

pygame.mixer.init()   #suoni
pygame.mixer.music.load(captatoPath) 
pygame.mixer.music.set_volume(5.5) 
pygame.mixer.music.play()

pygame.mixer.music.play()
conta = 0
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#qui definiamo il nome della finestra di gioco
pygame.display.set_caption("A scuola con Fico")
#Ora deiniamo i vari font: Quello "grosso" e quello "giusto"
Titlefont = pygame.font.SysFont('Impact', 70)
Normalfont = pygame.font.SysFont('Impact', 30)

# poi decidiamo cosa scrive alla fine del gioco come nel caso di "Game over" utilizzando i vari font (definiti prima). Abbiamo inserito anche il punteggio, ma non si legge sulla finestra di gioco,
#ma si legge sulla finestra di python alla fine
game_end = Titlefont.render("SEI STATO BOCCIATO!", True, "red")
close_tip = Normalfont.render("Click ESC to exit", True, "blue","yellow")
punteggio = Normalfont.render("Il punteggio si trova sotto" , conta, True, "yellow")
#Importiamo le immagini che poi andremo a posizionare nel gioco. Infatti utilizzeremo un immagine sfondo che andremo a modellare sull'intera finestra di gioco
#ma useremo anche due immagini diverse per i due nemicie una per il player che dopo aver importato andremo a definire la grandezza come ci piace

sfondoPath = homePath / "games" / "Ficosecco" / "classe.jpg"

imgSfondo = pygame.image.load(sfondoPath)
imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))

ficoPath = homePath / "games" / "Ficosecco" / "Fico.jpg"

imgFico = pygame.image.load(ficoPath) 
imgFico = pygame.transform.scale(imgFico,(100,100))

trePath = homePath / "games" / "Ficosecco" / "Tre.png"

imgTre = pygame.image.load(trePath) 
imgTre = pygame.transform.scale(imgTre,(40,40))

seiPath = homePath / "games" / "Ficosecco" / "Sei.jfif"

imgSei = pygame.image.load(seiPath) 
imgSei = pygame.transform.scale(imgSei,(40,40))


#creiamo un nuovo tipo di evento che ci permette di aggiungere i nemici ogni TOT tempo
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 1000)

# l'elenco dei nemici
enemies = []
enemies2 = []

# posizione iniziale del player
x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 2

# dimensioni rettangolo
w = 40
h = 20

# velocità di spostamento
speed = 8
enemy_speed = 10
enemy2_speed = 5

#poniamo runnig = True e iniziamo il ciclo che ci permettera di aggiungere nemici e di regolare lo spostamento del player e dei nemici
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

        testoIstruzioni1 = font.render("Muovi Fico usando il joystick",True,"white")
        testoIstruzioni2 = font.render("Evita le insufficenze",True, "white")
        testoIstruzioni3 = font.render("Raccogli più sufficenze che ti è possibile ",True, "white")
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
    
    pygame.time.delay(5)
    screen.blit(punteggio,(100,100))
    
    #definiamo l'evento e i tasti che ci fanno chiudere la finestra di gioco
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            
        #aggiungiamo le posizioni iniziali alle liste dei nemici. Che sarebbero 0 sulla x un qualsiasi punto da 0 all'altezza dello schermo sulla y   
        if event.type == ADD_ENEMY:
            enemies.append( (0, random.randint(0, SCREEN_HEIGHT)) )
            enemies2.append( (0, random.randint(0, SCREEN_HEIGHT)) )
            
    
    #con questo ciclo definiamo con quali tasti il player si potrà muovere e in quale direzione; inoltre stabiliamo che il player non potrà uscire dalla finestra di gioco
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and x > 0: 
        w,h = 40,20
        x -= speed 
    if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - w: 
        w,h = 40,20
        x += speed 
    if keys[pygame.K_UP] and y > 0: 
        w,h = 40,20
        y -= speed 
    if keys[pygame.K_DOWN] and y < SCREEN_HEIGHT - h: 
        w,h = 40,20
        y += speed 
    
    
    #Ora applichiamo l'immagine dello sfondo e del player scaricate.
    screen.blit( imgSfondo,(0,0) )
    player = screen.blit(imgFico, (x,y,w,h))
    
        
    
    
    #Consideriamo i due elementi della tupla inserita nelle liste enemies. Infatti con "b" analizziamo tutti  gli elementi della tupla e con "c" invece indichiamo
    #la posizione del nemico lungo la x.Poi con "l" aggiungiamo alla x la velocità del nemico (indicata in precedenza) mentre la y la lasciamo invariata.
    #Infine aggiungiamo "c" e "l" alla lista enemies, ma rimoviamo la "b" (contenuta nella tupla "l") così da eliminare le vecchie posizione x del proiettile mentre
    #aumentiamo la "c" di uno così da farm aumentare la x di 1 e facendo figura il nemico come un proiettile che si muove lungo una traiettoria.
    
    #Naturalmente facciamo lo stesso processo per entrambe le liste "enemies" e "enemies2"
    
    c2 = 0
    for b2 in  enemies2:
        l2 = ( ( b2[0] + enemy2_speed , b2[1] ) )
        enemies2.insert(c2 , l2 )
        enemies2.remove(b2)
        c2 +=1
    
    #Invece in questa parte con"i" andiamo ad indicare le due posizioni x e y contenute nelle liste enemies e definiamo che se la posizione x del nemico è maggiore
    #di quella della finestra la poszione scompare. Infatti i nemici quando avranno raggiunto il limite della finestra scompariranno. Inoltre sempre in questo ciclo for
    #apllichiamo l'immagine che abbiamo scelto per i nemici e scaricato e modellato prima.
        
    #Naturalmente anhe questo ciclo è da ripetere per le due liste enemies
    for i2 in enemies2:
        x2 = i2[0]
        y2 = i2[1]
        en2 = screen.blit(imgSei,(x2,y2))
        if i2[0] > SCREEN_WIDTH :
            enemies2.remove(i2)
            
        
        #infine trattiamo le collisioni dove se il player collide con enemies2 non succede niente perchè appunto enemies2 rappresenta le sufficenze 
        if player.colliderect(en2):
            
            enemies2.remove(l2)
            conta += 1
            
        
            
        
    c = 0
    for b in enemies:
        l = ( ( b[0] + enemy_speed , b[1] ) )
        enemies.insert(c , l )
        enemies.remove(b)
        c +=1
    
    for i in enemies:
        x3 = i[0]
        y3 = i[1]
        en = screen.blit(imgTre,(x3,y3))
        if i[0] > SCREEN_WIDTH :
            enemies.remove(i)
            
           
            
        
            
        #Mentre se il player collide con la lista enemies ha perso e dopo 1s sulla finestra di gioco compariranno le scritte che abbiamo creato e definito prima con i font
        if player.colliderect(en):
            pygame.mixer.music.pause()
            
            
            screen.blit(game_end, (200,200))
            screen.blit(close_tip, (100,300))
            pygame.time.delay(200)
            running = False
            
            
            
            
            
            
        
            
            
        
    #questa funzione aggiorna ciò che avviene sullo schermo
    pygame.display.flip()
    
    
print("Hai preso:",conta,"sufficienze")
            
time.sleep(3)
pygame.quit()
