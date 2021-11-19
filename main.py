import pygame
import random


def main():

    pygame.init()

    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)

    cell_size = 100
    grid_width = 4
    grid_height = 4
    display_width = cell_size * grid_width
    display_height = cell_size * grid_height

    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('MDP')

    def game_loop():
        game_quit = False

        on_agent_reset()

        agent_x = random.randint(0, grid_width - 1)
        agent_y = random.randint(0, grid_height - 1)

        food_x = random.randint(0, grid_width - 1)
        food_y = random.randint(0, grid_height - 1)

        while not game_quit:

            dx = dy = 0

            # get user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        dx = -1
                    elif event.key == pygame.K_RIGHT:
                        dx = 1
                    elif event.key == pygame.K_UP:
                        dy = -1
                    elif event.key == pygame.K_DOWN:
                        dy = 1

            # (dx, dy) = decide_action((agent_x, agent_y, food_x, food_y))

            # check if the agent is on the wall
            if agent_x >= grid_width or agent_x < 0 or agent_y >= grid_height or agent_y < 0:
                on_agent_update(agent_x, agent_y, True, False)
                game_loop()

            # update the agent position
            agent_x += dx
            agent_y += dy

            # clear the screen
            display.fill(white)

            # draw a grid in pygame
            for x in range(0, display_width, cell_size):
                pygame.draw.line(display, black, (x, 0), (x, display_height))
            for y in range(0, display_height, cell_size):
                pygame.draw.line(display, black, (0, y), (display_width, y))

            # draw the food
            pygame.draw.rect(
                display, green, [food_x * cell_size, food_y * cell_size, cell_size, cell_size])

            # draw the agent
            pygame.draw.rect(display, black, [
                             agent_x * cell_size, agent_y * cell_size, cell_size, cell_size])

            pygame.display.update()

            if agent_x == food_x and agent_y == food_y:
                on_agent_update(agent_x, agent_y, False, True)
                game_loop()

            on_agent_update(agent_x, agent_y, False, False)

        pygame.quit()
        return

    game_loop()


def on_agent_update(x, y, is_wall, is_food):
    pass


def on_agent_reset():
    pass


def decide_action(state):
    pass


if __name__ == "__main__":
    main()
    print("Bye!")
