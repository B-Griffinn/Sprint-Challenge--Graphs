from room import Room
from player import Player
from world import World
from util import Stack
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
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# adding to check visited rooms
prev_rooms_path = []

# create a dict for our rooms visited
rooms = {}


def flip_dir(dir):
    if dir == "n":
        return "s"
    if dir == "s":
        return "n"
    if dir == "w":
        return "e"
    if dir == "e":
        return "w"
    else:
        return "error"


# initialize our first room in the visited dict with a list of all exits for that room
rooms[player.current_room] = player.current_room.get_exits()
print('Exits of current room', rooms[player.current_room])


# while our rooms viisted dict is smaller than our actual graph we want to traverse BUT we need to remove the current room from the traversal so we do not over count
while len(rooms) < len(room_graph) - 1:

    # then we want to check if our current room has been visited...
    if player.current_room not in rooms:
        # ... set our list of exits to be our cuurent room
        rooms[player.current_room] = player.current_room.get_exits()

        # mark the room we just visited as visited by add the direction from this room to our prev_rooms_path list
        prev_room = prev_rooms_path[-1]
        # print('prev_room', prev_room)

        # remove that direction from our rooms dictionary so we do not traverse over again
        rooms[player.current_room].remove(prev_room)

    # check the current traversal for a dead end
    while len(rooms[player.current_room]) < 1:
        # remove the last direction from our prev_direction_path
        last_dir = prev_rooms_path.pop()
        # move our player back
        player.travel(last_dir)
        # add that path to paths traveled
        traversal_path.append(last_dir)

    # otherwise we check if there are any rooms left to explore
    else:
        # pick the last exit from our rooms dict at the position of our current room
        exit_dir = rooms[player.current_room].pop()
        # add the traversal path
        traversal_path.append(exit_dir)
        # save our exit_dir to our traversal path after we flip directions
        prev_rooms_path.append(flip_dir(exit_dir))
        # then move to the next room
        player.travel(exit_dir)


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
