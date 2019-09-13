import pygame

from models.maze import Maze

screen = (1024, 960)
run = True
sqr_width = 64
sqr_height = 64
window, font = None, None

mg = pygame.image.load(r'images/player_stand__.png')
guardian = pygame.image.load(r'images/soldier_stand__.png')
brick = pygame.image.load(r'images/wall.png')
ground = pygame.image.load(r'images/ground.png')
item_a = pygame.image.load(r'images/tube__.png')
item_a_top_offset = 0
item_b = pygame.image.load(r'images/needle__.png')
item_b_top_offset = 6
item_c = pygame.image.load(r'images/ether__.png')
item_c_top_offset = 6
highlight = pygame.image.load(r'images/highlight.png')


def main():
    global run, window, font

    pygame.init()
    font = pygame.font.SysFont("Arial", 15)
    window = pygame.display.set_mode(screen)
    pygame.display.set_caption("MySuperMaze")

    maze = Maze(15, 15)
    maze.generate_board()
    maze.place_items()

    while run:
        pygame.time.delay(10)

        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                maze.move_mg(maze.DIRECTION_UP)

            if keys[pygame.K_DOWN]:
                maze.move_mg(maze.DIRECTION_DOWN)

            elif keys[pygame.K_LEFT]:
                maze.move_mg(maze.DIRECTION_LEFT)

            elif keys[pygame.K_RIGHT]:
                maze.move_mg(maze.DIRECTION_RIGHT)

        # Rendering the maze
        render_maze(maze)
        pygame.display.update()


def render_maze(maze: Maze):
    if not (maze.get_game_over() or maze.get_game_won()):
        # Painting the maze by itself
        for x in range(len(maze.board)):
            for y in range(len(maze.board[x])):
                if maze.board[y][x] == '#':
                    window.blit(ground, (x * sqr_width, y * sqr_height))
                    window.blit(brick, (x * sqr_width, y * sqr_height))
                else:
                    window.blit(ground, (x * sqr_width, y * sqr_height))

        window.blit(mg, (maze.get_mg_xy_position()[0] * sqr_width + 8, maze.get_mg_xy_position()[1] * sqr_height))

        # Painting the right column
        for i in range(15):
            window.blit(ground, (15 * sqr_width, i * sqr_height))

        collect_slot_1_xy = (sqr_height * 15, 0 * sqr_height)
        collect_slot_2_xy = (sqr_height * 15, 1 * sqr_height)
        collect_slot_3_xy = (sqr_height * 15, 2 * sqr_height)

        window.blit(highlight, collect_slot_1_xy)
        window.blit(highlight, collect_slot_2_xy)
        window.blit(highlight, collect_slot_3_xy)

        if not maze.get_a_collected():
            window.blit(
                item_a, (
                    maze.get_a_xy_position()[0] * sqr_width,
                    maze.get_a_xy_position()[1] * sqr_height + item_a_top_offset
                )
            )
        else:
            window.blit(item_a, (collect_slot_1_xy[0], collect_slot_1_xy[1] + item_a_top_offset))

        if not maze.get_b_collected():
            window.blit(
                item_b, (
                    maze.get_b_xy_position()[0] * sqr_width,
                    maze.get_b_xy_position()[1] * sqr_height + item_b_top_offset
                )
            )
        else:
            window.blit(item_b, (collect_slot_2_xy[0], collect_slot_2_xy[1] + item_b_top_offset))

        if not maze.get_c_collected():
            window.blit(
                item_c, (
                    maze.get_c_xy_position()[0] * sqr_width,
                    maze.get_c_xy_position()[1] * sqr_height + item_c_top_offset
                )
            )
        else:
            window.blit(item_c, (collect_slot_3_xy[0], collect_slot_3_xy[1] + item_c_top_offset))

    # elif maze.get_game_over():
    #     screen.clear()
    #     screen.addstr(1, 1, 'Game over')
    #
    # elif maze.get_game_won():
    #     screen.clear()
    #     screen.addstr(1, 1, 'You win! Congrats!')


if __name__ == '__main__':
    main()
