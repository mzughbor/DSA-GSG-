# Implementation for Graph/s

class Edge:
    def __init__(self, target, weight):
        self.target = target
        self.weight = weight

class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = [] 

    def add_edge(self, target_vertex, weight):
        self.edges.append(Edge(target_vertex, weight))

    def remove_edge(self, target_vertex):
        for e in self.edges:
            if e.target == target_vertex:
                self.edges.remove(e)

class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, label):
        label_exists = False
        for l in self.vertices:
            if l.label == label:
                print(f"Can't add '{label}' — it already exists!")
                label_exists = True
                break
        if not label_exists:
            self.vertices.append(Vertex(label))

        #All of it ni couple lines!
        #if not any(v.label == label for v in self.vertices):
            #self.vertices.append(Vertex(label))

    def find_vertex(self, label):
        for v in self.vertices:
            if v.label == label:
                return v
        return None

    def add_edge(self, form_label, to_label, weight):
        from_vertex = self.find_vertex(form_label)
        to_vertex = self.find_vertex(to_label)
        if from_vertex and to_vertex:
            from_vertex.add_edge(to_vertex, weight)

    def remove_edge(self, form_label, to_label, weight):
        from_vertex = self.find_vertex(form_label)
        to_vertex = self.find_vertex(to_label)
        if from_vertex and to_vertex:
            from_vertex.remove_edge(to_vertex)
    
    def remove_vertex(self, label):
        target_vertex = self.find_vertex(label)
        if target_vertex:
            self.vertices = []
            for v in self.vertices:
                if v != target_vertex:
                    self.vertices.append(v)
            for v in self.vertices:
                v.remove_edge(target_vertex)
        else:
            print("The given vertex doesn't exist to remove!")


if __name__ == "__main__":
    g = Graph()

    # Add vertices
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")

    # Try adding an existing vertex
    g.add_vertex("A")

    # Add edges
    g.add_edge("A", "B", 5)
    g.add_edge("B", "C", 3)
    g.add_edge("A", "C", 10)

    # Show connections before removal
    print("\n Graph before removals:")
    for v in g.vertices:
        print(f"{v.label} -> {[ (e.target.label, e.weight) for e in v.edges ]}")

    # Remove edge
    g.remove_edge("A", "C", 10)

    # Remove vertex
    g.remove_vertex("F")
    
    #g.remove_vertex("C")

    # Show connections after removal
    print("\n Graph after removals:")
    for v in g.vertices:
        print(f"{v.label} -> {[ (e.target.label, e.weight) for e in v.edges ]}")


# 6. Graph Traversal Techniques >> 