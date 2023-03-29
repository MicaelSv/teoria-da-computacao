import pygame

pygame.init()

# Definição das cores
BLACK = (0, 0, 0)
WHITE = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (255, 51, 0)

# Definição das dimensões da tela
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Carrega a imagem do elevador
elevator_img = pygame.image.load('elevatore.png')
# Define as dimensões do elevador
ELEVATOR_WIDTH = elevator_img.get_width()
ELEVATOR_HEIGHT = elevator_img.get_height()

# Definição das dimensões do painel
PANEL_WIDTH = 50
PANEL_HEIGHT = 120

# Definição das coordenadas iniciais do elevador
elevator_x = SCREEN_WIDTH // 2 - ELEVATOR_WIDTH // 2
elevator_y = 550

# Definição das coordenadas iniciais do painel
panel_x = SCREEN_WIDTH - PANEL_WIDTH
panel_y = SCREEN_HEIGHT - PANEL_HEIGHT

# Definição da velocidade do elevador
elevator_speed = 2

# Definição do andar atual
current_floor = 0

# Criação da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Elevador")

# Criação dos botões de andares
floor_buttons = []
for i in range(4):
    button_rect = pygame.Rect(panel_x + 10, panel_y + 10 + i*25, PANEL_WIDTH - 20, 20)
    floor_buttons.append(button_rect)

# Loop principal do jogo
done = False
clock = pygame.time.Clock()

while not done:
    # Eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verifica se o botão de um andar foi clicado
            print("Estado atual: q0 (controlador)")
            print("Estado atual:", f"q{3 - current_floor + 1} (andar inicial)")
            for i, button_rect in enumerate(floor_buttons):
                if button_rect.collidepoint(event.pos):
                    current_floor = i
                    elevator_y = i * (SCREEN_HEIGHT // 4)
                    print("Estado atual:", f"q{3 - current_floor + 1} (andar final)\n")
                    sound = pygame.mixer.Sound('som.mp3')
                    sound.play()
    
    # Movimentação do elevador
    if current_floor > elevator_y // (SCREEN_HEIGHT // 4):
        elevator_y += elevator_speed
    elif current_floor < elevator_y // (SCREEN_HEIGHT // 4):
        elevator_y -= elevator_speed

    # Verifica se o elevador chegou a um andar
    if elevator_y % (SCREEN_HEIGHT // 4) == 0:
        current_floor = elevator_y // (SCREEN_HEIGHT // 4)

    # Desenho na tela
    screen.fill(WHITE)

    # Desenho do elevador
    elevator_img = pygame.image.load("elevatore.png").convert_alpha()
    screen.blit(elevator_img, (elevator_x, elevator_y))

    # Desenho do painel
    panel_img = pygame.image.load("panel.png").convert_alpha()
    screen.blit(panel_img, (panel_x, panel_y))

    # Desenho dos botões de andares
    for i, button_rect in enumerate(floor_buttons):
        if current_floor == i:
            color = BLACK
        else:
            color = GRAY
        pygame.draw.rect(screen, color, button_rect, 0)
        text = pygame.font.SysFont('Arial', 16).render(f"{3 - i}", True, BLUE)
        screen.blit(text, (button_rect.x + 5, button_rect.y + 2))

    # Atualização da tela
    pygame.display.flip()

    # Limitação de quadros por segundo
    clock.tick(60)

pygame.quit()