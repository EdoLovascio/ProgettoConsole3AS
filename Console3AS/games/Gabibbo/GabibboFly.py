#importazione pacchetto pygame e funzione random
import pygame
import random
from pathlib import Path

#inizio modifiche
pygame.init()

#dimensioni dello schermo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#impostazione del display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#titolo del gioco
pygame.display.set_caption("GABIBBOFLY")

path_home = Path.cwd()

#spawn delle mura con intervalli di 2 secondi uno dall'altro 
SPAWN_MURI = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_MURI, 2000)

#lista delle mura
muri = []

#posizione iniziale gabibbo
x = 300
y = SCREEN_HEIGHT // 2

#dimensioni del gabibbo 
w = 55
h = 45

#funzioni per musica
pygame.mixer.init()
salto_path = path_home / "games" / "Gabibbo" / "salto.mp3"
pygame.mixer.music.load(salto_path)

pygame.mixer.music.set_volume(4.5)
spazio = 180   # Spazio tra gli ostacoli
gravità = 3    # forza con cui il corpo viene spinto verso il basso
salto = 8      # potenza per ogni tocco di spazio
player_speed = 4     #velocità del gabibbo

score = 0    #punteggio iniziale

running = True   

#importo immagine del player(gabibbo)
gabibbo_path = path_home / "games" / "Gabibbo" / "gabibbo.png"
player_img = pygame.image.load(gabibbo_path)
player_img = pygame.transform.scale(player_img, (w, h))
#importo immagine del muro basso
spadaDOWN_path = path_home / "games" / "Gabibbo" / "spadaDOWN.png"
muro1_img = pygame.image.load(spadaDOWN_path)
muro1_img = pygame.transform.scale(muro1_img, (60, SCREEN_HEIGHT))
#importo immagine muro alto
spadaUP_path = path_home / "games" / "Gabibbo" / "spadaUP.png"
muro2_img = pygame.image.load(spadaUP_path)
muro2_img = pygame.transform.scale(muro2_img, (60, SCREEN_HEIGHT))

#importo sfondo
GerryScotti_path = path_home / "games" / "Gabibbo" / "GerryScotti.png"
screen_img = pygame.image.load(GerryScotti_path)
screen_img = pygame.transform.scale(screen_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

#font per la il punteggio(ostacoli evitati e game over)
game_over_carattere = pygame.font.Font(None, 80)
score_carattere = pygame.font.Font(None, 36)

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

        testoIstruzioni1 = font.render("Muovi il gabbibo con il joystick(solo UP)",True,"white")
        testoIstruzioni2 = font.render("Evita i MURI ",True, "white")
        testoIstruzioni3 = font.render("prova a sopravivere il più possibile",True, "white")
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
    pygame.time.delay(5) #tempo tra lo spawn di nuovi nemici

    for event in pygame.event.get():
        #processo per la chiusura del sistema
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == SPAWN_MURI:
            muro_height = random.randint(100, SCREEN_HEIGHT - spazio - 100) #spawn di muri in maniera causale(funzione random) con valore determinati da altezza e spazio
            muri.append((SCREEN_WIDTH, muro_height))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y > 0:       #funzione per il salto, se viene premuto lo spazio esso provoca un movimento di valore salto
        y -= salto
        pygame.mixer.music.play()

    y += gravità
    player_rect = pygame.Rect(x, y, w, h)    #funzione che si basa sulla gravità e fa abbassare il gabibbo

                
    screen.blit(screen_img, (0, 0))          #immagine importata che diventa lo sfondo(Gerry) seguendo i movimenti del player
    screen.blit(player_img, (x, y))          #immagine importata che diventa il player seguendo i suoi movimenti
    for muro_x, muro_height in muri:         #permette di creare i due muri 
        muro1 = pygame.Rect(muro_x , 0, 30, muro_height)   #implementa un rettangolo con cordinate diverse per ogni muro(muro basso)
        muro2 = pygame.Rect(muro_x , muro_height + spazio, 30, SCREEN_HEIGHT - muro_height - spazio)#implementa un rettangolo con cordinate diverse per ogni muro(muro basso)
        screen.blit(muro1_img, (muro_x - 10 , muro_height - SCREEN_HEIGHT))#rettangolo che forma il muro basso 
        screen.blit(muro2_img, (muro_x - 10 , muro_height + spazio))#rettangolo che forma il muro alto 

        if player_rect.colliderect(muro1) or player_rect.colliderect(muro2):  #prende in considerazione i nemici, se li colpisci finisce il gioco
            game_over_testo = game_over_carattere.render("SEI STATO GABIZZATO!", True, "red")  #true implica la scritta rossa
            game_over_rettangolo = game_over_testo.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)) #costruzione del rettangolo centrato 
            screen.blit(game_over_testo, game_over_rettangolo) #sovrapposizione del quadrato con scritta e la sua struttura 
            pygame.display.flip()   
            pygame.time.delay(2000) #dopo 2 secondi la scritta hai perso scompare 
            running = False

        if muro_x > 220:           #la funzione considera il valore dei nemici superati date le loro cordinate e somma +1 se essa viene superata dal gabibbo 
            muro_x -= player_speed
            muri[muri.index((muro_x + player_speed, muro_height))] = (muro_x, muro_height)
        else:
            muri.remove((muro_x, muro_height)) #i nemici vengono elimati se sorpassati dal gabibbo
            score += 1

    score_text = score_carattere.render("Punteggio: " + str(score), True, "black") #funzione che realizza un rettangolo dedicato allo score 
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
