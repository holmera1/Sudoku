import pygame
pygame.init()

#variables
start = 0
base = (start, start)
width = 900
length = 900
size = (width, length)

#screen and window initialization
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sudoku")

#draws the 9x9 sudoku board
def draw_board():
    screen.fill((255, 255, 255))
    for i in range (1, 9):
        if i % 3 == 0:
            pygame.draw.line(screen, (0, 0, 0), (start, i * 100), (width, i * 100), 5)
            pygame.draw.line(screen, (0, 0, 0), (i * 100, start), (i * 100, length), 5)
        else:
            pygame.draw.line(screen, (128, 128, 128), (start, 100 * i), (width, 100 * i), 2)
            pygame.draw.line(screen, (128, 128, 128), (100 * i, start), (100 * i, length), 2)
    pygame.display.update()


#main game loop
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_board()


#quits the game when main loop is broken
pygame.quit()

#WIP - still learning GUIs thru pygame