# Lovascio Edoardo
# Al Yousup Daud Aiman
# 2°AS


# Importiamo i moduli necessari per il gioco, in questo caso il modulo random e pygame
import pygame
import random

pygame.init()

# Definiamo le dimensioni della finestra di gioco
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# Creiamo lo schermo di gioco
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Guerre spaziali")

# Definiamo un utente per aggiungere nemici nel gioco
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 1000)

# Inizializziamo le liste per memorizzare gli avversari e i colpi sparati
enemies = []
shots = []
specialenemies = []
# Carichiamo le immagini dello sfondo, dell' astronave e dei nemici
imgSfondo = pygame.image.load("sfondo.jpg")
imgSfondo = pygame.transform.scale(imgSfondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

imgAstronave = pygame.image.load("astronave.jpg")
imgAstronave = pygame.transform.scale(imgAstronave, (80, 80))

imgNemici = pygame.image.load("nemici.jpg")
imgNemici = pygame.transform.scale(imgNemici, (40, 40))

imgNemici2 = pygame.image.load("nemici2.jpg")
imgNemici2 = pygame.transform.scale(imgNemici2, (40, 40))

# Definiamo la posizione iniziale dell'astronave, la posizione iniziale è al centro dello schermo
x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 2

# Definiamo le dimensioni dell'astronave e la sua velocità di movimento
w = 65
h = 65
speed = 6

# Definiamo le dimensioni degli avversari e la loro velocità di movimento (iniziale)
enemy_width = 40
enemy_height = 40
enemy_speed = 1.0

# Aggiungiamo il punteggio e il livello del giocatore
score = 0
level = 1

# Carichiamo il font per visualizzare il punteggio e il livello
font = pygame.font.Font(None, 36)

# Carichiamo il font per il messaggio "HAI PERSO!" quando il gioco termina
game_over_font = pygame.font.Font(None, 100)

# Variabili per il controllo del ciclo di gioco
running = True
game_over = False

# Carichiamo il font per il testo del menu
font = pygame.font.SysFont('Arial', 30)
fontTitolo = pygame.font.SysFont('Arial', 60)

# Creiamo il testo e il rettangolo per il titolo del gioco nel menu
scrittaRect = fontTitolo.render("GUERRE SPAZIALI", True, "white")
titoloRect = scrittaRect.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))

# Creiamo il testo e il rettangolo per il pulsante "Gioca" nel menu
textRect = font.render('Gioca', True, "white")
buttonRect = textRect.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# Creiamo il testo e il rettangolo per il pulsante "Istruzioni" nel menu
textRect2 = font.render('Istruzioni', True, "white")
buttonIstruzioni = textRect2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))

# Variabile per il controllo del menu
menu = True

# Ciclo while per il menu
while menu:
    # Gestiamo gli eventi del gioco
    for event in pygame.event.get():
        # Se viene premuto il pulsante di chiusura della finestra, terminiamo il gioco
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Riempimento dello schermo con il colore nero
    screen.fill("black")

    # Disegniamo il titolo del gioco nel menu
    screen.blit(scrittaRect, titoloRect)

    # Disegniamo il pulsante "Gioca" nel menu
    pygame.draw.rect(screen, "black", buttonRect)
    screen.blit(textRect, buttonRect)

    # Disegniamo il pulsante "Istruzioni" nel menu
    pygame.draw.rect(screen, "black", buttonIstruzioni)
    screen.blit(textRect2, buttonIstruzioni)

    # Aggiornamento della finestra di gioco
    pygame.display.update()

    # Otteniamo la posizione del mouse
    mPos = pygame.mouse.get_pos()

    # Se viene premuto il pulsante del mouse, controlliamo se è stato premuto il pulsante "Gioca"
    if event.type == pygame.MOUSEBUTTONDOWN:
        if buttonRect.collidepoint(mPos):
            # Avviamo il ciclo di gioco principale
            menu = False
            while running:
                pygame.time.delay(10)
                
                # Gestiamo gli eventi del gioco
                for event in pygame.event.get():
                    # Se viene premuto il pulsante di chiusura della finestra, terminiamo il gioco
                    if event.type == pygame.QUIT:
                        running = False
                    # Se viene premuto il tasto ESC, terminiamo il gioco
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        running = False
                    # Se viene premuto il tasto S, aumentiamo la velocità dell'astronave del giocatore
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                        speed += 1
                    # Se viene premuto il tasto A, diminuiamo la velocità dell'astronave del giocatore
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                        speed -= 1
                    # Se viene generato l'evento ADD_ENEMY e ci sono meno di 3 nemici sullo schermo, aggiungiamo un nuovo nemico
                    # Se il punteggio è multiplo di 10 aggiungo un nemico speciale
                    if event.type == ADD_ENEMY:
                        if len(enemies) < 3 and len(specialenemies) < 1:
                            if score % 10 == 0 and score != 0:
                                posx = random.randint(0, SCREEN_WIDTH - enemy_width)
                                posy = random.randint(-200, -enemy_height)
                                specialenemies.append(pygame.Rect(posx, posy, enemy_width, enemy_height)) 
                            else:
                                posx = random.randint(0, SCREEN_WIDTH - enemy_width)
                                posy = random.randint(-200, -enemy_height)
                                enemies.append(pygame.Rect(posx, posy, enemy_width, enemy_height))                        
                    # Se viene premuto il tasto SPAZIO e il gioco non è terminato, aggiungiamo un colpo alla lista degli oggetti sparati
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_over:
                        shots.append(pygame.Rect(x + w // 2 - 2, y, 7, 14))
                        # Aggiungiamo la musica per i colpi sparati
                        pygame.mixer.init()
                        pygame.mixer.music.load("suonocolpo.mp3")
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play()

                # Otteniamo lo stato dei tasti premuti
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and x > 0:
                    x -= speed
                if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - w:
                    x += speed
                if keys[pygame.K_UP] and y > SCREEN_HEIGHT / 6:
                    y -= speed
                if keys[pygame.K_DOWN] and y < SCREEN_HEIGHT - h - h/2:
                    y += speed

                # Disegniamo lo sfondo e l'astronave del giocatore
                screen.blit(imgSfondo, (0, 0))
                screen.blit(imgAstronave, (x, y))
                
                # Gestiamo gli avversari
                for enemy in enemies:
                    screen.blit(imgNemici, enemy)
                    enemy.y += enemy_speed
                    
                    # Se l'avversario esce dallo schermo, lo rimuoviamo e diminuiamo il punteggio
                    if enemy.y > SCREEN_HEIGHT:
                            enemies.remove(enemy)
                            score -= 1

                    # Se l'astronave del giocatore collide con un avversario, il gioco termina
                    if enemy.colliderect(pygame.Rect(x, y, w, h)):
                        game_over = True
                
                for Senemy in specialenemies:
                    screen.blit(imgNemici2, Senemy)
                    Senemy.y += enemy_speed
                    
                    # Se l'avversario esce dallo schermo, lo rimuoviamo e diminuiamo il punteggio
                    if Senemy.y > SCREEN_HEIGHT:
                            specialenemies.remove(Senemy)
                            score -= 1

                    # Se l'astronave del giocatore collide con un avversario, il gioco termina
                    if Senemy.colliderect(pygame.Rect(x, y, w, h)):
                        game_over = True
                
                # Se il gioco è terminato, visualizziamo il messaggio "HAI PERSO!"
                if game_over:
                    pygame.mixer.init()
                    pygame.mixer.music.load("scontro.mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play()

                    game_over_text = game_over_font.render("HAI PERSO!", True, "white")
                    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                    screen.blit(game_over_text, game_over_rect)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    running = False

                # Gestiamo i colpi sparati
                for shot in shots:
                    pygame.draw.rect(screen, "blue", shot)
                    shot.y -= speed

                    # Controlliamo se un colpo colpisce un avversario
                    for enemy in enemies:
                        if shot.colliderect(enemy):
                            shots.remove(shot)
                            enemies.remove(enemy)
                            score += 1

                            # Se il punteggio raggiunge un multiplo di 10, aumentiamo il livello e le velocità
                            if score == level * 10:
                                level += 1
                                enemy_speed += 0.25
                                speed += 1
                                level_text = font.render("Sei salito di livello!", True, "white")
                                # Aggiungiamo una musica per quando si raggiunge un nuovo livello
                                pygame.mixer.init()
                                pygame.mixer.music.load("nuovolivello.mp3")
                                pygame.mixer.music.set_volume(0.5)
                                pygame.mixer.music.play()
                                screen.blit(level_text,(SCREEN_WIDTH // 2 - level_text.get_width() // 2,SCREEN_HEIGHT // 2 - level_text.get_height() // 2))
                                pygame.display.flip()
                                pygame.time.delay(2000)

                            break

                    # Controlliamo se un colpo colpisce un avversario speciale
                    for Senemy in specialenemies:
                        if shot.colliderect(Senemy):
                            shots.remove(shot)
                            specialenemies.remove(Senemy)
                            score += 3

                            # Se il punteggio raggiunge un multiplo di 10, aumentiamo il livello e le velocità
                            if score == level * 10:
                                level += 1
                                enemy_speed += 0.25
                                speed += 1
                                level_text = font.render("Sei salito di livello!", True, "white")
                                # Aggiungiamo una musica per quando si raggiunge un nuovo livello
                                pygame.mixer.init()
                                pygame.mixer.music.load("nuovolivello.mp3")
                                pygame.mixer.music.set_volume(0.5)
                                pygame.mixer.music.play()
                                screen.blit(level_text,(SCREEN_WIDTH // 2 - level_text.get_width() // 2,SCREEN_HEIGHT // 2 - level_text.get_height() // 2))
                                pygame.display.flip()
                                pygame.time.delay(2000)

                            break

                    # Se il colpo esce dallo schermo, lo rimuoviamo
                    if shot.y < 0:
                        shots.remove(shot)

                # Visualizziamo il punteggio e il livello
                score_text = font.render("Punteggio: " + str(score), True, "white")
                level_text = font.render("Livello: " + str(level), True, "white")
                screen.blit(score_text, (10, 10))
                screen.blit(level_text, (SCREEN_WIDTH - level_text.get_width() - 10, 10))

                # Aggiornamento della finestra di gioco
                pygame.display.update()

            # Terminiamo il gioco
            pygame.quit()
            quit()

        # Se viene premuto il pulsante "Istruzioni" nel menu, visualizziamo le istruzioni
        if buttonIstruzioni.collidepoint(mPos):
            menu = False
            istruzioni = True

            while istruzioni:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    # Se viene premuto il tasto Esc, ritorna al menù principale    
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        istruzioni = False
                        menu = True

                screen.fill("black")

                scrittaRect = font.render("ISTRUZIONI", True, "white")
                titoloRect = scrittaRect.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8))

                testoIstruzioni1 = font.render("Muovi l'astronave con i tasti direzionali",True,"white")
                testoIstruzioni2 = font.render("Spara con il tasto SPAZIO",True, "white")
                testoIstruzioni3 = font.render("Evita gli avversari",True, "white")
                testoIstruzioni4 = font.render("Ogni 10 punti sali di livello e arrivano nemici speciali",True, "white")
                testoIstruzioni6 = font.render("Premi ESC per uscire dalle istruzioni",True, "white")
                testoIstruzioni5 = font.render("Buona fortuna!",True, "white")

                screen.blit(scrittaRect, titoloRect)
                screen.blit(testoIstruzioni1,(SCREEN_WIDTH // 2 - testoIstruzioni1.get_width() // 2, SCREEN_HEIGHT // 3 - testoIstruzioni1.get_height() // 2))
                screen.blit(testoIstruzioni2,(SCREEN_WIDTH // 2 - testoIstruzioni2.get_width() // 2, SCREEN_HEIGHT // 2 - testoIstruzioni2.get_height() // 2))
                screen.blit(testoIstruzioni3,(SCREEN_WIDTH // 2 - testoIstruzioni3.get_width() // 2, SCREEN_HEIGHT // 2 + testoIstruzioni3.get_height() // 2))
                screen.blit(testoIstruzioni4,(SCREEN_WIDTH // 2 - testoIstruzioni4.get_width() // 2, SCREEN_HEIGHT // 2 + testoIstruzioni4.get_height() // 2 + 30))
                screen.blit(testoIstruzioni6,(SCREEN_WIDTH // 2 - testoIstruzioni6.get_width() // 2, SCREEN_HEIGHT // 2 + testoIstruzioni6.get_height() // 2 + 90))
                screen.blit(testoIstruzioni5,(SCREEN_WIDTH // 2 - testoIstruzioni5.get_width() // 2, SCREEN_HEIGHT - testoIstruzioni5.get_height() - 50))

                pygame.display.update()



