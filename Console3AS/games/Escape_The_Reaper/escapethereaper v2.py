#importo pygame e random
import pygame
import random
import time
from pathlib import Path

pygame.init()

#scelgo la musica da mettere
pygame.mixer.init()

homePath = Path.cwd()

musicPath = homePath / "games" / "Escape_The_Reaper" / "musicagioco.mp3"

pygame.mixer.music.load(musicPath) 
pygame.mixer.music.set_volume(1.0) 
pygame.mixer.music.play(loops=-1)

#decido lo schermo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


#scelgo il titolo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("ESCAPE THE REAPER")

#scelgo lo sfondo
pavimentoPath = homePath / "games" / "Escape_The_Reaper" / "pavimento.png"

imgSfondo = pygame.image.load(pavimentoPath) 
imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))

#scelgo la protagonista
girlPath = homePath / "games" / "Escape_The_Reaper" / "girlrpg.png"

imgGirl = pygame.image.load(girlPath) 
imgGirl = pygame.transform.scale(imgGirl,(40,40))

#scelgo i nemici
enemyPath = homePath / "games" / "Escape_The_Reaper" / "enemies.png"

imgEnemy = pygame.image.load(enemyPath) 
imgEnemy = pygame.transform.scale(imgEnemy,(40,40))

#scelgo la cura
curaPath = homePath / "games" / "Escape_The_Reaper" / "cura.png"

imgXanax = pygame.image.load(curaPath) 
imgXanax = pygame.transform.scale(imgXanax,(30,30))

#aggiungo le scritte
game_over_carattere = pygame.font.Font(None,100)

#aggiungo lo score
score = 0


#creo il tempo di aggiunta dei nemici
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 1000)

#creo il tempo di aggiunta della cura
ADD_CURE = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_CURE, 1500)

# l'elenco dei nemici
enemies = []
# l'elenco degli xanax
xanax = []

#metto le informazioni per la protagonista
x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 2
w = 40
h = 20
speed = 10

running = True
paused = False

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

        testoIstruzioni1 = font.render("Muovi la protagonista con il joystick",True,"white")
        testoIstruzioni2 = font.render("Evita gli avversari, I REAPER",True, "white")
        testoIstruzioni3 = font.render("Raccogli 10 glifi per SCAPPARE",True, "white")
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

#creo un ciclo per mettere in movimento il giocatore
while running : 
    pygame.time.delay(10) 

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            
        #la comparsa random dei nemici
        if event.type == ADD_ENEMY:
            posx = random.randint(0,SCREEN_WIDTH - 20)
            posy = random.randint(0,SCREEN_HEIGHT - 20)
            enemies.append( (posx,posy) )
        
        #la comparsa random della cura
        if event.type == ADD_CURE:
            posx = random.randint(0,SCREEN_WIDTH - 20)
            posy = random.randint(0,SCREEN_HEIGHT - 20)
            xanax.append( (posx,posy) )
           
            
#scelgo i tasti che saranno utili durante l'esperienza 
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and x > 0: 
        w,h = 40,20
        x -= speed 
    if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - w: 
        w,h = 40,20
        x += speed 
    if keys[pygame.K_UP] and y > 0: 
        w,h = 20,40
        y -= speed 
    if keys[pygame.K_DOWN] and y < SCREEN_HEIGHT - h: 
        w,h = 20,40
        y += speed
        
      # metto lo sfondo
    screen.blit(imgSfondo,(0,0) )

    #definisco il giocatore
    player = screen.blit(imgGirl,(x,y)) 

    # creo i nemici immobili
    for posx,posy in enemies:
        # scelgo le informazioni del nemico
        en = screen.blit(imgEnemy,(posx,posy, 20, 20))
        
        # innesco la collisione tra la protagonista e i nemici
        if player.colliderect(en):
            game_over_testo = game_over_carattere.render("GAME OVER!",True, "red")
            game_over_rettangolo= game_over_testo.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(game_over_testo, game_over_rettangolo)
            pygame.display.flip()
            print("GAME OVER!", score,"/10")
            running = False
            break
        
    # creo la cura
    for posx,posy in xanax:
        # scelgo le informazioni della cura
        cu = screen.blit(imgXanax,(posx,posy, 20, 20))
        

        # innesco la collisione tra la protagonista e la cura (10)
        if player.colliderect(cu):
            score += 1
            xanax.remove((posx ,posy))
            break
        
        if score == 10:
            game_over_testo = game_over_carattere.render("YOU WON!",True, "black")
            game_over_rettangolo= game_over_testo.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(game_over_testo, game_over_rettangolo)
            pygame.display.flip()
            print("YOU WON!", score,"/10")
            running = False
            break
            
    

    pygame.display.flip()  

#BISOGNA CHIUDERE IL PROGETTO CLICCANDO STOP SU THONNY
time.sleep(3)
pygame.quit()