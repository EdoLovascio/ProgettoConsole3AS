
#pacchetti da importare
import pygame
import numpy as np
import tcod
import random
from enum import Enum


pygame.init()


#mette il suono di pac-man
pygame.mixer.init() 
pygame.mixer.music.load("Pac-Man Intro Music - Gaming Background Music.mp3") 
pygame.mixer.music.set_volume(0.5) 
pygame.mixer.music.play()



#comandi per il movimento di pac-man per non farlo andare il diagonale
class Direction(Enum):
    DOWN = -90
    RIGHT = 0
    UP = 90
    LEFT = 180
    NONE = 360
    

#punti che prendi per ogni oggetto mangiato
class ScoreType(Enum):
    COOKIE = 10
    POWERUP = 50
    GHOST = 400


#comportamento dei fantasmini
class GhostBehaviour(Enum):
    CHASE = 1
    SCATTER = 2


#visualizza il labirinto
def translate_screen_to_maze(in_coords, in_size=32):
    return int(in_coords[0] / in_size), int(in_coords[1] / in_size)

def translate_maze_to_screen(in_coords, in_size=32):
    return in_coords[0] * in_size, in_coords[1] * in_size



#crea le dimensioni degli oggetti
class GameObject:
    def __init__(self, in_surface, x, y,
                 in_size: int, in_color=(255, 0, 0),
                 is_circle: bool = False):
        self._size = in_size
        self._renderer: GameRenderer = in_surface
        self._surface = in_surface._screen
        self.y = y
        self.x = x
        self._color = in_color
        self._circle = is_circle
        self._shape = pygame.Rect(self.x, self.y, in_size, in_size)

    #disegna gli oggetti
    def draw(self):
        if self._circle:
            pygame.draw.circle(self._surface,
                               self._color,
                               (self.x, self.y),
                               self._size)
        else:
            rect_object = pygame.Rect(self.x, self.y, self._size, self._size)
            pygame.draw.rect(self._surface,
                             self._color,
                             rect_object,
                             border_radius=1)

    def tick(self):
        pass

    #imposta le forme
    def get_shape(self):
        return pygame.Rect(self.x, self.y, self._size, self._size)

    #imposta le posizioni
    def set_position(self, in_x, in_y):
        self.x = in_x
        self.y = in_y

    def get_position(self):
        return (self.x, self.y)


#crea i muri e li colora
class Wall(GameObject):
    def __init__(self, in_surface, x, y, in_size: int, in_color=(0, 0, 255)):
        super().__init__(in_surface, x * in_size, y * in_size, in_size, in_color)


#crea schermo, oggetti, vite e punteggio
class GameRenderer:
    def __init__(self, in_width: int, in_height: int):
        pygame.init()
        #dimensioni dello schermo
        self._width = in_width
        self._height = in_height
        self._screen = pygame.display.set_mode((in_width, in_height))
        #nome sopra lo schermo
        pygame.display.set_caption('Pac-Man by Valeria e Giulia')
        self._clock = pygame.time.Clock()
        self._done = False
        self._won = False
        #liste con gli oggetti del gioco
        self._game_objects = []
        #muri
        self._walls = []
        #cookie
        self._cookies = []
        #potenziamenti
        self._powerups = []
        #fantasmini
        self._ghosts = []
        #Pac-Man
        self._hero: Hero = None
        #vite di Pac-Man
        self._lives = 1
        #punteggio per ogni oggetto mangiato
        self._score = 0
        self._score_cookie_pickup = 10
        self._score_ghost_eaten = 400
        self._score_powerup_pickup = 50
        #powerup
        self._kokoro_active = False  
        self._current_mode = GhostBehaviour.SCATTER
        self._mode_switch_event = pygame.USEREVENT + 1  
        self._kokoro_end_event = pygame.USEREVENT + 2
        self._pakupaku_event = pygame.USEREVENT + 3
        self._modes = [
            (7, 20),
            (7, 20),
            (5, 20),
            (5, 99999)  
        ]
        self._current_phase = 0
        
        
    #crea il movimento di Pac-Man che apre e chiude la bocca
    def tick(self, in_fps: int):
        black = (0, 0, 0)

        self.handle_mode_switch()
        pygame.time.set_timer(self._pakupaku_event, 200) 
        while not self._done:
            for game_object in self._game_objects:
                game_object.tick()
                game_object.draw()
                
                
            #scrive il punteggio e le vite
            self.display_text(f"[Score: {self._score}]  [Lives: {self._lives}]")

            #scritte che appaiono se vinci o perdi il gioco
            if self._hero is None: self.display_text("GAME OVER", (self._width / 2 - 256, self._height / 2 - 256), 100)
            if self._hero is None: self.display_text("Click ESC to exit",( self._width / 2 - 128, self._height / 2 - 100), 50)
            if self.get_won(): self.display_text("YOU WON", (self._width / 2 - 256, self._height / 2 - 256), 100)
            pygame.display.flip()
            self._clock.tick(in_fps)
            self._screen.fill(black)
            self._handle_events()
            
            
    #passaggio del comportamento dei fantasmini da caccia a fuga e viceversa
    def handle_mode_switch(self):
        current_phase_timings = self._modes[self._current_phase]
        print(f"Current phase: {str(self._current_phase)}, current_phase_timings: {str(current_phase_timings)}")
        scatter_timing = current_phase_timings[0]
        chase_timing = current_phase_timings[1]

        if self._current_mode == GhostBehaviour.CHASE:
            self._current_phase += 1
            self.set_current_mode(GhostBehaviour.SCATTER)
        else:
            self.set_current_mode(GhostBehaviour.CHASE)

        used_timing = scatter_timing if self._current_mode == GhostBehaviour.SCATTER else chase_timing
        pygame.time.set_timer(self._mode_switch_event, used_timing * 1000)

    #durata del power up (15s)
    def start_kokoro_timeout(self):
        pygame.time.set_timer(self._kokoro_end_event, 15000)  

    #aggiunge gli oggetti nelle liste precedenti
    def add_game_object(self, obj: GameObject):
        self._game_objects.append(obj)

    #aggiunge i cookie
    def add_cookie(self, obj: GameObject):
        self._game_objects.append(obj)
        self._cookies.append(obj)
        
    #aggiunge i fantasmini
    def add_ghost(self, obj: GameObject):
        self._game_objects.append(obj)
        self._ghosts.append(obj)
        
    #aggiunge i potenziamenti
    def add_powerup(self, obj: GameObject):
        self._game_objects.append(obj)
        self._powerups.append(obj)
        
    #attiva il potenziamento
    def activate_kokoro(self):
        self._kokoro_active = True
        self.set_current_mode(GhostBehaviour.SCATTER)
        self.start_kokoro_timeout()

    #impostazioni per la vittoria
    def set_won(self):
        self._won = True

    def get_won(self):
        return self._won


    #aggiorna il punteggo
    def add_score(self, in_score: ScoreType):
        self._score += in_score.value

    #imposta la posizione iniziale di Pac-Man
    def get_hero_position(self):
        return self._hero.get_position() if self._hero != None else (0, 0)


    #imposta il comportamento dei fantasmini
    def set_current_mode(self, in_mode: GhostBehaviour):
        self._current_mode = in_mode

    def get_current_mode(self):
        return self._current_mode
    
    
    #rimuove pac-man se viene mangiato
    def end_game(self):
        if self._hero in self._game_objects:
            self._game_objects.remove(self._hero)
        self._hero = None

    #impostazioni per quando pac-man viene mangiato
    def kill_pacman(self):
        self._lives -= 1
        self._hero.set_position(32, 32)
        self._hero.set_direction(Direction.NONE)
        if self._lives == 0: self.end_game()
        
    #colora e scrive le scritte
    def display_text(self, text, in_position=(32, 0), in_size=30):
        font = pygame.font.SysFont('Arial', in_size)
        text_surface = font.render(text, False, (225, 0, 0))
        self._screen.blit(text_surface, in_position)

    #attiva il powerup
    def is_kokoro_active(self):
        return self._kokoro_active

    #aggiunge e visualizza i muri
    def add_wall(self, obj: Wall):
        self.add_game_object(obj)
        self._walls.append(obj)

    def get_walls(self):
        return self._walls

    #visualizza i cookie
    def get_cookies(self):
        return self._cookies

    #visualizza i fantasmini
    def get_ghosts(self):
        return self._ghosts

    #visualizza i powerup
    def get_powerups(self):
        return self._powerups

    #visualizza gli oggetti
    def get_game_objects(self):
        return self._game_objects

    #aggiunge pac-man
    def add_hero(self, in_hero):
        self.add_game_object(in_hero)
        self._hero = in_hero

    #comandi per uscire dal gioco
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._done = True
                
            #per chiudere premere ESC
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._done = True

            if event.type == self._mode_switch_event:
                self.handle_mode_switch()

            #attiva l'evento del powerup
            if event.type == self._kokoro_end_event:
                self._kokoro_active = False

            #attiva il movimento della boca di pac-man
            if event.type == self._pakupaku_event:
                if self._hero is None: break
                self._hero.mouth_open = not self._hero.mouth_open

        #tasti per muovere pac-man
        pressed = pygame.key.get_pressed()
        if self._hero is None: return
        if pressed[pygame.K_UP]:
            self._hero.set_direction(Direction.UP)
        elif pressed[pygame.K_LEFT]:
            self._hero.set_direction(Direction.LEFT)
        elif pressed[pygame.K_DOWN]:
            self._hero.set_direction(Direction.DOWN)
        elif pressed[pygame.K_RIGHT]:
            self._hero.set_direction(Direction.RIGHT)


#oggetti che si muovono
class MovableObject(GameObject):
    def __init__(self, in_surface, x, y, in_size: int, in_color=(255, 0, 0), is_circle: bool = False):
        super().__init__(in_surface, x, y, in_size, in_color, is_circle)
        self.current_direction = Direction.NONE
        self.direction_buffer = Direction.NONE
        self.last_working_direction = Direction.NONE
        self.location_queue = []
        self.next_target = None
        #immagine del fantasmino rosso
        self.image = pygame.image.load('ghost.png')

    def get_next_location(self):
        return None if len(self.location_queue) == 0 else self.location_queue.pop(0)

    def set_direction(self, in_direction):
        self.current_direction = in_direction
        self.direction_buffer = in_direction

    #imposta le collisioni con i muri
    def collides_with_wall(self, in_position):
        collision_rect = pygame.Rect(in_position[0], in_position[1], self._size, self._size)
        collides = False
        walls = self._renderer.get_walls()
        for wall in walls:
            collides = collision_rect.colliderect(wall.get_shape())
            if collides: break
        return collides
    
    def check_collision_in_direction(self, in_direction: Direction):
        desired_position = (0, 0)
        if in_direction == Direction.NONE: return False, desired_position
        if in_direction == Direction.UP:
            desired_position = (self.x, self.y - 1)
        elif in_direction == Direction.DOWN:
            desired_position = (self.x, self.y + 1)
        elif in_direction == Direction.LEFT:
            desired_position = (self.x - 1, self.y)
        elif in_direction == Direction.RIGHT:
            desired_position = (self.x + 1, self.y)

        return self.collides_with_wall(desired_position), desired_position

    #movimento automatico degli oggetti che si muovono
    def automatic_move(self, in_direction: Direction):
        pass

    def tick(self):
        self.reached_target()
        self.automatic_move(self.current_direction)

    #i fantasmini seguono pac-man
    def reached_target(self):
        pass
    
    #imposta le immagini della grandezza giusta
    def draw(self):
        self.image = pygame.transform.scale(self.image, (32, 32))
        self._surface.blit(self.image, self.get_shape())


#crea pac-man con il movimento della bocca
class Hero(MovableObject):
    def __init__(self, in_surface, x, y, in_size: int):
        super().__init__(in_surface, x, y, in_size, (255, 255, 0), False)
        self.last_non_colliding_position = (0, 0)
        self.open = pygame.image.load("paku.png")
        self.closed = pygame.image.load("man.png")
        self.image = self.open
        self.mouth_open = True


    #se pac-man non incontra il muro, passa e riappare nel muro opposto
    def tick(self):
        if self.x < 0:
            self.x = self._renderer._width

        if self.x > self._renderer._width:
            self.x = 0
            
        if self.y < 0:
            self.y = self._renderer._height

        if self.y > self._renderer._height:
            self.y = 0

        self.last_non_colliding_position = self.get_position()

        if self.check_collision_in_direction(self.direction_buffer)[0]:
            self.automatic_move(self.current_direction)
        else:
            self.automatic_move(self.direction_buffer)
            self.current_direction = self.direction_buffer

        if self.collides_with_wall((self.x, self.y)):
            self.set_position(self.last_non_colliding_position[0], self.last_non_colliding_position[1])

        self.handle_cookie_pickup()
        self.handle_ghosts()

    #dopo aver scelto la direzione, pac-man si muove in automatico verso di essa
    def automatic_move(self, in_direction: Direction):
        collision_result = self.check_collision_in_direction(in_direction)

        desired_position_collides = collision_result[0]
        if not desired_position_collides:
            self.last_working_direction = self.current_direction
            desired_position = collision_result[1]
            self.set_position(desired_position[0], desired_position[1])
        else:
            self.current_direction = self.last_working_direction

    #quando pac-man passa sopra ad un cookie o un powerup, questo si toglie e si aggiorna il punteggio
    def handle_cookie_pickup(self):
        collision_rect = pygame.Rect(self.x, self.y, self._size, self._size)
        cookies = self._renderer.get_cookies()
        powerups = self._renderer.get_powerups()
        game_objects = self._renderer.get_game_objects()
        cookie_to_remove = None
        for cookie in cookies:
            collides = collision_rect.colliderect(cookie.get_shape())
            if collides and cookie in game_objects:
                game_objects.remove(cookie)
                self._renderer.add_score(ScoreType.COOKIE)
                cookie_to_remove = cookie

        if cookie_to_remove is not None:
            cookies.remove(cookie_to_remove)

        if len(self._renderer.get_cookies()) == 0:
            self._renderer.set_won()

        for powerup in powerups:
            collides = collision_rect.colliderect(powerup.get_shape())
            if collides and powerup in game_objects:
                if not self._renderer.is_kokoro_active():
                    game_objects.remove(powerup)
                    self._renderer.add_score(ScoreType.POWERUP)
                    self._renderer.activate_kokoro()

    #se il powerup è attivo i fantasmini spariscono se colpiti, se non è attivo pac-man muore 
    def handle_ghosts(self):
        collision_rect = pygame.Rect(self.x, self.y, self._size, self._size)
        ghosts = self._renderer.get_ghosts()
        game_objects = self._renderer.get_game_objects()
        for ghost in ghosts:
            collides = collision_rect.colliderect(ghost.get_shape())
            if collides and ghost in game_objects:
                if self._renderer.is_kokoro_active():
                    game_objects.remove(ghost)
                    self._renderer.add_score(ScoreType.GHOST)
                else:
                    if not self._renderer.get_won():
                        self._renderer.kill_pacman()

    #disegna pac.man e il movimento della bocca
    def draw(self):
        half_size = self._size / 2
        self.image = self.open if self.mouth_open else self.closed
        self.image = pygame.transform.rotate(self.image, self.current_direction.value)
        super(Hero, self).draw()

#crea i fantasmini
class Ghost(MovableObject):
    def __init__(self, in_surface, x, y, in_size: int, in_game_controller, sprite_path="ghost_fright.png"):
        super().__init__(in_surface, x, y, in_size)
        self.game_controller = in_game_controller
        self.sprite_normal = pygame.image.load(sprite_path)
        #quando viene preso il powerup, i fantasmini cambiano aspetto
        self.sprite_fright = pygame.image.load("ghost_fright.png")

    def reached_target(self):
        if (self.x, self.y) == self.next_target:
            self.next_target = self.get_next_location()
        self.current_direction = self.calculate_direction_to_next_target()

    def set_new_path(self, in_path):
        for item in in_path:
            self.location_queue.append(item)
        self.next_target = self.get_next_location()

    #con il powerup attivo i fantasmini smettono di seguire pac-man
    def calculate_direction_to_next_target(self) -> Direction:
        if self.next_target is None:
            if self._renderer.get_current_mode() == GhostBehaviour.CHASE and not self._renderer.is_kokoro_active():
                self.request_path_to_player(self)
            else:
                self.game_controller.request_new_random_path(self)
            return Direction.NONE

        diff_x = self.next_target[0] - self.x
        diff_y = self.next_target[1] - self.y
        if diff_x == 0:
            return Direction.DOWN if diff_y > 0 else Direction.UP
        if diff_y == 0:
            return Direction.LEFT if diff_x < 0 else Direction.RIGHT

        if self._renderer.get_current_mode() == GhostBehaviour.CHASE and not self._renderer.is_kokoro_active():
            self.request_path_to_player(self)
        else:
            self.game_controller.request_new_random_path(self)
        return Direction.NONE

    def request_path_to_player(self, in_ghost):
        player_position = translate_screen_to_maze(in_ghost._renderer.get_hero_position())
        current_maze_coord = translate_screen_to_maze(in_ghost.get_position())
        path = self.game_controller.p.get_path(current_maze_coord[1], current_maze_coord[0], player_position[1],
                                               player_position[0])

        new_path = [translate_maze_to_screen(item) for item in path]
        in_ghost.set_new_path(new_path)


    #i fantasmini si muovono in automatico
    def automatic_move(self, in_direction: Direction):
        if in_direction == Direction.UP:
            self.set_position(self.x, self.y - 1)
        elif in_direction == Direction.DOWN:
            self.set_position(self.x, self.y + 1)
        elif in_direction == Direction.LEFT:
            self.set_position(self.x - 1, self.y)
        elif in_direction == Direction.RIGHT:
            self.set_position(self.x + 1, self.y)
            
    def draw(self):
        self.image = self.sprite_fright if self._renderer.is_kokoro_active() else self.sprite_normal
        super(Ghost, self).draw()

#crea i cookie (gialli)
class Cookie(GameObject):
    def __init__(self, in_surface, x, y):
        super().__init__(in_surface, x, y, 4, (255, 255, 0), True)


#crea i powerup (arancioni)
class Powerup(GameObject):
    def __init__(self, in_surface, x, y):
        super().__init__(in_surface, x, y, 8, (255, 128, 0), True)


#crea i sentieri
class Pathfinder:
    def __init__(self, in_arr):
        cost = np.array(in_arr, dtype=np.bool_).tolist()
        self.pf = tcod.path.AStar(cost=cost, diagonal=0)

    def get_path(self, from_x, from_y, to_x, to_y) -> object:
        res = self.pf.get_path(from_x, from_y, to_x, to_y)
        return [(sub[1], sub[0]) for sub in res]


#crea il labirinto con muri, sentieri e inserisce all'interno oggetti fermi e in muovimento
class PacmanGameController:
    def __init__(self):
        self.ascii_maze = [
            "XXXXXXXXXXXXX XXXXXXXXXXXXX",
            "XP                        X",
            "X XXXX XXXXX X XXXXX XXXX X",
            "X XXXXOXXXXX X XXXXXOXXXX X",
            "X XXXX XXXXX X XXXXX XXXX X",
            "X                         X",
            "X XXXX XX XXXXXXX XX XXXX X",
            "X XXXX XX XXXXXXX XX XXXX X",
            "X      XX    X    XX      X",
            "XXXXXX XXXXX X XXXXX XXXXXX",
            "XXXXXX XXXXX X XXXXX XXXXXX",
            "XXXXXX XX         XX XXXXXX",
            "XXXXXX XX XXX XXX XX XXXXXX",
            "          X G G X          ",
            "XXXXXX XX X GG  X XX XXXXXX",
            "XXXXXX XX XXXXXXX XX XXXXXX",
            "XXXXXX XX         XX XXXXXX",
            "XXXXXX XX XXXXXXX XX XXXXXX",
            "XXXXXX XX XXXXXXX XX XXXXXX",
            "X            X            X",
            "X XXXX XXXXX X XXXXX XXXX X",
            "X XXXX XXXXX X XXXXX XXXX X",
            "X   XX               XX   X",
            "XXX XX XX XXXXXXX XX XX XXX",
            "XXX XX XX XXXXXXX XX XX XXX",
            "X      XX    X    XX      X",
            "X XXXXXXXXXX X XXXXXXXXXX X",
            "X XXXXXXXXXX X XXXXXXXXXX X",
            "X   O                O    X",
            "XXXXXXXXXXXXX XXXXXXXXXXXXX",
        ]

        #inserisce le immagini dei fantasmini
        self.numpy_maze = []
        self.cookie_spaces = []
        self.powerup_spaces = []
        self.reachable_spaces = []
        self.ghost_spawns = []
        self.ghost_colors = [
            "ghost.png",
            "ghost_pink.png",
            "ghost_orange.png",
            "ghost_blue.png"
        ]
        self.size = (0, 0)
        self.convert_maze_to_numpy()
        self.p = Pathfinder(self.numpy_maze)

    def request_new_random_path(self, in_ghost: Ghost):
        random_space = random.choice(self.reachable_spaces)
        current_maze_coord = translate_screen_to_maze(in_ghost.get_position())

        path = self.p.get_path(current_maze_coord[1], current_maze_coord[0], random_space[1],
                               random_space[0])
        test_path = [translate_maze_to_screen(item) for item in path]
        in_ghost.set_new_path(test_path)

    def convert_maze_to_numpy(self):
        for x, row in enumerate(self.ascii_maze):
            self.size = (len(row), x + 1)
            binary_row = []
            for y, column in enumerate(row):
                #le G nel labirinto corrispondono ai fantasmini
                if column == "G":
                    self.ghost_spawns.append((y, x))
                    
                #le X nel labirinto corrispondono ai muri
                if column == "X":
                    binary_row.append(0)
                    
                #dove non ci sono i muri vengono messi i cookie
                else:
                    binary_row.append(1)
                    self.cookie_spaces.append((y, x))
                    self.reachable_spaces.append((y, x))
                    
                    #le O nel labirinto corrispondono ai powerup
                    if column == "O":
                        self.powerup_spaces.append((y, x))

            self.numpy_maze.append(binary_row)


#serve per far funzionare le funzioni
if __name__ == "__main__":
    unified_size = 32
    pacman_game = PacmanGameController()
    size = pacman_game.size
    game_renderer = GameRenderer(size[0] * unified_size, size[1] * unified_size)

    for y, row in enumerate(pacman_game.numpy_maze):
        for x, column in enumerate(row):
            if column == 0:
                game_renderer.add_wall(Wall(game_renderer, x, y, unified_size))

    for cookie_space in pacman_game.cookie_spaces:
        translated = translate_maze_to_screen(cookie_space)
        cookie = Cookie(game_renderer, translated[0] + unified_size / 2, translated[1] + unified_size / 2)
        game_renderer.add_cookie(cookie)

    for powerup_space in pacman_game.powerup_spaces:
        translated = translate_maze_to_screen(powerup_space)
        powerup = Powerup(game_renderer, translated[0] + unified_size / 2, translated[1] + unified_size / 2)
        game_renderer.add_powerup(powerup)

    for i, ghost_spawn in enumerate(pacman_game.ghost_spawns):
        translated = translate_maze_to_screen(ghost_spawn)
        ghost = Ghost(game_renderer, translated[0], translated[1], unified_size, pacman_game,
                      pacman_game.ghost_colors[i % 4])
        game_renderer.add_ghost(ghost)

    #impostazioni iniziali della partita
    pacman = Hero(game_renderer, unified_size, unified_size, unified_size)
    game_renderer.add_hero(pacman)
    game_renderer.set_current_mode(GhostBehaviour.CHASE)
    game_renderer.tick(120)
    

    #aggiorna lo schermo
    pygame.display.flip()  

#chiude pygame
pygame.quit()














