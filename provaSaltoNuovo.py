import pygame

# Inizializzazione di Pygame
pygame.init()

# Impostazione della finestra di gioco
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Salto Pygame")

# Caricamento dell'immagine del personaggio
player_image = pygame.Surface((50, 50))
player_image.fill('blue')
player_rect = player_image.get_rect()
player_rect.center = (width // 2, height - 50)

# Variabili per il salto
jumping = False
jump_count = 10

# Impostazione dell'orologio per controllare il frame rate
clock = pygame.time.Clock()

# Ciclo di gioco
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

    keys = pygame.key.get_pressed()

    # Rilevamento della pressione del tasto di salto (spazio)
    if keys[pygame.K_SPACE] and not jumping:
        jumping = True

    # Salto
    if jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_rect.y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10

    # Disegno della finestra di gioco
    screen.fill('white')
    screen.blit(player_image, player_rect)

    # Aggiornamento della finestra di gioco
    pygame.display.flip()

    # Impostazione del frame rate
    clock.tick(30)
