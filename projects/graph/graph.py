"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # set of edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
          # If they're both in the graph
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")
                    

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]  # 

    def bft(self, starting_vertex_id):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue 
        q = Queue()  
        q.enqueue(starting_vertex_id)
        # keep track of visited nodes
        visited = set()

        # repeat until queue is empty

        while q.size() > 0:

            #Dequeue first item
            v = q.dequeue()

            # IF it's not visited:
            if v not in visited:
                print(v)
                visited.add(v)
                

                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
                
        
    def dft(self, starting_vertex_id):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()

        # Init: push the starting node
        s.push(starting_vertex_id)

        # Create a set to store the visited nodes
        visited = set()

      

        # while the stack isn't empty
        while s.size() > 0:
            # pop the first item
            v = s.pop()
            # If it's not been visited:
            if v not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited.add(v)
                # Do something with the node
                print(v)
                # Add all neighbors to the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

            

    def dft_recursive(self, starting_vertex_id, visited=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if starting_vertex_id not in visited:
            # Add starting vertex to visited
            visited += [starting_vertex_id]
            print(starting_vertex_id)
        # Find neighbors to starting vertex
            for next_vert in self.get_neighbors(starting_vertex_id):
            # Recursively call function on new verticies if not in path yet
                self.dft_recursive(next_vert, visited)
               
          
               

    def bfs(self, starting_vertex_id, destination_vertex_id):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
          # Create an empty queue 
        q = Queue()  
        q.enqueue([starting_vertex_id])
         # keep track of visited nodes
        visited = set()
         
        while q.size() > 0:
          path = q.dequeue()
          # Grab last vertex from the path
          v = path[-1]
          # if not visited yet, check destination and return path
          if v not in visited:
              if v == destination_vertex_id:
                  return path
              # Mark visited
          visited.add(v)
          # Then add path to neighbors to back of queue, copy path, append neighbor to the back
          for next_vert in self.get_neighbors(v):
              new_path = list(path) # copy the list
              new_path.append(next_vert)
              q.enqueue(new_path)
                # Return none if we didn't find
        return None
          
            
    def dfs(self, starting_vertex_id, destination_vertex_id):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
       # Create an empty stack
        s = Stack()

        # Create a set to store the visited nodes
        visited = set()

        # Init: push the starting node
        s.push([starting_vertex_id])

         # while the stack isn't empty
        while s.size() > 0:
            # pop the first path
            path = s.pop()
            # Grab last vertex from the path
            v = path[-1]
            # If it's not been visited:
            if v not in visited:
                if v == destination_vertex_id:
                    return path
                # Mark as visited (i.e. add to the visited set)
                visited.add(v)
                # Do something with the node
                print(f"Visited {v}")
                # Add all neighbors to the stack
                for next_vert in self.get_neighbors(v):
                     new_path = path.copy()
                new_path.append(next_vert)
                s.push(new_path)


    def dfs_recursive(self, starting_vertex_id, destination_vertex_id, visited=[], path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Check if starting vertex has been visited
        if starting_vertex_id not in visited:
            # Add to path if visited and make copy
            visited += [starting_vertex_id]
            path_copy = list(path)
            path_copy.append(starting_vertex_id)
            # If starting vertex is destination
        if starting_vertex_id == destination_vertex_id:
            return path_copy
        
        for next_vert in self.get_neighbors(starting_vertex_id):
            # Recursively call function on new verticies if not visited yet
            if next_vert not in visited:
                new_path = self.dfs_recursive(next_vert, destination_vertex_id, visited, path_copy)
                if new_path is not None:
                    return new_path
     
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
