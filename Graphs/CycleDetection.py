# Exercise 2: Cycle Detection in a Directed Graph Given a graph, write a function that detects 
                # whether a cycle exists using DFS.
"""
from GraphImplementation import Graph

class CycleDetector(Graph):

    def has_cycle(self):
        visited = set()
        recursion_stack = set()
        
        for vertex_label in self.vertices:
            if vertex_label not in visited:
                if self._dfs_util(vertex_label, visited, recursion_stack):
                    return True        
        return False

    def _dfs_util(self, vertex_label, visited, recursion_stack):

        visited.add(vertex_label)
        recursion_stack.add(vertex_label)
        
        current_vertex = self.find_vertex(vertex_label)
        
        for edge in current_vertex.edges:
            neighbor_label = edge.target.label
            
            if neighbor_label not in visited:
                if self._dfs_util(neighbor_label, visited, recursion_stack):
                    return True
            
            elif neighbor_label in recursion_stack:
                print(f"Cycle detected! Back edge found from {vertex_label} to {neighbor_label}.")
                return True
        
        recursion_stack.remove(vertex_label)
        
        return False


if __name__ == "__main__":
    
    # --------------------------------------------------------------------------
    # Example 1: Graph with a cycle (A -> B -> C -> A)
    # --------------------------------------------------------------------------
    print("--- Testing a graph with a cycle ---")
    cyclic_graph = CycleDetector()
    
    cyclic_graph.add_vertex("A")
    cyclic_graph.add_vertex("B")
    cyclic_graph.add_vertex("C")
    cyclic_graph.add_vertex("D")
    
    cyclic_graph.add_edge("A", "B")
    cyclic_graph.add_edge("B", "C")
    cyclic_graph.add_edge("C", "A") # This is the back edge creating the cycle.
    cyclic_graph.add_edge("D", "A")
    
    if cyclic_graph.has_cycle():
        print("Result: Cycle detected in the cyclic graph.\n")
    else:
        print("Result: No cycle detected in the cyclic graph.\n")

    # --------------------------------------------------------------------------
    # Example 2: Graph without a cycle (A -> B -> C, D -> A)
    # --------------------------------------------------------------------------
    print("--- Testing a graph without a cycle ---")
    acyclic_graph = CycleDetector()
    
    acyclic_graph.add_vertex("A")
    acyclic_graph.add_vertex("B")
    acyclic_graph.add_vertex("C")
    acyclic_graph.add_vertex("D")
    
    acyclic_graph.add_edge("A", "B")
    acyclic_graph.add_edge("B", "C")
    acyclic_graph.add_edge("D", "A")
    
    if acyclic_graph.has_cycle():
        print("Result: Cycle detected in the acyclic graph.")
    else:
        print("Result: No cycle detected in the acyclic graph.")




"""

































#
# A simple implementation of a directed graph for cycle detection.
#
class Edge:
    """Represents a directed edge with a target vertex."""
    def __init__(self, target):
        self.target = target

class Vertex:
    """Represents a vertex in the graph."""
    def __init__(self, label):
        self.label = label
        self.edges = []  # List of Edge instances

    def add_edge(self, target_vertex):
        """Adds a directed edge to another vertex."""
        self.edges.append(Edge(target_vertex))

class Graph:
    """A directed graph implemented with an adjacency list."""
    def __init__(self):
        self.vertices = {} # Using a dictionary for faster vertex lookup

    def add_vertex(self, label):
        """Adds a new vertex to the graph."""
        if label not in self.vertices:
            self.vertices[label] = Vertex(label)

    def find_vertex(self, label):
        """Finds a vertex by its label."""
        return self.vertices.get(label)

    def add_edge(self, from_label, to_label):
        """Adds a directed edge between two vertices."""
        from_vertex = self.find_vertex(from_label)
        to_vertex = self.find_vertex(to_label)
        if from_vertex and to_vertex:
            from_vertex.add_edge(to_vertex)

class CycleDetector(Graph):
    """
    A class that inherits from Graph and adds cycle detection functionality.
    """

    def has_cycle(self):
        """
        Checks if the graph contains a cycle using DFS.

        Returns:
            bool: True if a cycle exists, False otherwise.
        """
        # A set to keep track of all visited vertices to avoid redundant checks.
        visited = set()
        
        # A set to keep track of vertices in the current recursion stack.
        # This is the key for cycle detection in a directed graph.
        recursion_stack = set()
        
        # Iterate through all vertices. We need to do this because the graph
        # might be disconnected.
        for vertex_label in self.vertices:
            # If the vertex hasn't been visited, start a new DFS traversal from it.
            if vertex_label not in visited:
                if self._dfs_util(vertex_label, visited, recursion_stack):
                    return True  # A cycle was found in this traversal.
        
        return False # No cycles were found in any traversal.

    def _dfs_util(self, vertex_label, visited, recursion_stack):
        """
        Recursive helper function for DFS traversal and cycle detection.
        """
        # Mark the current vertex as visited and add it to the recursion stack.
        visited.add(vertex_label)
        recursion_stack.add(vertex_label)
        
        current_vertex = self.find_vertex(vertex_label)
        
        # This is a crucial check to prevent the 'AttributeError'.
        # It's a defensive measure in case a non-existent vertex label
        # is somehow passed to this function.
        if current_vertex is None:
            print(f"Error: Vertex with label '{vertex_label}' not found.")
            recursion_stack.remove(vertex_label)
            return False

        # Explore all neighbors of the current vertex.
        for edge in current_vertex.edges:
            neighbor_label = edge.target.label
            
            # If the neighbor hasn't been visited, recurse on it.
            if neighbor_label not in visited:
                if self._dfs_util(neighbor_label, visited, recursion_stack):
                    return True # Pass the 'cycle found' signal up the stack.
            
            # If the neighbor IS in the current recursion stack, we have found a cycle!
            elif neighbor_label in recursion_stack:
                print(f"Cycle detected! Back edge found from {vertex_label} to {neighbor_label}.")
                return True
        
        # After visiting all neighbors, remove the current vertex from the
        # recursion stack. This "unmarks" it from the current path.
        recursion_stack.remove(vertex_label)
        
        return False # No cycle found from this path.

# --- Example Usage ---
if __name__ == "__main__":
    
    # --------------------------------------------------------------------------
    # Example 1: Graph with a cycle (A -> B -> C -> A)
    # --------------------------------------------------------------------------
    print("--- Testing a graph with a cycle ---")
    cyclic_graph = CycleDetector()
    
    cyclic_graph.add_vertex("A")
    cyclic_graph.add_vertex("B")
    cyclic_graph.add_vertex("C")
    cyclic_graph.add_vertex("D")
    
    cyclic_graph.add_edge("A", "B")
    cyclic_graph.add_edge("B", "C")
    cyclic_graph.add_edge("C", "A") # This is the back edge creating the cycle.
    cyclic_graph.add_edge("D", "A")
    
    if cyclic_graph.has_cycle():
        print("Result: Cycle detected in the cyclic graph.\n")
    else:
        print("Result: No cycle detected in the cyclic graph.\n")

    # --------------------------------------------------------------------------
    # Example 2: Graph without a cycle (A -> B -> C, D -> A)
    # --------------------------------------------------------------------------
    print("--- Testing a graph without a cycle ---")
    acyclic_graph = CycleDetector()
    
    acyclic_graph.add_vertex("A")
    acyclic_graph.add_vertex("B")
    acyclic_graph.add_vertex("C")
    acyclic_graph.add_vertex("D")
    
    acyclic_graph.add_edge("A", "B")
    acyclic_graph.add_edge("B", "C")
    acyclic_graph.add_edge("D", "A")
    
    if acyclic_graph.has_cycle():
        print("Result: Cycle detected in the acyclic graph.")
    else:
        print("Result: No cycle detected in the acyclic graph.")
