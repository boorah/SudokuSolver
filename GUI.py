import pygame
from SudokuSolver import SudokuSolver


class Gui:
    screen_width = 540
    screen_height = 620

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sudoku")

        self.sudoku = None
        self.screen = None
        self.cells = []
        self.font = pygame.font.SysFont('Arial', 40)

    def print_grid(self):
        for i in range(9):
            row = []
            for j in range(9):
                box = pygame.draw.rect(self.screen, (0, 0, 0), (j * 60, i * 60, 60, 60), 2)

                if self.sudoku[i][j] > 0:
                    digit = str(self.sudoku[i][j])
                else:
                    digit = ' '

                text = self.font.render(digit, True, (0, 0, 0))

                text_rect = text.get_rect()

                text_rect.center = box.center

                self.screen.blit(text, text_rect.topleft)
                row.append(box)
                pygame.display.flip()

            self.cells.append(row)

    def update_cell(self, value, box):
        if value > 0:
            value = str(value)
        else:
            value = ' '

        self.clear_empty()
        self.screen.fill((255, 255, 255), box)
        x1, y1 = box.topleft
        x2, y2 = box.bottomright

        box = pygame.draw.rect(self.screen, (0, 0, 0), (x1, y1, x2 - x1, y2 - y1), 2)
        text = self.font.render(value, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = box.center
        self.screen.blit(text, text_rect.topleft)
        pygame.display.flip()

    def clear_empty(self):
        for p in range(9):
            for q in range(9):
                if self.sudoku[p][q] == 0:
                    cell = self.cells[p][q]
                    self.screen.fill((255, 255, 255), cell)
                    x1, y1 = cell.topleft
                    x2, y2 = cell.bottomright
                    cell = pygame.draw.rect(self.screen, (0, 0, 0), (x1, y1, x2 - x1, y2 - y1), 2)
                    pygame.display.update()

    def start(self, solver):
        self.sudoku = solver.sudoku

        is_running = True

        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.screen.fill((255, 255, 255))
        self.print_grid()

        button_font = pygame.font.SysFont('comicsans', 28)
        solve_button = pygame.draw.rect(self.screen, (0, 0, 0), (225, 560, 70, 40), 1)

        button_text = button_font.render("Solve", True, (0, 0, 0))

        button_text_rect = button_text.get_rect()
        button_text_rect.center = solve_button.center

        self.screen.blit(button_text, button_text_rect.topleft)
        pygame.display.update()

        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if 225 <= mouse_pos[0] <= (225 + 70):
                        if 560 <= mouse_pos[1] <= (560 + 40):
                            self.screen.fill((220, 220, 220), solve_button)
                            pygame.display.update()

                            pygame.time.delay(100)

                            self.screen.fill((255, 255, 255), solve_button)
                            solve_button = pygame.draw.rect(self.screen, (0, 0, 0), (225, 560, 70, 40), 1)

                            button_text = button_font.render("Solve", True, (0, 0, 0))

                            button_text_rect = button_text.get_rect()
                            button_text_rect.center = solve_button.center

                            self.screen.blit(button_text, button_text_rect.topleft)

                            print('Button clicked!')
                            solver.solveBoard()


gui = Gui()

# Easy
# [[0, 4, 0, 0, 0, 2, 0, 1, 9],
#  [0, 0, 0, 3, 5, 1, 0, 8, 6],
#  [3, 1, 0, 0, 9, 4, 7, 0, 0],
#  [0, 9, 4, 0, 0, 0, 0, 0, 7],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [2, 0, 0, 0, 0, 0, 8, 9, 0],
#  [0, 0, 9, 5, 2, 0, 0, 4, 1],
#  [4, 2, 0, 1, 6, 9, 0, 0, 0],
#  [1, 6, 0, 8, 0, 0, 0, 7, 0]]

# [[9, 0, 0, 0, 0, 0, 5, 3, 0],
#  [2, 0, 0, 8, 0, 1, 0, 0, 9],
#  [0, 3, 0, 0, 0, 9, 0, 2, 7],
#  [3, 0, 0, 0, 0, 0, 0, 6, 0],
#  [0, 0, 6, 9, 0, 8, 0, 0, 4],
#  [4, 9, 0, 7, 0, 0, 0, 0, 0],
#  [0, 0, 4, 0, 0, 0, 0, 1, 0],
#  [0, 0, 0, 1, 0, 7, 0, 0, 0],
#  [1, 0, 0, 0, 0, 0, 0, 0, 0]]

# Expert
# [[0, 0, 0, 0, 1, 0, 9, 2, 0],
#  [0, 0, 0, 4, 9, 3, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 7, 0],
#  [6, 0, 0, 0, 0, 0, 3, 0, 0],
#  [0, 5, 0, 0, 0, 0, 0, 0, 0],
#  [0, 1, 3, 0, 0, 0, 0, 6, 8],
#  [0, 0, 2, 9, 0, 0, 7, 3, 0],
#  [4, 0, 0, 0, 0, 0, 0, 0, 5],
#  [5, 0, 8, 0, 0, 7, 0, 0, 0]]

solver = SudokuSolver([[0, 0, 0, 0, 1, 0, 9, 2, 0],
                       [0, 0, 0, 4, 9, 3, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 7, 0],
                       [6, 0, 0, 0, 0, 0, 3, 0, 0],
                       [0, 5, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 3, 0, 0, 0, 0, 6, 8],
                       [0, 0, 2, 9, 0, 0, 7, 3, 0],
                       [4, 0, 0, 0, 0, 0, 0, 0, 5],
                       [5, 0, 8, 0, 0, 7, 0, 0, 0]], gui)

gui.start(solver)
solver.solveBoard()
