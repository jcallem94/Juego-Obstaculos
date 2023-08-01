import pygame
import sys
import random

# Dimensiones de la pantalla
WIDTH, HEIGHT = 1000, 800

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Inicializar Pygame
pygame.init()

# Crear la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Obstáculos")

# Reloj para controlar los fps
clock = pygame.time.Clock()

# Tamaño y posición del jugador
player_width, player_height = 50, 50
player_x, player_y = (WIDTH - player_width) // 2, HEIGHT - player_height

# Velocidad de los obstáculos
obstacle_speed = 5

# Puntaje
score = 0
high_score = 0

# Lista de obstáculos
obstacles = []

# Bandera para indicar si estamos en el menú de inicio o en el juego
in_menu = True

def draw_player():
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))

def draw_menu():
    pygame.font.init()
    font = pygame.font.SysFont(None, 74)
    text = font.render("Presiona Enter para Jugar", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 250, HEIGHT // 2 - 50))

    high_score_text = font.render(f"Puntaje Máximo: {high_score}", True, WHITE)
    screen.blit(high_score_text, (WIDTH // 2 - 150, HEIGHT // 2 + 50))

def draw_obstacles():
    for obstacle in obstacles:
        if obstacle['shape'] == 'rectangle':
            pygame.draw.rect(screen, RED, obstacle['rect'])
        elif obstacle['shape'] == 'circle':
            pygame.draw.circle(screen, RED, obstacle['rect'].center, 25)
        elif obstacle['shape'] == 'triangle':
            pygame.draw.polygon(screen, RED, obstacle['points'])
        elif obstacle['shape'] == 'rhombus':
            pygame.draw.polygon(screen, RED, obstacle['points'])

def spawn_obstacle():
    global obstacle_speed
    obstacle_type = random.choice(['square', 'circle', 'triangle', 'rhombus'])
    if obstacle_type == 'square':
        obstacle_width, obstacle_height = 50, 50
        obstacle_x, obstacle_y = random.randint(0, WIDTH - obstacle_width), 0
        obstacles.append({'shape': 'square', 'rect': pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)})
    elif obstacle_type == 'circle':
        obstacle_radius = 25
        obstacle_x, obstacle_y = random.randint(obstacle_radius, WIDTH - obstacle_radius), 0
        obstacles.append({'shape': 'circle', 'center': (obstacle_x, obstacle_y), 'radius': obstacle_radius, 'rect': pygame.Rect(obstacle_x - obstacle_radius, obstacle_y - obstacle_radius, obstacle_radius * 2, obstacle_radius * 2)})
    elif obstacle_type == 'triangle':
        obstacle_side = 50
        obstacle_x, obstacle_y = random.randint(0, WIDTH - obstacle_side), 0
        obstacles.append({'shape': 'triangle', 'points': [(obstacle_x-obstacle_side/2, obstacle_y), (obstacle_x + obstacle_side/2, obstacle_y), (obstacle_x, obstacle_y + obstacle_side)], 'rect': pygame.Rect(obstacle_x, obstacle_y, obstacle_side, obstacle_side)})
    elif obstacle_type == 'rhombus':
        obstacle_side = 50
        obstacle_x, obstacle_y = random.randint(0, WIDTH - obstacle_side), 0
        obstacles.append({'shape': 'rhombus', 'points': [(obstacle_x - obstacle_side/2, obstacle_y), (obstacle_x, obstacle_y - obstacle_side/2), (obstacle_x + obstacle_side/2, obstacle_y), (obstacle_x, obstacle_y + obstacle_side/2)], 'rect': pygame.Rect(obstacle_x, obstacle_y, obstacle_side, obstacle_side)})

    # Aumentar velocidad de caída progresivamente
    if obstacle_speed < 10:
        obstacle_speed += 0.1
    

def check_collisions():
    global in_menu

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for obstacle in obstacles:
        if obstacle['rect'].colliderect(player_rect):
            in_menu = True
            game_over()
            return True

            
def game_over():
    global score, high_score
    pygame.font.init()
    font = pygame.font.SysFont(None, 74)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2))
    pygame.display.flip()

    pygame.time.wait(2000)

    if score > high_score:
        high_score = score

    score = 0
    obstacles.clear()

def main():
    global player_x, player_y, obstacle_speed, score, high_score, in_menu

    speed_spawn = 1000
    
    in_menu = True

    while True:
        while in_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        in_menu = False

            screen.fill((0, 0, 0))
            draw_menu()
            pygame.display.update()
            clock.tick(60)

        running = True
        last_obstacle_spawn_time = pygame.time.get_ticks()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= 5
            if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
                player_x += 5

            screen.fill((0, 0, 0))

            draw_player()
            draw_obstacles()

            if pygame.time.get_ticks() - last_obstacle_spawn_time > speed_spawn:
                spawn_obstacle()
                last_obstacle_spawn_time = pygame.time.get_ticks()

            for obstacle in obstacles:
                obstacle['rect'].move_ip(0, obstacle_speed)
                if obstacle['shape'] == 'triangle' or obstacle['shape'] == 'rhombus':
                    for i in range(len(obstacle['points'])):
                        x, y = obstacle['points'][i]
                        obstacle['points'][i] = (x, y + obstacle_speed)


                # Eliminar obstáculos cuando salgan de la pantalla
                if obstacle['rect'].top > HEIGHT:
                    obstacles.remove(obstacle)

            if check_collisions():
                running = False

            # Incrementar el puntaje proporcional al tiempo sobrevivido
            global score
            score += 1

            # Aumentar la velocidad de los obstáculos a medida que aumenta el puntaje
            obstacle_speed = 5 + score // 1000

            # Aumentar la velocidad con la que aparecen los obstáculos a medida que aumenta el puntaje
            speed_spawn -= score // 1000

            # Mostrar puntaje en la pantalla
            font = pygame.font.SysFont(None, 36)
            score_text = font.render(f"Puntaje: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

            pygame.display.update()
            clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
