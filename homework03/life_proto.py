import copy
import random
import typing as tp
import copy

import ipdb
import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10
    ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """Отрисовать сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color("black"), (x, 0), (x, self.height)
            )
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color("black"), (0, y), (self.width, y)
            )

    def run(self) -> None:
        """Запустить игру"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        # Создание списка клеток

        self.grid = self.create_grid(True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw_lines()
            self.draw_grid()

            # Отрисовка списка клеток
            self.draw_grid()
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.grid = self.get_next_generation()

            self.grid = self.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.
        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.
        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.
        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """

        if randomize:
            return [
                [random.randint(0, 1) for j in range(self.width)]
                for i in range(self.height)
            ]
        else:
            return [[0 for j in range(self.width)] for i in range(self.height)]


    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """

        colors = {0: pygame.Color("white"), 1: pygame.Color("green")}
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(
                    self.screen,
                    colors[self.grid[y][x]],
                    (
                        y * self.cell_size + 1,
                        x * self.cell_size + 1,
                        self.cell_size - 1,
                        self.cell_size - 1,
                    ),

                )

    def get_neighbours(self, cell: Cell) -> Cells:

        """
        Вернуть список соседних клеток для клетки `cell`.
        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.
        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.
        Returns
        ----------
        out : Cells
            Список соседних клеток.

        y,x = cell
        res = []

        for ydelta in range(-1,2):
            for xdelta in range(-1,2):
                if (ydelta or xdelta) and (x+xdelta in range(self.width)) and (y+ydelta in range(self.height)):
                    res.append(self.grid[y+ydelta][x+xdelta])
        return res
        """

        neighbours = []
        row, col = cell
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (
                    0 <= row + i < self.cell_height
                    and 0 <= col + j < self.cell_width
                    and (i, j) != (0, 0)
                ):
                    neighbours.append(self.grid[row + i][col + j])
        return neighbours

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.
        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """

        new_grid = self.create_grid()
        for y, yval in enumerate(self.grid):
            new_line = []
            for x, xval in enumerate(yval):
                if xval:
                    if sum(self.get_neighbours((y, x))) in (2, 3):
                        new_grid[y][x] = 1
                else:
                    if sum(self.get_neighbours((y, x))) == 3:
                        new_grid[y][x] = 1

        return new_grid



