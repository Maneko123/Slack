import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.WHITE = pygame.Color(255, 255, 255)
        self.BLACE = pygame.Color(0, 0, 0)
        self.RED = pygame.Color(255, 0, 0)
        self.BLYE = pygame.Color(0, 0, 255)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        colors = [self.BLACE, self.RED, self.BLYE]
        for y in range(self.height):
            for x in range(self.width):
                print(self.board[y][x])
                pygame.draw.rect(screen, colors[self.board[y][x]],
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size))
                pygame.draw.rect(screen, self.WHITE, (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos[0] - self.left, mouse_pos[1] - self.top
        if 0 <= x < self.width * self.cell_size and 0 <= y < self.height * self.cell_size:
            cell_coords = x // self.cell_size, y // self.cell_size
            return self.on_click(cell_coords)

    def on_click(self, cell):
        for i in range(self.width):
            self.board[cell[1]][i] = (self.board[cell[1]][i]) % 2
        for i in range(self.height):
            self.board[i][cell[0]] = (self.board[i][cell[0]]) % 2
        self.board[cell[1]][cell[0]] = (self.board[cell[1]][cell[0]] + 1) % 2


if __name__ == '__main__':
    pygame.init()
    size = 600, 600
    screen = pygame.display.set_mode(size)

    board = Board(5, 7)
    board.set_view(50, 50, 55)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.get_cell(pygame.mouse.get_pos())

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()

    pygame.quit()
