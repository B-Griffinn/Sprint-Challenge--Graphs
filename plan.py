"""
- we need a dict to hold the visited rooms
- we need a function to flip directions when someone reaches a dead end
- we need to initialize our traversal with the first room visited along with all of its exits
- only traverse the maze when the length of the rooms dict is less than the entire maze length bc that means we have rooms to visit. We also need to subtract one to ensure we do not overcount.
- then we want to check if our current room has been visited...
- mark the room we just visited as visited by add the direction from this room to our prev_rooms_path list
- remove that direction from our rooms dictionary so we do not traverse over again
- check the current traversal for a dead end
- remove the last direction from our prev_direction_path
- move our player back to where they came from
- add that path to paths traveled
- otherwise we check if there are any rooms left to explore
- pick the last exit from our rooms dict at the position of our current room
- save our exit_dir to our traversal path after we flip directions
- move to next room
"""
