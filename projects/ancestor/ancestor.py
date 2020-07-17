class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)
    
def earliest_ancestor(ancestors, starting_node):
    
    # Create an empty stack
    s = Stack()
    # Init: push the starting node
    s.push(starting_node)
    # Create sets to store the visited nodes
    visited = set()
    parents= set()

      # while the stack isn't empty
    while s.size() > 0:
         # pop the first item
        current_node = s.pop()
         # If it's not been visited:
        if current_node not in visited:
            # Mark as visited (i.e. add to the visited set)
            visited.add(current_node)
           # Add parents to the stack
            for next_parent in get_parents(current_node, ancestors):
                if next_parent:
                    parents= set()
                    parents.add(next_parent)
                    s.push(next_parent)
    if len(parents) > 0:
        return min(parents)
    else:
        return -1
    
def get_parents(child, ancestors):
    # go through ancestor data list
    parents = set()
    for ancestor in ancestors:
        par = ancestor[0]
        ch = ancestor[1]
        if ch == child:
            # add the parent from that pair as one of 'child's' parents
            parents.add(par)
   
    return parents