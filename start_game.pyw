import pygame            
from player import Player
from enemy import Enemy
import random
pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 580

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("images\\music and sounds\\raidendx.mp3")
    pygame.mixer.music.play(loops=3)

play_music()

# Inicializar puntaje y fuente de texto
score = 0
font = pygame.font.Font(None, 30)

# Función para actualizar la ventana con el puntaje
def actualizar_puntaje():
    texto = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(texto, (10, 10))

# Cuando un enemigo es eliminado agrega 100 puntos al puntaje actual
def eliminar_enemigo():
    if collision:
        global score
        score += 100
    if score == 1000 or score == 10000 or score == 20000:
        show_text =  font.render("Great! ", True, "red", "lightblue")
        window.blit(show_text, (0, 150))
        pygame.mixer.init()
        great_message = pygame.mixer.Sound("images\music and sounds\great_message.wav")
        pygame.mixer.Sound.set_volume(great_message, 0.1)
        great_message.play()

window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
icon = pygame.image.load("C:\\Users\\jairo O\\Desktop\\Alura\\space_ship_game\\images\\ft.png")
set_icon = pygame.display.set_icon((icon))
title_window = pygame.display.set_caption("Yairosoft!")

FPS = 60
clock = pygame.time.Clock()

#Grupo de sprites e instanciaciones
sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
# puts the space_ship in the botton of window
player.rect.move_ip(125,530)
sprites.add(player)

for x in range(random.randrange(5) + 1):
    enemy = Enemy()
    enemies.add(enemy) 

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    player.check_key_pressed(bullets)
    player.keep_player_in_screen(SCREEN_WIDTH ,SCREEN_HEIGHT)

    #actualizacion de sprits
    sprites.update()
    enemies.update()
    bullets.update()

    collisions = pygame.sprite.spritecollide(player, enemies, True, pygame.sprite.collide_circle)
    collision = pygame.sprite.groupcollide(enemies,bullets,False, True)

    for enemy in collision:
        enemy.image = pygame.image.load("images\\fuego-removebg.png")
        enemy.speed_y += 10
        pygame.mixer.init()
        explote = pygame.mixer.Sound("images\\music and sounds\\explosion.wav")
        pygame.mixer.Sound.set_volume(explote, 0.1)
        explote.play()
    if enemy.rect.top <= 580:
        enemy.kill()

    if len(enemies) == 0:
    # Add a random number of enemies between 1 and 5
        for x in range(random.randrange(5) + 1):
            enemy = Enemy()
            enemies.add(enemy)
            bg_img = pygame.image.load("images\\fuego-removebg.png")
        
    bg_img = pygame.image.load("images\\city 3\\6.png")
    bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    window.blit(bg_img,(0,0))
    
    # Draw the player on the screen
    sprites.draw(window)
    enemies.draw(window)
    bullets.draw(window)
    
    line = pygame.draw.line(window, "white", (0,300), (580,300), 1) 
    line = pygame.draw.line(window, "white", (0,300), (380,580), 1)
    line = pygame.draw.line(window, "white", (0,100), (380,300), 1)
    line = pygame.draw.line(window, "white", (0,200), (380,300), 1)

    # Aquí se podría llamar a la función que aumenta el puntaje 
    eliminar_enemigo()

    # Actualizar la ventana con el puntaje
    actualizar_puntaje()
    pygame.display.update()

    pygame.display.flip()
pygame.quit()
