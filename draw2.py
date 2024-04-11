import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_s:
                    draw_square(screen, points, radius, mode)
                elif event.key == pygame.K_t:
                    draw_right_triangle(screen, points, radius, mode)
                elif event.key == pygame.K_e:
                    draw_equilateral_triangle(screen, points, radius, mode)
                elif event.key == pygame.K_h:
                    draw_rhombus(screen, points, radius, mode)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def draw_square(screen, points, radius, color_mode):
    if len(points) < 2:
        return
    start = points[-2]
    end = points[-1]
    side_length = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    side_length = int(side_length / math.sqrt(2))  # Make it a square
    rect = pygame.Rect(start[0], start[1], side_length, side_length)
    pygame.draw.rect(screen, (255, 255, 255), rect, width=radius)

def draw_right_triangle(screen, points, radius, color_mode):
    if len(points) < 2:
        return
    start = points[-2]
    end = points[-1]
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    hypotenuse = math.sqrt(dx**2 + dy**2)
    angle = math.atan2(dy, dx)
    base_length = int(hypotenuse * math.cos(angle))
    height = int(hypotenuse * math.sin(angle))
    if height < 0:
        base_length, height = -base_length, -height
    points = [(start[0], start[1]), (start[0] + base_length, start[1]), (end[0], end[1])]
    pygame.draw.polygon(screen, (255, 255, 255), points, width=radius)

def draw_equilateral_triangle(screen, points, radius, color_mode):
    if len(points) < 2:
        return
    start = points[-2]
    end = points[-1]
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    hypotenuse = math.sqrt(dx**2 + dy**2)
    angle = math.atan2(dy, dx)
    side_length = int(hypotenuse / math.sqrt(3))
    height = int(side_length * math.sqrt(3) / 2)
    points = [(start[0], start[1]), (start[0] + side_length, start[1]), (start[0] + side_length / 2, start[1] - height)]
    pygame.draw.polygon(screen, (255, 255, 255), points, width=radius)

def draw_rhombus(screen, points, radius, color_mode):
    if len(points) < 2:
        return
    start = points[-2]
    end = points[-1]
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    hypotenuse = math.sqrt(dx**2 + dy**2)
    angle = math.atan2(dy, dx)
    side_length = int(hypotenuse / math.sqrt(2))
    height = int(side_length * math.sin(math.pi / 4))
    points = [(start[0], start[1]), (start[0] + side_length, start[1]), (end[0], end[1]), (start[0] + side_length / 2, start[1] - height)]
    pygame.draw.polygon(screen, (255, 255, 255), points, width=radius)

main()