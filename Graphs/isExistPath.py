#Exercise 1: Path Existence Given a directed graph, determine if there exists a path from node x to node y.

from GraphImplementation import Graph

class PathFindingGraph(Graph):
    def dfs_path_exists(self, start_label, target_label):
        start_vertex = self.find_vertex(start_label)
        target_vertex = self.find_vertex(target_label)

        # Handle cases where one or both vertices don't exist
        if not start_vertex or not target_vertex:
            return False

        # Use a stack for the DFS traversal
        stack = [start_vertex]
        visited = set()

        while stack:
            current_vertex = stack.pop()
            
            # If we've reached the target, a path exists
            if current_vertex.label == target_label:
                return True
            
            # If the current vertex has not been visited, process it
            if current_vertex.label not in visited:
                visited.add(current_vertex.label)
                
                # Add unvisited neighbors to the stack
                for edge in current_vertex.edges:
                    neighbor = edge.target
                    if neighbor.label not in visited:
                        stack.append(neighbor)
                        
        # If the loop finishes without finding the target, no path exists
        return False

        
""" 
def dfs(self, start_label):
    start_vertex = self.find_vertex(start_label)
    if not start_vertex:
        return
    visited = set()
    stack = [start_vertex]

    while stack:
        vertex = stack.pop()
        if vertex.label not in visited:
            print(vertex.label)
            visited.add(vertex.label)
            for edge in reversed(vertex.edges): # reverse to maintain consistent order
                if edge.target.label not in visited:
                    stack.append(edge.target)
"""


if __name__ == "__main__":
    
    g = PathFindingGraph()
    
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", None)
    g.add_edge("A", "C", None)
    g.add_edge("B", "D", None)
    g.add_edge("C", "D", None)
    g.add_edge("C", "E", None)
    g.add_edge("E", "F", None)

    # Example 1: Path exists from A to F
    start_node = "A"
    end_node = "F"
    if g.dfs_path_exists(start_node, end_node):
        print(f"Path exists from {start_node} to {end_node}.")
    else:
        print(f"No path exists from {start_node} to {end_node}.")
    
    # Expected output: Path exists from A to F.




    # Example 2: Path exists from C to D
    start_node = "C"
    end_node = "D"
    if g.dfs_path_exists(start_node, end_node):
        print(f"Path exists from {start_node} to {end_node}.")
    else:
        print(f"No path exists from {start_node} to {end_node}.")
    # Expected output: Path exists from C to D.

    # Example 3: No path exists from D to A
    start_node = "D"
    end_node = "A"
    if g.dfs_path_exists(start_node, end_node):
        print(f"Path exists from {start_node} to {end_node}.")
    else:
        print(f"No path exists from {start_node} to {end_node}.")
    # Expected output: No path exists from D to A.

    # Example 4: No path exists from A to a non-existent node 'Z'
    start_node = "A"
    end_node = "Z"
    if g.dfs_path_exists(start_node, end_node):
        print(f"Path exists from {start_node} to {end_node}.")
    else:
        print(f"No path exists from {start_node} to {end_node}.")
    # Expected output: No path exists from A to Z.
