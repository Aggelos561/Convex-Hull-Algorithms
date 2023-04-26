import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.Font(None, 36)
text = font.render("Press any key to continue", True, (255, 255, 255))
text_rect = text.get_rect(center=(640, 360))

while True:
    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print("Key pressed!")

    pygame.display.update()