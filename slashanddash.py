import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Definições de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slash and Dash!")

# Carregar e redimensionar imagens
background_image = pygame.image.load('sprites/background.png')  # Imagem de fundo
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Redimensiona para a tela

hero_image = pygame.image.load('sprites/hero.png')
hero_image = pygame.transform.scale(hero_image, (50, 50))  # Redimensionando para 50x50

enemy_image = pygame.image.load('sprites/enemy.png')
enemy_image = pygame.transform.scale(enemy_image, (50, 50))  # Redimensionando para 50x50

arrow_image = pygame.image.load('sprites/arrow.png')
arrow_image = pygame.transform.scale(arrow_image, (20, 10))  # Redimensionando para 20x10

# Configurações do jogador
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 10

# Configurações dos inimigos
enemy_size = 50
enemy_speed = 5
enemies = []

# Configurações das flechas
arrows = []
arrow_speed = 15

# Função para criar inimigos
def create_enemy():
    x_pos = random.randint(0, WIDTH - enemy_size)
    enemies.append([x_pos, 0])

# Função para detectar colisões
def detect_collision(player_pos, enemy_pos):
    p_x, p_y = player_pos
    e_x, e_y = enemy_pos
    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

# Função para detectar colisões entre flechas e inimigos
def detect_arrow_collision(arrow_pos, enemy_pos):
    a_x, a_y = arrow_pos
    e_x, e_y = enemy_pos
    if (e_x >= a_x and e_x < (a_x + 20)) or (a_x >= e_x and a_x < (e_x + enemy_size)):
        if (e_y >= a_y and e_y < (a_y + 10)) or (a_y >= e_y and a_y < (e_y + enemy_size)):
            return True
    return False

# Função para mostrar o menu principal
def show_menu():
    while True:
        screen.fill(WHITE)
        font = pygame.font.Font(None, 74)
        text = font.render("Slash and Dash!", True, BLACK)
        screen.blit(text, (WIDTH // 2 - 200, HEIGHT // 4))

        font = pygame.font.Font(None, 36)
        start_text = font.render("Press ENTER to Start", True, GREEN)
        screen.blit(start_text, (WIDTH // 2 - 100, HEIGHT // 2))

        instructions_text = font.render("Press I for Instructions", True, BLACK)
        screen.blit(instructions_text, (WIDTH // 2 - 140, HEIGHT // 2 + 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                if event.key == pygame.K_i:
                    show_instructions()  # Chama a tela de instruções

# Função para mostrar a tela de instruções
def show_instructions():
    while True:
        screen.fill(WHITE)
        font = pygame.font.Font(None, 74)
        instructions_text = font.render("Como Jogar", True, BLACK)
        screen.blit(instructions_text, (WIDTH // 2 - 150, HEIGHT // 4))

        font = pygame.font.Font(None, 36)
        controls_text1 = font.render("Use as setas esquerda e direita para mover", True, BLACK)
        screen.blit(controls_text1, (WIDTH // 2 - 300, HEIGHT // 2 - 50))

        controls_text2 = font.render("Pressione Espaço para atirar", True, BLACK)
        screen.blit(controls_text2, (WIDTH // 2 - 200, HEIGHT // 2))

        back_text = font.render("Pressione Q para voltar ao menu", True, RED)
        screen.blit(back_text, (WIDTH // 2 - 200, HEIGHT // 2 + 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return  # Retorna ao menu principal

# Função para mostrar a tela de Game Over
def show_game_over(score):
    while True:
        screen.fill(WHITE)
        font = pygame.font.Font(None, 74)
        game_over_text = font.render("Game Over!", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 4))

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Sua pontuação: {score}", True, RED)
        screen.blit(score_text, (WIDTH // 2 - 100, HEIGHT // 2))

        restart_text = font.render("Pressione ENTER para Reiniciar", True, GREEN)
        screen.blit(restart_text, (WIDTH // 2 - 150, HEIGHT // 2 + 50))

        quit_text = font.render("Pressione Q para Sair", True, BLACK)
        screen.blit(quit_text, (WIDTH // 2 - 100, HEIGHT // 2 + 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Retorna para o menu principal
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Função principal do jogo
def game_loop():
    clock = pygame.time.Clock()
    score = 0

    while True:
        screen.blit(background_image, (0, 0))  # Desenha o fundo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Atirar ao pressionar a barra de espaço
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Adiciona uma nova flecha
                    arrow_pos = [player_pos[0] + player_size // 2 - 10, player_pos[1]]
                    arrows.append(arrow_pos)

        # Movimentação do jogador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
            player_pos[0] += player_speed

        # Criação de inimigos
        if random.randint(1, 40) == 1:  # Menos inimigos
            create_enemy()

        # Atualização da posição dos inimigos
        for enemy in enemies:
            enemy[1] += enemy_speed
            if enemy[1] > HEIGHT:
                show_game_over(score)  # Game Over se um inimigo passar
                return  # Retorna para o menu principal

        # Atualização da posição das flechas
        for arrow in arrows:
            arrow[1] -= arrow_speed  # Move a flecha para cima
            if arrow[1] < 0:  # Remove a flecha se sair da tela
                arrows.remove(arrow)

        # Verificação de colisões
        for enemy in enemies:
            for arrow in arrows:
                if detect_arrow_collision(arrow, enemy):
                    arrows.remove(arrow)
                    enemies.remove(enemy)
                    score += 1  # Aumenta a pontuação ao matar um inimigo
                    break  # Sai do loop após atingir um inimigo

            # Verifica se o jogador colide com o inimigo
            if detect_collision(player_pos, enemy):
                show_game_over(score)
                return  # Retorna para o menu principal

        # Desenhar o jogador
        screen.blit(hero_image, (player_pos[0], player_pos[1]))

        # Desenhar os inimigos
        for enemy in enemies:
            screen.blit(enemy_image, (enemy[0], enemy[1]))

        # Desenhar as flechas
        for arrow in arrows:
            screen.blit(arrow_image, (arrow[0], arrow[1]))

        # Mostrar score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Pontuação: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

# Execução do jogo
show_menu()
game_loop()




