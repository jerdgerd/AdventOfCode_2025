import heapq
from typing import List, Tuple
from dataclasses import dataclass
import math

@dataclass
class UnionFind:
    parent: List[int]
    size: List[int]

    @classmethod
    def create(cls, n: int) -> "UnionFind":
        return cls(parent=list(range(n)), size=[1] * n)

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

    def component_sizes(self) -> List[int]:
        roots = {}
        for i in range(len(self.parent)):
            r = self.find(i)
            roots[r] = roots.get(r, 0) + 1
        return list(roots.values())


class JunctionBoxConnector:
    def __init__(self, boxes, verbose = False):
        self.boxes = boxes
        self.verbose = verbose
        self.uf = UnionFind.create(len(self.boxes))

    def _all_edges_sorted(self):
        n = len(self.boxes)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                d2 = math.dist(self.boxes[i], self.boxes[j])
                edges.append((d2, i, j))
        edges.sort(key=lambda t: t[0])
        return edges

    def k_smallest_edges(self, k = -1):
        n = len(self.boxes)

        if k == -1:
            k = n * (n - 1) // 2

        heap = []

        for i in range(n):
            for j in range(i + 1, n):
                d2 = math.dist(self.boxes[i], self.boxes[j])

                if len(heap) < k:
                    heapq.heappush(heap, (-d2, i, j))
                else:
                    if d2 < -heap[0][0]:
                        heapq.heapreplace(heap, (-d2, i, j))

        edges = [(-neg_d2, i, j) for (neg_d2, i, j) in heap]
        edges.sort(key=lambda t: t[0])
        return edges

    def connect_boxes(self, number_to_connect = -1):
        edges = self.k_smallest_edges(number_to_connect)

        for idx, (d2, i, j) in enumerate(edges, start=1):
            merged = self.uf.union(i, j)
            if self.verbose:
                print(f"{idx:4d}: {i} <-> {j}  d2={d2}  merged={merged}")

            if len(self.uf.component_sizes()) == 1:
                return self.boxes[i][0] * self.boxes[j][0]

    def find_part_1_math(self):
        sizes = sorted(self.uf.component_sizes(), reverse=True)
        return sizes[0] * sizes[1] * sizes[2]
