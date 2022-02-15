import pygame
import random
import pyperclip

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def generate_password(n):
    temp = ""
    for i in range(n):
        temp += random.choice(chars)
    return temp

password = "----------------"
SIZE = WIDTH, HEIGHT = 400, 200

pygame.init()
pygame.display.set_caption("Генератор паролей")

enter_image = pygame.image.load("./assets/enter.png")
enter_image = pygame.transform.scale(enter_image, (32, 32))
sound = pygame.mixer.Sound("./assets/sound.wav")

game_run = True
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
font = pygame.font.Font("./assets/Montserrat.ttf", 18)
password_font = pygame.font.Font("./assets/Montserrat.ttf", 40)
text = font.render("Для генерации пароля нажми", True, [255, 255, 255])

buffer_text = font.render("Пароль скопирован в буфер обмена!", True, [0, 0, 0])
buffer_anim_opacity = 0
buffer_anim_play = False
buffer_anim_idle = 5
buffer_anim_stop = False

while game_run:
    clock.tick(60)
    password_text = password_font.render(password, True, [0, 250, 0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                password = generate_password(12)
                sound.play()
                buffer_anim_play = True
                buffer_anim_stop = False
                buffer_anim_opacity = 0
                pyperclip.copy(password)
    
    screen.fill((0, 0, 0))
    screen.blit(enter_image, (WIDTH - 32 - 10, HEIGHT - 32 - 10))
    screen.blit(text, (60, HEIGHT - 30))
    screen.blit(password_text, (WIDTH // 2 - password_text.get_width() // 2, 0))
    pygame.draw.rect(screen, (int(255 * buffer_anim_opacity), int(255 * buffer_anim_opacity), int(255 * buffer_anim_opacity)), (WIDTH // 2 - buffer_text.get_width() // 2 - 10, HEIGHT // 2 - buffer_text.get_height() // 2 - 5, buffer_text.get_width() + 20, buffer_text.get_height() + 10), border_radius=5)
    screen.blit(buffer_text, (WIDTH // 2 - buffer_text.get_width() // 2, HEIGHT // 2 - buffer_text.get_height() // 2))


    if buffer_anim_play:
        buffer_anim_opacity += 0.1
        if buffer_anim_opacity > 1:
            buffer_anim_opacity = 1
            buffer_anim_play = False
            buffer_anim_idle = 5

    if buffer_anim_idle > 0:
        buffer_anim_idle -= 0.05
        if buffer_anim_idle < 0:
            buffer_anim_idle = 0
            buffer_anim_stop = True
    
    if buffer_anim_stop:
        buffer_anim_opacity -= 0.1
        if buffer_anim_opacity < 0:
            buffer_anim_opacity = 0
            buffer_anim_stop = False


    pygame.display.flip()

pygame.quit()