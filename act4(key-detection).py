import pygame
pygame.init()
display = pygame.display.set_mode((300, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            print("A key has been pressed")
            if event.key == pygame.K_UP:
                print("Key Up has been pressed")
            elif event.key == pygame.K_DOWN:
                print("Key Down has been pressed")
            elif event.key == pygame.K_LEFT:
                print("Key Left has been pressed")
            elif event.key == pygame.K_RIGHT:
                print("Key Right has been pressed")
            elif event.key == pygame.K_SPACE:
                print("Spacebar has been pressed")
            
