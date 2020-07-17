from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph= literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# backward direction
backward_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Keeping track of backward direction
backward_path = []

# dictionary to iterate through exits
rooms = dict()

# Add room zero to rooms

rooms[0] = player.current_room.get_exits()

# While rooms visited is less than total rooms

while len(rooms) < len(room_graph) - 1:
    # Add exit if room not visited yet
    if player.current_room.id not in rooms:
        rooms[player.current_room.id] = player.current_room.get_exits()
        # Grab last traveld direction
        last_direction = backward_path[-1]
        # Remove last exit 
        rooms[player.current_room.id].remove(last_direction)

        # while there are no more rooms to go
    while len(rooms[player.current_room.id]) < 1:
        # pop last direction from backward path
        backward = backward_path.pop()
        # Add backward direction to traversal path in order to travel
        traversal_path.append(backward)
        player.travel(backward)

        # Travel to first exit direction

    exit_direction = rooms[player.current_room.id].pop(0)
    # Add to traversal path
    traversal_path.append(exit_direction)
    # Add backward direction to backward path
    backward_path.append(backward_direction[exit_direction])
    # Travel
    player.travel(exit_direction)
        
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
