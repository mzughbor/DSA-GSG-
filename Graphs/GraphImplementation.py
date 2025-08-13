class Edge:
    def __init__(self, target, weight):
        self.target = target # Reference to target Vertex
        self.weight = weight

class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = [] # List of Edge instances

    def add_edge(self, target_vertex, weight=1):
        self.edges.append(Edge(target_vertex, weight))
    
    def remove_edge(self, target_vertex):
        self.edges = [e for e in self.edges if e.target != target_vertex]

class Graph:
    def __init__(self):
        self.vertices = [] # List of Vertex instances
    
    def add_vertex(self, label):
        if not any(v.label == label for v in self.vertices):
            self.vertices.append(Vertex(label))    

    def find_vertex(self, label):
        for v in self.vertices:
            if v.label == label:
                return v
        return None

    def add_edge(self, from_label, to_label, weight=1):
        from_vertex = self.find_vertex(from_label)
        to_vertex = self.find_vertex(to_label)
        if from_vertex and to_vertex:
            from_vertex.add_edge(to_vertex, weight)

    def remove_edge(self, from_label, to_label):
        from_vertex = self.find_vertex(from_label)
        to_vertex = self.find_vertex(to_label)
        if from_vertex and to_vertex:
            from_vertex.remove_edge(to_vertex)

    def remove_vertex(self, label):
        target_vertex = self.find_vertex(label)
        if target_vertex:
            self.vertices = [v for v in self.vertices if v != target_vertex]
            for v in self.vertices:
                v.remove_edge(target_vertex)