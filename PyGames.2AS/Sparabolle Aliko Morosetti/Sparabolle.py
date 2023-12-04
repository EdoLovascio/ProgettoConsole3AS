import pygame
import random

# Inizializzazione
pygame.init()


# Dimensioni finestra di gioco
WIDTH = 800
HEIGHT = 600

# Creazione finestra di gioco
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Shooter")

clock = pygame.time.Clock()
FPS = 60 #frames per second -> le immagini al secondo


myfont = pygame.font.SysFont("monospace", 15) #definiamo font e grandezza delle scritte

# mostriamo delle scritte sulla finestra di gioco
label = myfont.render("Bolla del giocatore:", True, "black")
label2 = myfont.render("Punteggio:", True, "black")

# Variabili
bubble_radius = 20 #raggio della bolla
bubble_colors = ["red", "green", "blue", "yellow", "magenta", "cyan"] #colori
bubble_speed = 1 #velocità della bolla
shoot_radius = 20 #raggio della bolla sparata
shoot_speed = 5 #velocità proiettile
player_bubble_x = 0 #coordinate iniziali
player_bubble_y = 0 #coordinate iniziali

occupied_positions = set() #lista per tenere elencati gli spazi occupati


actual_color = None



def create_new_bubble(x, y, occupied_positions, col):
    '''
    creare una nuova bolla evitando sovrapposizioni controllando che occupi una determinata posizione vuota
    '''
    while True:
        position = (x, y)
        if position not in occupied_positions:
            occupied_positions.add((x, y))
            return create_bubble(x, y, col)
        y += bubble_radius * 2


def create_bubble(x, y, c):
    '''
    generare una bolla casuale senza controllare dove si trovi
    '''
    if c == 0:
        color = random.choice(bubble_colors)
    else:
        color = c
    return {'x': x, 'y': y, 'color': color, 'popped': False}

# Funzione per disegnare una bolla
def draw_bubble(x, y, color):
    '''
    disegnare una bolla a schermo
    '''
    pygame.draw.circle(screen, color, (x, y), bubble_radius)

def NewColor():
    '''
    seglie un colore a caso e lo restituisce
    '''
    color = random.choice(bubble_colors)
    return {'color': color}


def check_collision(bubbles, shoot, punteggio):
    '''
    controlla se ogni bolla è scoppiata, in tal caso la
    rimuove dalla lista oppure la aggiunge
    '''
    for bubble in bubbles:
        if bubble['popped']:
            continue
        distance = ((bubble['x'] - shoot['x']) ** 2 + (bubble['y'] - shoot['y']) ** 2) ** 0.5
        if distance <= bubble_radius + shoot_radius and bubble['color'] == shoot['color']:
            occupied_positions.remove((bubble['x'], bubble['y']))
            bubble['popped'] = True
            bubbles.remove(bubble)
            return True
        elif distance <= bubble_radius + shoot_radius:
            bubbles.append(create_new_bubble(shoot['x'], shoot['y'], occupied_positions, shoot['color']))
            return True
    return False




# Funzione principale del gioco
def game():
    bubbles = []
    player_bubble = None
    actual_color = NewColor()
    punteggio=0
    spostamento=0

    # Creazione delle righe iniziali di bolle
    for i in range(4):
        for j in range(WIDTH // (bubble_radius * 2)-4):
            x = (j * bubble_radius * 2) + bubble_radius
            y = (i * bubble_radius * 2) + bubble_radius
            x += bubble_radius*4
            # generazione delle righe alternate
            if spostamento % 2 == 1:
                x += bubble_radius
            bubble = create_new_bubble(x, y, occupied_positions, 0)
            bubbles.append(bubble)
        spostamento += 1

    # Ciclo di gioco
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not player_bubble:
                    player_bubble_x, player_bubble_y = pygame.mouse.get_pos()
                    player_bubble = create_bubble(player_bubble_x, player_bubble_y, actual_color['color'])
                    actual_color = NewColor()

        # Aggiorna il movimento del proiettile e controlla le collisioni
        if player_bubble:
            player_bubble['y'] -= shoot_speed #gli sottraiamo la velocità così scorre verso l'alto

            if player_bubble['y']-bubble_radius <= 0:
                bubbles.append(create_new_bubble(player_bubble['x'], player_bubble['y'], occupied_positions, player_bubble['color']))
                player_bubble = None
            elif not player_bubble['popped']: #se la bolla non scoppia
                v = len(bubbles)
                if check_collision(bubbles, player_bubble, punteggio):
                    v -= len(bubbles)
                    if v>0:
                        punteggio += 1 #se la bolla scoppia aumenta il punteggio
                    player_bubble = None



        # Sfondo
        sfondo = pygame.image.load("cielo.png")
        sfondo = pygame.transform.scale(sfondo,(WIDTH, HEIGHT))
        screen.blit(sfondo,(0,0))

        #scritte
        label2 = myfont.render('Punteggio: ' + str(punteggio), True, ("black"))
        screen.blit(label, (610, 450))
        screen.blit(label2, (610, 550))

        # Disegna le bolle
        draw_bubble(700, 500, actual_color['color'])
        for bubble in bubbles:
            if not bubble['popped']: # se non è scoppiata si attacca
                draw_bubble(bubble['x'], bubble['y'], bubble['color'])

        # Disegna la bolla del giocatore
        if player_bubble:
            draw_bubble(player_bubble['x'], player_bubble['y'], player_bubble['color'])

        # Aggiorna la schermata
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Esegui il gioco
game()