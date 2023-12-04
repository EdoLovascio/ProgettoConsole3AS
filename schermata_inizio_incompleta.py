import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #creo la finestr

font = pygame.font.SysFont('Arial', 30)

# Crea una lista di 9 rettangoli per i pulsanti
buttonRects = []
 #misure pulsanti
buttonWidth = 200
buttonHeight = 100
buttonMargin = 50

for x in range(3):
    for y in range(3):
        buttonRect = pygame.Rect(
            (buttonWidth + buttonMargin) * y + SCREEN_WIDTH // 10,
            (buttonHeight + buttonMargin) * x + SCREEN_HEIGHT // 10,
            buttonWidth,
            buttonHeight
        )
        buttonRects.append(buttonRect)

running = True

while running:

    mPos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Loop attraverso tutti i pulsanti
            for buttonRect in buttonRects:
                if buttonRect.collidepoint(mPos):
                    running = False

    screen.fill("white")

    for buttonRect in buttonRects:
        buttonColor = "red"
        if buttonRect.collidepoint(mPos): # se passo sopra il pulsante cambia colore
            buttonColor = "green"
        pygame.draw.rect(screen, buttonColor, buttonRect)

    for x, buttonRect in enumerate(buttonRects):
        textRect = font.render(f'Pulsante {x + 1}', True, "white")
        screen.blit(textRect, (buttonRect.x + 10, buttonRect.y + 10))

    pygame.display.flip()

pygame.quit()
