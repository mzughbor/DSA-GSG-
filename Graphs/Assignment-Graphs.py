import heapq
from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}

    def add_location(self, location):
        if location not in self.adj:
            self.adj[location] = []

    def remove_location(self, location):
        if location in self.adj:
            del self.adj[location]
        for loc in self.adj:
            self.adj[loc] = [(nbr, w) for nbr, w in self.adj[loc] if nbr != location]

    def add_road(self, from_loc, to_loc, time):
        if from_loc not in self.adj:
            self.add_location(from_loc)
        if to_loc not in self.adj:
            self.add_location(to_loc)
        self.adj[from_loc].append((to_loc, time))

    def remove_road(self, from_loc, to_loc):
        if from_loc in self.adj:
            self.adj[from_loc] = [(nbr, w) for nbr, w in self.adj[from_loc] if nbr != to_loc]

    def bfs(self, start):
        if start not in self.adj:
            return []

        visited = set()
        queue = deque([start])
        reachable = []

        while queue:
            loc = queue.popleft()
            if loc not in visited:
                visited.add(loc)
                reachable.append(loc)

                for nbr, _ in self.adj[loc]:
                    if nbr not in visited:
                        queue.append(nbr)

        return reachable

    #Dijkstra: Shortest path
    def shortest_path(self, start, end):
        if start not in self.adj or end not in self.adj:
            return None, float("inf")

        distances = {loc: float("inf") for loc in self.adj}
        distances[start] = 0
        prev = {loc: None for loc in self.adj}
        pq = [(0, start)]

        while pq:
            curr_dist, loc = heapq.heappop(pq)
            if curr_dist > distances[loc]:
                continue

            for nbr, weight in self.adj[loc]:
                new_dist = curr_dist + weight
                if new_dist < distances[nbr]:
                    distances[nbr] = new_dist
                    prev[nbr] = loc
                    heapq.heappush(pq, (new_dist, nbr))

        path = []
        node = end
        while node is not None:
            path.insert(0, node)
            node = prev[node]
        return path, distances[end]


# Tesst
if __name__ == "__main__":
    g = Graph()

    # Adding locations
    for loc in ["Hospital", "Cinema", "Park", "School", "Library", "Station"]:
        g.add_location(loc)

    # Add roads (direct and time cost)
    g.add_road("Hospital", "School", 10)
    g.add_road("School", "Park", 12)
    g.add_road("School", "Library", 15)
    g.add_road("Park", "Station", 7)
    g.add_road("Cinema", "Library", 10)
    g.add_road("Cinema", "Station", 5)
    g.add_road("Hospital", "Cinema", 15)
    g.add_road("Library", "Hospital", 6)
    g.add_road("Station", "School", 8)
    g.add_road("Station", "Cinema", 30)
    print("reachable from hospital:", g.bfs("Hospital"))
    path, dist = g.shortest_path("Hospital", "Park")
    print(f"shortest path hospital → Park: {path}, distance={dist}")
