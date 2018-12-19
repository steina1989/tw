#!/usr/bin/env python3

import random, math
from visualizer import Visualizer


class TSP:
    def __init__(self, nodes: set):
        self.nodes = nodes

    @classmethod
    def from_file(cls, file_path: str):
        """ Parse newline seperated data from filepath """
        data = set()
        with open(file_path) as f:
            for line in f.readlines():
                x, y = map(float, line.strip().split())
                data.add((x, y))
        return cls(data)

    def visualize(self, path):
        Visualizer(path).draw()

    def nearest_neighbour(self):
        """ A simple heuristic approach to the TSP
        Random node is chosen from the set, from which we travel iteratively
        to the nearest node until all nodes are visited.
        """

        nodes = set(self.nodes)
        length = 0

        node = random.sample(nodes, 1)[0]
        nodes.remove(node)
        path = [node]

        while len(nodes) != 0:
            lowest_dist = float("inf")
            nearest_neighbour = None

            for node in nodes:
                dist = self.dist(path[-1], node)
                if dist < lowest_dist:
                    lowest_dist = dist
                    nearest_neighbour = node

            path.append(nearest_neighbour)
            length += lowest_dist
            nodes.remove(nearest_neighbour)
        return path, length

    @staticmethod
    def repeat_n(fn, n=100):
        """ Repeats a heuristic method n times
        fn: A function that returns a tuple (path: [], length: int)
        """

        shortest_length = float("inf")
        shortest_path = None

        for _ in range(n):
            path, length = fn()
            if length < shortest_length:
                shortest_path = path
                shortest_length = length
        return shortest_path, shortest_length

    def dist(self, a: tuple, b: tuple):
        x1, y1 = a
        x2, y2 = b
        distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
        return math.sqrt(distance)


if __name__ == "__main__":
    tsp = TSP.from_file("dataset.tsv")
    path, dist = TSP.repeat_n(tsp.nearest_neighbour)

    tsp.visualize(path)
