import pygame
import sys

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Draw Shapes")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Shape points
shape_points = []
current_shape = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                # Start drawing a triangle
                current_shape = "triangle"
                shape_points = []
            elif event.key == pygame.K_h:
                # Start drawing a rhombus
                current_shape = "rhombus"
                shape_points = []
            elif event.key == pygame.K_s:
                # Start drawing a square
                current_shape = "square"
                shape_points = []
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Add the mouse position to the shape points
            shape_points.append(event.pos)
            if len(shape_points) == 2 and current_shape == "square":
                # Draw the square
                pygame.draw.rect(screen, RED, (shape_points[0], (shape_points[1][0] - shape_points[0][0], shape_points[1][1] - shape_points[0][1])))
                pygame.display.flip()
            elif len(shape_points) == 2 and current_shape == "rhombus":
                # Draw the rhombus
                pygame.draw.polygon(screen, RED, [(shape_points[0][0], (shape_points[0][1] + shape_points[1][1]) // 2), ((shape_points[0][0] + shape_points[1][0]) // 2, shape_points[1][1]), (shape_points[1][0], (shape_points[0][1] + shape_points[1][1]) // 2), ((shape_points[0][0] + shape_points[1][0]) // 2, shape_points[0][1])])
                pygame.display.flip()
            elif len(shape_points) == 3 and current_shape == "triangle":
                # Draw the triangle
                pygame.draw.polygon(screen, RED, shape_points)
                pygame.display.flip()

    screen.fill(WHITE)

    # Draw the current shape
    if len(shape_points) == 2 and current_shape == "square":
        pygame.draw.rect(screen, BLACK, (shape_points[0], (shape_points[1][0] - shape_points[0][0], shape_points[1][1] - shape_points[0][1])), 2)
    elif len(shape_points) == 2 and current_shape == "rhombus":
        pygame.draw.polygon(screen, BLACK, [(shape_points[0][0], (shape_points[0][1] + shape_points[1][1]) // 2), ((shape_points[0][0] + shape_points[1][0]) // 2, shape_points[1][1]), (shape_points[1][0], (shape_points[0][1] + shape_points[1][1]) // 2), ((shape_points[0][0] + shape_points[1][0]) // 2, shape_points[0][1])], 2)
    elif len(shape_points) == 3 and current_shape == "triangle":
        pygame.draw.polygon(screen, BLACK, shape_points, 2)

    pygame.display.flip()

pygame.quit()
sys.exit()