# SPACE SOMETHING
# PYGAME programma
# 2AS 2022//23
# JIA LING WANG
# ARNAU MAZZARINI

# Importiamo i moduli pygame e random
import pygame
import random

# Importiamo i vari tasti della tastiera
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_p,
    K_SPACE,
    K_KP_ENTER,
    K_RETURN
)


pygame.init()

# MUSICA SOTTOFONDO
pygame.mixer.init()

pygame.mixer.music.load("Spaceinvaders.mpeg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

#-----------------------------------------
# SCHERMO
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


imgSfondo = pygame.image.load("Spazio3.png")
imgSfondo = pygame.transform.scale(imgSfondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

# POSIZIONE INIZIALE PLAYER
x1 = SCREEN_WIDTH // 4
y1 = SCREEN_HEIGHT // 2

x2 = SCREEN_WIDTH // 4 * 3
y2 = SCREEN_HEIGHT // 2

#--------------------------------

# DIMENSIONI
w1 = 70
h1 = 66

w2 = 70
h2 = 66

w3 = 12
h3 = 6

# VELOCITà
speed = 20


#---------------------------------------------
# GAMING
# player1
img_navicella1 = pygame.image.load("Navicella1.png")
img_navicella1 = pygame.transform.scale(img_navicella1, (w1, h1))

# player2
img_navicella2 = pygame.image.load("Navicella2.png")
img_navicella2 = pygame.transform.scale(img_navicella2, (w2, h2))

# BULLET
bullet_speed = 30

bullets1 = []
bullets2 = []

# BULLET SOUND

bullet_SOUND = pygame.mixer.Sound("Bullet_sound.wav")
pygame.mixer.Sound.set_volume(bullet_SOUND , 0.1)

bullet_IMPACT = pygame.mixer.Sound("Bullet_impact.wav")
pygame.mixer.Sound.set_volume(bullet_IMPACT , 0.1)

player_explosion = pygame.mixer.Sound("Explosion.wav")
pygame.mixer.Sound.set_volume(player_explosion, 0.5)

# LIFE
vita1 = 10
vita2 = 10


#RICARICHE
ricarica_SOUND = pygame.mixer.Sound("Suono_ricarica.mp3")
pygame.mixer.Sound.set_volume(ricarica_SOUND, 0.8)

# SPAWN RICARICA FOR  PLAYER1 

SPAWN_RICARICHE1 = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_RICARICHE1, 7000)

ricariche1 = []

# SPAWN RICARICA FOR  PLAYER2

SPAWN_RICARICHE2 = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_RICARICHE2, 7000)

ricariche2 = []


#ricarica1
img_ricarica1 = pygame.image.load("Ricarica.png")
img_ricarica1 = pygame.transform.scale(img_ricarica1, (40, 40))

#ricarica2
img_ricarica2 = pygame.image.load("Ricarica.png")
img_ricarica2 = pygame.transform.scale(img_ricarica2, (40, 40))

#--------------------------
#SCRITTE
font = pygame.font.Font("retro_computer_personal_use.ttf" ,40)
font1 = pygame.font.Font("Early GameBoy.ttf" ,60)
font2 = pygame.font.Font("Early GameBoy.ttf" ,80)
font3 = pygame.font.Font("retro_computer_personal_use.ttf" ,40)


TITOLO1 = font2.render('SPACE' , True , "white")
TITOLO2 = font2.render('SOMETHING ' , True , "white")

titolo1 = font1.render('SPACE' , True , "white")
titolo2 = font1.render('SOMETHING ' , True , "white")

QUIT = font.render('QUIT' , True , "white")
START = font.render('START' , True , "white")
RESUME = font.render('RESUME' , True , "white")
RESTART = font.render('RESTART' , True , "white")

WINNER1 = font1.render('PLAYER1 WIN' , True , "white")
WINNER2 = font1.render('PLAYER2 WIN' , True , "white")

PLAYER1 = font3.render('PLAYER1' , True , "white")
PLAYER2 = font3.render('PLAYER2' , True , "white")

#---------------------------
#PAUSA

BOTTONE_PAUSA = pygame.Rect(SCREEN_WIDTH // 2 -100, SCREEN_HEIGHT //2 + 50, 200, 50)
BOTTONE_QUIT_P = pygame.Rect( SCREEN_WIDTH // 2 - 75  , SCREEN_HEIGHT //2 + 150 , 150, 50)
BOTTONE_RESTART_P = pygame.Rect(SCREEN_WIDTH // 2 -115 , SCREEN_HEIGHT //2 - 50 ,  230, 50)

bottone_pausa_selezionato = 1

#-------------------------------------------------
#MENU STARTING

stato = "STARTING"

# SFONDO MENU
img_STARTING = pygame.image.load("Spazio4.png")
img_STARTING = pygame.transform.scale(img_STARTING, (SCREEN_WIDTH, SCREEN_HEIGHT))

BOTTONE_START = pygame.Rect(200, SCREEN_HEIGHT //2 - 50 , 180, 50)
BOTTONE_QUIT = pygame.Rect( 200, SCREEN_HEIGHT //2 + 50  , 150, 50)

img_wasd = pygame.image.load("WASD.png")
img_wasd  = pygame.transform.scale(img_wasd, (205, 205 ))

img_arrow = pygame.image.load("ARROW.png")
img_arrow   = pygame.transform.scale(img_arrow , (205, 205 ))

img_invio =  pygame.image.load("INVIO.png")
img_invio  = pygame.transform.scale(img_invio, (205, 205 ))

img_navicella3 = pygame.image.load("Navicella1.png")
img_navicella3 = pygame.transform.scale(img_navicella3, (120, 113 ))
img_navicella3 = pygame.transform.rotate(img_navicella3, 90 )

img_navicella4 = pygame.image.load("Navicella2.png")
img_navicella4 = pygame.transform.scale(img_navicella4, (120, 113 ) )
img_navicella4 = pygame.transform.rotate(img_navicella4, 270 )

bottone_menu_selezionato = 1

# -----------------------------------------------------------------------
#MORTE
BOTTONE_QUIT_M = pygame.Rect((SCREEN_WIDTH // 4)*2.5, SCREEN_HEIGHT //2 , 150, 50)
BOTTONE_RESTART = pygame.Rect(SCREEN_WIDTH // 4, SCREEN_HEIGHT //2 ,  230, 50)

img_coppa = pygame.image.load("COPPA.png")
img_coppa = pygame.transform.scale(img_coppa, (200, 200 ) )

bottone_morte_selezionato = 1

#---------------------------------
# SCHERMO
bottone_PAUSA = pygame.Rect(SCREEN_WIDTH // 2 - 29  , 24 , 45 , 45 )

img_pausa = pygame.image.load("PAUSA3.png")
img_pausa_active = pygame.image.load("PAUSA4.png")
img_pausa  = pygame.transform.scale(img_pausa, (60 , 60 ))
img_pausa_active = pygame.transform.scale(img_pausa_active , (60 , 60 ))

img_cornice = pygame.image.load("CORNICE.png")
img_cornice  = pygame.transform.scale(img_cornice, (1000, 700 ))

img_interno =pygame.image.load("INTERNO1.png").convert_alpha()
img_interno = pygame.transform.scale(img_interno, (1000 , 700 ))
img_interno.set_alpha(10)


winner = WINNER1

running = True
paused = False

# STARTING THE GAME CYCLE
while running:

    pygame.time.delay(50)
    
    
    for event in pygame.event.get():
        # QUIT
        if event.type == pygame.QUIT: 
            running = False
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            
        #POSIZIONE DELLE RICARICHE del PLAYER1 DELLLE VITE
        if event.type == SPAWN_RICARICHE1 and len(ricariche1) < 5 and vita1 < 8 :
            Rx1 = random.randint(30 ,SCREEN_WIDTH //2 -30 )
            Ry1 = random.randint(160 ,SCREEN_HEIGHT - 40)
            ricariche1.append( (Rx1,Ry1) )
            
        #POSIZIONE DELLE RICARICHE del PLAYER2 DELLLE VITE
        if event.type == SPAWN_RICARICHE2 and len(ricariche2) < 5 and vita2 < 8 :
            Rx2 = random.randint(SCREEN_WIDTH //2 + 30, SCREEN_WIDTH - 30)
            Ry2 = random.randint(160 ,SCREEN_HEIGHT - 40)
            ricariche2.append( (Rx2,Ry2) )
            
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if bottone_PAUSA.collidepoint(mPos):
                stato = "PAUSA"
    
    
    #PAUSA
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p or stato == "PAUSA":
            if paused:
                paused = False
                pygame.mixer.music.play()
                stato = "GAMING"
            
            else:
                paused = True
                stato = "PAUSA"
                pygame.mixer.music.pause()
                
                while paused == True :
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT: 
                        running = False
                        stato = "GAMING"
                        paused = False
                        break
                    
                    bottone_restart_color = "red"
                    bottone_quit_color = "red"
                    buttonColor = "red"
                    
                    if bottone_pausa_selezionato == 1 :
                        buttonColor = "blue"
                        
                    if bottone_pausa_selezionato == 2:
                        bottone_quit_color = "blue"
                        
                    if bottone_pausa_selezionato == 3 :
                        bottone_restart_color = "blue"
                    
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN :
                            if event.key == pygame.K_p:
                                paused = False
                                stato = "GAMING"
                                pygame.mixer.music.play()
                                break
                                
                            if event.key == pygame.K_DOWN :
                                if bottone_pausa_selezionato < 3 :
                                    bottone_pausa_selezionato +=1
                                else :
                                    bottone_pausa_selezionato = 1
                            
                            if event.key == pygame.K_UP: 
                                if bottone_pausa_selezionato > 1 :
                                    bottone_pausa_selezionato -=1
                                else :
                                    bottone_pausa_selezionato = 3
                            
                            if event.key == pygame.K_RETURN :
                                if bottone_pausa_selezionato == 1 :
                                    paused = False
                                    stato = "GAMING"
                                    pygame.mixer.music.play()
                                    break
                                if bottone_pausa_selezionato == 2:
                                    running = False
                                    paused = False
                                    stato = "GAMING"
                                    break
                                else :
                                    x1 = SCREEN_WIDTH // 4
                                    y1 = SCREEN_HEIGHT // 2
                                    x2 = SCREEN_WIDTH // 4 * 3
                                    y2 = SCREEN_HEIGHT // 2
                                
                                    w1 = 60
                                    h1 = 30
                                    w2 = 60
                                    h2 = 30
                                    
                                    bullets1 = []
                                    bullets2 = []
                                    vita1 = 10
                                    vita2 = 10
                                    ricariche1 = []
                                    ricariche2 = []
                                    
                                    paused = False
                                    stato = "GAMING"
                                    pygame.mixer.music.play()
                                    break

                    
                    screen.blit(img_cornice, (SCREEN_WIDTH //6 , 60 ))
                    screen.blit(img_interno, (SCREEN_WIDTH //6 , 60))
                    screen.blit(titolo1, (SCREEN_WIDTH // 2 - 150 ,150))
                    screen.blit(titolo2 , (SCREEN_WIDTH //2 - 270 , 220))
                    
                    bottone_restart = pygame.draw.rect(screen,bottone_restart_color,BOTTONE_RESTART_P )
                    bottone_quit = pygame.draw.rect(screen, bottone_quit_color, BOTTONE_QUIT_P )
                    screen.blit(QUIT, (SCREEN_WIDTH // 2 - 65  , SCREEN_HEIGHT //2 + 150 ))
                    screen.blit(RESTART, (SCREEN_WIDTH // 2 -115 , SCREEN_HEIGHT //2 - 50))
                    
                    button = pygame.draw.rect(screen,buttonColor,BOTTONE_PAUSA)
                    screen.blit(RESUME, (SCREEN_WIDTH // 2 -100, SCREEN_HEIGHT //2 + 50))
                    
                    bottone_pausa_m_color = "blue"
                    pausa_b = img_pausa_active

                    bottone_pausa = pygame.draw.rect(screen,bottone_pausa_m_color,bottone_PAUSA )
                    screen.blit(pausa_b, (SCREEN_WIDTH // 2 -35  , 20) )
    
                    pygame.display.flip()

    if paused:
        continue
    
    #MENU INIZIALE 
    if stato == "STARTING" :
        while stato == "STARTING" :
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                running = False
                break
                    
            screen.blit(img_STARTING ,(0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                       stato = "GAMING"
                
                    if event.key == pygame.K_DOWN :
                        if bottone_menu_selezionato == 1 :
                            bottone_menu_selezionato = 2
                        else :
                            bottone_menu_selezionato = 1
                    
                    if event.key == pygame.K_UP: 
                        if bottone_menu_selezionato == 2 :
                            bottone_menu_selezionato = 1
                        else :
                            bottone_menu_selezionato = 2
                            
                    if event.key == pygame.K_RETURN :
                        if bottone_menu_selezionato == 1 :
                            stato = "GAMING"
                            
                        if bottone_menu_selezionato == 2 :
                            running = False
                            break
                        
            
            bottone_quit_color = "red"
            
            if bottone_menu_selezionato == 2 :
                bottone_quit_color = "blue"
            
            bottone_quit = pygame.draw.rect(screen, bottone_quit_color, BOTTONE_QUIT )
            screen.blit(QUIT, (210, SCREEN_HEIGHT //2 + 50)  )
            
            bottone_start_color = "red"
            
            if bottone_menu_selezionato == 1 :
                bottone_start_color = "blue"
            
            bottone_start = pygame.draw.rect(screen,bottone_start_color,BOTTONE_START )
            screen.blit(START,(210, SCREEN_HEIGHT //2 - 50 ))
            
            #-----------------------------------------------
            screen.blit(TITOLO1, ( 50 , 25 ))
            screen.blit(TITOLO2, ( 50, 125 ))
            
            #-----------------------------------------
            #superficie
            s1 = pygame.Surface((480, 650 ), pygame.SRCALPHA)   
            s1.fill((20 ,20,20 , 120 ))                       
            screen.blit(s1, ((SCREEN_WIDTH // 2 + 150  ) , 100 ))
            screen.blit(img_wasd, ((SCREEN_WIDTH // 2 + 230 ) , 200  ))
            screen.blit(img_arrow, ((SCREEN_WIDTH // 2 + 170 ) , SCREEN_HEIGHT // 2 + 125 ))
            screen.blit(img_invio , ((SCREEN_WIDTH // 2 + 300 ) , SCREEN_HEIGHT // 2 + 100 ))
            screen.blit(PLAYER2 , ((SCREEN_WIDTH // 2 + 230 ) , SCREEN_HEIGHT // 2 + 50 ))
            screen.blit(PLAYER1 , ((SCREEN_WIDTH  // 2 + 230 ) , 150 ))
            screen.blit(img_navicella3 , ((SCREEN_WIDTH //2 + 450 ) , 225   ))
            screen.blit(img_navicella4 , ((SCREEN_WIDTH //2 + 450 ) , SCREEN_HEIGHT // 2 + 125   ))
            
            pygame.display.flip()
            
    #MORTE
            
    if stato == "GAMEOVER1" or stato == "GAMEOVER2":
        while stato == "GAMEOVER1" or stato == "GAMEOVER2" :
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                running = False
                break
        
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT :
                        if bottone_morte_selezionato == 1 :
                            bottone_morte_selezionato = 2
                        else :
                            bottone_morte_selezionato = 1
                    
                    if event.key == pygame.K_LEFT: 
                        if bottone_morte_selezionato == 2 :
                            bottone_morte_selezionato = 1
                        else :
                            bottone_morte_selezionato = 2
                            
                    if event.key == pygame.K_RETURN :
                        if bottone_morte_selezionato == 1 :
                            x1 = SCREEN_WIDTH // 4
                            y1 = SCREEN_HEIGHT // 2
                            x2 = SCREEN_WIDTH // 4 * 3
                            y2 = SCREEN_HEIGHT // 2
                            
                            w1 = 60
                            h1 = 30
                            w2 = 60
                            
                            h2 = 30
                            bullets1 = []
                            bullets2 = []
                            vita1 = 10
                            vita2 = 10
                            ricariche1 = []
                            ricariche2 = []
                            
                            stato = "GAMING"
                        
                        if bottone_morte_selezionato == 2 :
                            running = False
                            stato = "GAMING"
            
            bottone_restart_color = "red"
           
            if bottone_morte_selezionato == 1 :
                bottone_restart_color = "blue"
            
            bottone_quit_color = "red"
            
            if bottone_morte_selezionato == 2 :
                bottone_quit_color = "blue"
            
            bottone_restart = pygame.draw.rect(screen,bottone_restart_color,BOTTONE_RESTART )
            bottone_quit = pygame.draw.rect(screen, bottone_quit_color, BOTTONE_QUIT_M )
            
            #---------
            s2 = pygame.Surface((850, 400 ), pygame.SRCALPHA)   
            # (r, g, b, opacità)
            s2.fill((150 , 150, 150, 10 ))
            
            screen.blit(s2, ((SCREEN_WIDTH // 4 -50  ) , SCREEN_HEIGHT // 4 - 50  ))
            screen.blit(winner , (SCREEN_WIDTH // 3.5 , SCREEN_HEIGHT // 4 ) )
            screen.blit(QUIT, ((SCREEN_WIDTH // 4)*2.5, SCREEN_HEIGHT //2))
            screen.blit(RESTART, (SCREEN_WIDTH // 4, SCREEN_HEIGHT //2))
            screen.blit(img_coppa , (SCREEN_WIDTH // 2 - 75 , SCREEN_HEIGHT // 2 - 100 ) )
            pygame.display.flip()
    
    

    
    #------------------------------------------------------------------------------------------
    
    pressed_keys = pygame.key.get_pressed()
    
    # QUI SI GESTISCE IL PLAYER!!!
        
    if pressed_keys[K_w] and y1 > 104 + h2 :
        y1 -= speed

    if pressed_keys[K_s]  and y1 < SCREEN_HEIGHT - 2  - h1:
        y1 += speed

    if pressed_keys[K_a] and x1 > w1 :
        x1 -= speed

    if pressed_keys[K_d] and x1 < ((SCREEN_WIDTH // 2 ) - w1 ):
        x1 += speed 
    
    if pressed_keys[K_SPACE] and len(bullets1) < 10 :
        x3 = x1
        y3 = y1
        bullets1.append( (x3, y3) )
        pygame.mixer.Sound.play(bullet_SOUND)
        
    
    #-----------------------------------------
    
    if pressed_keys[K_UP] and y2 > 104 + h2 :
        y2 -= speed

    if pressed_keys[K_DOWN] and y2 < SCREEN_HEIGHT - 2  - h2:
        y2 += speed

    if pressed_keys[K_LEFT] and x2 > ((SCREEN_WIDTH // 2 ) + w2):
        x2 -= speed

    if pressed_keys[K_RIGHT] and x2 < SCREEN_WIDTH - w2: 
        x2 += speed 

    if pressed_keys[K_KP_ENTER] and len(bullets2)< 10:
        x4 = x2
        y4 = y2
        bullets2.append( (x4, y4) )
        pygame.mixer.Sound.play(bullet_SOUND)
        
    
    #------------------------------------------------------------
              
    # Fill the background with "color"
    screen.blit(imgSfondo ,(0, 0))
    
    # Draw all sprites
    player1 = img_navicella1.get_rect()
    player2 = img_navicella2.get_rect()
    player1.center = (x1 , y1, )
    player2.center = (x2 , y2 )
    
    screen.blit(img_navicella1, player1 )
    screen.blit(img_navicella2, player2 )
    
    #vita del giocatori 
    barra1 = pygame.draw.rect(screen, "white", (45, 50 , 510 , 50))
    barra2 = pygame.draw.rect(screen, "white", (SCREEN_WIDTH -555 , 50 , 510 , 50))
    
    #---------------------------------------------------------
    #SPAW RICARICHE
    #PLAYER1
    
    for r1 in ricariche1 :
        ricarica1 = img_ricarica1.get_rect()
        ricarica1.center = (r1[0], r1 [1])
        
        screen.blit(img_ricarica1, ricarica1 )
    
        if player1.colliderect(ricarica1):
            if vita1 < 10 :
                vita1 += 1
            
            pygame.mixer.Sound.play(ricarica_SOUND)
            ricariche1.remove(r1)
            
    #PLAYER2
    
    for r2 in ricariche2 :
        ricarica2 = img_ricarica2.get_rect()
        ricarica2.center = (r2[0], r2 [1])
        
        screen.blit(img_ricarica2, ricarica2 )
        
        if player2.colliderect(ricarica2):
            if vita2 < 10 :
                vita2 += 1
            
            pygame.mixer.Sound.play(ricarica_SOUND)
            ricariche2.remove(r2)
    

    #------------------------------------------------------------------------------------------------------------------
    c = 0

    for b in bullets1 :
        l = ( ( b[0]+bullet_speed , b[1] ) )
        bullets1.insert(c , l )
        bullets1.remove(b)
        c +=1
    
    for i in bullets1:
        x3 = i[0]
        y3 = i[1]
        bullet1 = pygame.draw.rect(screen, "white", (x3, y3, w3, h3))
        
        if i[0] > SCREEN_WIDTH :
            bullets1.remove(i)
        
        if player2.colliderect(bullet1):
            vita2 += -1
            bullets1.remove(i)
            pygame.mixer.Sound.play(bullet_IMPACT)
            
    if vita2 < 1 :
        stato = "GAMEOVER2"
        winner = WINNER1
        
    
    if vita2 < 8 and vita2 > 3 :
        life2_color = "yellow"
    
    elif vita2 <= 3 :
        life2_color = "red"
    
    else :
        life2_color = "green"
        
    life2 = pygame.draw.rect(screen, life2_color , (SCREEN_WIDTH -550 , 55 , 50*vita2 , 40 ))
    
    #-------------------------------------------------------------------------------------------------------
        
    c = 0    
    
    for b in bullets2 :
        l = ( ( b[0]- bullet_speed , b[1] ) )
        bullets2.insert(c , l )
        bullets2.remove(b)
        c +=1
    
    for i in bullets2:
        x4 = i[0]
        y4 = i[1]
        bullet2 = pygame.draw.rect(screen, "white", (x4, y4, w3, h3))
        if i[0]  < 0 :
            bullets2.remove(i)
        
        if player1.colliderect(bullet2):
            vita1 += - 1
            bullets2.remove(i)
            pygame.mixer.Sound.play(bullet_IMPACT)
    
    if vita1 < 1 :
        stato = "GAMEOVER1"
        winner = WINNER2
        
    if vita1 < 8 and vita1 > 3 :
        life1_color = "yellow"
    
    elif vita1 <= 3 :
        life1_color = "red"
    
    else :
        life1_color = "green"
        
            
    life1 = pygame.draw.rect(screen, life1_color , (50, 55, 50*vita1 , 40))
    #------------------------------------------------------------------------
    #botton su lo schermo
    pausa_b = img_pausa
    
    bottone_pausa_m_color = "red"
    
    bottone_pausa = pygame.draw.rect(screen,bottone_pausa_m_color,bottone_PAUSA )
    screen.blit(pausa_b, (SCREEN_WIDTH // 2 -35  , 20) )
    
    
    pygame.display.flip() 
                 
# Done! Time to quit.
pygame.quit()

