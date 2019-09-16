import pygame

import constants
from viewmodels.maze import ViewModel

screen = (1024, 960)
loop = True
window = None

# Assets declarations
macgyver_asset = pygame.image.load(r'assets/player_stand__.png')
guardian_asset = pygame.image.load(r'assets/soldier_stand__.png')
wall_asset = pygame.image.load(r'assets/wall.png')
ground_asset = pygame.image.load(r'assets/ground.png')

objects_asset_offset = [
    (pygame.image.load(r'assets/tube__.png'), 0),
    (pygame.image.load(r'assets/needle__.png'), 6),
    (pygame.image.load(r'assets/ether__.png'), 6)
]

highlight_asset = pygame.image.load(r'assets/highlight.png')


def main():
    global loop, window

    pygame.init()
    window = pygame.display.set_mode(screen)
    pygame.display.set_caption("MySuperMaze")

    view_model = ViewModel()

    while loop:
        pygame.time.delay(10)

        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                view_model.move_mg(view_model.DIRECTION_UP)

            if keys[pygame.K_DOWN]:
                view_model.move_mg(view_model.DIRECTION_DOWN)

            elif keys[pygame.K_LEFT]:
                view_model.move_mg(view_model.DIRECTION_LEFT)

            elif keys[pygame.K_RIGHT]:
                view_model.move_mg(view_model.DIRECTION_RIGHT)

        # Rendering the maze
        render_maze(view_model)
        pygame.display.update()


def render_maze(view_model: ViewModel):
    board = view_model.get_maze().get_board()
    macgyver = view_model.get_macgyver()
    objects = view_model.get_objects()

    # Painting the background
    for x in range(constants.MAZE_WIDTH + 1):
        for y in range(constants.MAZE_HEIGHT):
            window.blit(ground_asset, (x * constants.SQUARE_WIDTH, y * constants.SQUARE_HEIGHT))

    if not (view_model.get_game_over() or view_model.get_game_won()):
        # Painting the maze by itself
        for x in range(constants.MAZE_WIDTH):
            for y in range(constants.MAZE_HEIGHT):
                if board[y][x] == '#':
                    window.blit(wall_asset, (x * constants.SQUARE_WIDTH, y * constants.SQUARE_HEIGHT))

        window.blit(
            macgyver_asset, (
                macgyver.get_position()[0] * constants.SQUARE_WIDTH + 8,
                macgyver.get_position()[1] * constants.SQUARE_HEIGHT
            )
        )

        collect_slots_xy = []

        for index in range(3):
            collect_slots_xy.append((constants.SQUARE_WIDTH * constants.MAZE_WIDTH, index * constants.SQUARE_HEIGHT))

        for xy in collect_slots_xy:
            window.blit(highlight_asset, xy)

        for index in range(len(objects)):
            obj = objects[index]
            asset = objects_asset_offset[index]

            if not obj.is_collected():
                window.blit(
                    asset[0], (
                        obj.get_position()[0] * constants.SQUARE_WIDTH,
                        obj.get_position()[1] * constants.SQUARE_HEIGHT + asset[1]
                    )
                )
            else:
                window.blit(
                    asset[0],
                    (
                        collect_slots_xy[index][0],
                        collect_slots_xy[index][1] + asset[1]
                    )
                )

    elif view_model.get_game_over():
        pass

    elif view_model.get_game_won():
        pass


if __name__ == '__main__':
    main()
